import os
import uuid
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv

# Load API keys
load_dotenv()

# Initialize the ElevenLabs client
client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

# Create a folder called 'audio' to store the temporary mp3 files
os.makedirs("audio", exist_ok=True)

# ---------------------------------------------------------
# NEW: Dynamically fetch an allowed free-tier voice ID ONCE 
# to avoid the 402 Payment Required error and prevent latency
# ---------------------------------------------------------
try:
    voices_response = client.voices.get_all()
    # Get the very first available voice authorized for your free account
    SAFE_VOICE_ID = voices_response.voices[0].voice_id
    print(f"Connected to ElevenLabs. Using allowed Voice ID: {SAFE_VOICE_ID}")
except Exception as e:
    print(f"Error fetching voices: {e}")
    SAFE_VOICE_ID = "JBFqnCBrubY8rowUnjtB" # Fallback to a standard default
# ---------------------------------------------------------

def generate_voice(text: str) -> str:
    """
    Takes the text from Gemini, sends it to ElevenLabs, 
    and saves the audio as an MP3 file.
    Returns the generated filename.
    """
    try:
        # Generate the audio using the safe, dynamically fetched voice ID
        audio = client.text_to_speech.convert(
            text=text,
            voice_id=SAFE_VOICE_ID, 
            model_id="eleven_turbo_v2_5",
            output_format="mp3_22050_32"
        )
        
        # Create a unique filename (e.g., response_abc123.mp3)
        filename = f"response_{uuid.uuid4().hex}.mp3"
        filepath = os.path.join("audio", filename)
        
        # Save the audio bytes to the file safely
        with open(filepath, "wb") as f:
            if isinstance(audio, bytes):
                f.write(audio)
            else:
                for chunk in audio:
                    if chunk:
                        f.write(chunk)
                
        return filename
        
    except Exception as e:
        print(f"ElevenLabs Error: {e}")
        return None

# --- Quick Local Test ---
# Run this file directly to test the text-to-speech connection
if __name__ == "__main__":
    print("Testing ElevenLabs generation...")
    test_text = "Hello, I am your oil and gas assistant. How can I help you today?"
    test_file = generate_voice(test_text)
    
    if test_file:
        print(f"Success! Audio saved as audio/{test_file}")
        print("Check your project folder to listen to the MP3!")
    else:
        print("Failed to generate audio.")