from typing import Dict


class MealPlannerAgent:
"""Simple meal planner. Replace `plan_logic` with LLM prompt calls in production."""


def __init__(self, llm_client=None):
self.llm = llm_client


def generate_plan(self, preferences: Dict) -> Dict:
# For demo purposes we return a hard-coded 7-day plan influenced by preferences
base = [
{"day": "Monday", "breakfast": "Oats + Banana", "lunch": "Paneer Rice Bowl", "dinner": "Dal Khichdi"},
{"day": "Tuesday", "breakfast": "Poha", "lunch": "Chole Rice", "dinner": "Grilled Paneer Wrap"},
{"day": "Wednesday", "breakfast": "Idli + Sambar", "lunch": "Veg Pulao", "dinner": "Palak Paneer"},
{"day": "Thursday", "breakfast": "Upma", "lunch": "Rajma Rice", "dinner": "Mixed Veg Curry + Rice"},
{"day": "Friday", "breakfast": "Smoothie Bowl", "lunch": "Paneer Bhurji + Roti", "dinner": "Vegetable Stir Fry"},
{"day": "Saturday", "breakfast": "French Toast", "lunch": "Lemon Rice + Curd", "dinner": "Veg Biryani"},
{"day": "Sunday", "breakfast": "Paratha", "lunch": "Sambar Rice", "dinner": "Paneer Butter Masala + Rice"},
]
# Simple preference filtering: remove dishes containing dislikes
dislikes = set(preferences.get('dislikes', []))
for d in base:
for meal in ['breakfast','lunch','dinner']:
if any(bad in d[meal].lower() for bad in dislikes):
d[meal] = d[meal] + ' (modified)'
return {"week": base}
