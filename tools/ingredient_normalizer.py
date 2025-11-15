from typing import List


UNIT_MAP = {
'kg': 1000,
'g': 1,
'l': 1000,
}




def normalize_ingredients(ingredients: List[dict]) -> List[dict]:
"""Very simple normalization: lowercase names and keep qty string.
Real implementation should parse quantities and convert to standard units.
"""
normalized = []
for i in ingredients:
name = i.get('name','').strip().lower()
qty = i.get('qty','')
normalized.append({'name': name, 'qty': qty})
return normalized
