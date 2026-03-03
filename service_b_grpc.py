import grpc
import hello_pb2
import hello_pb2_grpc

def call_service_a():

    channel = grpc.insecure_channel("localhost:50051")
    stub = hello_pb2_grpc.HelloServiceStub(channel)

    response1 = stub.SayHello(
        hello_pb2.HelloRequest(name="Nij")
    )

    print("Response1 from Service A:", response1.message)

    
    response2 = stub.AddNumbers(
        hello_pb2.AddRequest(num1=10, num2=20)
    )
    print("Response2 from Service A:", response2.result)


if __name__ == "__main__":
    call_service_a()