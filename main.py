from agent import StudentAgent
from planner import generate_plan

agent = StudentAgent()
agent.add_subject("Chemistry")
agent.add_topic("Chemistry", "Organic Chemistry", "hard")
agent.add_topic("Chemistry", "Inorganic Chemistry", "medium")



plan = generate_plan(agent)

for item in plan:
    print(item)