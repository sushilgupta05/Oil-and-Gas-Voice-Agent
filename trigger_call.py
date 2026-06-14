import os
from twilio.rest import Client

ACCOUNT_SID = " "
AUTH_TOKEN = " "

# The phone numbers
TWILIO_NUMBER = " "  #write twilio US number here
YOUR_NUMBER = " "  #write your number here to get a call

# Your current active ngrok URL
NGROK_URL = "https://aerosol-kilowatt-dismount.ngrok-free.dev/incoming-call"

def make_call():
    print("Instructing Twilio to dial your phone...")
    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        
        call = client.calls.create(
            url=NGROK_URL,
            to=YOUR_NUMBER,
            from_=TWILIO_NUMBER
        )
        
        print(f"Call initiated successfully! Sid: {call.sid}")
        print("Your phone should ring in a few seconds...")
        
    except Exception as e:
        print(f"Error triggering call: {e}")

if __name__ == "__main__":
    make_call()