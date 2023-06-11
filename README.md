# netcat
A simple program that can be useful for sending HTTP requests and creating a server

# Usage:

# Creating the server:

netcat.py -t 127.0.0.1 -p 8080 -l yes

if you want to use program in listening mode (create the server), type something to -l


# Sending http request:

netcat.py -t www.google.com -p 80 -d "GET / HTTP/1.1\r\n"

if you send data, please enter the data into ""
