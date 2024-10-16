from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route to serve the index.html page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle chat responses
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('message').strip().lower()

    # Simple response logic handling numeric inputs
    if user_input == 'hello':
        response = ("Hello! Welcome to SKARK Banking System. How can I assist you today?<br>"
                    "You can ask me about:<br>"
                    "1.🧾 <span style='color:white;'>Check your balance</span><br>"
                    "2.💸 <span style='color:white;'>Make a transfer</span><br>"
                    "3.📋 <span style='color:white;'>Get help</span><br>"
                    "Please enter the number of the option you'd like to choose.")

    elif user_input in ['1', 'check balance', 'balance']:
        response = ("To check your balance, please log in to your account through our banking portal.<br>"
                    "Would you like me to guide you to the login page?")

    elif user_input in ['2', 'make a transfer', 'transfer']:
        response = ("You can transfer money using our online banking service.<br>"
                    "Here are your options:<br>"
                    "1.📑 <span style='color:white;'>Get the steps to make a transfer</span><br>"
                    "2.🔗 <span style='color:white;'>I can guide you to the transfer section</span><br>"
                    "What would you prefer?")

    elif user_input in ['3', 'help']:
        response = ("I'm here to assist you! You can choose from the following options:<br>"
                    "1.🧾 <span style='color:white;'>'Check balance' to view your account balance</span><br>"
                    "2.💸 <span style='color:white;'>'Make a transfer' to transfer money</span><br>"
                    "3.ℹ️ <span style='color:white;'>'Account details' to view your account info</span><br>"
                    "Which one would you like help with?")

    elif 'how are you' in user_input:
        response = ("I'm doing well! Thank you for asking. I'm here to assist you with your banking needs.<br>"
                    "You can ask about:<br>"
                    "1.🧾 <span style='color:white;'>Checking your balance</span><br>"
                    "2.💸 <span style='color:white;'>Making a transfer</span><br>"
                    "3.📋 <span style='color:white;'>Getting help</span><br>"
                    "Please choose an option by entering its number.")

    else:
        response = ("I'm sorry, I didn't understand that.<br>"
                    "Here are a few options you can try:<br>"
                    "1.🧾 <span style='color:white;'>'Check balance' to view your account balance</span><br>"
                    "2.💸 <span style='color:white;'>'Make a transfer' to transfer money</span><br>"
                    "3.📋 <span style='color:white;'>'Help' to see available options.</span><br>"
                    "Please choose an option by entering its number.")

    # Return the response as JSON
    return jsonify({'response': response})

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
