from agent import StudentAgent
from planner import generate_plan

agent = StudentAgent()
#Currnent Menu

while True:
    print("\n1. Add topic")
    print("2. Generate plan")
    print("3. Mark completed")
    print("4. Show status")
    print("5. Give feedback")
    print("6. Save and exit")
    

    choice = input("Choose: ")

    if choice == "1":
        s = input("Subject: ")
        t = input("Topic: ")
        d = input("Difficulty (easy/medium/hard): ")
        agent.add_topic(s, t, d)

    elif choice == "2":
        plan = generate_plan(agent)
        if not plan:
            print("No pending topics.")
        else:
            print("\nStudy Plan:")
            for item in plan:
                print(item)

    elif choice == "3":
        t = input("Topic name: ")
        agent.mark_completed(t)

    elif choice == "4":
        agent.show_status()

    elif choice == "5":
     topic = input("Topic name: ")
     feedback = input("Feedback (done / hard): ")
     agent.give_feedback(topic, feedback)
    
    elif choice == "6":
        agent.save_data()
        print("Data saved. Goodbye!")
        break

 

