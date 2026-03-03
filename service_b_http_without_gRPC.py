import requests

def call_service_a():
    response = requests.get(
        "http://localhost:8000/hello",
        params={"name": "nij"}
    )

    print("Response from Service A:", response.json())

if __name__ == "__main__":
    call_service_a()