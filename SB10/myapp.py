import requests
import json

URL="http://127.0.0.1:8000/stud/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    headers={'content-type':'application/json'}
    json_data=json.dumps(data)
    req=requests.get(url=URL, headers=headers,data=json_data)
    msg=req.json()
    print("msg: ", msg)

#get_data()
#get_data(2)

def post_data():
    data={
        'name':'ramesh',
        'roll':104,
        'city':'pune'
    }

    headers={'content-type':'application/json'}
    json_data=json.dumps(data)
    req=requests.post(url=URL, headers=headers, data=json_data)
    msg=req.json()
    print("msg: ", msg)

#post_data()

def update_data():
    data={
        "id":4,
        "name":"ram",
        #'roll':104,
        "city":"thane"
    }
    headers={'content-type':'application/json'}
    json_data=json.dumps(data)
    req=requests.put(url=URL, headers=headers,data=json_data)
    msg=req.json()
    print('msg: ', msg)

#update_data()

def delete_data():
    data={'id':4}
    headers={'content-type':'application/json'}
    json_data=json.dumps(data)
    req=requests.delete(url=URL, headers=headers,data=json_data)
    msg=req.json()
    print("msg: ", msg)

delete_data()
