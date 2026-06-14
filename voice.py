import os
import uuid
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv

load_dotenv()

client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
os.makedirs("audio", exist_ok=True)

try:
    voices_response = client.voices.get_all()
    SAFE_VOICE_ID = voices_response.voices[0].voice_id
    print(f"Connected to ElevenLabs. Using allowed Voice ID: {SAFE_VOICE_ID}")
except Exception as e:
    print(f"Error fetching voices: {e}")
    SAFE_VOICE_ID = "JBFqnCBrubY8rowUnjtB" 

def generate_voice(text: str) -> str:
    """
    Takes the text from Gemini, sends it to ElevenLabs, 
    and saves the audio as an MP3 file.
    Returns the generated filename.
    """
    try:
        
        audio = client.text_to_speech.convert(
            text=text,
            voice_id=SAFE_VOICE_ID, 
            model_id="eleven_turbo_v2_5",
            output_format="mp3_22050_32"
        )
        
        filename = f"response_{uuid.uuid4().hex}.mp3"
        filepath = os.path.join("audio", filename)
        
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



if __name__ == "__main__":
    print("Testing ElevenLabs generation...")
    test_text = "Hello, I am your oil and gas assistant. How can I help you today?"
    test_file = generate_voice(test_text)
    
    if test_file:
        print(f"Success! Audio saved as audio/{test_file}")
        print("Check your project folder to listen to the MP3!")
    else:
        print("Failed to generate audio.")