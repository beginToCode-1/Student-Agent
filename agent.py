class StudentAgent :
    #added some of the initial subjects and topics.
    def __init__(self):
        self.subjects = {
    "Math": {
        "Algebra": {
            "difficulty": "hard",
            "confidence": 0.4,
            "attempts": 1
        }
    }
}

        self.completed = set({"Algebra", "Motion"})
        self.hours_per_day = 4  
        
        #adding methods to add subjects and topics   
    def add_subject(self, subject,):
           if subject not in self.subjects:
             self.subjects[subject] = {}
           
             #adding method to add topics to subjects
    def add_topic(self, subject, topic, difficulty):
           if subject not in self.subjects:
            self.subjects[subject] = {}

           self.subjects[subject][topic] = {
        "difficulty": difficulty,
        "confidence": 0.5,
        "attempts": 0
    }


   # def add_topic(self, subject, topic, difficulty):
            #  if subject in self.subjects:
             #   self.subjects[subject][topic] = difficulty
           
             #adding method to give feedback on topics
    def give_feedback(self, subject, topic, feedback):
            data = self.subjects[subject][topic]
            data["attempts"] += 1

            if feedback == "easy":
             data["confidence"] = min(1.0, data["confidence"] + 0.2)
            elif feedback == "hard":
             data["confidence"] = max(0.0, data["confidence"] - 0.2)

  #  def give_feedback(self, topic, feedback):
   #       if feedback == "easy":
    #          self.completed.add(topic)
     #     elif feedback == "hard":
      #           if topic in self.subjects[subject]:
       #                self.subjects[subject][topic] = "hard"
                    
