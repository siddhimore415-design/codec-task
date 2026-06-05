import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from datetime import datetime

# Download tokenizer
nltk.download('punkt')
nltk.download('punkt_tab')

# Initialize stemmer
stemmer = PorterStemmer()

# ------------------------------
# Customer Service Chatbot
# ------------------------------

print("=" * 50)
print("🤖 Welcome to Smart Customer Service Chatbot")
print("Type 'bye' to exit")
print("=" * 50)

# FAQ database
responses = {
    "hello": "Hello 👋 Welcome to our customer support service!",
    "hi": "Hi 😊 How can I help you today?",
    "order": "📦 You can track your order using your Order ID on our website.",
    "refund": "💰 Refunds are processed within 5-7 business days.",
    "cancel": "❌ To cancel an order, visit 'My Orders' section.",
    "payment": "💳 We support UPI, Credit Card, Debit Card, and Net Banking.",
    "delivery": "🚚 Delivery usually takes 3-5 working days.",
    "contact": "📞 Contact us at support@company.com",
    "support": "🛠️ Our support team is available 24/7.",
    "hours": "🕒 Our business hours are 9 AM to 6 PM.",
    "thanks": "😊 You're welcome! Happy to help.",
}

# Chat history
chat_history = []

# Function to process user input
def chatbot_response(user_input):

    # Convert to lowercase
    user_input = user_input.lower()

    # Tokenize words
    words = word_tokenize(user_input)

    # Stem words
    stemmed_words = [stemmer.stem(word) for word in words]

    # Search for matching keywords
    for keyword in responses:
        if stemmer.stem(keyword) in stemmed_words:
            return responses[keyword]

    # Default response
    return "🤔 Sorry, I didn't understand that. Please try another question."

# Main chatbot loop
while True:

    user = input("\nYou: ")

    # Exit condition
    if user.lower() == "bye":
        print("Bot: 👋 Thank you for visiting. Have a great day!")
        break

    # Get bot response
    response = chatbot_response(user)

    # Save chat history
    current_time = datetime.now().strftime("%H:%M:%S")

    chat_history.append({
        "time": current_time,
        "user": user,
        "bot": response
    })

    # Print response
    print("Bot:", response)

# ------------------------------
# Save Chat History
# ------------------------------

with open("chat_history.txt", "w", encoding="utf-8") as file:

    file.write("Customer Service Chatbot History\n")
    file.write("=" * 50 + "\n\n")

    for chat in chat_history:
        file.write(f"[{chat['time']}]\n")
        file.write(f"You : {chat['user']}\n")
        file.write(f"Bot : {chat['bot']}\n")
        file.write("-" * 40 + "\n")

print("\n✅ Chat history saved to 'chat_history.txt'")
