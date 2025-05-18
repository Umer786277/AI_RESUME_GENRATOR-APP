from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
import json
import os

load_dotenv()

open_ai_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=open_ai_key)

class resume_structure(BaseModel):
    title     : str
    skills    : str
    experince : str

import json
import re
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

open_ai_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=open_ai_key)

def extract_json(text):
    """
    Extract JSON object from possibly markdown-wrapped text.
    """
    try:
        # Attempt to directly parse first
        return json.loads(text)
    except json.JSONDecodeError:
        # Try to extract JSON from a code block
        match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', text, re.DOTALL)
        if match:
            json_text = match.group(1)
            return json.loads(json_text)
        else:
            raise  # Re-raise the original exception if no match found

def generate_resume(title, experince, skills, education):
    prompt = f"""
You are a professional resume generator. Follow these structured steps to create an ATS-optimized, highly professional resume in JSON format.

---

## 1. Analyze the Position:
- Job Title: {title}
- Required Skills: {skills}
- Experience Level: {experince}
- Education : {education}

---

## 2. Plan the Structure:
- Key Sections: Professional Summary, Work Experience, Skills, Education, Additional Achievements
- Prioritize experiences and skills most relevant to the job title
- Keep layout ATS-friendly (no fancy formatting)

---

## 3. Develop the Content:
- **Professional Summary**: Write a 4–7 sentence summary tailored to the job title.
- **Work Experience**: Write 2–4 main entries. Use bullet points for each job, include metrics or achievements if available.
- **Skills**: Present the skills in clear bullet-point format, each as a string item in a list.
- **Education**: Include degree, institution, and achievements if any.
- **Additional Achievements**: Include awards, certifications, notable accomplishments. Bullet points preferred.

---

## 4. ATS Optimization:
- Use simple section names: professional_summary, work_experience, skills, education, additional_achievements
- Keep language professional and relevant
- Avoid wrapping response in markdown or explanations

---

## FINAL INSTRUCTIONS:
Return the resume as a **pure JSON object** with these exact keys:
- professional_summary
- work_experience
- skills
- education
- additional_achievements

⚠️ DO NOT include markdown (no ```), explanations, or extra text — only return a valid JSON object.

---
"""



    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "You are a professoional resume writer"},{"role": "user", "content": prompt}],
        temperature=0.7
    )

    content = response.choices[0].message.content.strip()
    
    try:
        return extract_json(content)
    except json.JSONDecodeError as e:
        print("❌ JSON decode error:", e)
        print("🔍 GPT returned:", content)
        return {
            "professional_summary": "Failed to parse resume.",
            "work_experience": "",
            "skills": "",
            "education": "",
            "additional_achievements": ""
        }

    
