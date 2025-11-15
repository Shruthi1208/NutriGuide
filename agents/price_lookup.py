import time
from concurrent.futures import ThreadPoolExecutor


class PriceLookupAgent:
def __init__(self, search_client=None):
self.search = search_client


def _mock_price_for(self, item):
# deterministic mock price by item name length
base = 40 + (len(item['name']) * 3)
# small sleep to simulate network
time.sleep(0.05)
return {'name': item['name'], 'qty': item['qty'], 'price': round(base, 2)}


def lookup_prices(self, items: list) -> list:
# run in parallel to simulate parallel agents
with ThreadPoolExecutor(max_workers=4) as ex:
results = list(ex.map(self._mock_price_for, items))
return results
