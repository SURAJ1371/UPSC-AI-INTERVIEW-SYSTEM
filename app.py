from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/questions', methods=['GET'])
def get_questions():
    questions = [
        {
            "question": "What are the main challenges facing India today?",
            "keywords": ["poverty", "education", "corruption", "healthcare", "environment"]
        },
        {
            "question": "Discuss the importance of the Constitution.",
            "keywords": ["rights", "justice", "equality", "fraternity", "democracy"]
        },
        {
            "question": "What is the significance of the Green Revolution?",
            "keywords": ["agriculture", "food security", "technology", "production"]
        },
        {
            "question": "Explain the role of the Election Commission in India.",
            "keywords": ["free and fair elections", "independence", "voter turnout"]
        },
        {
            "question": "How does globalization affect India?",
            "keywords": ["economy", "culture", "trade", "technology"]
        }
        # Add more questions and keywords as needed
    ]
    return jsonify({"questions": questions})

if __name__ == '__main__':
    app.run(debug=True)
