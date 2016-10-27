import requests
import generatejson

with open("input.txt", 'r') as input_file:
    data = generatejson.main(input_file)

    response = requests.post(url='https://vision.googleapis.com/v1/images:annotate?key=AIzaSyCcczu2Kj2NvCkiRsWTZO_qbsgolfx9gCk',
    data=data,
    headers={'Content-Type': 'application/json'})

    print response.text
