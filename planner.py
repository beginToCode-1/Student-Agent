from agent import StudentAgent
def generate_plan(agent):
    plan = []

    for subject, topics in agent.subjects.items():
        for topic, data in topics.items():
            if data["confidence"] > 0.85:
               continue
 
           # if topic in agent.completed:
            #    continue
            if data == "easy":
                hours_needed = 1
            elif data == "medium":
                hours_needed = 2
            else:  # hard
                hours_needed = 3

            plan.append((subject, topic, hours_needed))


    return plan   