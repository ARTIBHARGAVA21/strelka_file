import json
data={}

res=response.json()

#customization formating to json 
for key, value in res.item():
    if key=="file_id":
        data['file_id']=value
    elif key=="meta":
        data['meta']=value
    elif key=="response":
        data['response']=value
        with open("response.json","w") as f:
            f.writelines(json.dumps(data,indent=4))

# define response json data  only the content of the file
    if key=="response":
        data['file']=value[0]['file']
        data['scan']['hash']=value[0]['scan']['hash']


# define subkey and subvalue

    for subkey, subvalue in value[0]['file']:
           print(subkey,subvalue)
           with open("file.json", 'w') as f:
               f.writelines(json.dumps(value[0]['file'],indent=4))

# define only open file
           with open("file.json", 'w') as f:
               f.writelines(json.dumps(res,indent=4))

#define file inner data
    # if key=="response":
    #     with open("response.json", 'w') as f:
    #         f.writelines(json.dumps(value[0]['file'], indent=4))


#define for loop json

for key, value in res.item():
    if key=="response":
        with open("response.json", 'w') as f:
            f.writelines(json.dump(value[0]['file'], indent=4))

def Scanningimage(filename, api, outputfilename):
    try:
        with open(filename, "r") as f:
            f.read()

        res=response.json()
        my_data={}
        for key, value in res.items():
            if key=="file_id":
             my_data['file_id']=value
            elif key=="meta":
             my_data['meta']=value
            elif key=="response":
             my_data['response']=value
             with open(outputfilename, 'w') as f:
                 f.writelines(json.dump(my_data,indent=4))
        Scanningimage.close()
    except Exception as e:
        print(e)
        return 1
    
def Scanningimage(filename, api, outputfilename):
    try:
        with open(filename, "r") as f:
            f.read()
        for key, value in res.items():
            if key=="file_id":
                

        Scanningimage.close()
    except Exception as e:
        print(e)
        return 1



