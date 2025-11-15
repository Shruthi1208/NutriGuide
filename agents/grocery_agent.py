from tools.ingredient_normalizer import normalize_ingredients


class GroceryAgent:
def from_plan(self, plan: dict) -> list:
# naive mapping for demo; in real system parse recipes to ingredients
# return list of dicts: {name, qty}
sample = [
{"name": "rice", "qty": "2 kg"},
{"name": "paneer", "qty": "1 kg"},
{"name": "oats", "qty": "500 g"},
{"name": "milk", "qty": "2 L"},
{"name": "tomato", "qty": "1 kg"},
]
return normalize_ingredients(sample)
