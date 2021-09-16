FROM python:3.7
RUN pip install protobuf grpcio

COPY ./grpcserver ./app
WORKDIR ./app
CMD python server.py
EXPOSE 50051