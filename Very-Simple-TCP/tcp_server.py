import socket as sck


# A socket is an object which represents an endpoint of a communications channel
__SOCKET__ = sck.socket(sck.AF_INET,sck.SOCK_STREAM)

# SOCK_STREAM - Type of transport protocol used for communication  [TCP] 
# AF_INET - IPv4 Address Family 

_HOST = "127.0.0.1" # Loopback Interface; localhost  
PORT = 8000

__SOCKET__.bind((_HOST, PORT))
__SOCKET__.listen(10)

while True:
    # Program opens port on localhost and waits for client to connect 
    d, a = __SOCKET__.accept()
    d.send(b"TY!")
    
    print('C:\>   ', a)
    d.close()

