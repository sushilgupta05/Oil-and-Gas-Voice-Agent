from voice import generate_voice
# Run this once to create your greeting
greeting_file = generate_voice("Hello. I am the Oil and Gas AI Assistant. How can i help you sir.")
print(f"Rename the file {greeting_file} to 'greeting.mp3' and put it in your /audio folder.")