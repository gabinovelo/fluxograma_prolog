class User:
    def __init__(self):
        self.history = []

    def addCourse(self, id: str):
        if id in self.history:
            return False
        else:
            self.history.append(id)
            return True

    def removeCourse(self, id: str):
        if id not in self.history:
            return False
        else:
            self.history.remove(id)
            return True