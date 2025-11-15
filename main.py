import json
import logging
from agents.user_profile_agent import UserProfileAgent
from agents.meal_planner import MealPlannerAgent
from agents.grocery_agent import GroceryAgent
from agents.price_lookup import PriceLookupAgent
from agents.optimizer_agent import OptimizerAgent


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("nutriguide")




def demo_flow():
logger.info("Starting NutriGuide demo flow")


user_agent = UserProfileAgent()
user = user_agent.create_demo_user()


planner = MealPlannerAgent()
plan = planner.generate_plan(user['preferences'])
logger.info("Generated meal plan")


grocery_agent = GroceryAgent()
grocery_list = grocery_agent.from_plan(plan)
logger.info("Built grocery list")


price_agent = PriceLookupAgent()
prices = price_agent.lookup_prices(grocery_list)
logger.info("Fetched prices")


optimizer = OptimizerAgent()
final = optimizer.optimize(plan, grocery_list, prices, user['constraints'])
logger.info("Optimization complete")


print(json.dumps(final, indent=2))




if __name__ == '__main__':
demo_flow()
