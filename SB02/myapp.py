import requests
import json
URL="http://127.0.0.1:8000/stud/"

data={
    'name':'suraj',
    'roll':106,
    'city':'vaduth'
}

json_data=json.dumps(data)

req=requests.post(url=URL,data=json_data)

data=req.json()

print('data:',data)