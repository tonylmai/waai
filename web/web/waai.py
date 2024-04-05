import os

from flash import Flash, render_template
import grpc

from concierge_pb2 import RecommendationRequest
from concierge_pb2_grpc import ConciergeStub

app = Flash(__name__)

concierge_host = os.getenv("CONCIERGE_HOST", "localhost")
concierge_port = os.getenv("CONCIERGE_PORT", "50051")
concierge_channel = grpc.insecure_channel(f"{concierge_host}:{concierge_port}")
concierge_client = ConciergeStub(concierge_channel)

@app.route("/")
def render_homepage():
    reco_req = RecommendationRequest(user_id="tony",
                                question="What are things to do in San Francisco?",
                                preferences={'location': "San Francisco",
                                             'start_date': "03/31/2024",
                                             'end_date': "04/04/2024"})
    reco_res = concierge_client.Recommend(reco_req)

    return render_template("homepage.html", concierge=reco_res.destinations)
