from flask import Flask, render_template, request
from dotenv import load_dotenv
from google import genai
import os
import json


load_dotenv()

app = Flask(__name__)


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():


    name = request.form.get("name")
    profession = request.form.get("profession")
    about = request.form.get("about")
    skills = request.form.get("skills")
    projects = request.form.get("projects")
    github = request.form.get("github")
    linkedin = request.form.get("linkedin")

    prompt = f"""
You are an expert portfolio writer and software engineer.

Your task is to create a professional portfolio for a developer.

User Details:
Name: {name}
Profession: {profession}
About: {about}
Skills: {skills}
Projects: {projects}

IMPORTANT RULES:

1. Rewrite everything professionally.
2. Do NOT copy the user's text.
3. Expand and improve the content.
4. Make the portfolio suitable for recruiters.
5. For every project, infer what it does from its name and write a professional description.
6. Keep descriptions realistic.
7. Return ONLY valid JSON.

Return in this exact format:

{{
    "tagline":"One professional tagline",

    "about":"A professional About Me section (120-150 words).",

    "projects":[
        {{
            "title":"Project Name",
            "description":"Professional description explaining the project, technologies used and purpose."
        }},
        {{
            "title":"Project Name",
            "description":"Professional description."
        }}
    ]
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    ai_text = response.text.strip()

    
    ai_text = ai_text.replace("```json", "").replace("```", "").strip()

    print("\n===== GEMINI RESPONSE =====")
    print(ai_text)
    print("===========================\n")

    try:
        data = json.loads(ai_text)

    except Exception as e:
        print(e)

        data = {
            "tagline": "AI Portfolio",
            "about": "Unable to generate portfolio content.",
            "projects": []
        }

    return render_template(
        "portfolio.html",
        name=name,
        profession=profession,
        tagline=data["tagline"],
        about=data["about"],
        projects=data["projects"],
        skills=[skill.strip() for skill in skills.split(",")],
        github=github,
        linkedin=linkedin
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=False)