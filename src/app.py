from openai import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv

st.title("Cover Letter AI Generator")


st.subheader("Job Information")
with st.form("job"):
    application_question = st.text_input("Application Question", "Write me a cover letter for this job.")
    job_title = st.text_input("Job Title", "Machine Learning Engineer")
    job_company = st.text_input("Company", "AWS Generative AI Innovation Center")
    job_desc = st.text_input("Job description",
    """Who you are
Masters degree (or European advanced degree equivalent) in Computer Science, or related technical, math, or scientific field
Relevant experience in building large scale machine learning or deep learning models and solutions
Experience communicating across technical and non-technical audiences
Experience in using Python and hands on experience building models with deep learning frameworks like Tensorflow, Keras, PyTorch, MXNet
Fluency in written and spoken English
Desirable

Proven knowledge of Generative AI and hands-on experience of building applications with large foundation models
Proven knowledge of AWS platform and tools
PhD degree in Computer Science, or related technical, math, or scientific field
Hands-on experience of building ML solutions on AWS
What the job involves
The Generative AI Innovation Center at AWS is a new strategic team that helps AWS customers implement Generative AI solutions and realize transformational business opportunities
This is a team of strategists, data scientists, engineers, and solution architects working step-by-step with customers to build bespoke solutions that harness the power of generative AI
You will work directly with customers and innovate in a fast-paced organization that contributes to game-changing projects and technologies
You will design and run experiments, research new algorithms, and find new ways of optimizing risk, profitability, and customer experience
Collaborate with ML scientist and architects to research, design, develop, and evaluate cutting-edge generative AI algorithms to address real-world challenges
Interact with customers directly to understand the business problem, help and aid them in implementation of generative AI solutions, deliver briefing and deep dive sessions to customers and guide customer on adoption patterns and paths to production
Create and deliver best practice recommendations, tutorials, blog posts, sample code, and presentations adapted to technical, business, and executive stakeholder
Provide customer and market feedback to Product and Engineering teams to help define product direction.""")
    job_submit = st.form_submit_button()


st.subheader("Your information")
with st.form("worker"):
    worker_first_name = st.text_input("First Name", "Callum")
    worker_last_name = st.text_input("Last Name", "Macpherson")
    worker_email = st.text_input("Email",
    "callumjmac@outlook.com")
    worker_submit = st.form_submit_button()



st.subheader("What experience and skills do you have?")
with st.form("experience"):
    experience = st.text_input("Experience", """
             • Freelance Sydney, Australia
AI Engineer & Consultant Jun. 2023 - Jan. 2024
◦ LLMs: Developing LLM systems, including data collection, curation, fine-tuning, prompt engineering, evaluation
and deployment using OpenAI API.
◦ Prototyping: Integrated LLM system into proof-of-concept applications using Streamlit.
◦ Continual Learning: Delivered presentations and reports on Distribution Drift Metrics for Deep Learning
models.
• Self Elected Career Break Around the world
Travelled to 16 countries Oct. 2022 - Mar. 2024
◦ Highlights: Everest Base Camp Three Passes Trek, Salkantay Trek to Machu Picchu, Ha Giang Motorbike Loop,
Deep Water Free Solo Climbing in Ha Long Bay, Surfing, Scuba Diving.
• Advai London, UK
Machine Learning Researcher Sep. 2021 - Oct. 2022
◦ Adversarial Attacks: Implemented adversarial (poisoning and evasion) attacks against Computer Vision (YOLO,
Faster R-CNN, Mask R-CNN, ViT), Optical Character Recognition (Tesseract, EasyOCR), Natural Language
Processing models (XLNet, BERT, LSTMs, GPTs) in PyTorch and logged experiments using WandB.
◦ Out-of-Distribution (OOD) Detection: Implemented and deployed a library using JAX and Flax to allow
users to detect OOD inputs using a pre-trained transformer and metrics such as the Mahalanobis Distance. The
method achieved an AUROC of 98.82% on the CIFAR 10 vs. 100 benchmark.
◦ OCR Modelling: Smart Ensemble: Designed, implemented and deployed an intelligent ensemble method for
OCR models with an automated preprocessing algorithm using meta-learning techniques (such as multi-task
learning and model stacking), to reduce the character error rate of an OCR pipeline by 23%.
◦ Literature Review: A systematic literature of methods to predict the effectiveness and readiness of Deep
Reinforcement Learning Models for deployment.
◦ Bid proposals: Achieved a 100% success rate in writing technical bid proposals, with each completed contract
resulting in additional business from returning customers for the company.""")
    education = st.text_input("What higher education do you have?", """
                              University of Leeds West Yorkshire, UK
Master of Science in Data Science and Analytics; Grade: 88.2%. Sep. 2020 – Sep. 2021
◦ Relevant Courses: Machine Learning, Data Science, Artificial Intelligence, Python Programming, Data Mining
and Text Analytics, Statistical Theory and Methods, Statistical Learning.
◦ Thesis: ”Fully automated hand tracking for Parkinson’s Disease Diagnosis” Grade: 90%.
• University of Leeds West Yorkshire, UK
Bachelor of Engineering in Civil and Structural Engineering; Grade: First Class Honours. Sep. 2016 – Jul. 2020
◦ Awards: £500 CF Lunoe Trust Prize for top performing students.
""")
    
    skills = st.text_input("What relevant technical skills do you have?", """
                           • Programming Languages: Python, R, SQL, C++, Matlab, JavaScript, HTML, CSS
• Key Frameworks: PyTorch, Lightning, TensorFlow, Keras, JAX, Flax, Hugging Face, Timm, Django, Sci-kit Learn,
Pandas, Numpy, WandB, OpenCV, OpenAI, LangChain, Matplotlib, Seaborn, Tableau, Plotly.
• Software Development: VSCode, AWS (EC2, S3), Azure (VMs), SSH, Docker, venv, Git.
• High Performance Computing: Utilising multiple accelerators (GPUs, TPUs), multiprocessing and multithreading.""")
    experience_submit = st.form_submit_button()
    

#load api key
load_dotenv()

systm_msg = """Your role is to answer questions for job applications, using the "Application question" which will be inputted shortly. If the prompt requests a cover letter, it is important that you keep the body of the cover letter to a maximum of 3 paragraphs and use a structure and writing style to maximise application success. If the prompt does not request a cover letter, try to use the STAR technique (situation, task, action, result) to create a response. The user will provide you with some important information that you must use when writing the message."""

user_msg = f"""
Job title = {job_title} \n
Company name = {job_company} \n
Application question = {application_question} \n
Job Description = {job_desc} \n
Application question = {application_question}
Applicant name = {worker_first_name} \n
Applicant email address = {worker_email} \n
Relevant applicant experience = {experience} \n

"""

# Relevant applicant education = {education} \n
# Relevant applicant skills = {skills} \n

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# Create a dataset using GPT
response = client.chat.completions.create(model="gpt-3.5-turbo",
                                        messages=[
                                        {"role": "system", "content": systm_msg},
                                        {"role": "user", "content": user_msg}
                                         ])

rsp = response.choices[0].message.content

# print(rsp)

st.write(rsp)