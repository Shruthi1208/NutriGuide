# NutriGuide – AI-Powered Meal Planning Multi-Agent System

## 🧩 1. Problem Statement

Meal planning is time-consuming, especially for students and busy individuals who struggle with:

* deciding what to cook every day,
* generating balanced meal plans,
* sticking to a weekly budget,
* creating grocery lists,
* comparing real-time prices across stores.

This leads to overspending, unhealthy choices, and high mental load.

**NutriGuide solves this by fully automating weekly meal planning using a multi-agent system.**

---

## 🤖 2. Why Agents?

Traditional scripts can plan meals, but **cannot coordinate tasks** like:

* planning meals based on preferences,
* optimizing cost and nutrition,
* fetching real-time prices,
* generating structured outputs.

Agents excel at **collaboration, reasoning, and specialization**:

* Planner Agent → builds meals
* Nutrition Agent → checks nutritional balance
* Price Agent → fetches store prices (Google Search Tool)
* Optimizer Agent → adjusts plan to fit budget
* Grocery Agent → generates final list

Each agent works independently but communicates through **sequential workflows**, making the system modular, scalable, and maintainable.

---

## 🏗️ 3. System Architecture

### **⚙️ Multi-Agent Workflow**

```
User → Session Manager → Planner Agent → Nutrition Agent → Price Agent → Optimizer Agent → Grocery Agent → Final Output
```

### **Key Concepts Used**

* **Sequential Agents** – pipeline architecture for meal → nutrition → price → optimization
* **Parallel Agents** – price checking across multiple stores
* **Loop Agent** – optimizer iterates until budget is satisfied
* **Tools** – Google Search, Code Execution, custom normalization tool
* **Session Memory** – stores user preferences and budget
* **Observability** – logging and trace IDs
* **Context Engineering** – compacted summaries of previous runs

---

## 🧪 4. Demo Workflow

1. User enters:

   * cuisine preferences
   * allergies
   * weekly budget
   * number of meals

2. Planner Agent produces 7-day meals.

3. Nutrition Agent validates:

   * calories
   * protein
   * carbs & fiber

4. Price Agent fetches estimated prices using Google Search Tool.

5. Optimizer Agent loops until the plan meets the budget.

6. Grocery Agent generates:

   * categorized list
   * total cost
   * preparation time

### **Final Output Example**

* Weekly meal plan with macros
* Optimized grocery list under user’s budget
* Price comparison chart

---

## 🏗️ 5. Build Details

### **Tech Stack**

* **Python 3.10**
* **Google Agent Framework (Gemini Agents)**
* **Google Search Tool API**
* **InMemorySessionService** (for session state)
* **Custom Tools:**

  * `ingredient_normalizer` – cleans and standardizes ingredients
* **Observability:**

  * built-in tracing
  * debug logs

---

## 📂 6. Repository Structure

```
nutriguide/
│
├── agents/
│   ├── planner_agent.py
│   ├── nutrition_agent.py
│   ├── price_agent.py
│   ├── optimizer_agent.py
│   └── grocery_agent.py
│
├── tools/
│   └── ingredient_normalizer.py
│
├── services/
│   └── session_manager.py
│
├── main.py
├── README.md
└── requirements.txt
```

---

## 🚀 7. Setup Instructions

### **1. Clone the repo**

```
git clone https://github.com/Shruthi1208/NutriGuide
cd NutriGuide
```

### **2. Install dependencies**

```
pip install -r requirements.txt
```

### **3. Run the application**

```
python main.py
```

---

## 🧭 8. Future Improvements

* Add live store APIs (BigBasket, Blinkit)
* Add weekly calorie tracking charts
* Deploy to Cloud Run with FastAPI wrapper
* Add voice-based interaction agent
* Multi-language meal planners

---

## ✨ Summary

NutriGuide is a fully functioning **multi-agent system** that automates the entire meal planning workflow using:

* LLM-powered agents
* custom tools
* sequential & parallel workflows
* memory & context management
* observability & logging

It is built for the **Concierge Agent Track** and designed to be production-ready.
