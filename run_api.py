import requests
import generatejson
import json
import time

with open("input.txt", 'r') as input_file:

    out = ""
    for i,line in enumerate(input_file):
        image_filename, features, id = line.lstrip().split(' ', 2)

        try:
            data = generatejson.main(image_filename, features)
            response = requests.post(url='https://vision.googleapis.com/v1/images:annotate?key=AIzaSyBBpVtsrJ2HPE9KKEwZyTrmwI-pPSBXtYA',

            data=data[0],
            headers={'Content-Type': 'application/json'})

            if i%10==0:
                print i
            
            #print json.dumps(json.loads(response.text))
            out += json.dumps(json.loads(response.text))+"\t"+str(id)+"\n"

        except:
            print str(id)+" can't find image'"
            out += "nan\t"+str(id)+"\n"


        '''    response = requests.post(url='https://vision.googleapis.com/v1/images:annotate?key=AIzaSyCcczu2Kj2NvCkiRsWTZO_qbsgolfx9gCk','''
        
        time.sleep(0.01) # delays for 5 seconds


    with open("pittsburgh_vision.txt", "w") as text_file:
        text_file.write(out)

