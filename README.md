# HackAI-2021
**Tranquil.ai** - Expects a list of symptoms that the user may be experiencing, and provides a simple diagnosis and prediction of potential illnesses. The program also suggests treatment and performs a search query to find the user a near location of a facility that may be of help. This project is for **HackAI**, an AI-focused hackathon held by AIS at UTD.
***

## Technologies
* [OpenAI's beta API](https://beta.openai.com/docs/introduction)
  * Engine: davinci, a pre-trained model
  * Receives a dataset of a conversation between a patient and a doctor, Apollo, to perform text completion
  * The dataset maintains a pattern so that the API will output the first word to identify the potential illness
* [Google Maps Places API](https://developers.google.com/maps/documentation/places/web-service/search)
  * Find Places Search
  * Performs a search query using the keyword given by Apollo's diagnosis
  * Searches nearby locations that specialize in countering the illness

## Sample Outputs
### Sample 1
`How have you been feeling? inflammation in the ear`<br>
`Otitis media - a middle ear infection that is accompanied by swelling and pain.` <br>
<br>
`Patient: What is the best way to treat otitis media?`<br>
<br>
`Apollo: The best way to treat otitis media is to treat the infection with antibiotics`
<br>
<br>
`There is no specialized facility for otitis media in your area.`
<br>
### Sample 2
`How have you been feeling? backpain`<br>
`Muscle strain - a a type of injury caused by overusing a muscle.` <br>
<br>
`Patient: What is the best way to treat muscle strain?`<br>
<br>
`Apollo: The best way to treat muscle strain is to rest`
<br>
<br>
`Health location(s) that may be of help to you:`<br>
`Texas Institute of Orthopedic Surgery & Sports Medicine`<br>
`815 Ira E Woods Ave #100, Grapevin, TX 75061, United States`

## What's next for Tranquil.ai
Creating a GUI to make it more accessible to clients.
