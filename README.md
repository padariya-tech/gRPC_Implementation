Service B ---gRPC--> Service A

Step 1 — Install gRPC
    ```pip install grpcio grpcio-tools```

Step 2 — Create Proto File
    ```hello.proto```

Step 3 — Generate gRPC Code
    ``` python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. hello.proto ```