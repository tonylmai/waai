from concierge_pb2 import (
    Destination
)

# from mocked import concierge as rag
from concierge.recommendation import recommendation as rag

def recommend(question: str, preferences: str) -> list[Destination]:
    """Return a list of destinations recommended by the Concierge (Reco) Engine"""
    # print(f"Recommendation request with question: {question} and preferences: {preferences}")
    result = rag.recommend(question=question, preferences=preferences)
    return result
