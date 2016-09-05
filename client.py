import socket

sck = socket.socket()
sck.connect(("localhost", 12321))

x = 1.0

poly = [-945, 1689, -950, 230, -25, 1]
poly_str = [str(i) for i in poly]

a = 0
b = 2
tol = 1e-15

# message = "" # empty request to test if server can receive it

#message = "E" + str(x) + " " + ' '.join(poly_str)
message = "S" + str(a) + " " + str(b) + " " + ' '.join(poly_str) + " " + str(tol)

encoded_message = message.encode()
sck.sendall(encoded_message)
sck.shutdown(1)

response = ""
encoded_message = sck.recv(2048)

while len(encoded_message) > 0:
    response += encoded_message.decode()
    encoded_message = sck.recv(2048)

print("received: " + response)
sck.close()
