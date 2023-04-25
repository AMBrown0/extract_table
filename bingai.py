import requests

# Get your Bing Web Search API key from https://portal.azure.com/.
subscription_key = "YOUR_SUBSCRIPTION_KEY"

# Define the search query.
query = "What is the weather in London today?"

# Make a request to the Bing Web Search API.
response = requests.get("https://api.cognitive.microsoft.com/bing/v7.0/search?q=" + query + "&mkt=en-us&subscription_key=" + subscription_key)

# Format and display the response.
results = response.json()
print("The weather in London today is:")
print(results["d"]["weather"][0]["description"])
