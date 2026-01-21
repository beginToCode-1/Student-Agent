class StudentAgent :
    #added some of the initial subjects and topics.
    def __init__(self):
        self.subjects = {
  "Math": {
      "Algebra": "hard",
      "Trigonometry": "medium"
  },
  "Physics": {
      "Motion": "easy"
  }
}
        self.completed = set({"Algebra", "Motion"})
        self.hours_per_day = 4  
        #adding methods to add subjects and topics   
    def add_subject(self, subject,):
           if subject not in self.subjects:
             self.subjects[subject] = {}
    def add_topic(self, subject, topic, difficulty):
              if subject in self.subjects:
                self.subjects[subject][topic] = difficulty

