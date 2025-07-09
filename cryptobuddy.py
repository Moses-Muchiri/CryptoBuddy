crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  
}

print("👋 Hey there! I’m CryptoBuddy, your friendly crypto sidekick! 🌟")
print("Ask me about crypto trends, sustainability, or investment advice!")
print("Type 'exit' to quit.\n")

while True:
    user_query = input("You: ").lower()

    if user_query == "exit":
        print("CryptoBuddy: 👋 Bye! Remember, crypto is risky!")
        break

    elif "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"CryptoBuddy: Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!")

    elif "trending" in user_query or "trend" in user_query:
        trending = [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]
        print(f"CryptoBuddy: These cryptos are trending up: {', '.join(trending)} 🚀")

    elif "long-term" in user_query or "growth" in user_query:
        options = []
        for name, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7:
                options.append(name)
        if options:
            print(f"CryptoBuddy: {', '.join(options)} is trending up and sustainable! 📈🌍")
        else:
            print("CryptoBuddy: Hmm, I don't see any crypto that fits both right now.")

    elif "profit" in user_query or "profitable" in user_query:
        profitable = []
        for name, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                profitable.append(name)
        if profitable:
            print(f"CryptoBuddy: For profitability, check out: {', '.join(profitable)} 💰")
        else:
            print("CryptoBuddy: I can't find a super profitable option at the moment!")

    else:
        print("CryptoBuddy: Sorry, I didn’t get that! Try asking about trending coins, sustainability, or profitability.")