from openai_init import OpenAICompletion
from colorama import Fore
from flask import Flask, request
from twilio.rest import Client
from dotenv import load_dotenv

openai = OpenAICompletion()

app = Flask(__name__)
@app.route('/whatsapp', methods=['POST'])
def handle_incoming_messages():
    message = request.form['Body']
    # Generate response with chatbot
    response = openai.obtain_completion(message)

    # Send response to whatsapp
    account_sid='AC9bb93369da6628415e740ccbd6ec13cb'
    auth_token='89836183f6bf2f7e86e1dda9dc02f928'
    client = Client(account_sid, auth_token)
    number = request.form['From']

    to_number = number
    client.messages.create(
        to=to_number,
        from_='whatsapp:+14155238886',
        body=response
    )

    # Send respopnse to twilio
    return 'Return: OK'



if __name__ == '__main__':
    load_dotenv()
    
    app.run()

