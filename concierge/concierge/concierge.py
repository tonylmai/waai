""" This is a micro-service that provides gRPC methods for recommending a complete
  itinerary based on user's input (list of locations and context from user's preferences)"""
from concurrent import futures
import sys
from signal import signal, SIGTERM

sys.path.append('./')                   # Needs to add local folder to traverse between modules
sys.path.append('../protobufs/python')  # Need to traverse up then down to pick up the protobuf stuffs

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor, ServerInterceptor
from grpc_interceptor.exceptions import NotFound

from concierge_pb2 import (
    RecommendationResponse
)

import concierge_pb2_grpc
from service import concierge as svc

class ConciergeService(concierge_pb2_grpc.ConciergeServicer):
    def Recommend(self, request, context):
        """Recommend a complete itinerary based on user's input (list of locations and context from user's preferences)"""
        if not request.question:
            # context.abort(grpc.StatusCode.INVALID_ARGUMENT, "question is empty")
            raise NotFound("question is empty")

        # print(f"Recommendation request for user {request.user_id} with question: {request.question} and preferences: {request.preferences}")
        dests = svc.recommend(question=request.question, preferences=request.preferences)
        return RecommendationResponse(destinations=dests)

class ErrorLogger(ServerInterceptor):
    """An intercepter that logs error message"""
    def intercept(self, method, request, context, method_name):
        """Intercepts the method call"""
        try:
            return method(request, context)
        except Exception as e:
            self.log_error(method_name, e)
            raise

    def log_error(self, method_name: str, e: Exception) -> None:
        """Logs error messages"""
        print(f"An error has occurred in method {method_name} with exception: {e}")

def serve():
    """Bring up the server and begin serving"""
    host = "[::]"
    port = 50051
    print(f"Starting server at {host}:{port}...")

    interceptors = [ExceptionToStatusInterceptor(), ErrorLogger()]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors)
    concierge_pb2_grpc.add_ConciergeServicer_to_server(
        ConciergeService(), server
    )
    server.add_insecure_port(f"{host}:{port}")
    server.start()

    def handle_sigterm(*_):
        print("Received shutdown signal")
        all_rpcs_done_event = server.stop(30)
        all_rpcs_done_event.wait(30)
        print("Shut down gracefully")

    # Register the handler for signals from Kubernetes or almost any other process
    signal(SIGTERM, handle_sigterm)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
