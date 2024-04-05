from concierge_pb2 import (
    Destination
)


def recommend(question: str, preferences: str) -> list[Destination]:
    """Return a list of destinations recommended by the Reco Engine"""
    print(f"RAG request with question: {question} and preferences: {preferences}")

    # Connect to Vector DB and 
    results = []


    return results
