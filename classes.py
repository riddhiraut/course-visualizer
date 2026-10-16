from typing import Iterable

class Course:
    def __init__(self, code: str, name: str, credits: int, prereqs: list[str] = None):
        self.code = code
        self.name = name
        self.credits = credits
        self.prereqs = prereqs or []

    # prereq check
    def can_take(self, completed_set: set[str]) -> bool:
        return all(p in completed_set for p in self.prereqs)

class ComputingProgram:
    def __init__(self, name: str, courses: dict[str, Course]):
        self.name = name
        # dict mapping course code to Course object
        self.courses = courses

class StudentPlanner:
    def __init__(self, program: ComputingProgram):
        self.program = program
        self.completed: set[str] = set()
        self.enrolled: set[str] = set()

    def update_status(self, completed: Iterable[str], enrolled: Iterable[str]):
        self.completed = set(completed)
        self.enrolled = set(enrolled)

    # returns courses not yet completed or currently enrolled in
    def get_remaining(self) -> dict[str, Course]:
        remaining_courses = {}
        for code, course in self.program.courses.items():
            if code not in self.completed and code not in self.enrolled:
                remaining_courses[code] = course
        return remaining_courses
      
    # returns remaining courses whose prerequisites are fully met
    def get_unlocked_remaining(self) -> dict[str, Course]:
        remaining = self.get_remaining()
        satisfied = self.completed | self.enrolled
        unlocked_courses = {}
        for code, course in remaining.items():
            if course.can_take(satisfied):
                unlocked_courses[code] = course
        return unlocked_courses
