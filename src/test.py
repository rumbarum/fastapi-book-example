# 3-5
import requests

r = requests.get("http://localhost:8000/hi")
assert "Hello? World?" == r.json()

# 3-6
import httpx

r = httpx.get("http://localhost:8000/hi")
assert "Hello? World?" == r.json()

# 3-14
import requests

r = requests.get("http://localhost:8000/hi/Mom")
assert "Hello? Mom?" == r.json()

# 3-19
import requests

r = requests.get("http://localhost:8000/hi?who=Mom")
assert "Hello? Mom?" == r.json()

# 3-20
import requests

params = {"who": "Mom"}
r = requests.get("http://localhost:8000/hi", params=params)
assert "Hello? Mom?" == r.json()

# 3-23
import requests

r = requests.post("http://localhost:8000/hi", json={"who": "Mom"})
assert "Hello? Mom?" == r.json()
