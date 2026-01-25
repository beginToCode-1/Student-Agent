
def generate_plan(agent):
    plan = []

    for subject, topics in agent.subjects.items():
        for topic, difficulty in topics.items():

            if topic in agent.completed:
                continue

            hours = {
                "easy": 1,
                "medium": 2,
                "hard": 3
            }.get(difficulty, 2)

            plan.append((subject, topic, hours))

    return plan
