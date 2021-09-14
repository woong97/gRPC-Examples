try:
    import grpc
    from concurrent import futures
    import time
    import calculator
    import calculator_pb2       #This are File GRPC Gegerated for me
    import calculator_pb2_grpc  #This are File GRPC Gegerated for me
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
    print('Starting server. Listening on port 80')
    server.add_insecure_port('[::]:80')
    server.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    run()