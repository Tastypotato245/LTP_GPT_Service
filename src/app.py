from flask import Flask, render_template, request, jsonify
from chat_gpt import chatGPT

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index_kor.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_question = request.json.get('question')
        if not user_question:
            return jsonify({"error": "No question provided"}), 400
        response = chatGPT(user_question)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=8080)
