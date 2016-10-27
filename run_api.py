import requests
data = open('output.txt', 'rb').read()
response = requests.post(url='https://vision.googleapis.com/v1/images:annotate?key=AIzaSyCcczu2Kj2NvCkiRsWTZO_qbsgolfx9gCk',
data=data,
headers={'Content-Type': 'application/json'})

print response.text
