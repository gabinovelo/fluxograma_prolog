class Course:
    def __init__(self, id: str, name: str, semester: int, requirements: list[str] = None):
        self.id = id.lower().replace(" ", "_")
        self.name = name
        self.semester = semester
        self.requirements = requirements if requirements else []