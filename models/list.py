from models.course import Course
from services.prolog_interface import assert_course, retract_course

class Register:
    def __init__(self):
        self.courses = []

    def addCourse(self, id: str, name: str, semester: int, requirements: list[str] = None):

        for course in self.courses:
            if course.id == id.lower():
                return False
            
        self.courses.append(Course(id.lower(), name, semester, requirements))
        assert_course(id, requirements)
        return True
    
    def removeCourse(self, id: str):
        
        for course in self.courses:
            if course.id == id.lower():
                self.courses.remove(course)
                retract_course(id)
                return True
            
        return False