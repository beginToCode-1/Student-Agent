from agent import StudentAgent
agent = StudentAgent()
agent.add_subject("Chemistry")
agent.add_topic("Chemistry", "Organic Chemistry", "medium")
print("Updated subjects:", agent.subjects)
