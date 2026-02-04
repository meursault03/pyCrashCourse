from pathlib import Path
import json

user_dict = {'name': 'Jeff', 'age': 25, 'city': 'New York'}
path = Path("user_info.json")
contents = path.write_text(json.dumps(user_dict))

loaded_json = json.loads(path.read_text())

for key, value in user_dict.items():
    print(f"{key.title()}: {value}")


