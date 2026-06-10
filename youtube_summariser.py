import streamlit as st
from openai import  OpenAI
from youtube_transcript_api import YouTubeTranscriptApi
#setup client to send message to open ai 
client=OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["OPENROUTER_API_KEY"])

def extract_id(input):
    url=str.split(input,"v=")
    x=url[1]
    t=""
    for i in x:
     if(i.isalnum()):
        t+=i     
     else:
      break
    return t

def yt_api(id):
    
    ytt_api = YouTubeTranscriptApi()
    transcript = ytt_api.fetch(id)
    text=""
    for i in transcript:
        text+=" "+i.text
    return text
# now send query and ask it to summarise this 
def aisummary(query):
    responses=client.chat.completions.create(
        model="nex-agi/nex-n2-pro:free",
        messages=[{"role":"user","content":(f"summarise the following content {query}")}]
    )
    return responses.choices[0].message.content
st.title("youtube video summariser")
input=st.text_area("enter the video url")
button1=st.button("submit")
try:
  if button1:
   a=extract_id(input)
   b=yt_api(a)
   c=aisummary(b)

   st.markdown( f"## the summary of the respective youtube video is :\n")
   st.write(c)
except Exception as e:
 st.error(f" something went wrong {e}")



