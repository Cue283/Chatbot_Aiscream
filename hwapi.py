from socket import *
import requests
import random

# NASA APOD API
NASA_API_URL = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

SPACE_FACTS = [
    "Neutron stars can spin at a rate of 600 rotations per second.",
    "A day on Venus is longer than a year on Venus.",
    "There are more trees on Earth than stars in the Milky Way.",
    "Saturn could float in water because it is mostly gas.",
    "The largest volcano in the solar system is on Mars (Olympus Mons)."
]

def get_nasa_apod():
    try:
        res = requests.get(NASA_API_URL, timeout=5)
        data = res.json()
        title = data.get("title", "No title")
        date = data.get("date", "No date")
        explanation = data.get("explanation", "No explanation")
        url = data.get("url", "No URL")
        return f" NASA Astronomy Picture of the Day \r\nTitle: {title}\r\nDate: {date}\r\nURL: {url}\r\nExplanation: {explanation}\r\n"
    except Exception as e:
        return f"Failed to get NASA APOD: {e}\r\n"

def get_space_fact():
    return f"Space Fact\r\n{random.choice(SPACE_FACTS)}\r\n"

# เซิร์ฟเวอร์
serversocket = socket(AF_INET, SOCK_STREAM)
serversocket.bind(("", 9000))
serversocket.listen(5)

while True:
    clientsocket, addr = serversocket.accept()
    print("Connected from %s" % str(addr))

    main_msg = (
        "Welcome to Space Chatbot\r\n"
        "1. Space Info\r\n"
        "2. About this chatbot\r\n"
        "3. End Chat\r\n"
    )

    while True:
        clientsocket.send(main_msg.encode())
        data = clientsocket.recv(2000)
        choice = data.decode('ascii').strip()

        if choice == "1":
            
            while True:
                sub_msg = (
                    "Space Info \r\n"
                    "1. Show NASA Astronomy Picture of the Day\r\n"
                    "2. Show a random space fact\r\n"
                    "3. Back to main menu\r\n"
                )
                clientsocket.send(sub_msg.encode())
                data2 = clientsocket.recv(2000)
                choice2 = data2.decode('ascii').strip()

                if choice2 == "1":
                    reply = get_nasa_apod()
                elif choice2 == "2":
                    reply = get_space_fact()
                elif choice2 == "3":
                    reply = "Back to main menu.\r\n"
                    clientsocket.send(reply.encode())
                    break  
                else:
                    reply = "Invalid choice, try again.\r\n"

                clientsocket.send(reply.encode())

        elif choice == "2":
            reply = (
                "This is a Space Chatbot demo.\r\n"
                "It can show NASA APOD and random space facts.\r\n"
                "Created by Teeramate.\r\n"
            )
            clientsocket.send(reply.encode())

        elif choice == "3":
            reply = "Thank you for chatting! Goodbye!\r\n"
            clientsocket.send(reply.encode())
            break

        else:
            reply = "Invalid choice, please try again.\r\n"

    clientsocket.close()
    print(f"Closed connection from {addr}")
