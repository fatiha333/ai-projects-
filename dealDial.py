import streamlit as st
import requests
import io
from openai import OpenAI
from elevenlabs import ElevenLabs
from twilio.rest import Client
from dotenv import load_dotenv
import os
load_dotenv()

client=OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"))

def hunt1(service ,location):
  
  url="https://google.serper.dev/search"
  headers=os.getenv("SER_API_KEY")
  payload = {
    "q": f"dental clinic USA contact email",
    "num": 10
}

  response = requests.post(url, json=payload, headers=headers)
  data=response.json()

  clients=[]
  for result in data.get("organic", [])[:5]:
        clients.append({
            "name": result.get("title"),
            "website": result.get("link"),
            "description": result.get("snippet")
        })
  st.session_state["clients"]=clients
  return clients
def generate_pitch(service, client_name, client_description):
    response = client.chat.completions.create(
        model="poolside/laguna-m.1:free",
        messages=[{
            "role": "user",
            "content": f"""You are a world-class B2B sales agent making a cold call to a dental clinic owner.

Service: {service}
Client: {client_name}
Context: {client_description}

Rules:
- Never say "I'll be fast" — it screams salesperson
- Never assume their problem — ask about it instead
- Add ONE credibility signal (a result you got for a similar client)
- End with a specific commitment, not a vague question
- Sound like a colleague calling, not a vendor pitching
- Maximum 40 seconds when read aloud
- "NEVER start with 'Hi this is [name] from [company]' — that's the fastest way to get hung up on. 
  Start mid-conversation like you already know them."

Structure:
1. Disarming opener (not sales-y)
2. Curiosity question about their specific situation  
3. One sentence credibility — real result for similar client
4. Specific next step with a time commitment

Example of bad close: "Want to stop losing money?"
Example of good close: "I can show you exactly how [competitor clinic in their city] cut no-shows by 40% in 3 weeks — worth a 10-minute call Thursday at 2pm?"

Important: Research the client's location from their description and name a realistic competing dental clinic in that same city/area as the success story. Make the competitor feel real and local — not generic.
"""


    }]
    )
    return response.choices[0].message.content

def pitch_to_voice(pitch):
   client3=ElevenLabs(
      api_key=os.getenv("ELEVENLABS_API_KEY")
   )

   audio=client3.text_to_speech.convert(
      text=pitch,
      voice_id="pNInz6obpgDQGcFmaJgB",
      model_id="eleven_multilingual_v2",
      output_format="mp3_44100_128"
   )

   return audio
def save_and_play(audio):
   audio_bytes=io.BytesIO()
   for chunk in audio:
      audio_bytes.write(chunk)
   audio_bytes.seek(0)  
   st.audio(audio_bytes,format="audio/mp3", autoplay=True)


def make_phncall(pitch):
    account_sid=os.getenv("TWILIO_ACCOUNT_SID")
    auth_token=os.getenv("TWILIO_AUTH_TOKEN")
    client4=Client(account_sid,auth_token)
    call=client4.calls.create(
        to="+919761712139",
        from_="+19843517691",
        url="https://dental-voice-bot-production.up.railway.app/answer"
    )
    return (call.sid)

st.title("Deal Dial")
st.header(" your ai calling assistant")
st.divider()

st.header("Step 1 — Tell us about you")
service=st.text_input("enter the service u can provide" ,placeholder="eg :ai agents for dental clinic")
location=st.text_input("enter the  or location niche" ,placeholder="eg :dental clinic in usa")

st.header("Step 2 — hunt clients")
hunt=st.button("search clients")

if hunt:
  x=hunt1(service,location)
  st.session_state["clients"]=x
if "clients" in st.session_state:
  st.subheader("potential clients found")
  for i,client1 in enumerate(st.session_state["clients"]):
      with st.expander(f"{i+1}:{client1['name']}"):
         st.write(f"🌐 Website: {client1['website']}")
         st.write(f"📝 {client1['description']}")
         
         call_clients=st.button(
            "let ai call  ",
            key=f"aicall_{i}"
            )                    
         if call_clients:
             u=hunt1(service,location)
             y=generate_pitch(service,st.session_state["clients"][i]["name"],st.session_state["clients"][i]["description"])
             st.write(y)
             a=pitch_to_voice(y)
             save_and_play(a)
             make_phncall(y)


