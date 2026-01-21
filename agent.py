class StudentAgent :
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

print("StudentAgent initialized with subjects:", StudentAgent().subjects)