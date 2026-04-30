from utils import predict_message

tests = [
    # 🔴 SPAM
    "Congratulations! You won a $1000 gift card. Claim now!",
    "URGENT! Your account is compromised. Verify immediately.",
    "Win cash prizes now!!! Text WIN to 12345.",
    "You have been selected for a FREE vacation to Bahamas!",
    "Claim your free iPhone now. Limited time offer.",
    "Get cheap loans instantly. Apply now!",
    "Exclusive deal just for you. Click here to claim reward.",
    "Earn money from home without any investment!",
    "Act now! Limited time discount on all products.",
    "You are a lucky winner! Call now to claim your prize.",

    # 🟢 HAM
    "Hey bro, are we still meeting today?",
    "Don't forget to bring the assignment tomorrow.",
    "I will call you later in the evening.",
    "Can you send me the notes from class?",
    "Let's go for lunch after lecture.",
    "Did you complete the lab assignment?",
    "I am running a bit late, will reach in 10 minutes.",
    "Please check your email for the document.",
    "Are you coming to the gym today?",
    "Let me know when you reach home safely."
]

for msg in tests:
    print(msg)
    print("Prediction:", predict_message(msg))
    print("-" * 50)