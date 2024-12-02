import os
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/start_quiz', methods=['POST'])
def start_quiz():
    """
    Endpoint to start the quiz and generate questions.
    Accepts JSON payload with company, profession, and skills.
    """
    data = request.json  
    company = data.get('company')
    profession = data.get('profession')
    skills = data.get('skills')

    print(f"Company: {company}, Profession: {profession}, Skills: {skills}")

    if not company or not profession or not skills:
        return jsonify({'error': 'Please provide all required inputs.'}), 400

    questions = generate_questions(profession, skills)

    if not questions:
        return jsonify({'error': 'Error generating questions. Please try again later.'}), 500

    return jsonify({'questions': questions})

def generate_questions(profession, skills):
    """
    Generate job interview questions using the Hugging Face API.
    """
    API_URL = "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-2.7b"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    prompt = f"Generate 5 job interview questions for a {profession} skilled in {skills}."

    payload = {
        "inputs": prompt,
        "parameters": {"temperature": 0.7, "max_new_tokens": 150}
    }

    try:
    
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        response_data = response.json()

        if isinstance(response_data, list) and "generated_text" in response_data[0]:
            raw_text = response_data[0]["generated_text"]
            questions = [q.strip() for q in raw_text.split("\n") if q.strip()]

       
            return questions[:5] if questions else ["No relevant questions generated."]
    except requests.RequestException as e:
        print(f"Request Exception: {e}")
        return None
    except KeyError:
        print("Unexpected API Response Format")
        return None

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    """
    Endpoint to submit the quiz and calculate the score.
    """
    data = request.json 
    answers = data.get('answers', [])

   
    print(f"Answers received: {answers}")


    score = calculate_score(answers)

    eligibility = "You are eligible to apply!" if score >= 70 else "You are not eligible to apply."

    return jsonify({'score': score, 'eligibility': eligibility})

def calculate_score(answers):
    """
    Calculate the score based on the submitted answers.
    """
    correct_answers = ["yes", "no", "yes", "yes", "no"]  
    score = 0
    for i, answer in enumerate(answers):
        if i < len(correct_answers) and answer.lower() == correct_answers[i]:
            score += 20  
    return score  

if __name__ == '__main__':
   
    app.run(debug=True)
