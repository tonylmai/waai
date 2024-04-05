""" This is a micro-service that provides gRPC methods for recommending a complete
  itinerary based on user's input (list of locations and context from user's preferences)"""
from concurrent import futures
# import sys
import grpc
# from grpc_interceptor import ErrorLogger
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

# sys.path.append('../')  # Need to traverse one level up before we could traverse down

from concierge_pb2 import (
    RecommendationResponse
)

import concierge_pb2_grpc
from service import concierge as svc

class ConciergeService(concierge_pb2_grpc.ConciergeServicer):
    @catch_and_log_exceptions
    @log_request_counts
    @log_latency
    def Recommend(self, request, context):
        """Recommend a complete itinerary based on user's input (list of locations and context from user's preferences)"""
        if not request.question:
            # context.abort(grpc.StatusCode.INVALID_ARGUMENT, "question is empty")
            raise NotFound("question is empty")

        # print(f"Recommendation request for user {request.user_id} with question: {request.question} and preferences: {request.preferences}")
        dests = svc.recommend(question=request.question, preferences=request.preferences)
        return RecommendationResponse(destinations=dests)

def serve():
    """Bring up the server and begin serving"""
    host = "[::]"
    port = 50051
    print(f"Starting server at {host}:{port}...")
    # interceptors = [ErrorLogger()]
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors)
    concierge_pb2_grpc.add_ConciergeServicer_to_server(
        ConciergeService(), server
    )
    server.add_insecure_port(f"{host}:{port}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
