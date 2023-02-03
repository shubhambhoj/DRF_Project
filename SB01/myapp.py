import requests
URL='http://127.0.0.1:8000/stud_list/'

req=requests.get(url=URL)

data=req.json()

print("Data:",data)