from classes import Course, ComputingProgram

# curriculum framework for data sci
datascience_major = ComputingProgram(
    name="B.S. in Data Science",
    courses={
        "MATH 2250": Course("MATH 2250", "Calculus I for Science and Engineering", 4, []),
        "MATH 2260": Course("MATH 2260", "Calculus II for Science and Engineering", 4, ["MATH 2250"]),
        "MATH 2270": Course("MATH 2270", "Calculus III", 4, ["MATH 2260"]),
        "STAT 2000": Course("STAT 2000", "Introductory Statistics", 4, []),
        "CSCI 1301": Course("CSCI 1301", "Intro to Computing and Programming", 4, []),
        "CSCI 3360": Course("CSCI 3360", "Data Science & Applied Machine Learning I", 3, ["CSCI 1301", "MATH 2250"]),
        "CSCI 3030": Course("CSCI 3030", "Computing, Ethics, and Society", 3, []),
        "CSCI 2610": Course("CSCI 2610", "Discrete Mathematics for Computer Science", 4, []),
        "CSCI 1302": Course("CSCI 1302", "Software Development", 4, ["CSCI 1301"]),
        "MATH 3300": Course("MATH 3300", "Applied Linear Algebra", 3, ["MATH 2260"]),
        "CSCI 4360": Course("CSCI 4360", "Data Science II", 4, ["CSCI 3360"]),
        "STAT 4365": Course("STAT 4365", "Modern Statistical Programming", 3, ["STAT 2000"]),
        "STAT 4230": Course("STAT 4230", "Applied Regression Analysis", 3, ["STAT 2000", "MATH 2250"]),
        "CSCI 2725": Course("CSCI 2725", "Data Structures for Data Science", 4, ["CSCI 1302"]),
        "CSCI 2670": Course("CSCI 2670", "Introduction to Theory of Computing", 4, ["CSCI 2610"]),
        "CSCI 4050": Course("CSCI 4050", "Software Engineering", 4, ["CSCI 2725"]),
        "CSCI 4260": Course("CSCI 4260", "Data Security and Privacy", 4, ["CSCI 2725"]),
        "STAT 4510": Course("STAT 4510", "Mathematical Statistics I", 3, ["MATH 2270"]),
        "CSCI 4470": Course("CSCI 4470", "Algorithms", 4, ["CSCI 2725", "CSCI 2670"]),
        "CSCI 4370": Course("CSCI 4370", "Database Management", 4, ["CSCI 2725"]),
        "STAT 4220": Course("STAT 4220", "Applied Experimental Designs", 3, ["STAT 4230"]),
        "CSCI 4380": Course("CSCI 4380", "Data Mining", 4, ["CSCI 2725"]),
        "STAT 4530": Course("STAT 4530", "Statistical Inference for Data Scientists", 3, ["CSCI 3360", "STAT 4510"]),
        "STAT 5030": Course("STAT 5030", "Statistical Methods / Consulting", 3, ["STAT 4230"]),
    }
)

# expand programs here later:
# computerscience_major = ComputingProgram(...)

PROGRAMS = {
    "B.S. in Data Science": datascience_major,
    # "B.S. in Computer Science": computerscience_major,
}
