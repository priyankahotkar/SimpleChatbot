# Install required library
!pip install google-api-python-client

# Import required libraries
from googleapiclient.discovery import build

# Set up your API key and Search Engine ID
API_KEY = "AIzaSyBrGQy8imhn-Zb0RuS6OHzqFVDVCEjslUY"  # Replace with your API key
SEARCH_ENGINE_ID = "f2791d5b3d8ed4621"  # Replace with your Search Engine ID

# Define the chatbot function
def google_chatbot():
    print("Hi! I am your Google chatbot. Ask me anything or type 'exit' to stop.")
    
    # Build the service object
    service = build("customsearch", "v1", developerKey=API_KEY)
    
    while True:
        # Take user input
        query = input("You: ")
        
        # Exit condition
        if query.lower() == "exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        try:
            # Perform the search
            result = service.cse().list(q=query, cx=SEARCH_ENGINE_ID, num=1).execute()
            
            # Extract and display the top result
            if "items" in result:
                top_result = result["items"][0]
                title = top_result.get("title")
                snippet = top_result.get("snippet")
                link = top_result.get("link")
                
                print(f"Chatbot: {title}\n{snippet}\nLearn more: {link}")
            else:
                print("Chatbot: Sorry, I couldn't find anything on that topic.")
        except Exception as e:
            print(f"Chatbot: An error occurred: {e}")

# Run the chatbot
google_chatbot()
