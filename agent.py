import json
import os


class StudentAgent:
    def __init__(self, filename ="data/student_data.txt"):
        self.filename = filename
        self.subjects = {}        # {subject: {topic: difficulty}}
        self.completed = set()
        self.load_data()

    def add_topic(self, subject, topic, difficulty):
        if subject not in self.subjects:
            self.subjects[subject] = {}

        self.subjects[subject][topic] = difficulty.lower()

    def mark_completed(self, topic):
        self.completed.add(topic)

    def show_status(self):
        print("\nCurrent topics:")
        for subject, topics in self.subjects.items():
            for topic, diff in topics.items():
                status = "DONE" if topic in self.completed else "PENDING"
                print(f"- {subject} | {topic} | {diff} | {status}")

    def save_data(self):
        data ={
            "subjects": self.subjects,
            "completed": list(self.completed)
        }
        with open(self.filename, 'w') as f:
            import json
            json.dump(data, f, indent=4)
    
    def load_data(self):
        if not os.path.exists(self.filename):
            return
        
        with open(self.filename, 'r') as f:
            data =json.load(f)
            
            self.subjects = data.get("subjects", {})
            self.completed = set(data.get("completed", []))