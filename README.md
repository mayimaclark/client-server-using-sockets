# client-server-using-sockets

This is a quick Python project that allows you to make polynomial computations from client to server by using the included polynomial functionn module, polynomials.py.

The server listens on port 12321 and carries out polynomial computations using the functions in the provided module. Requests are in the following format:
 
  Evaluate Request
    Request starts with ‘E’
    Followed by an argument value
    Followed by a single space
    Followed by he coefficients of a polynomial, separated by single spaces
  
  Bisection Request
    Requests starts with ‘S’
    Followed by ‘a’, ‘b’, polynomial, tolerance separated by single spaces
    
A sample evaluate request: E1.0 -945 1689 -950 230 -25 1
A sample bisection request: S0 2 -945 1689 -950 230 -25 1 1e-15

The server creates a response to the client for each request. The first character of the response will indicate various responses so X for error, E for successful evaluate, and S for successful bisection.

The server operates in a continuing manner where it repeatedly accepts a connection, gets a request, sends a response, and closes the connection to the client. Only one request is handled per connection.

As for the client, it defines important variables at the beginning. The client first makes a request to the server for a bisection. The data defined is provided in the variables and the value is displayed. After the first request, the result is used in another request to the server to evaluate the polynomial and that result is then displayed as well.
