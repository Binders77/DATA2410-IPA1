from socket import *
import botsTest

"""
Gets socket message from host/client decodes it and prints it out

"""
def getSocketMsg(_socket, BUFSIZE):
    get_msg = _socket.recv(BUFSIZE)     # Receives msg from host/client
    msg = get_msg.decode('utf-8')       # Decodes msg
    return msg

"""
Sends message to a connected sockets
"""
def sendSocketMsg(_socket, msg):
    if not msg:
        print("No alt action")
    else:
        send_msg = msg.encode('utf-8')      # Encodes msg
        _socket.send(send_msg)              # Sends msg from host/client
        print("\nHjelpemetode sendSocketMsg success")



def yes_no(Yes_or_no):
    if Yes_or_no == "Yes":
        return True
    return False


"""
- Takes in a name of a bot as a string an calls that bots,
- with 2 actions
- Validate that the input string for the name has a bot method with the same name
"""

def callBot(botName, ac1, ac2):
    bot_to_call = getattr(botsTest, botName)
    _response = bot_to_call(ac1, ac2)
    print(_response)
    return _response



