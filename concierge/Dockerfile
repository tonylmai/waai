FROM python

RUN mkdir /service
COPY protobuf/ /service/protobuf
COPY concierge/ /service/concierge
WORKDIR /service/concierge
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobuf/concierge.proto

EXPOSE 50051
ENTRYPOINT [ "python", "concierge.py" ]
