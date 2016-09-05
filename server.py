import polynomials
import comibinatorial
import logging
import socket

logging.basicConfig(filename='math_server.log', level=logging.INFO)

listener = socket.socket()
listener.bind(("", 12321))

listener.listen()

while 1:
    conn = listener.accept()
    sock = conn[0]

    request = ""
    encoded_message = sock.recv(2048)

    while len(encoded_message) > 0:
        request += encoded_message.decode()
        encoded_message = sock.recv(2048)

    logging.info(" request received |" + request + "|")

    if len(request) == 0:
        message = "XEmpty request"
        logging.error("response " + message)
        sock.sendall(message.encode())
        sock.shutdown(1)

    else:
        request_code = request[0]
        if request_code == "E":
            parameters = request[1:].split(' ')

            if len(parameters) < 1:
                message = "XInvalid request syntax: wrong number of fields in request: " + request[1:]
                logging.error("response " + message)
                sock.sendall(message.encode())
                sock.shutdown(1)

            else:
                x = float(parameters[0])

                # poly = float(parameters[1])
                poly = [float(i) for i in parameters[1:len(parameters)]]

                value = polynomials.evaluate(x, poly)
                message = "E" + str(value)
                logging.info("response " + message)
                sock.sendall(message.encode())
                sock.shutdown(1)

        elif request_code == "S":
            try:
                parameters = request[1:].split(' ')
                a = float(parameters[0])
                b = float(parameters[1])

                # poly = float(parameters[2])
                poly = [float(i) for i in parameters[2:len(parameters)-1]]

                tol = parameters[len(parameters)-1]

                value = polynomials.bisection(a, b, poly, tol)
                message = "S" + str(value)
                logging.info("response " + message)
                sock.sendall(message.encode())
                sock.shutdown(1)

            except Exception as ex:
                logging.error("Input value conversion error " + request[1:])
                logging.error(str(ex))

                message = "XInvalid numeric input: " + request[1:]
                logging.error("response " + message)
                sock.sendall(message.encode())
                sock.shutdown(1)

        else:
            message = "XInvalid request code: " + request_code
            logging.error("response " + message)
            sock.sendall(message.encode())
            sock.shutdown(1)

    sock.close()
