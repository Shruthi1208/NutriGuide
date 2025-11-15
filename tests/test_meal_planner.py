from agents.meal_planner import MealPlannerAgent




def test_generate_plan_contains_week():
mp = MealPlannerAgent()
plan = mp.generate_plan({'dislikes': []})
assert 'week' in plan
assert len(plan['week']) == 7
