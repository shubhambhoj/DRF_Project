import requests
import json

URL="http://127.0.0.1:8000/stud/"
def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    req=requests.get(url=URL,data=json_data)
    data=req.json()
    print("DATA: ",data)

#get_data()
#get_data(2)

def post_data():
    data={
        'name':'shubham',
        'roll':103,
        'city':'satara'
    }
    json_data=json.dumps(data)
    req=requests.post(url=URL,data=json_data)
    data=req.json()
    print("DATA: ",data)

#post_data()

def update_data():
    data={
        'id':1,
        'name':'shiv',
        #'roll':101,
        'city':'nagpur'
    }
    json_data=json.dumps(data)
    req=requests.put(url=URL, data=json_data)
    data=req.json()
    print('DATA: ',data)

#update_data()

def delete_data():
    data={'id':3}
    json_data=json.dumps(data)
    req=requests.delete(url=URL, data=json_data)
    data=req.json()
    print("DATA: ",data)    

delete_data()