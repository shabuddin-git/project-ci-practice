import streamlit as st

st.title("User Registration Application")

st.write("Create your account by filling in the details below.")

# Registration form
with st.form("registration_form"):

    name = st.text_input("Full Name")

    email = st.text_input("Email Address")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=18
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )

    submitted = st.form_submit_button("Register")

# Process the form
if submitted:

    if not name or not email or not password:
        st.error("Please fill in all required fields.")

    elif "@" not in email:
        st.error("Please enter a valid email address.")

    elif password != confirm_password:
        st.error("Passwords do not match.")

    else:
        st.success("Registration successful!")

        st.subheader("Registered User Details")

        st.write("Name:", name)
        st.write("Email:", email)
        st.write("Age:", age)