additional_info = """
    Usage:
    # Connecting to the server and sending data
    netcat.py -t www.google.com -p 80 -d \"GET / HTTP/1.1\"
    # Creating the server on host 127.0.0.1 and port 8080
    netcat.py -t 127.0.0.1 -p 8080 -l #into -l type something (it does not matter)
"""
