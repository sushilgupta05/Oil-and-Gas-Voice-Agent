import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_INSTRUCTION = """
You are a highly knowledgeable, professional, and conversational AI assistant representing the Oil and Gas industry. 
Your strict rule: You may ONLY answer questions related to the oil and gas domain (e.g., drilling, refining, pipelines, petroleum economics, geology, petrochemicals). 

If a user asks a question about ANY other topic (e.g., weather, sports, general trivia, history, coding), you must politely decline and state that you are only programmed to discuss the oil and gas industry.

Keep your answers concise (1-3 sentences maximum), natural-sounding, and easy to understand over a phone call. Do not use markdown formatting like bolding or bullet points, as your text will be read aloud by a text-to-speech engine.
"""

def get_agent_response(user_query: str) -> str:
    """
    Takes the transcribed voice input from Twilio, sends it to Gemini, 
    and returns the strictly filtered text response.
    """
    try:
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_query,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION,
                temperature=0.3
            ),
        )
        return response.text.strip()
        
    except Exception as e:
        print(f"LLM Error: {e}")
        return "I apologize, but I am having trouble connecting to my database right now. Please try your question again."


if __name__ == "__main__":
    print("Testing Oil & Gas Query:")
    print(get_agent_response("What is the difference between upstream and downstream?"))
    print("\nTesting Off-Topic Query:")
    print(get_agent_response("What is the capital of France?"))