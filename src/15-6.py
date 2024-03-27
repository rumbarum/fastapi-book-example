import requests

url = "http://localhost:8000/big"
files = {"big_file": open("1GB.bin", "rb")}
resp = requests.post(url, files=files)
print(resp.json())
