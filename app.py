import streamlit as st
from data import PROGRAMS
from classes import StudentPlanner

st.set_page_config(page_title="Course Plan Visualizer", page_icon="🎓", layout="wide")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Merriweather+Sans:wght@400;600;700&family=Oswald:wght@300;500&display=swap');
    
    /* page */
    .stApp {
        background-color: #FFFFFF !important; /* white */
        color: #000000 !important; /* black */
        font-family: 'Merriweather Sans', 'Georgia', serif !important;
    }
    
    /* content headings */
    h1, h2 {
        font-family: 'Oswald', 'Merriweather Sans', sans-serif !important;
        color: #000000 !important; /* black */
        letter-spacing: 0.02em;
    }
    
    h1 {
        border-bottom: 3px solid #BA0C2F; /* bulldog red */
        padding-bottom: 0.35rem;
    }
    
    /* body text */
    p, li, span, label, div[data-testid="stMarkdownContainer"] {
        color: #000000 !important; /* black */
    }
    
    /* sidebar (cosmetic — no sidebar widgets yet, but harmless) */
    section[data-testid="stSidebar"] {
        background-color: #F2F2F2 !important; /* light grey */
        border-right: 1px solid #DEDEDE; /* light grey (border) */
    }
    
    /* progress bar */
    div[data-testid="stProgress"] > div > div > div {
        background-color: #E4002B !important; /* glory red */
    }
    
    /* tabs */
    .stTabs [data-baseweb="tab-list"] {
        border-bottom: 1px solid #DEDEDE; /* light grey (border) */
    }
    
    .stTabs [data-baseweb="tab"] {
        font-family: 'Oswald', sans-serif !important;
        color: #666666 !important; /* dark grey */
        font-weight: 400;
    }
    
    .stTabs [aria-selected="true"] {
        color: #BA0C2F !important; /* bulldog red */
        border-bottom: 2px solid #BA0C2F !important; /* bulldog red */
        font-weight: 500;
    }
    
    /* selectbox / input widgets
       (input rules kept for future minor-credit text entry) */
    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div {
        background-color: #FFFFFF !important; /* white */
        border-color: #DEDEDE !important; /* light grey (border) */
        color: #000000 !important; /* black */
    }
    
    div[data-baseweb="select"]:focus-within > div,
    div[data-baseweb="input"]:focus-within > div {
        border-color: #BA0C2F !important; /* bulldog red */
        box-shadow: 0 0 0 1px #BA0C2F !important; /* bulldog red */
    }
    
    /* multiselect pills */
    span[data-baseweb="tag"] {
        background-color: #BA0C2F !important; /* bulldog red */
        color: #FFFFFF !important; /* white */
        border: none !important;
    }
    
    /* horizontal rule (st.divider) */
    hr {
        border-color: #DEDEDE !important; /* light grey */
    }
    
    /* caption text */
    [data-testid="stCaptionContainer"] {
        color: #666666 !important; /* dark grey */
        font-family: 'Merriweather Sans', sans-serif !important;
    }
    
    /* alerts (st.success / st.info) */
    div[data-testid="stAlert"] {
        border-radius: 4px;
        border-left: 4px solid #BA0C2F; /* bulldog red */
    }
    """,
    unsafe_allow_html=True,
)

st.title("UGA Computing Course Plan Visualizer 🐾")
st.markdown("Select your program, check off completed and active courses, and instantly track your path to graduation!")

# program selector
prog_name = st.selectbox("Select Program", list(PROGRAMS.keys()))
program = PROGRAMS[prog_name]

# initialize or reset planner state on program switch
if "current_program" not in st.session_state or st.session_state.current_program != prog_name:
    st.session_state.planner = StudentPlanner(program)
    st.session_state.current_program = prog_name
    st.session_state.comp_sel = []
    st.session_state.enr_sel = []

planner = st.session_state.planner
all_codes = list(program.courses.keys())

# user inputs
col1, col2 = st.columns(2)
with col1:
    completed = st.multiselect("Courses Completed", all_codes, key="comp_sel")
with col2:
    available_for_enroll = []
    for c in all_codes:
        if c not in completed:
            available_for_enroll.append(c)
    if "enr_sel" in st.session_state: # remove stale selections BEFORE the widget renders
        st.session_state.enr_sel = [c for c in st.session_state.enr_sel if c in available_for_enroll]
    enrolled = st.multiselect("Courses Currently Enrolled", available_for_enroll, key="enr_sel")

# update planner state
planner.update_status(completed, enrolled)

st.divider()

# metrics
total_courses = len(program.courses)
comp_count = len(completed)
progress_pct = comp_count / total_courses if total_courses > 0 else 0

st.subheader("📊 Degree Progress")
st.progress(progress_pct)
st.write(f"Completed **{comp_count}** of **{total_courses}** core program requirements ({progress_pct*100:.1f}%)")

# tabs
tab1, tab2, tab3 = st.tabs(["Remaining Courses", "Unlocked (Ready to Take)", "Full Catalog Status"])

unlocked = planner.get_unlocked_remaining() # compute to reuse in tab1 + tab2
unlocked_codes = set(unlocked.keys())

with tab1:
    st.subheader("Courses Left to Complete")
    remaining = planner.get_remaining()
    if not remaining:
        st.success("🎉 You have completed all core courses in this degree program!")
    else:
        for code, course in remaining.items():
            ready = code in unlocked_codes
            status = "🟢 Ready to Enroll" if ready else "🔒 Locked (Missing Prereqs)"
            st.markdown(f"**{code}: {course.name}** ({course.credits} credits) — *{status}*")
            if course.prereqs:
                missing = [p for p in course.prereqs if p not in planner.completed | planner.enrolled]
                if missing:
                    st.caption(f"Prerequisites: {', '.join(course.prereqs)} — missing: {', '.join(missing)}")
                else:
                    st.caption(f"Prerequisites: {', '.join(course.prereqs)}")

with tab2:
    st.subheader("Unlocked & Available Next Semester")
    if not unlocked:
        st.info("No core courses currently unlocked. Complete more prerequisites to unlock new classes.")
    else:
        for code, course in unlocked.items():
            st.markdown(f"✅ **{code}: {course.name}** — *{course.credits} credits*")

with tab3:
    st.subheader("Complete Program Curriculum")
    for code, course in program.courses.items():
        if code in planner.completed:
            state_label = "✅ Completed"
        elif code in planner.enrolled:
            state_label = "🟡 Enrolled"
        else:
            state_label = "⏳ Remaining"
        st.write(f"- **{code}**: {course.name} — *{state_label}*")
