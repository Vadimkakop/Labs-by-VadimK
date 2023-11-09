import json
FILENAME = 'input.json'


def task() -> float:
    with open(FILENAME) as file:
        data = json.load(file)
    return round(sum([i['score'] * i['weight'] for i in data]), 3)


print(task())
