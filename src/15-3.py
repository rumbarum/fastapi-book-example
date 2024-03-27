import requests

url = "http://localhost:8000/small"
files = {"small_file": open("1KB.bin", "rb")}
resp = requests.post(url, files=files)
print(resp.json())
