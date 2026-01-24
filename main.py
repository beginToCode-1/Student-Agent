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
        subject = input("Subject name: ").strip().title()
        topic = input("Topic name: ").strip().title()

        # Difficulty validation
        while True:
            difficulty = input("Difficulty (easy/medium/hard): ").lower()
            if difficulty in ["easy", "medium", "hard"]:
                break
            print("Invalid difficulty. Please enter easy, medium, or hard.")

            agent.add_topic(subject, topic, difficulty)
            print("Topic added successfully.")

    elif choice == "2":
        plan = generate_plan(agent)
        print("\nYour Study Plan:")

        if not plan:
            print("No topics to study. You're either done or your data is broken.")
        else:
            for subject, topic, hours in plan:
                print(f"- {subject} → {topic}: {hours} hour(s)")

    elif choice == "5":
        print("Bye.")
        break

    else:
        print("Invalid choice.")
     