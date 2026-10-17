# **Course Planner and Progress Visualizer for UGA's Computing Programs (Live | WIP 🏗️)**

IMPORTANT: THIS PROJECT WAS CREATED ENTIRELY TO HELP MYSELF, NOT TO BE TECHNICALLY IMPRESSIVE. PLEASE DON'T JUDGE ME BEFORE READING BELOW 😭

My course plan keeps changing and I'm indecisive about my minors, but UGA's course planning website (DEGREEWORKS) is pretty janky. I've chosen to only include Computing programs at UGA because those are the only ones I'm interested in taking. This project was created to save me time, because I'm tired of using Degreeworks.

Currently integrated just my own major, will be expanding soon :)

---

**How it Works**

The application is built using a clean Object-Oriented Programming (OOP) architecture in Python, separating domain logic from the presentation layer.

classes.py {
Course Class: Details individual course attributes (such as course code, title, credit hours, and prerequisite lists) + validation logic to verify if prerequisites are satisfied.
ComputingProgram Class: Models an academic program by keeping a structured dictionary of course code-to-object mappings.
StudentPlanner Class: Maintains the student's dynamic state (completed and enrolled courses) to compute remaining core requirements, credit tracking, and prerequisite unlocking.
}
app.py {
Streamlit frontend: Powers an interactive web UI featuring multi-select inputs, progress metrics, and a tabbed interface separating remaining courses, unlocked classes, and full catalog statuses.
Plan logic: Handles user state management, tracks active/completed multiselect inputs, filters course catalogs into remaining vs. unlocked paths based on prerequisite fulfillment, and computes real-time degree completion percentages.
}

---

**Roadmap**
- [x] Build prototype with just 1 major
- [x] Expand to all programs incorporated within UGA's College of Computing
- [ ] Add user profile persistence (database or local storage) to save customized degree roadmaps across sessions
- [ ] Integrate cumulative GPA tracking and GPA analytics
- [ ] Support custom elective tracks and minor combinations
- [ ] Incorporate "what-if" scenario modeling
