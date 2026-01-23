from agent import StudentAgent
from planner import generate_plan

agent = StudentAgent()

while True:
    print("\n===== Study Planner AI =====")
    print("1. Add study topic")
    print("2. Generate study plan")
    print("5. Exit")

    choice = input("Choose: ").strip()

    if choice == "1":
        subject = input("Subject name: ")
        topic = input("Topic name: ")
        difficulty = input("Difficulty (easy/medium/hard): ")

        agent.add_topic(subject, topic, difficulty)
        print("Topic added.")

    elif choice == "2":
        plan = generate_plan(agent)
        print("\nYour Study Plan:")
        for subject, topic, hours in plan:
            print(f"- {subject} - {topic}: {hours} hour(s)")

    elif choice == "5":
        print("Bye.")
        break

    else:
        print("Invalid choice.")
