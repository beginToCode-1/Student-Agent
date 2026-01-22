from agent import StudentAgent
def generate_plan(agent):
    plan = []

    for subject, topics in agent.subjects.items():
        for topic, difficulty in topics.items():
            if topic in agent.completed:
                continue
            if difficulty == "easy":
                hours_needed = 1
            elif difficulty == "medium":
                hours_needed = 2
            else:  # hard
                hours_needed = 3

            plan.append((subject, topic, hours_needed))


    return plan   