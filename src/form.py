import openai 
import streamlit as st
import os
from dotenv import load_dotenv

st.title("Cover Letter AI Generator")

# st.subheader("Job Information")
# with st.form("job"):
#     job_title = st.text_input("Job Title", "Enter a job title")
#     job_company = st.text_input("Company", "Enter the company's name")
#     job_desc = st.text_input("Job description",
#     "Please copy and paste the job description into this box")
#     job_submit = st.form_submit_button()

# st.subheader("Your information")
# with st.form("worker"):
#     worker_first_name = st.text_input("First Name", "Enter your first name")
#     worker_last_name = st.text_input("Last Name", "Enter your last name")
#     worker_email = st.text_input("Email",
#     "Enter your email")
#     worker_submit = st.form_submit_button()

st.subheader("Job Information")
with st.form("job"):
    job_title = st.text_input("Job Title", "Bartender")
    job_company = st.text_input("Company", "Hibiscus Tavern")
    job_desc = st.text_input("Job description",
    """The Hibiscus Tavern/ Dolly's Bar and Restaurant are currently seeking experienced and energetic people who have a passion for hospitality to join our team for an immediate start.

    We have casual positions in our Sports Bar and Restaurant available with a competitive hourly rate.

    The candidate must be presentable and have a high level of customer service.

    The position involves but is not limited to:

    Cash handling
    Use of a POS System
    Great customer service/interaction skills
    Service of food and beverage
    General product knowledge
    Keno and Gaming experience
    Ability to stand for lengthy periods of time
    Some repetitive lifting
    The Candidate must have a current RSA and RSG (RCG)

    Must have working rights in Australia.  """)
    job_submit = st.form_submit_button()


st.subheader("Your information")
with st.form("worker"):
    worker_first_name = st.text_input("First Name", "Callum")
    worker_last_name = st.text_input("Last Name", "Macpherson")
    worker_email = st.text_input("Email",
    "callumjmac@outlook.com")
    worker_submit = st.form_submit_button()



st.subheader("What experience and skills do you have?")
# with st.form("experience"):
#     experience = st.text_input("Experience", "You can copy and paste the experience and/or skills section from your CV")
#     st.write(""" Examples: \n
#              Bartender
#              - Effective communication and teamwork skills.
#              - Preparing espresso-based hot drinks, and alcoholic drinks including signature and classic cocktails.
#              - Attention to detail and ability to follow procedures.

#              """)
with st.form("experience"):
    experience = st.text_input("Experience", """Bartender \n
             - Effective communication and teamwork skills. \n
             - Preparing espresso-based hot drinks, and alcoholic drinks including signature and classic cocktails. \n
             - Attention to detail and ability to follow procedures. \n """)
    experience_submit = st.form_submit_button()
    

#api key
load_dotenv()
openai.api_key  = os.getenv("OPENAI_API_KEY")

systm_msg = """Your role is to write cover letters for job applications. It is important that you keep the body of the cover letter to a maximum of 3 paragraphs and use a structure and writing style to maximise application success. The user will provide you with some important information that you must use when writing the message."""

user_msg = f"""
Job title = {job_title} \n
Company name = {job_company} \n
Job Description = {job_desc} \n
Applicant name = {worker_first_name} \n
Applicant email address = {worker_email} \n
Relevant applicant experience = {experience} \n
"""


# Create a dataset using GPT
response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                        messages=[{"role": "system", "content": systm_msg},
                                         {"role": "user", "content": user_msg}])

rsp = response['choices'][0]['message']['content']

st.write(rsp)