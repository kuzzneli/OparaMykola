import json
file = open('info.json')
text = ' { "x": 100 } '
dictionary = json.load(file)

print(dictionary)
