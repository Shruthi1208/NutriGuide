import copy
import logging


logger = logging.getLogger(__name__)


class OptimizerAgent:
def __init__(self, max_iters=5):
self.max_iters = max_iters


def _estimate_total(self, prices):
return sum(p['price'] for p in prices)


def optimize(self, plan, grocery_list, prices, constraints):
# Very simple optimizer: if total > budget, reduce paneer qty
best = {
'plan': plan,
'grocery': grocery_list,
'prices': prices,
'total': self._estimate_total(prices)
}
iter_count = 0
while best['total'] > constraints.get('budget', 999999) and iter_count < self.max_iters:
logger.info(f"Optimization iter {iter_count}, total={best['total']}")
# find paneer and reduce
changed = False
for g in best['grocery']:
if g['name'] == 'paneer' and isinstance(g.get('qty'), str):
# crude reduce: change 1kg -> 500g
if '1 kg' in g['qty']:
g['qty'] = g['qty'].replace('1 kg','500 g')
changed = True
if not changed:
# fallback: reduce expensive item price by 15%
for p in best['prices']:
p['price'] = round(p['price'] * 0.85, 2)
best['total'] = self._estimate_total(best['prices'])
iter_count += 1
best['iterations'] = iter_count
return best
