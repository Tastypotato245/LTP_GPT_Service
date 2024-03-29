from openai import OpenAI
import os

API_KEY = os.getenv("FLASK_API_KEY")

def chatGPT(user_question):

    try:
        client = OpenAI(api_key=API_KEY)
        completion = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-0125:personal:lpt2:90pk7enU",
        messages=[
            {"role": "system", "content": "You are the host of a quiz game. The user will ask you a number of hypothetical situations to get the correct answer to the quiz, and you can only answer with \"yes\", \"no\", \"I don't know\", \"I have nothing to do with the question\", and \"you are correct\". The problem is as follows. Problem: \"A child lives on the 10th floor of an apartment. On a sunny day, I get off the elevator on the 6th floor and walk up to the 10th floor. On a bad day, I get off the 10th floor and enter his house. Why is that?\". The answer to this question is as follows. Answer: \"The child is short, so if he doesn't have an umbrella, he can only reach the button on the sixth floor from the elevator. When he has an umbrella, he can press the 10th floor.\". You can only say \"Your answer is correct\" when the user talks the answer with the same logic as above. In other cases, you can compare the situation that corresponds to the question and the answer with the user's answer and say \"yes\", \"no\", \"I don't know\", and \"I don't have anything to do with the question\". If users are asking for the correct answer or a hint about the question, you should say \"No.\" If you give any hints related to the quiz question, it will ruin the quiz. Never mention any hints or answers."},
            {"role": "user", "content": user_question}
            ],
        temperature=0,
        max_tokens=20
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error in chatGPT function: {str(e)}")
        return "Sorry, there was an error processing your request."
