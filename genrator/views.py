from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from .models import Resume
from .llm import generate_resume
from .utils import generate_resume_pdf_to_file

# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# load_dotenv()

# open_ai_key = os.getenv('OPENAI_API_KEY')
# client = OpenAI(api_key=open_ai_key)

# def generate_resume(title,experince,skills,education):
#     prompt = f"""You are a professional resume generator. Follow these steps to create an ATS-friendly resume:

#     1. Analyze the Position:
#     - Job Title: {title}
#     - Required Skills: {skills}
#     - Experience Level: {experince}

#     2. Structure Planning:
#     - First, outline the key sections needed
#     - Identify the most relevant skills and experiences
#     - Plan the optimal section order

#     3. Content Development:
#     - Create a compelling professional summary
#     - Format the experience section with measurable achievements
#     - Highlight relevant skills with specific examples
#     - Ensure all keywords from the job requirements are naturally incorporated

#     4. ATS Optimization:
#     - Use standard section headings
#     - Incorporate relevant keywords from the skills list
#     - Keep formatting simple and clean

#     Based on this analysis, generate a professional, ATS-friendly resume that includes:
#     - Professional Summary
#     - Work Experience
#     - Skills Section
#     - Education (with relevant coursework and achievements)
#     - Additional Achievements (if relevant)

#     Format the resume in a clean, professional layout using standard sections."""
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "You are a professional resume writer."},
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0.7)
#     return response.choices[0].message.content.strip()



# Create your views here.






def home(request):
    return render(request,'genrator/home.html')

def register(request):
    if request.method == 'POST':
        # Check if user exists
        if User.objects.filter(email=request.POST['email']).exists():
            return render(request, 'genrator/register.html', {'error': 'User already exists'})
        
        try:
            User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
                email=request.POST['email'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
            )
            return redirect('login')
            return render(request, 'genrator/register.html', {'success': 'User created successfully'})
        except Exception as e:
            return render(request, 'genrator/register.html', {'error': str(e)})
    
    # If GET request, just show the form
    return render(request, 'genrator/register.html')

def user_login(request):
    if request.user.is_authenticated:
        return render(request, 'login.html',{'message':"Usrt alraedy loged in"})
    if request.method=='POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'genrator/login.html',{'message':"Invalid credentials"})
    else:
        return render(request, 'genrator/login.html')





def resume_builder(request):
    if request.method == 'POST':
        # Get the form data
        job_title = request.POST['job_title']
        skills = request.POST['skills']
        experince = request.POST['experience'] 
        education = request.POST['education']
        # Generate the resume using OpenAI A
        resume_data = generate_resume(job_title, skills, experince, education)
        generate_resume_pdf_to_file(resume_data)
        # Save the resume to the database
        resume = Resume(user=request.user, job_title=job_title, skills=skills, experince=experince, education=education, genrated_resume=str(resume_data))
        resume.save()
        return render(request, 'genrator/resume_builder.html', {'resume_data': resume_data})

    return render(request, 'genrator/resume_builder.html')



