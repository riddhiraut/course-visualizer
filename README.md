# **Course Planner and Progress Visualizer for UGA's Computing Programs (Live | WIP 🏗️)**

IMPORTANT: THIS PROJECT WAS CREATED ENTIRELY TO HELP MYSELF, NOT TO BE TECHNICALLY IMPRESSIVE. PLEASE DON'T JUDGE ME BEFORE READING BELOW 😭

I love my major, but I'm always debating on what minors I want to take. Because of my indecisiveness about said minors, my course plan keeps changing. However, UGA's course planning website (DEGREEWORKS) is pretty janky, so I'm always irritated every time I have to use it. I've chosen to only include Computing minors at UGA (along with my major, ofc) because those are the only ones I'm interested in taking. This project was created to save me time, because I'm tired of using Degreeworks.

Currently integrated just my own major, will be expanding soon :)

---

**How it Works**

The application is built using a clean Object-Oriented Programming (OOP) architecture in Python, separating domain logic from the presentation layer.

classes.py
- Course Class: Details individual course attributes (such as course code, title, credit hours, and prerequisite lists) + validation logic to verify if prerequisites are satisfied.
- ComputingProgram Class: Models an academic program by keeping a structured dictionary of course code-to-object mappings.
- StudentPlanner Class: Maintains the student's dynamic state (completed and enrolled courses) to compute remaining core requirements, credit tracking, and prerequisite unlocking.

app.py
- Streamlit frontend: Powers an interactive web UI featuring multi-select inputs, progress metrics, and a tabbed interface separating remaining courses, unlocked classes, and full catalog statuses.
- Plan logic: Handles user state management, tracks active/completed multiselect inputs, filters course catalogs into remaining vs. unlocked paths based on prerequisite fulfillment, and computes real-time degree completion percentages.

data.py
- Core course entry for programs.

---

**Roadmap**
- [x] Build prototype for my major
- [x] Format according to UGA's official Style Guide
- [ ] Expand to incorporate logic for computing/computing-adjacent adjacent minors that I'm interested in (CS Minor, Stat Minor, Math Minor, Cog Sci Minor)
- [ ] Support custom multi-select Minor/Major combinations
- [ ] Integrate cumulative GPA tracking and GPA analytics
- [ ] Add user profile persistence (database or local storage) to save customized degree roadmaps across sessions
- [ ] Incorporate "what-if" scenario modeling
- [ ] Create system to save "what-if" plans
