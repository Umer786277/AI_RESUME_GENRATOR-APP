from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

open_ai_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=open_ai_key)

def genrate_resume(title,experince,skills,education):
        prompt = f"""You are a professional resume generator. Follow these steps to create an ATS-friendly resume:

    1. Analyze the Position:
    - Job Title: {title}
    - Required Skills: {skills}
    - Experience Level: {experince}

    2. Structure Planning:
    - First, outline the key sections needed
    - Identify the most relevant skills and experiences
    - Plan the optimal section order

    3. Content Development:
    - Create a compelling professional summary
    - Format the experience section with measurable achievements
    - Highlight relevant skills with specific examples
    - Ensure all keywords from the job requirements are naturally incorporated

    4. ATS Optimization:
    - Use standard section headings
    - Incorporate relevant keywords from the skills list
    - Keep formatting simple and clean

    Based on this analysis, generate a professional, ATS-friendly resume that includes:
    - Professional Summary
    - Work Experience
    - Skills Section
    - Education (with relevant coursework and achievements)
    - Additional Achievements (if relevant)

    Format the resume in a clean, professional layout using standard sections."""
    response = client.responses.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

