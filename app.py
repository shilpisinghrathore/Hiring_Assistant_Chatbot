import streamlit as st
from utils import generate_questions_for_tech, validate_email, validate_phone

def main():
    st.title("🤖 TalentScout Hiring Assistant")

    # Initialize session state variables
    if "step" not in st.session_state:
        st.session_state.step = "greeting"

    if "candidate_info" not in st.session_state:
        st.session_state.candidate_info = {
            "name": "",
            "email": "",
            "phone": "",
            "experience": "",
            "position": "",
            "location": "",
            "tech_stack": [],
        }

    if "current_tech_index" not in st.session_state:
        st.session_state.current_tech_index = 0

    if "current_question_index" not in st.session_state:
        st.session_state.current_question_index = 0

    if "questions" not in st.session_state:
        st.session_state.questions = []

    if "answers" not in st.session_state:
        st.session_state.answers = {}

    # Greeting step
    if st.session_state.step == "greeting":
        st.write("Hello! Welcome to TalentScout Hiring Assistant. I will help you with an initial screening by asking some questions.")
        if st.button("Start Screening"):
            st.session_state.step = "collect_info"
            st.rerun()

    # Collect candidate info
    if st.session_state.step == "collect_info":
        with st.form("candidate_form"):
            name = st.text_input("Full Name", value=st.session_state.candidate_info["name"])
            email = st.text_input("Email", value=st.session_state.candidate_info["email"])
            phone = st.text_input("Phone Number", value=st.session_state.candidate_info["phone"])
            experience = st.number_input("Years of Experience", min_value=0, max_value=50, value=int(st.session_state.candidate_info["experience"] or 0))
            position = st.text_input("Desired Position(s)", value=st.session_state.candidate_info["position"])
            location = st.text_input("Current Location", value=st.session_state.candidate_info["location"])
            tech_stack_input = st.text_input(
                "Tech Stack (comma separated, e.g., Python, Java, Machine Learning)", 
                value=", ".join(st.session_state.candidate_info["tech_stack"])
            )

            submitted = st.form_submit_button("Submit")

            if submitted:
                if not validate_email(email):
                    st.error("Please enter a valid email address.")
                    st.stop()

                if not validate_phone(phone):
                    st.error("Please enter a valid phone number.")
                    st.stop()

                st.session_state.candidate_info.update({
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "experience": str(experience),
                    "position": position,
                    "location": location,
                    "tech_stack": [tech.strip() for tech in tech_stack_input.split(",") if tech.strip()]
                })

                if not st.session_state.candidate_info["tech_stack"]:
                    st.error("Please specify at least one technology in your tech stack.")
                    st.stop()

                # Generate questions for first tech
                first_tech = st.session_state.candidate_info["tech_stack"][0]
                st.session_state.questions = generate_questions_for_tech(first_tech)
                st.session_state.current_tech_index = 0
                st.session_state.current_question_index = 0
                st.session_state.step = "ask_questions"
                st.session_state.answers = {}
                st.rerun()

    # Question asking step
    if st.session_state.step == "ask_questions":
        techs = st.session_state.candidate_info["tech_stack"]
        current_tech_idx = st.session_state.current_tech_index
        current_question_idx = st.session_state.current_question_index
        questions = st.session_state.questions

        current_tech = techs[current_tech_idx]

        st.markdown(f"### Questions on {current_tech}")

        question_text = questions[current_question_idx]
        st.write(f"**Question {current_question_idx + 1}:** {question_text}")

        answer = st.text_area("Your answer:", key=f"answer_input_{current_tech}_{current_question_idx}")

        if st.button("Submit Answer"):
            if not answer.strip():
                st.error("Please provide an answer before submitting.")
                st.stop()

            key = f"{current_tech}_Q{current_question_idx + 1}"
            st.session_state.answers[key] = answer.strip()

            if current_question_idx + 1 < len(questions):
                st.session_state.current_question_index += 1
            else:
                if current_tech_idx + 1 < len(techs):
                    st.session_state.current_tech_index += 1
                    next_tech = techs[st.session_state.current_tech_index]
                    st.session_state.questions = generate_questions_for_tech(next_tech)
                    st.session_state.current_question_index = 0
                else:
                    st.session_state.step = "finished"

            st.rerun()

    # Finished step
    if st.session_state.step == "finished":
        st.success("Thank you for completing the initial screening!")
        st.write("Here is a summary of your responses:")
        for key, ans in st.session_state.answers.items():
            st.write(f"**{key}:** {ans}")

        st.write("Our team will review your responses and get back to you soon.")
        if st.button("Restart"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()


if __name__ == "__main__":
    main()