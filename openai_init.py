from openai import OpenAI
from dotenv import load_dotenv
from colorama import Fore

context = [{'role': 'system', 'content': 'Eres un chatbot de soporte para un canal de Whatsapp.'}]

class OpenAICompletion:
    def __init__(self):
        load_dotenv()  # Load environment variables from .env file
        self.client = OpenAI()  # Initialize the OpenAI client
        self.model = 'gpt-3.5-turbo-0125'

    def obtain_completion(self, messages):
        try:
            # Create a completion using the GPT-3.5-turbo model
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0,
                max_tokens=200
            )
            # Extract the response content from the completion
            return completion.choices[0].message.content
        except Exception as e:
            # Return the error message if an exception occurs
            return f"Error: {str(e)}"
        
    def collect_messages(self, prompt):
        context.append({'role': 'user', 'content': prompt})
        response = self.obtain_completion(context)
        context.append({'role': 'assistant', 'content': response})
        return response