import grpc
from concurrent import futures
import hello_pb2
import hello_pb2_grpc

class HelloService(hello_pb2_grpc.HelloServiceServicer):

    def SayHello(self, request, context):
        print("Service A received:", request.name)
        return hello_pb2.HelloResponse(
            message=f"Hello {request.name} from Service A (gRPC)"
        )
    def AddNumbers(self, request, context):
        print(f"Service A received numbers: {request.num1} and {request.num2}")
        result = request.num1 + request.num2
        return hello_pb2.AddResponse(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_HelloServiceServicer_to_server(
        HelloService(),server
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Service A gRPC running on port 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()