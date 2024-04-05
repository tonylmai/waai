# import os
# import sys
import grpc

# sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
# sys.path.append('../')  # Need to traverse one level up before we could traverse down

from concierge_pb2 import RecommendationRequest
from concierge_pb2_grpc import ConciergeStub

channel = grpc.insecure_channel("localhost:50051")
client = ConciergeStub(channel)
request = RecommendationRequest(user_id="tony",
                                question="What are things to do in San Francisco?",
                                preferences={'location': "San Francisco",
                                             'start_date': "03/31/2024",
                                             'end_date': "04/04/2024"})
response = client.Recommend(request)
if not response.destinations:
    print("No recommendations for you. Stay home!")
else:
    destinations = [dest.poi.description for dest in response.destinations]
    print("\n".join(destinations))

