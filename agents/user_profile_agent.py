import json
from pathlib import Path


MEMORY_FILE = Path(__file__).resolve().parents[1] / 'memory' / 'memory_bank.json'


class UserProfileAgent:
def __init__(self):
MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
if not MEMORY_FILE.exists():
MEMORY_FILE.write_text("{}")


def create_demo_user(self):
user = {
'user_id': 'demo',
'preferences': {
'likes': ['rice', 'paneer'],
'dislikes': ['mushroom'],
'diet': 'vegetarian'
},
'constraints': {
'budget': 1500, # currency rupees
'meals_per_day': 3
}
}
self._save_user(user)
return user


def _save_user(self, user):
existing = json.loads(MEMORY_FILE.read_text())
existing[user['user_id']] = user
MEMORY_FILE.write_text(json.dumps(existing, indent=2))


def load_user(self, user_id: str):
existing = json.loads(MEMORY_FILE.read_text())
return existing.get(user_id)
