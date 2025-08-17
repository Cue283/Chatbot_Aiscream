from socket import *

serversocket = socket(AF_INET, SOCK_STREAM)
serversocket.bind(("", 9000))
serversocket.listen(5)

while True:
    clientsocket, addr = serversocket.accept()
    print("I am Mirai chatbot. %s" % str(addr))

    msg = (
        "1. Ruby-chan?\r\n"
        "2. Ayumu-chan?\r\n"
        "3. Shiki-chan?\r\n"
        "4. Minna?\r\n"
        "5. End Chat\r\n"
    )

    while True:
        clientsocket.send(msg.encode())
        data = clientsocket.recv(1000)
        choice = data.decode("ascii").strip()

        if choice == "1":
            submsg = "Hai! \r\n" "1. Nani ga suki?\r\n"
            clientsocket.send(submsg.encode())
            data2 = clientsocket.recv(1000)
            choice2 = data2.decode("ascii").strip()
            if choice2 == "1":
                reply = "Chokominto yori mo a-na-ta\r\n"
            else:
                reply = "Back to main menu.\r\n"

        elif choice == "2":
            submsg = "Hai! \r\n" "Nani ga suki?\r\n"
            clientsocket.send(submsg.encode())
            data2 = clientsocket.recv(1000)
            choice2 = data2.decode("ascii").strip()
            if choice2 == "1":
                reply = "Sutoroberii fureibaa yori mo a-na-ta\r\n"
            else:
                reply = "Back to main menu.\r\n"
        elif choice == "3":
            submsg = "Hai! \r\n" "Nani ga suki?\r\n"
            clientsocket.send(submsg.encode())
            data2 = clientsocket.recv(1000)
            choice2 = data2.decode("ascii").strip()
            if choice2 == "1":
                reply = "Kukkii and kuriimu yori mo a-na-ta\r\n"
            else:
                reply = "Back to main menu.\r\n"
        elif choice == "4":
            submsg = "Hai! \r\n" "Nani ga suki?\r\n"
            clientsocket.send(submsg.encode())
            data2 = clientsocket.recv(1000)
            choice2 = data2.decode("ascii").strip()
            if choice2 == "1":
                reply = "Mochiron daisuki aisukuriimu\r\n"
            else:
                reply = "Back to main menu.\r\n"
        elif choice == "5":
            reply = "Thank you for chatting with me!\r\n"
            clientsocket.send(reply.encode())
            break
        else:
            reply = "nani kore.\r\n"
            break

        clientsocket.send(reply.encode())

    clientsocket.close()
    print(f"Closed connection from {addr}")
