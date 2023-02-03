import requests
import json

URL="http://127.0.0.1:8000/stud/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print("DATA:",data)

#get_data()
#get_data(1)

def post_data():
    '''
    data={
        'name':input("Enter Name Of Student: "),
        'roll':int(input("Enter Rol Number Of Student: ")),
        'city':input("Enter City Of Student: ")
    }
    '''
    data={
        'name':'shubham',
        'roll':109,
        'city':'satara'
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)
    d=r.json()
    print("DATA:",d)

#post_data()

def update_data():
    data={
        'id':9,
        'name':'shubham',
        #'roll':107,
        'city':'pune'
    }
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    d=r.json()
    print("DATA:",d)

#update_data()

def delete_data():
    data={'id':9}
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    d=r.json()
    print("DATA:",d)

delete_data()


