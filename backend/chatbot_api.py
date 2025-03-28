from fastapi import FastAPI

app = FastAPI()

slang_dict = {
    "bet": "Bet means 'okay' or 'deal'. It's used to confirm something.",
    "sus": "Sus is short for 'suspicious', often used when something seems shady.",
    "cap": "Cap means a lie. Saying 'no cap' means you're telling the truth.",
    "bruh": "Bruh is a casual way of saying 'bro' or 'dude'.",
    "goat": "GOAT stands for 'Greatest Of All Time', used for top athletes and legends.",
    "lit": "Lit means something is exciting, fun, or amazing!"
}

@app.get("/chat/{user_input}")
def chat_response(user_input: str):
    response = slang_dict.get(user_input.lower(), "Sorry, I don't know that slang yet!")
    return {"response": response}
