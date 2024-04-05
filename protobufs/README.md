## Protobufs
```
cd protobuf
python -m grpc_tools.protoc -I . --python_out=./concierge --grpc_python_out=./concierge ./concierge.proto

#### where
* -I ../model/protobuf is where to find the protobuf file and its imports
* --python_out=../model is where to put the model file
* --grpc_python_out=../model is where to put the grpc file
```
