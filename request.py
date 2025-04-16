import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')
url_base="http://192.168.32.129:9980/api/strelka"

# Define headers
headers = {"X-API-KEY": api_key,
           "Content-Type": "application/json",
           "Accept": "application/json"
           }


url_route = "/scans?page=1&per_page=10"
response = requests.get(url_base + url_route, headers=headers)

if response.status_code==200:
      print("response.text")
else:
      print(f"Error:{response.status_code}-{response.text}")



url_route="/upload"
filename="sample.txt"
description="This is a Sample file"

headers = {"X-API-KEY": api_key,
           }

with open(filename, "rb") as f:
    file_data = f.read()
files = [("file", (filename, file_data))]
data = {"description": description, "password": ""}
response = requests.post(url_base + url_route, files=files, data=data, headers=headers)
my_data={}
if response.status_code==200:  
    res = response.json()
    for key, value in res.items():
            if key == "file_id":
                my_data['file_id']=value
            elif key == "meta":
                my_data['meta']=value
            elif key =="response":
                 my_data['response']=value
            with open('response.json', 'w') as f:
              f.writelines(json.dumps(my_data,indent=4)) 
    print("Data successfully saved in response.json file")             
else:
    print(f"Error: {response.status_code} - {response.text}") 


