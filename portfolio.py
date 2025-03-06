import streamlit as st
from streamlit_option_menu import option_menu

# Sidebar menu
def sidebar_menu():
    with st.sidebar:
        selected = option_menu("Menu", ["Home", "Projects", "Skills & Achievements", "Testimonials", "Contact"],
                              icons=["house", "folder", "bar-chart", "chat", "envelope"],
                              menu_icon="cast", default_index=0)
    return selected

# Home Section
def home_section():
    st.title("Welcome to My Digital Portofolio")
    st.image("profile_picture.jpg", width=200)
    st.header("ISHIMWE Bernardin")
    st.subheader("BSc Computer Science in option of Software Engineering, Year 3")
    st.write("I am passionate about technology and driven to innovate. Explore my academic journey, projects, and skills!")
    with open("resume.pdf", "rb") as file:
        resume_bytes = file.read()
    st.download_button(label="Download Resume",data=resume_bytes,file_name="resume.pdf")
    st.markdown("---")

# Projects Section
def projects_section():
    st.title("Projects")
    st.write("### Year 1 Project: Rock Paper Sissor game")
    st.write("**Type:** Individual")
    st.write("**Description:** build using js, OpenCV.")
    st.write("[GitHub Repo](https://github.com/bell250/rockPaperSissors.git)")

    st.write("### Final Year Project: Integrated Digital Mediation Management System")
    st.write("**Type:** Individual Project")
    st.write("**Description:** A system to manage and predict case trends in mediation committees. Technologies: Node.js, MySQL.")
    

# Skills and Achievements Section
def skills_section():
    st.title("Skills & Achievements")
    st.write("#### Programming Languages")
    st.progress(90)
    st.write("#### Web Development")
    st.progress(95)
    st.write("#### Machine Learning/Data Science")
    st.progress(60)
    
    st.write("### Achievements")
    st.write("- Completed ATLP Kickstart program")
    st.write("- Software development course at IPRC Ngoma")

# Testimonials Section
def testimonials_section():
    st.title("Testimonials")
    st.write("*\"Bernardin ISHIMWE is a brilliant problem solver! His final year project was truly innovative.\"* - Mr.Emmanuel,Lecturer")
    st.write("*\"His skills in data analytics are impressive and inspiring.\"* - Cyprien, Student")

# Contact Section
def contact_section():
    st.title("Contact Me")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success("Message sent successfully!")

    st.write("### Social Links")
    st.write("[LinkedIn](https://www.linkedin.com/in/bernardin-ishimwe-b9ba27206)")
    st.write("[GitHub](https://github.com/bell250)")

# Main function
def main():
    st.set_page_config(page_title="Digital Portofolio", layout="wide")
    selected = sidebar_menu()

    if selected == "Home":
        home_section()
    elif selected == "Projects":
        projects_section()
    elif selected == "Skills & Achievements":
        skills_section()
    elif selected == "Testimonials":
        testimonials_section()
    elif selected == "Contact":
        contact_section()

if __name__ == "__main__":
    main()
