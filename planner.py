
def generate_plan(agent):
    plan = []
    remaining_hours = agent.hours_per_day

    difficulty_weight = {
        "hard": 3,
        "medium": 2,
        "easy": 1
    }

    tasks = []

    for subject, topics in agent.subjects.items():
        for topic, info in topics.items():

         if topic in agent.completed:
            continue

        base = difficulty_weight.get(info["difficulty"], 2)
        penalty = 1 - info["confidence"]
        priority = base + penalty

        tasks.append((priority, subject, topic, info))


    # Sort by priority (hard first)
    tasks.sort(reverse=True)

    for priority, subject, topic, difficulty in tasks:
        hours_needed = {
            "hard": 3,
            "medium": 2,
            "easy": 1
        }.get(difficulty, 2)

        if hours_needed <= remaining_hours:
            plan.append((subject, topic, hours_needed))
            remaining_hours -= hours_needed

        if remaining_hours == 0:
            break

    return plan
