import requests
import os
import openai
from dotenv import load_dotenv
#https://www.twilio.com/blog/environment-variables-python#:~:text=Below%20you%20can%20see%20how%20to%20import%20a,variable%20definitions%20in%20it%20to%20the%20os.environ%20dictionary.

load_dotenv()
openai.api_key = os.environ['OPENAI_KEY']
placesKey = os.environ['PLACES_KEY']


#get input about the symptoms
inputString = input("How have you been feeling? ")

#Ensure user is referring to self
firstLetter = inputString[0]
if "i" not in firstLetter.lower():
    inputString = "I have been " + inputString



response = openai.Completion.create(
  engine="davinci",
  prompt="""Apollo is a doctor that is providing the patient a general medical diagnosis.\n\n\"\"\"\n\n

            Patient: I have been coughing, nasal congestion, and it's been difficult to breath. I feel dizzy and I can't sleep. What am I experiencing?\n\n
            Apollo: Flu - a viral infection that causes a fever, cough, sore throat, and body aches. It is spread through the air when people cough or sneeze. It can also be spread through direct contact with infected people.\n\n
            Patient: What is the best way to treat the flu?\n\n
            Apollo: The best way to treat the flu is to rest and drink plenty of fluids. You should also take over-the-counter cough and cold medicines to relieve your symptoms.\n\n\"\"\"\n\n
            
            Patient: I have been having chest pain and sore throat. What am I experiencing?\n\n
            Apollo: Scurvy - a disease that is caused by a vitamin C deficiency.\n\n
            Patient: What is the best way to trDizzeat scurvy?\n\n
            Apollo: The best way to treat scurvy is to eat fresh fruits and vegetables that are rich in Vitamin C\n\n\"\"\"\n\n

            Patient: I have been feeling like I have a lot of mucus in my throat and can't breath. What am I experiencing?\n\n
            Apollo: Postnasal drip - the accumulation of mucus in the nose and throat.\n\n
            Patient: What is the best way to treat Postnasal drip?\n\n
            Apollo: The best way to treat postnasal drip is to drink warm fluids and rinse your sinuses.\n\n\"\"\"\n\n
            
            Patient: I have been feeling inflammation in the ear. What am I experiencing?\n\n
            Apollo: Otitis media - a middle ear infection that is accompanied by swelling and pain.\n\n
            Patient: What is the best way to treat otitis media?\n\n
            Apollo: The best way to treat otitis media is to treat the infection with antibiotics.\n\n\"\"\"\n\n
            
            Patient: """ + inputString + """. What am I experiencing?\n\n
            Apollo:""",
  temperature=0.7,
  max_tokens=64,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

info = response.get("choices")
answer = info[0].get("text")
illness = answer.split('-')
print(illness[0] + illness[1]) #illness keyword + description and suggestion follow up actions

print("\n\n")

url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
query = illness[0]
inputtype="textquery"
fields="formatted_address,name,types"

response = requests.get(url + "input=" + query + "&inputtype=" + inputtype + "&fields=" + fields + "&key=" + placesKey).json()
print(response["candidates"])