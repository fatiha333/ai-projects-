
import streamlit as st
import pymupdf
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=""
)

def extract_text(pdf_file):
    pdf_bytes = pdf_file.read()
    doc = pymupdf.open(
        stream=pdf_bytes,
        filetype="pdf"
    )
    text=""
    for page in doc:
        text+=page.get_text()
    return text 

def chunk_text(text, doc_name, chunk_size=500):
    
    t=[]
    t=text.split(" ")
    chunks=[]
    for i in range(0,len(t),chunk_size):
        kuch_bhi={}
        kuch_bhi["text"]=" ".join(t[i:i+chunk_size])
        kuch_bhi["source"]=doc_name
        chunks.append(kuch_bhi)
    return chunks

def find_relevant_chunks(question, all_chunks):
    keywords=question.lower().split()
    relevant=[]
    for chunk in all_chunks:
     text=chunk["text"]
     if any(keyword in text.lower() for keyword in keywords):
      relevant.append(chunk)
    return relevant[:5]


def ask_ai(question, relevant_chunks):

    responses=client.chat.completions.create(
        model="nex-agi/nex-n2-pro:free",
        messages=[{"role":"user","content":(f"based on the context {relevant_chunks} answer the following question {question}")}]
    )
    return responses.choices[0].message.content

# streamlit UI
st.title("Multi-Document Research Assistant")
uploaded_files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)
question = st.text_input("Ask a question about your documents")
button = st.button("Ask")
try:
 if button and uploaded_files and question:
    chunk=[]
    for pdf in uploaded_files:
     
      a=extract_text(pdf)
      b=chunk_text(a,pdf.name,500)
      chunk.extend(b)
    c=find_relevant_chunks(question,chunk)
    source=[]

    d=ask_ai(question,c)
    st.write(d)
    st.write("sources")
    unique_sources = list(set([chunk["source"] for chunk in c]))
    for source in unique_sources:
     st.write(source)
 
except Exception as e:
   st.error(e)