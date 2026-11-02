#Apple ChatBot
print("Welcome to Apple's ChatBot!.\nThis can answer questions about Recently launched IPhones.")
#chatbot memeory building 
iphone_data = {
    "iphone_18_pro": {
        "name": "iPhone 18 Pro",
        "price_INR_from":"1,64,900",
        "storage": ["256GB", "512GB", "1TB", "2TB"],
        "colors": ["Black", "Silver", "Glacier", "Burgundy"],
        "screen": "6.3 inches",
        "chip": "A20 Pro",
        "camera": "48MP Pro Fusion camera system"
    },

    "iphone_18_pro_max": {
        "name": "iPhone 18 Pro Max",
        "price_INR_from":"1,79,900",
        "storage": ["256GB", "512GB", "1TB", "2TB"],
        "colors": ["Black", "Silver", "Glacier", "Burgundy"],
        "screen": "6.9 inches",
        "chip": "A20 Pro",
        "camera": "48MP Pro Fusion camera system"
    },

    "iphone_duo": {
        "name": "iPhone Duo",
        "price_INR_from":"2,99,900",
        "storage": ["256GB", "512GB", "1TB", "2TB"],
        "colors": ["Night Sky", "Star White"],
        "screen": "7.6-inch inside screen and 5.4-inch outside screen",
        "chip": "A20 Pro",
        "camera": "48MP Dual Fusion camera system",
        "type": "Foldable"
    } 
}
def getrespo(userQuestion):
    question = userQuestion.lower().replace("_", " ")

    for eachkey in sorted(iphone_data, key=len, reverse=True):
        phone = iphone_data[eachkey]
        name = phone["name"].lower()
        short_name = name.replace("iphone ", "")

        if name in question or short_name in question:
            if "storage" in question or "memory" in question:
                return ", ".join(phone["storage"])
            elif "color" in question or "colour" in question:
                return ", ".join(phone["colors"])
            elif "screen" in question or "display" in question:
                return phone["screen"]
            elif "chip" in question or "processor" in question:
                return phone["chip"]
            elif "camera" in question:
                return phone["camera"]
            elif "type" in question or "foldable" in question:
                return phone.get("type", "Standard iPhone")
            elif "price" in question or "cost" in question or "how much" in question:
                return f"₹{phone['price_INR_from']}"

            return f"What would you like to know about the {phone['name']}?"

    return "Sorry, I couldn't find that iPhone."
# taking input
while True: 
    userinput = input('How may I help you today.')

    if "bye" in userinput.lower():
        print('Apple_Assist: Goodbye')
        break

    reply = getrespo(userinput)
    print('Apple_Assist:',reply)
    
