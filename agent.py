class StudentAgent:
    def __init__(self):
        self.subjects = {}        # {subject: {topic: difficulty}}
        self.completed = set()

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
