from flask import Flask, request
from datetime import datetime
import util
import conversationsfile
import whatsappservice

app = Flask(__name__)

@app.route('/welcome', methods = ['GET'])
def index():
    return "welcome developer"

@app.route('/whatsapp', methods=['GET'])
def VerifyToken():

    try:
        accessToken = "Your Access token"
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if token != None and challenge != None and token == accessToken:
            return challenge
        else:
            return "",400

    except:
        return "",400

@app.route('/whatsapp', methods=['POST'])
def ReceivedMessage():

    try:
        body = request.get_json()
        entry = (body["entry"])[0]
        changes = (entry["changes"])[0]
        value = changes["value"]
        message = (value["messages"])[0]
        number = message["from"]

        text = util.GetTextUser(message)
        GenerateMessage(text, number)
        print(text)
        return "EVENT_RECEIVED"
    
    except:
        return "EVENT_RECEIVED"

def GenerateMessage(text, number):
    
    if conversationsfile.CheckConversation(number):
        data = util.MainMenu(number)
    
    elif "text" in text:
        data = util.TextMessage("Text", number)

### Menu y Respuestas de Metodo de Pago ###
    elif "Payment methods 💳" in text:
        data = util.PaymentMethods(number)

    elif "Paypal 🤳" in text:
        data = util.SendPaypal(number)

    elif "Bank transfer 🏦" in text:
        data = util.Banktransfer(number)
    
    elif "Zelle 💰" in text:
        data = util.Zelle(number)

### Ubicaciones ###

    elif "Location 📍" in text:
        data = util.LocationMenu(number)
    elif "New York 📍" in text:
        data = util.NewYorkLocation(number)
    elif "Chicago 📍" in text:
        data = util.ChicagoLocation(number)

### Otras consultas ###

    elif "Other inquiries 🤔" in text:
        data = util.OtherInquiries(number)
    whatsappservice.SendMessageWhatsapp(data)

if(__name__ == "__main__"):
    app.run()