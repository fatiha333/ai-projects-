from openai import OpenAI
#first create client
client=OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="")
# send and recieve response  
def ask_ai(question):
 responses=client.chat.completions.create(
    model="nex-agi/nex-n2-pro:free",
    messages=[{"role":"user","content":question}]
  )
 return responses.choices[0].message.content
x=""
#print response 
while(x!="quit"):
  x=input("enter question ")
  y=ask_ai(x)
  print(y)