def GetTextUser(message):
    text = ""
    typeMessage = message["type"]

    if typeMessage == "text":
        text = (message["text"])["body"]
    elif typeMessage == "interactive":
        interactiveObject = message["interactive"]
        typeInteractive = interactiveObject["type"]

        if typeInteractive == "button_reply":
            text = (interactiveObject["button_reply"])["title"]
        elif typeInteractive == "list_reply":
            text = (interactiveObject["list_reply"])["title"]
        else:
            print("sin mensaje")

    else:
        print ("sin mensaje")

    return text
"""
def TextMessage(text,number):
    data = {
            "messaging_product": "whatsapp",    
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "Texto informacion"
            }
        }
    return data
"""
def LocationMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "location",
            "location": {
                "latitude": "40.714399716007975",
                "longitude": "-74.00537119261615",
                "name": "Auto Repuestos Gonper c.a.",
                "address": "Catia La Mar 1162, La Guaira"
            }
        }
    return data

def MainMenu(number):
    data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                    "text": "Hello! I'm Alicia, the SparePartsSafe Bot.\n*How can I help you today?*😁\n\n*Tap the option you like the most*"
                },
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {
                                "id": "<UNIQUE_BUTTON_ID_1>",
                                "title": "Payment methods 💳"
                            }
                        },
                        {
                            "type": "reply",
                            "reply": {
                                "id": "<UNIQUE_BUTTON_ID_2>",
                                "title": "Location 📍"
                            }
                        },
                                                {
                            "type": "reply",
                            "reply": {
                                "id": "<UNIQUE_BUTTON_ID_3>",
                                "title": "Other inquiries 🤔"
                            }
                        }
                    ]
                }
            }
        }
    return data

####### Menu de metodos de pago y respuestas de Metodos de pago ######

def PaymentMethods(number):
    data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                    "text": "We offer various payment methods \n*Choose the one you prefer 👇*"
                },
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {
                                "id": "<UNIQUE_BUTTON_ID_1>",
                                "title": "Paypal 🤳"
                            }
                        },
                        {
                            "type": "reply",
                            "reply": {
                                "id": "<UNIQUE_BUTTON_ID_2>",
                                "title": "Bank transfer 🏦"
                            }
                        },
                                                {
                            "type": "reply",
                            "reply": {
                                "id": "<UNIQUE_BUTTON_ID_3>",
                                "title": "Zelle 💰"
                            }
                        }
                    ]
                }
            }
        }
    return data

def SendPaypal(number):
    data = {
            "messaging_product": "whatsapp",    
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "*Paypal Email 🤳* \nrafaelantoniomarinr@gmail.com"
            }
        }
    return data

def Banktransfer(number):
    data = {
            "messaging_product": "whatsapp",    
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "*Bank Data 🏦*\nAccount number \n013************10 \nRafael Marin\nCédula: 25***128"
            }
        }
    return data

def Zelle(number):
    data = {
            "messaging_product": "whatsapp",    
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "*Zelle 💰*\nBank: Wells Bank\nRafael Marin\nrafaelantoniomarinr@gmail.com"
            }
        }
    return data

####### Menu de Ubicacion y respuestas de ubicacion ######

def LocationMenu(number):
    data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                    "text": "We have different branches where you can make a purchase or pick up your package.\n*Select the one closest to you👇*"
                },
                "action": {
                    "buttons": [
                        {
                            "type": "reply",
                            "reply": {
                                "id": "<UNIQUE_BUTTON_ID_1>",
                                "title": "New York 📍"
                            }
                        },
                        {
                            "type": "reply",
                            "reply": {
                                "id": "<UNIQUE_BUTTON_ID_2>",
                                "title": "Chicago 📍"
                            }
                        }
                    ]
                }
            }
        }
    return data

def NewYorkLocation(number):
    data = {
            "messaging_product": "whatsapp",    
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "🏪 You can find us in New York\n👉 https://maps.app.goo.gl/JVYcz2Mc3mxT5WAHA"
            }
        }
    return data

def ChicagoLocation(number):
    data = {
            "messaging_product": "whatsapp",    
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "🏪 You can find us in Chicago, Illinois\n👉 https://maps.app.goo.gl/fWkkithjRmNSwUt29"
            }
        }
    return data

#### Respuesta para Otras consultas

def OtherInquiries(number):
    data = {
            "messaging_product": "whatsapp",    
            "recipient_type": "individual",
            "to": number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": "I will transfer you to one of our sales advisors who can assist you with your inquiries in more detail\n\n*Thank you for reaching out, SPAREPARTSSAFE at your service 😁*"
            }
        }
    return data