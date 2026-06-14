# 🛢️ Oil & Gas AI Voice Agent

An intelligent, real-time voice assistant built to answer complex, domain-specific questions about the oil and gas industry over a standard phone call.

Powered by **Google Gemini 2.5 Flash** and **ElevenLabs**, this conversational AI is designed with strict guardrails to decline off-topic queries and maintain a professional, industry-focused interaction.

---

## ✨ Core Features

### 🔒 Strict Domain Guardrails

The agent utilizes a rigid system prompt. If asked an off-topic question (e.g., weather, sports, trivia), it politely declines and re-centers the conversation on the oil and gas sector.

### 🎙️ Unified Voice Experience

Seamlessly transitions between pre-generated static greetings and dynamically generated ElevenLabs text-to-speech to prevent voice mismatch.

### 🔄 Resilient Loop Handling

Intelligently handles caller silence by re-prompting the user and looping the webhook flow to prevent accidental call drops.


# 💻 Option 1: Run Locally (Inbound Direct Call)

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
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
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

# 📲 Option 2: Run Locally via Trigger Script (Outbound Call)

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

# ☁️ Option 3: Deploy on Render (Recommended)

Once you've tested the application locally, you can deploy it to Render for 24/7 access.

## Step 1: Push Your Code to GitHub

Make sure your project is committed and pushed to a GitHub repository.

```bash
git add .
git commit -m "Initial deployment"
git push origin main
```

---

## Step 2: Create a Render Web Service

1. Log in to Render.
2. Click **New → Web Service**.
3. Connect your GitHub account.
4. Select this repository.
5. Configure the service:

```text
Runtime: Python
Build Command: pip install -r requirements.txt
Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
```

6. Click **Create Web Service**.

---

## Step 3: Add Environment Variables

In the Render dashboard, navigate to:

```text
Settings → Environment Variables
```

Add the following:

```env
GEMINI_API_KEY=your_gemini_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key

TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
```

Save and redeploy the service.

---

## Step 4: Configure Twilio Webhook

After deployment, Render will provide a URL similar to:

```text
https://your-app-name.onrender.com
```

Open Twilio Console and navigate to:

```text
Phone Numbers → Manage → Active Numbers
```

Select your Twilio number and set:

```text
https://your-app-name.onrender.com/incoming-call
```

under **"A Call Comes In"**.

Save the configuration.

---

## Step 5: Call the Agent

Dial your Twilio phone number.

The call will be routed to your Render-hosted AI agent, allowing anyone with access to the number to interact with the system without running a local server.


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

# Important points

* Designed exclusively for oil & gas industry discussions.
* Free-tier hosting may introduce cold-start delays.
* Requires valid API credentials for Gemini and ElevenLabs.
* Twilio charges may apply depending on usage and call volume.

---

