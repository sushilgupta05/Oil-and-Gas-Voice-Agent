import os
import shutil
from voice import generate_voice

print("Generating consistent greeting...")
# 1. Generate the audio using your exact ElevenLabs setup
temp_filename = generate_voice("Hello. I am the Oil and Gas Assistant. How can i help you sir.")

if temp_filename:
    # 2. Rename it to 'greeting.mp3' so main.py can always find it
    old_path = os.path.join("audio", temp_filename)
    new_path = os.path.join("audio", "greeting.mp3")
    
    # Overwrite if it already exists
    if os.path.exists(new_path):
        os.remove(new_path)
        
    shutil.move(old_path, new_path)
    print("Success! 'greeting.mp3' is now ready in your audio folder.")
else:
    print("Failed to generate greeting. Check your ElevenLabs API key.")