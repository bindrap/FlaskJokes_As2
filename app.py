from flask import Flask, jsonify, request
import requests
import random

app = Flask(__name__)

# API route for generating random jokes
@app.route('/jokes', methods=['GET'])
def get_jokes():
    num_jokes = int(request.args.get('num', 1))  # Get the 'num' parameter from the URL, default to 1 if not provided
    jokes = fetch_random_jokes(num_jokes)  # Fetch random jokes from an external API or database
    return jsonify(jokes)

# Function to fetch random jokes from a local source
def fetch_random_jokes(num):
    jokes = []
    # Your logic to fetch random jokes from a local source
    for _ in range(num):
        joke = generate_random_joke()  # Call a function to generate a random joke
        jokes.append(joke)
    return jokes

# Function to generate a random joke
def generate_random_joke():
    # Your logic to generate a random joke goes here
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Did you hear about the mathematician who's afraid of negative numbers? He will stop at nothing to avoid them!",
        "I'm reading a book about anti-gravity. It's impossible to put down!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "I used to play piano by ear, but now I use my hands.",
        "Why don't oysters donate to charity? Because they are shellfish!",
        "I'm on a whiskey diet. I've lost three days already!",
        "Why don't eggs tell jokes? Because they might crack up!",
        "I'm reading a book about mazes. I got lost in it!",
        "Why don't skeletons fight each other? They don't have the guts!",
    ]
    return random.choice(jokes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

