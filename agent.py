import json
import os


class StudentAgent:
    def __init__(self, filename ="student_data.txt"):
        self.filename = filename
        self.subjects = {}        # {subject: {topic: difficulty}}
        self.completed = set()
        self.hours_per_day = 4
        self.load_data() # for loading old memory from disk


    def mark_completed(self, topic):
        self.completed.add(topic)

 # new code:
    def add_topic(self, subject, topic, difficulty):
        subject = subject.strip().lower()
        topic = topic.strip().lower()
        difficulty = difficulty.strip().lower()

        if subject not in self.subjects:
          self.subjects[subject] = {}

        self.subjects[subject][topic] = {
        "difficulty": difficulty,
        "confidence": 0.5,
        "attempts": 0
    }
#showing status of the topics:
    def show_status(self):
        print("\nCurrent topics:")
        for subject, topics in self.subjects.items():
            for topic, diff in topics.items():
                status = "DONE" if topic in self.completed else "PENDING"
                print(f"- {subject} | {topic} | {diff} | {status}")
#saving data using json format:
    def save_data(self):
        data ={
            "subjects": self.subjects,
            "completed": list(self.completed)# Convert set to list cuz JSON doesn't support sets   
        }
        with open(self.filename, 'w') as f:
            import json
            json.dump(data, f, indent=4)
#loading data from disk:
    def load_data(self):
        if not os.path.exists(self.filename):
            return
        
        with open(self.filename, 'r') as f:
            data =json.load(f)
            
            self.subjects = data.get("subjects", {})
            self.completed = set(data.get("completed", []))
#giving feedback to the user about the topic:
    def give_feedback(self, topic, feedback):
        topic = topic.strip().lower()

        for subject, topics in self.subjects.items():
          if topic in topics:
            info = topics[topic]

            info["attempts"] += 1

            if feedback == "done":
                info["confidence"] = min(1.0, info["confidence"] + 0.2)
            elif feedback == "hard":
                info["confidence"] = max(0.0, info["confidence"] - 0.2)

            self._adjust_difficulty(info)
            print("Feedback recorded.")
            return

        print("Topic not found. Check spelling.")


    def _adjust_difficulty(self, info):
           if info["confidence"] < 0.3:
             info["difficulty"] = "hard"
           elif info["confidence"] < 0.6:
             info["difficulty"] = "medium"
           else:
             info["difficulty"] = "easy"
    