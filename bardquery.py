import os
import requests

# Set the API key
API_KEY = "AIzaSyAONUM8ScgrRnnM-HVjAAGj4BmyypqhRLU"

# Create the request URL
URL = "https://bard.ai/v1/generate"

# Set the request parameters
PARAMS = {
    "prompt": "What is the meaning of life?",
    "temperature": 0.7,
    "max_tokens": 100,
    "n": 1,
    "no_repeat_ngram_size": 3,
    "presence_penalty": 0.2,
    "stop_token": "</s>",
    "early_stopping": True,
    "do_sample": True,
    "num_return_sequences": 1,
    "use_gpu": False,
    "seed": 42,
}

# Make the request
response = requests.post(URL, params=PARAMS, headers={"Authorization": "Bearer " + API_KEY})

# Check the response status code
if response.status_code == 200:
    # Get the response body
    response_body = response.json()

    # Print the generated text
    print(response_body["generated_text"])
else:
    print(response.status_code)
