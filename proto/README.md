## Protobufs
```
python -m grpc_tools.protoc -I . --python_out=./python --grpc_python_out=./python --mypy_out=. ./concierge.proto

#### where
* -I ./ is where to find the protobuf file and its imports
* --python_out=./python is where to put the model file
* --grpc_python_out=./python is where to put the grpc file
* --mypy_out=. is where to put mypy output
```
