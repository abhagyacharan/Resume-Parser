from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os
import json

test_abc = '''BHAGYA CHARAN A
+91 7095666777 © Hyderabad, India
a.bhagyacharan@gmail.com 6 LinkedIn o Github © X/Twitter

OBJECTIVE

A passionate tech enthusiast focused on building practical solutions and exploring new technologies. I thrive on turning
ideas into real-world applications while constantly learning and growing. My drive to create meaningful projects is
matched by my dedication to staying current with emerging tech trends.

EDUCATION
B V Raju Institute of Technology 2021 - current
Bachelor of Technology in Computer Science - Data Science CGPA: 7.9
SKILLS

Languages Python, Java

Data Science Machine Leanrning, Deep Learning, NLP, Analysis, Visualization

Web Dev HTML, CSS, JS, React, Bootstrap

Databases MySQL

Frameworks Django, Flask, Lang-Chain

PROJECTS

CalorEase — Python, Lang-Chain, Django, HTML, CSS, JS (GitHub)

‘© Engineered an Image classification Model using transfer learning on the pretrained InceptionV3 architecture, en-
abling accurate prediction of up to 20 classes of Indian food items.

‘* Integrated Chat-Grog chat model using Lang-Chain framework to utilize Llama 70B LLM to generate precise calorie
estimates and detailed macro-nutrient breakdowns for classified food items.

‘© Designed and incorporated an alternative “Search Food” feature to extend calorie lookup capabilities beyond the
image classification dataset, enhancing app usability for diverse dietary inputs.

‘© Built a robust full-stack application with Django, providing a scalable backend API and an intuitive, responsive
user interface.

Diagno-Guide — Python, HTML, CSS, JS, Flask, AJAX (GitHub)
‘* Developed a comprehensive disease prediction and personalized medicine recommendation system using machine
learning, integrated with Flask, Python, HTML, CSS, JavaScript, and AJAX.
‘© Delivered precise disease diagnoses and personalized prescription recommendations, enhancing user access to tai-
lored healtheare insights.
‘* Incorporated precautionary measures, detailed disease descriptions, and real-time Geo-Location services to locate
nearby hospitals, facilitating timely access to medical assistance.
Voice Assisted Camera — Python, OpenCV (GitHub)
‘© Designed a voice-activated camera application using Python and OpenCV, enabling users to capture photos, apply
filters, zoom, and record videos through voice commands.
‘* Integrated threading for parallel execution, ensuring smooth performance and responsiveness during multitasking
operations.'''

test_anil = '''Anil Kumar Borige

+91 8088459201 - Hyderabad, India
anilkumnasborigetyanailcom - linkedin com/anidkumarborige github com, Anil951

A passionate and dedicated learner with strong basies anda desire to expand knowledge and expertise. Looking
to join a eallaborative team to work on impactful projects together.

EDUCATION
Bachelor of ‘Technology. Il V Raju Institute of Technology. Narsapur 22k - 2005,
Relevant Coursework: Computer Science (Data Science) GPA: 892
SKILLS AND ABILITIES

Languages Java, Python Web Development React, HTML. CSS, JavaSeript
Database MySQL Soft Skills Team Player, Adaptability

PROJECTS

DiagnoGuide : AI for Disease Diagnosis, Medication, Hospital Mapping (itlub) (huplementation)
# Utilizes Random Forest and SVM algorithms to provide accurate disease predictions.

+ Provides personalized medication based on user data an allows prescription downloads

«# Includes precautions, disease descriptions, and geolocation services for finding nearby hospitals using KNN.
Sentiment Based YouTube Video Recommendation (sith)
+ Developed using NEP, LSM, Python, and the YouTube Data APL for domain-specific video suggestions,
«Incorporated sentiment analysis, spam filtering, multilingual and transliterated text support on comments.
‘Implemented a video ranking system based on nornalized scores to improve recommendations
Fair Split : Expense Tracking and Management (situ) (implementation)
«React app for tracking shared expenses among users, detailing expenses, and caleulating fair shares
«# Simplifies expense management by accurately dividing costs among participants based on consumption, sup-

porting multiple expense categories.

CERTIFICATIONS

Data Analyst Professional Certification by IBM (link)
Java Foundations Certification by Infosys SpringBoard (lik)
Machine Learning Specialization by Stanford University, DeepLeat

LEADERSHIP

Voluntary Coordinator for Delegates - NASSCOM NASTeek 2023 Now 2028
Managed delegate coordination by onganizing and guiding team members, ensuring Hyderabad, Telangana
‘ficient excention of tasks to meet event objectives.

Organizer, Coordinator - Code Breakers - Promethean 2425 BVRIT Jan 2024
Dixected a national-level coding event with 3 rounds, managing participant registration Narsapur, ‘Telangana,
and event logistics, ensuring stooth execution.'''


def categorize_resume(extracted_text: str) -> dict:
    prompt = f"""
    Categorize the following text into:
    Name, Contact, Skills, Experience, Projects, Achievements. 
    Use 'Not available' for missing fields.

    Text: {extracted_text}

    Return the response as a JSON array containing a single object with these exact fields and format:

        [{{
            "Name": "<name>",
            "Contact": "<Phone number or 'Not available'>",
            "Skills": {{"<skills (if multiple, separate by category, e.g., Languages, Web Development, Database, etc.) or 'Not available'>"}},
            "Experience": "<experience (if multiple, separate by category, e.g., Internships, Work Experience, etc.) or 'Not available'>",
            "Projects": {{"<projects (if multiple, separate by category or list) or 'Not available'>"}},
            "Achievements": {{"<achievements (if multiple, separate by category or list) or 'Not available'>"}}
        }}]

    Important:
        1. Return ONLY the JSON array, no additional text
        2. Use exact field names as shown
        3. Use "Not available" for unknown values
        4. Make sure the response is valid JSON
    """
    # Initialize the Groq chat model
    chat = ChatGroq(
        api_key=os.getenv('GROQ_API_KEY'),
        model_name="llama-3.1-70b-versatile",
        temperature=0.1
    )

    try:
        messages = [
            HumanMessage(content=prompt)
        ]

        response = chat.invoke(messages)
        content = response.content

        # Parse and validate the JSON response
        parsed_content = json.loads(content)

        # Post-process to ensure desired output format
        for item in parsed_content:
            if isinstance(item.get("Projects"), list):
                item["Projects"] = {proj for proj in item["Projects"]}

            if isinstance(item.get("Achievements"), list):
                item["Achievements"] = {ach for ach in item["Achievements"]}

        return parsed_content

    except Exception as e:
        print(e)
        return {}


print(categorize_resume(test_anil))