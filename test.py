import requests
import json

utterence = 'Hello there!'

# params = {url = "https://mumble.stream/speak", headers: {"Accept": "application/json", "Content-Type": "application/json"}, body: json.dumps({speaker: vocodeVoice, text: utterance})}
#r = requests.post(params)
# r = requests.get('https://mumble.stream/speak',
#                  params={'speaker': 'david-attenborough',
#                          'text': 'Hello there!'},
#                  headers={'Accept': 'application/json', 'Content-Type': 'application/json'})

# print(r.content)
response = requests.post('https://mumble.stream/speak',
                         json={'speaker': 'vegeta',
                               'text': "Your array of bytes won't just be audio data, it all also include the various headers that describe the file."},
                         headers={'Accept': 'application/json', 'Content-Type': 'application/json'})
print(response.content)

with open('myfile.wav', mode='bx') as f:
    f.write(response.content)


# request.post(params, function (error, response, body)
# request.post(params, function (error, response, body)
