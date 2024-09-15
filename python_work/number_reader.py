from pathlib import Path
import json

username = input('whats your name?')

path = Path('username.json')

contents = json.dumps(username)

path.write_text(contents)

print(f'well remember you {username}')