try:
    import grpc
    from concurrent import futures
    import time
    from function import calculator
    from grpc_generated_files import calculator_pb2, calculator_pb2_grpc  #This are File GRPC Gegerated for me
except Exception as e:
    print("error loading modules")


class CalcuatorServicer(calculator_pb2_grpc.CalculatorServicer):

    def Calculate(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.calculate(
                                lvalue=request.lvalue,
                                rvalue=request.rvalue,
                                operator=request.operator
                        )
        return response


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalcuatorServicer(), server)
    print('Starting server. Listening on port 50051')

    with open("./ssl_key/server.key", "rb") as f:
        private_key = f.read()
    with open("./ssl_key/server.crt", "rb") as f:
        certificate_chain = f.read()
    server_credentials = grpc.ssl_server_credentials(((private_key, certificate_chain,),))
    server.add_secure_port('[::]:50051', server_credentials)

    # server.add_insecure_port('[::]:50051')
    server.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    run()