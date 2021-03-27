import os
import openai
from dotenv import load_dotenv
#https://www.twilio.com/blog/environment-variables-python#:~:text=Below%20you%20can%20see%20how%20to%20import%20a,variable%20definitions%20in%20it%20to%20the%20os.environ%20dictionary.

load_dotenv()
openai.api_key = os.environ['API_KEY']
response = openai.Completion.create(engine="davinci", prompt="This is a test", max_tokens=5)

#openai.Engine.list()
print(response.get("model"))