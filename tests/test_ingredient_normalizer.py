# tests/test_ingredient_normalizer.py
from tools.ingredient_normalizer import normalize_ingredients




def test_normalize_basic():
data = [{'name':'Rice','qty':'1 kg'},{'name':'Paneer','qty':'500 g'}]
out = normalize_ingredients(data)
assert out[0]['name'] == 'rice'
assert out[1]['name'] == 'paneer'
