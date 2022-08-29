import json
x = [1, 'simple', 'list']
print(json.dumps(x))

json.dump(x, f)
x = json.load(f)