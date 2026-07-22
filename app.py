import streamlit as st

st.set_page_config(page_title = "Smart Resume - AI", page_icon = "📄", layout = "wide")

st.title("📄 Smart Resume - AI")
st.subheader("AI - Powered Resume Builder")

st.write(
    """
    Welcome to the Smart Resume - AI!

    This application helps you generate a professional resume using Artificial Intelligence.
    """
)

st.divider()

st.header("Personal Information")

name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")

education = st.text_area("Education")
skills = st.text_area("Skills")
experience = st.text_area("Experience")
projects = st.text_area("Projects")
certificates = st.text_area("Certificates")

if st.button("Generate Resume"):
    st.success("Resume generation module will be added in the next step.")

    st.write("### Preview")

    st.markdown(f"## {name}")
    st.write(f"📧 {email}")
    st.write(f"📱 {phone}")

    st.markdown("### Education")
    st.write(education)

    st.markdown("### Skills")
    st.write(skills)

    st.markdown("### Experience")
    st.write(experience)

    st.markdown("### Projects")
    st.write(projects)

    st.markdown("### Certificates")
    st.write(certificates)