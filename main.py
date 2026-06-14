import os
from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from twilio.twiml.voice_response import VoiceResponse, Gather
from agent import get_agent_response
from voice import generate_voice

app = FastAPI()

os.makedirs("audio", exist_ok=True)
app.mount("/audio", StaticFiles(directory="audio"), name="audio")

@app.post("/incoming-call")
async def incoming_call(request: Request):
    """
    Endpoint 1: Triggered when someone dials your Twilio phone number.
    """
    response = VoiceResponse()
    gather = Gather(input='speech', action='/process-speech', timeout=5, speechTimeout=2)
    base_url = str(request.base_url).rstrip('/')
    gather.play(f"{base_url}/audio/greeting.mp3")
    
    response.append(gather)
    
    response.redirect('/incoming-call')
    
    return Response(content=str(response), media_type="application/xml")

@app.post("/process-speech")
async def process_speech(request: Request):
    """
    Endpoint 2: Triggered when Twilio has successfully transcribed the caller's speech.
    """
    form_data = await request.form()
    user_speech = form_data.get('SpeechResult', '')
    
    print(f"\n[CALLER SAID]: {user_speech}")

    response = VoiceResponse()

    if not user_speech:
        gather = Gather(input='speech', action='/process-speech', timeout=5)
        base_url = str(request.base_url).rstrip('/')
        gather.play(f"{base_url}/audio/greeting.mp3")
        response.append(gather)
        response.redirect('/incoming-call')
        return Response(content=str(response), media_type="application/xml")

    print("Thinking...")
    ai_text = get_agent_response(user_speech)
    print(f"[AGENT THOUGHT]: {ai_text}")

    print("Generating voice...")
    audio_filename = generate_voice(ai_text)

    if audio_filename:
        base_url = str(request.base_url).rstrip('/')
        audio_url = f"{base_url}/audio/{audio_filename}"
        
        print(f"[PLAYING AUDIO]: {audio_url}")
        response.play(audio_url)
    else:
        response.say(ai_text, voice='alice')

    gather = Gather(input='speech', action='/process-speech', timeout=5, speechTimeout=2)
    response.append(gather)
    
    response.redirect('/incoming-call')

    return Response(content=str(response), media_type="application/xml")