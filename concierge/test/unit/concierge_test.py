import sys

sys.path.append('../../concierge')
sys.path.append('../../protobufs/python')  # Need to traverse up then down to pick up the protobuf stuffs

from concierge import ConciergeService

from concierge_pb2 import RecommendationRequest

def test_recommendations():
    service = ConciergeService()
    request = RecommendationRequest(user_id="tony",
                                    question="What are things to do in San Francisco?",
                                    preferences={'location': "San Francisco",
                                                'start_date': "03/31/2024",
                                                'end_date': "04/04/2024"})
    response = service.Recommend(request, None)
    assert len(response.destinations) == 1
