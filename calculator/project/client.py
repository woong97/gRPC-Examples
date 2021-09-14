import grpc
import calculator_pb2
import calculator_pb2_grpc

# Step 1: Create a Channel
channel = grpc.insecure_channel('localhost:80')

# Step 2: Create a Stub
stub = calculator_pb2_grpc.CalculatorStub(channel)

# Step 3: call API
number = calculator_pb2.RequestInfo(lvalue=16, rvalue=10, operator='*')
response = stub.Calculate(number)
print(response.value)