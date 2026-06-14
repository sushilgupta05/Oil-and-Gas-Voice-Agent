import requests

# This is your local server endpoint that Twilio normally talks to
url = "http://127.0.0.1:8000/process-speech"

# We are simulating the exact data Twilio sends when a caller speaks
mock_twilio_data = {
    "SpeechResult": "What is the difference between upstream and downstream in the oil industry?"
}

print("Simulating inbound Twilio call...")
try:
    response = requests.post(url, data=mock_twilio_data)
    print("\n--- Success! Here is what your server told Twilio to do ---")
    print(response.text)
except Exception as e:
    print(f"Error connecting to server: {e}")