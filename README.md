# 🛢️ Oil & Gas AI Voice Agent

An intelligent, real-time voice assistant built to answer complex, domain-specific questions about the oil and gas industry over a standard phone call.

Powered by **Google Gemini 2.5 Flash** and **ElevenLabs**, this conversational AI is designed with strict guardrails to decline off-topic queries and maintain a professional, industry-focused interaction.

---

## ✨ Core Features

### 🔒 Strict Domain Guardrails

The agent utilizes a rigid system prompt. If asked an off-topic question (e.g., weather, sports, trivia), it politely declines and re-centers the conversation on the oil and gas sector.

### ⚡ Low-Latency Architecture

Optimized token generation limits and aggressive Twilio speech-timeout parameters ensure fast, natural conversational pacing.

### 🎙️ Unified Voice Experience

Seamlessly transitions between pre-generated static greetings and dynamically generated ElevenLabs text-to-speech to prevent voice mismatch.

### 🔄 Resilient Loop Handling

Intelligently handles caller silence by re-prompting the user and looping the webhook flow to prevent accidental call drops.

---

# 📞 Option 1: Try the Live Cloud Demo (Direct Call)

The fastest way to test the agent is to call the live deployment hosted on Render.

## Step 1: Wake the Server

Open your browser and visit:

```text
https://your-render-app.onrender.com
```

> **Note**
>
> Since the backend is hosted on a free-tier instance, it automatically sleeps after periods of inactivity. Visiting the URL wakes the server before placing a call.
>
> The page may display **"Not Found"** — this is expected behavior and simply indicates the server is awake.

## Step 2: Dial the Agent

Call your Twilio phone number:

```text
+1 XXX XXX XXXX
```

## Step 3: Start Talking

Wait for the greeting to finish, then ask an oil and gas related question.

### Example Questions

* What is the difference between upstream and downstream operations?
* How does hydraulic fracturing work?
* What are the major refining processes?
* What is LNG and how is it transported?

---

# 💻 Option 2: Run Locally (Inbound Direct Call)

In this setup, anyone can call your Twilio number and Twilio will route the conversation directly to your local machine.

---

## Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/oil-gas-ai-agent.git
cd oil-gas-ai-agent
```

---

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 3: Configure Environment Variables

Create a file named `.env` in the project root directory:

```env
GEMINI_API_KEY=your_gemini_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

---

## Step 4: Start the FastAPI Server

Run:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Keep this terminal running.

---

## Step 5: Create a Public Tunnel with ngrok

Open a second terminal and run:

```bash
ngrok http 8000
```

You will see output similar to:

```text
Forwarding https://abcdef123.ngrok-free.dev -> http://localhost:8000
```

Copy the HTTPS URL.

Keep this terminal running.

---

## Step 6: Connect Twilio to Your Local Server

1. Log in to your Twilio Console.
2. Navigate to:

```text
Phone Numbers → Manage → Active Numbers
```

3. Select your Twilio phone number.
4. Scroll to the **Routing** section.
5. Under **"A Call Comes In"**, paste:

```text
https://abcdef123.ngrok-free.dev/incoming-call
```

6. Save the configuration.

---

## Step 7: Test the Application

Call your Twilio number.

You should immediately see logs appearing in your FastAPI terminal as the AI processes the conversation in real time.

---

# 📲 Option 3: Run Locally via Trigger Script (Outbound Call)

Use this method if you cannot directly dial your Twilio number (for example, due to international calling restrictions).

Instead, Twilio will call your personal phone and connect you to the AI.

---

## Step 1: Start Local Services

Complete the following from **Option 2**:

* Start FastAPI (`uvicorn`)
* Start ngrok

Both services must remain running.

---

## Step 2: Update Your Environment Variables

Add Twilio credentials to your `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key

TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token

TWILIO_NUMBER=your_twilio_phone_number
MY_PHONE_NUMBER=your_personal_mobile_number
```

---

## Step 3: Configure the Trigger Script

Open:

```text
trigger_call.py
```

Locate:

```python
NGROK_URL = "https://abcdef123.ngrok-free.dev/incoming-call"
```

Replace it with your active ngrok URL.

Example:

```python
NGROK_URL = "https://abcdef123.ngrok-free.dev/incoming-call"
```

Save the file.

---

## Step 4: Initiate the Call

Open a third terminal and run:

```bash
python trigger_call.py
```

Expected output:

```text
Call initiated successfully!
```

---

## Step 5: Answer the Phone

Within a few seconds:

1. Your phone will ring.
2. Answer the call.
3. Wait for the AI greeting.
4. Start asking oil and gas related questions.

---

# 🏗️ Technology Stack

| Component       | Technology              |
| --------------- | ----------------------- |
| LLM             | Google Gemini 2.5 Flash |
| Voice Synthesis | ElevenLabs              |
| Telephony       | Twilio                  |
| Backend         | FastAPI                 |
| Tunneling       | ngrok                   |
| Hosting         | Render                  |
| Language        | Python                  |

---

# 📂 Project Structure

```text
├── main.py
├── trigger_call.py
├── requirements.txt
├── .env
├── static/
│   └── greeting.mp3
├── utils/
├── templates/
└── README.md
```

---

# ⚠️ Limitations

* Designed exclusively for oil & gas industry discussions.
* Free-tier hosting may introduce cold-start delays.
* Requires valid API credentials for Gemini and ElevenLabs.
* Twilio charges may apply depending on usage and call volume.

---

