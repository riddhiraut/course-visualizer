from typing import Iterable

class Course:
    def __init__(self, code: str, name: str, credits: int,
                 prereqs: list[str] = None, aliases: list[str] = None):
        self.code = code
        self.name = name
        self.credits = credits
        self.prereqs = prereqs or []
        self.aliases = aliases or []

    def can_take(self, completed_set: set[str]) -> bool:
        return all(p in completed_set for p in self.prereqs)

    def matches_code(self, user_input: str) -> bool:
        """Case-sensitive match against the primary code or any alias."""
        return user_input == self.code or user_input in self.aliases


class ComputingProgram:
    def __init__(self, name: str, courses: dict[str, Course],
                 electives: dict[str, Course] = None,
                 electives_required: int = 0):
        self.name = name
        self.courses = courses
        self.electives = electives or {}
        self.electives_required = electives_required


class StudentPlanner:
    def __init__(self, program: ComputingProgram):
        self.program = program
        self.completed: set[str] = set()
        self.enrolled: set[str] = set()
        # list, not set — order matters so ELECTIVE 1/2/3/4 display in add order
        self.selected_electives: list[str] = []

    def update_status(self, completed: Iterable[str], enrolled: Iterable[str]):
        self.completed = set(completed)
        self.enrolled = set(enrolled)

    def get_remaining(self) -> dict[str, Course]:
        return {c: crs for c, crs in self.program.courses.items()
                if c not in self.completed and c not in self.enrolled}

    def get_unlocked_remaining(self) -> dict[str, Course]:
        satisfied = self.completed | self.enrolled
        return {c: crs for c, crs in self.get_remaining().items()
                if crs.can_take(satisfied)}

    # ---------- electives ----------
    def find_elective_code(self, user_input: str) -> str | None:
        """Return the canonical elective code matching the input, else None."""
        user_input = user_input.strip()
        for code, course in self.program.electives.items():
            if course.matches_code(user_input):
                return code
        return None

    def add_elective(self, user_input: str) -> tuple[str, str]:
        """Returns (status, message); status is 'ok', 'warn', or 'error'."""
        code = self.find_elective_code(user_input)
        if code is None:
            return "error", f"❌ '{user_input}' isn't a valid elective for this program."
        if code in self.selected_electives:
            return "error", f"❌ {code} is already in your electives."
    
        course = self.program.electives[code]
        satisfied = self.completed | self.enrolled
        self.selected_electives.append(code)
    
        if course.can_take(satisfied):
            return "ok", f"✅ Added {code} as ELECTIVE {len(self.selected_electives)}."
    
        missing = [p for p in course.prereqs if p not in satisfied]
        return "warn", (f"⚠️ Added {code} as ELECTIVE {len(self.selected_electives)} — "
                            f"prerequisite(s) not yet met: {', '.join(missing)}.")

    def remove_elective(self, code: str):
        if code in self.selected_electives:
            self.selected_electives.remove(code)

    def get_elective_credits(self) -> int:
        return sum(self.program.electives[c].credits for c in self.selected_electives)

    def get_electives_count(self) -> int:
        return len(self.selected_electives)

    def get_unlocked_electives(self) -> dict[str, Course]:
        """Electives whose prereqs are met AND that haven't been picked yet."""
        satisfied = self.completed | self.enrolled
        return {c: e for c, e in self.program.electives.items()
                if c not in self.selected_electives and e.can_take(satisfied)}
