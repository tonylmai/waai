""" This service provides a canned itinerary given a (ignored) list of locations and 
#  context from user's preferences """
import sys

sys.path.append('../')  # Need to traverse one level up before we could traverse down

from concierge_pb2 import (
    DestinationCategory,
    Destination,
    PointOfInterest,
    Address,
    Location,
    LatLng,
)


_pois = [PointOfInterest(id=1,
                         description="Golden Gate Bridge",
                         address=Address(id=1,
                                         location=Location(latLng=LatLng(lat=111.1, lng=222.2)),
                                         city="San Francisco",
                                         state="CA",
                                         country="United States"),
                         ),
         PointOfInterest(id=1,
                         description="Fisherman Wharf",
                         address=Address(id=1,
                                         location=Location(latLng=LatLng(lat=111.1, lng=222.2)),
                                         city="San Francisco",
                                         state="CA",
                                         country="United States"),
                         )
        ]

_destinations = [Destination(id=1,
                             category=DestinationCategory.TOUR,
                             poi=_pois[0]
                            ),
                 Destination(id=1,
                             category=DestinationCategory.TOUR,
                             poi=_pois[1]
                            )
                ]

def recommend(question: str, preferences: str) -> list[Destination]:
    """Return a list of destinations recommended by the Reco Engine"""
    print(f"Mocked recommendation request for question: {question} with preferences: {preferences}")
    return _destinations
