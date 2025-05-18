

# 🧠 AI Resume Generator 

An MVP (Minimum Viable Product) **AI-powered Resume Generator** built using the Django framework. This application allows users to **sign up, log in, and log out**, and then generate professional resumes with the help of AI.

---

## 🚀 Features

* ✅ **User Authentication**

  * Sign up with email and password
  * Secure login and logout system
  * Session-based authentication

* 🧾 **AI-Powered Resume Generation**

  * Smart resume content generation using AI
  * Automatically generates relevant job descriptions, skills, and summaries
  * Option to export or download generated resume (PDF, DOCX, etc.)

* 🛠️ **Minimal & Clean UI**

  * Simple and responsive interface
  * Focused on user experience

---

## 🔧 Tech Stack

* **Backend**: Django (Python)
* **Frontend**: HTML5, CSS3, Bootstrap (or Tailwind CSS)
* **Database**: SQLite (default, can be upgraded to PostgreSQL)
* **Authentication**: Django’s built-in authentication system
* **AI Integration**: (Placeholder for GPT/OpenAI/LLM integration)

---

## 📦 Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/ai-resume-generator.git
   cd ai-resume-generator
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the Server**

   ```bash
   python manage.py runserver
   ```

6. **Access the App**
   Visit `http://127.0.0.1:8000/` in your browser.

---

## 🧪 Usage

1. Create a user account via the **Signup** page.
2. Log in with your credentials.
3. Use the resume generator form to enter personal and professional details.
4. Click **Generate Resume**.
5. Download or copy your AI-generated resume content.

---

## 🔐 Authentication Routes

* `/signup/` – Register a new user
* `/login/` – Login existing user
* `/logout/` – Logout user

---

## 📁 Project Structure (MVP)

```
ai_resume_generator/
├── manage.py
├── resume/
│   ├── templates/
│   ├── views.py
│   ├── models.py
│   └── urls.py
├── users/
│   ├── templates/
│   ├── views.py
│   ├── models.py
│   └── urls.py
├── static/
├── media/
└── requirements.txt
```

---

## 🧠 Future Enhancements

* Multi-template resume formats
* Export as PDF/DOCX
* Add job targeting and keyword optimization
* AI feedback and scoring

---

## 🤝 Contributing

Contributions are welcome! Fork the repo, make your changes, and submit a pull request.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).


