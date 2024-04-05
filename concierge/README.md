# concierge
AI Concierge


## Getting Started

### Prerequisites
#### Anaconda
1. Download
```
https://www.anaconda.com/download
```

## Protobufs
```
cd protobuf
python -m grpc_tools.protoc -I . --python_out=../protobuf --grpc_python_out=../protobuf ./concierge.proto

#### where
* -I ../model/protobuf is where to find the protobuf file and its imports
* --python_out=../model is where to put the model file
* --grpc_python_out=../model is where to put the grpc file
```

### Installing

## To build Docker image
```
docker build . -f concierge/Dockerfile -t concierge
```

## Running
```
```docker run -p 127.0.0.1:50051:50051/tcp concierge
```

## Creating proxy
```
docker network create microservices
```

And
```
docker run -p 127.0.0.1:50051:50051/tcp --network microservices --name concierge concierge
```





