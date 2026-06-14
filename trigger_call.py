import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
YOUR_NUMBER = os.getenv("MY_PHONE_NUMBER")

RENDER_URL = "https://oil-and-gas-voice-agent.onrender.com/incoming-call"

def make_call():
    print("Instructing Twilio to dial your phone via Render...")
    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        
        call = client.calls.create(
            url=RENDER_URL,
            to=YOUR_NUMBER,
            from_=TWILIO_NUMBER
        )
        
        print(f"Call initiated successfully! Sid: {call.sid}")
        print("Your phone should ring in a few seconds...")
        
    except Exception as e:
        print(f"Error triggering call: {e}")

if __name__ == "__main__":
    make_call()