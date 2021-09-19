import grpc
from grpc_generated_files import calculator_pb2, calculator_pb2_grpc

#
# #Step 1: Create a Channel
# channel = grpc.insecure_channel('calculator-1219181542.ap-northeast-2.elb.amazonaws.com:50051')
#
# # Step 2: Create a Stub
# stub = calculator_pb2_grpc.CalculatorStub(channel)
#
# # Step 3: call API
# number = calculator_pb2.RequestInfo(lvalue=16, rvalue=10, operator='/')
# response = stub.Calculate(number)
# print(response.value)
# grpc.insecure_channel('localhost:50051', options=(('grpc.enable_http_proxy', 0),))

with open("ssl_key/server.crt", "rb") as f:
    credentials = grpc.ssl_channel_credentials(f.read())

with grpc.insecure_channel("localhost:50051") as channel:
    stub = calculator_pb2_grpc.CalculatorStub(channel)
    number = calculator_pb2.RequestInfo(lvalue=16, rvalue=10, operator='/')
    response = stub.Calculate(number)
    print(response.value)