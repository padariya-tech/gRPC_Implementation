import grpc
import hello_pb2
import hello_pb2_grpc

def call_service_a():

    channel = grpc.insecure_channel("localhost:50051")
    stub = hello_pb2_grpc.HelloServiceStub(channel)

    response = stub.SayHello(
        hello_pb2.HelloRequest(name="Nij")
    )

    print("Response from Service A:", response.message)

if __name__ == "__main__":
    call_service_a()