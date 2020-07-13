import json

f = open("TokenLibrary/Python/PythonTokens.json","r")
jsonPy = json.load(f)
f.close()

print(jsonPy)

if "+" in jsonPy:
    print(jsonPy["+"].key)
else:
    print("\nNot found")

