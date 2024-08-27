import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.json())

payload = {
    "name": "John Doe",
    "job": "Software Engineer"
}

response = requests.post("https://reqres.in/api/users", json=payload)
print(response.json())