import os
import shutil
from voice import generate_voice

print("Generating consistent greeting...")

temp_filename = generate_voice("Hello. I am the Oil and Gas Assistant. How can i help you sir.")

if temp_filename:
    old_path = os.path.join("audio", temp_filename)
    new_path = os.path.join("audio", "greeting.mp3")
    
    if os.path.exists(new_path):
        os.remove(new_path)
        
    shutil.move(old_path, new_path)
    print("Success! 'greeting.mp3' is now ready in your audio folder.")
else:
    print("Failed to generate greeting. Check your ElevenLabs API key.")