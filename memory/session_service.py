import json
from pathlib import Path


MEM_FILE = Path(__file__).resolve().parent / 'memory_bank.json'


class SessionService:
def __init__(self):
MEM_FILE.parent.mkdir(parents=True, exist_ok=True)
if not MEM_FILE.exists():
MEM_FILE.write_text('{}')


def save(self, user_id: str, data: dict):
content = json.loads(MEM_FILE.read_text())
content[user_id] = data
MEM_FILE.write_text(json.dumps(content, indent=2))


def load(self, user_id: str):
content = json.loads(MEM_FILE.read_text())
return content.get(user_id)
