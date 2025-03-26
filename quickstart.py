from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(
    # This will load your API key from the OPENAI_API_KEY environment variable

    api_key=os.getenv("OPENAI_API_KEY")
)

def get_completion(prompt):
    # Create a chat completion using the GPT-3.5-turbo model
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    # Return the generated response
    return completion.choices[0].message.content

def main():
    # Example usage
    prompt = "What is artificial intelligence?"
    response = get_completion(prompt)
    print(f"Prompt: {prompt}")
    print(f"Response: {response}")

if __name__ == "__main__":
    main() 