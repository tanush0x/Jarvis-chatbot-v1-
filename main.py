# this is a jarvis created by tanush r 
import os
  

print("---------J.A.R.V.I.S---------------------")
print("        🤖🤖JARVIS ONLINE ")
while True:
  

  from groq import Groq
  

  client = Groq(
    api_key="",
)

  chat_completion = client.chat.completions.create(
    messages=[
         {
            "role": "system",
            "content": "You are a helpful assistant named as jarvis . Keep your answers brief, scannable, and under 3 sentences.and you are created by Tanush R",
        },
        {
            "role": "user",
            "content":input("enter the question below :- "),
            
          
       
             
        }
    ],
   
    model="openai/gpt-oss-120b",
    max_tokens=100, #set the tokens as you want for better answer 
)

  print(chat_completion.choices[0].message.content)

  
