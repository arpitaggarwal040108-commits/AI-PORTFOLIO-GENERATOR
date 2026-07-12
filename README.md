# 🚀 AI Portfolio Generator

An AI-powered portfolio website generator built with **Flask** and **Google Gemini AI**. Simply enter your personal details, skills, and projects, and the application automatically generates a polished developer portfolio suitable for recruiters and personal branding.

## 🌐 Live Demo

**Live Website:** https://arpitaggarwal2.pythonanywhere.com/

---

# 📌 Features

* 🤖 AI-generated professional portfolio content
* ✨ Creates a recruiter-friendly "About Me"
* 🏷️ Generates a professional personal tagline
* 📂 Automatically enhances project descriptions
* 💻 Displays technical skills
* 🔗 Supports GitHub and LinkedIn profile links
* 📱 Responsive and clean user interface
* ⚡ Instant portfolio generation using Google Gemini AI

---

# 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* Jinja2 Templates

### Backend

* Python
* Flask

### AI Model

* Google Gemini 2.5 Flash API

### Deployment

* PythonAnywhere

---

# 📂 Project Structure

```
AI-Portfolio-Generator/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
│
├── templates/
│   ├── index.html
│   └── portfolio.html
│
├── static/
│   ├── style.css
│   └── images/
│
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/your-username/AI-Portfolio-Generator.git
```

```bash
cd AI-Portfolio-Generator
```

---

## 2. Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create a `.env` File

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

## 5. Run the Application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# 📖 How It Works

1. User enters:

   * Name
   * Profession
   * About
   * Skills
   * Projects
   * GitHub
   * LinkedIn

2. Flask receives the form data.

3. A carefully designed prompt is created.

4. Google Gemini generates:

   * Professional Tagline
   * About Me
   * Improved Project Descriptions

5. Gemini returns the response in JSON format.

6. Flask parses the JSON.

7. The generated portfolio is rendered dynamically using Jinja templates.

---

# 🤖 AI Prompt Engineering

The application instructs Gemini to:

* Rewrite user input professionally
* Avoid copying the original text
* Expand content for better readability
* Generate recruiter-friendly descriptions
* Infer realistic project descriptions from project names
* Return structured JSON only

This structured output allows the Flask application to render the portfolio dynamically without additional processing.

---

# 📸 Screenshots

Add screenshots here.

Example:

```
Home Page

Generated Portfolio
```

---

# 📦 Requirements

* Python 3.10+
* Flask
* python-dotenv
* google-genai

---

# 🔒 Environment Variables

```
GEMINI_API_KEY=YOUR_API_KEY
```

Never commit your `.env` file to GitHub.

---

# 🚀 Future Improvements

* PDF portfolio export
* Multiple portfolio themes
* Dark and Light mode
* Resume generation
* Portfolio templates
* Custom color selection
* Project image uploads
* AI-generated profile picture suggestions
* Deployment on Docker
* User authentication and saved portfolios

---

# 🧠 Learning Outcomes

This project demonstrates practical experience with:

* Flask web development
* REST-style request handling
* Prompt engineering
* Google Gemini API integration
* JSON parsing
* Environment variable management
* Dynamic HTML rendering with Jinja2
* PythonAnywhere deployment
* Full-stack application development

---

# 👨‍💻 Author

**Arpit Aggarwal**

Mechanical Engineering Undergraduate
Delhi Technological University (DTU)

GitHub: *(Add your GitHub profile link)*

LinkedIn: *(Add your LinkedIn profile link)*

---

# ⭐ If you like this project

Give the repository a ⭐ on GitHub.
