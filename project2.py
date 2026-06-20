
import streamlit as st
import pymupdf
from openai import OpenAI
from sentence_transformers import SentenceTransformer
import faiss 
import numpy as np
from dotenv import load_dotenv
import os

import nltk
nltk.download('punkt_tab')

load_dotenv()
model=SentenceTransformer("all-MiniLM-L6-v2")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
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

def chunk_text(text, doc_name,threshold,min_sentences):
   
   sentences=nltk.sent_tokenize(text)
   if( len(sentences)<=1):
      return [{'text':" ".join(sentences),'source':doc_name}]
   embedding=model.encode(sentences)
   #un embedding ko similarity match 
   sims=[]
   for i in range(len(embedding)-1):
      a,b=embedding[i],embedding[i+1]
      sim=np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))#np.linalg.norm(a) ye length of vector k liye 
      sims.append(sim)
   #ab hum groups bnayenge according to similarity scores 
   groups=[]
   chunk=[sentences[0]]
   for i,sim in enumerate(sims):
      if(sim >=threshold):
         chunk.append(sentences[i+1])
      else:
         groups.append(chunk)
         chunk=[sentences[i+1]]
   groups.append(chunk)
 # ab agr koi chota grp ha toh usko previous m merge kr denge 
 #iterate through each item in group if chunk size is less than 
   merged=[]
   for g in groups:
      if merged and len(g)< min_sentences:
         merged[-1].extend(g)
      else:
         merged.append(g)
    
   chunks=[]
   for c in merged:
      chunks.append({'text':" ".join(c),'source':doc_name})
   return chunks
      
         

      
      
   

def find_relevant_chunks(question, all_chunks):

   embedding=model.encode([chunk['text'] for chunk in all_chunks])#ye andar isliye daala kyunki list comprehension or ye ek list hi return krta h toh isliye naye variable m store nhi kiya 
   index=faiss.IndexFlatL2(384)
   index.add(embedding)
   query=np.array([model.encode(question)])
   distances,indices=index.search(query,5)
   final=[]
   for x in indices[0]:
      final.append(all_chunks[x])
   return final

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
      b=chunk_text(a,pdf.name,0.65,2)
      chunk.extend(b)
    c=find_relevant_chunks(question,chunk)
    source=[]
    print(f"{len(b)} chunks created")
    for chunk in b:
     st.write(len(chunk['text']), "chars —", chunk['text'][:80])
    
    st.divider()
    d=ask_ai(question,c)
    st.write(d)
    st.write("sources")
    unique_sources = list(set([chunk["source"] for chunk in c]))
    for source in unique_sources:
     st.write(source)
 
except Exception as e:
   st.error(e)
