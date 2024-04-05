FROM python

RUN mkdir /service
COPY protobuf/ /service/protobuf/
COPY waai/ /service/waai/
WORKDIR /service/waai
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobuf --python_out=. grpc_python_out=. ../protobuf/concierge.protoc

EXPOSE 5000
ENV FLASH_APP=concierge.py
ENTRYPOINT [ "flash", "run", "--host=0.0.0.0" ]
