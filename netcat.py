# Made by NairLxrd (AKA pos 1 or feed, clqwnless)
# Name of the utility: NetCat
# Description: A simple program, that can be useful for creating a socket and sending http requests


import argparse
from pystyle import Write, Colors, Colorate, System
import socket
import threading
import sys
from banner import banner
from additional import additional_info


class Parser:
    def __init__(self, epilog):
        self.epilog = epilog
        self.parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter, epilog=self.epilog
        )

        self.parser.add_argument(
            "-target", "-t", help="Target host", required=True
        )
        self.parser.add_argument(
            "-port", "-p", help="Target port", type=int, required=True
        )
        self.parser.add_argument(
            "-data", "-d", help="Data to send"
        )
        self.parser.add_argument(
            "-listen", "-l", help="If you want to use the program in listener mode"
        )
        self.parser.add_argument(
            "-bytes", "-b", help="Bytes to receive", type=int, default=512
        )
        self.args = self.parser.parse_args()

    def parse_args(self):
        if self.args.listen:
            obj_listen = Listen(self.args)
            obj_listen.start_server()
        else:
            obj_attacker = Attacker(self.args)
            obj_attacker.connect()


class Listen:
    def __init__(self, args):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.host = args.target
        self.port = args.port
        self.bytes_to_recv = args.bytes

    def start_server(self):
        Write.Print(
            "\n\n[*] Trying to create the server",
            Colors.red_to_yellow, interval=0.01
        )
        try:
            self.server.bind((self.host, self.port))
            self.server.listen(5)
        except Exception as e:
            Write.Print(
                f"\n\n[*] An error occurred while creating the server: {e}",
                Colors.red_to_yellow, interval=0.01
            )
            sys.exit(1)
        else:
            Write.Print(
                "\n\n[*] Successfully created the server "
                f"on host: {self.host} and on port: "
                f"{self.port}", Colors.red_to_yellow, interval=0.01
            )
            self.accept()

    def accept(self):
        Write.Print(
            "\n\n[*] Waiting for client connection\n",
            Colors.red_to_yellow, interval=0.01
        )

        while True:
            try:
                client, address = self.server.accept()
            except Exception as e:
                Write.Print(
                    "\n\n[*] An error occurred while client connects: "
                    f"{e}", Colors.red_to_yellow, interval=0.01
                )
                self.server.close()
                sys.exit(1)
            else:
                Write.Print(
                    "\n\n[*] Client with host: "
                    f"{address[0]} and port: "
                    f"{address[1]} connected...", Colors.red_to_yellow, interval=0.01
                )
                Write.Print(
                    "\n\n[*] Trying to receive data from the client",
                    Colors.red_to_yellow, interval=0.01
                )
                t = threading.Thread(target=self.handle_client, args=(client,))
                t.start()

    def handle_client(self, client):
        while True:
            try:
                data = client.recv(self.bytes_to_recv)
                data = data.decode("utf-8")
                if data:
                    Write.Print(
                        "\n\n[*] Data received: "
                        f"\n{data}",
                        Colors.red_to_yellow, interval=0.01
                    )
            except Exception as e:
                Write.Print(
                    "\n\n[*] An error occurred while "
                    f"receiving data: {e}",
                    Colors.red_to_yellow, interval=0.01
                )
                return


class Attacker:
    def __init__(self, args):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = args.target
        self.port = args.port
        if args.data:
            self.data = args.data
            self.data = self.data.encode()
            self.data = self.data.decode("unicode-escape")
            self.data = self.data.encode("utf-8")
        self.bytes_to_recv = args.bytes

    def connect(self):
        try:
            self.client.connect((self.host, self.port))
        except Exception as e:
            Write.Print(
                "\n\n[*] An error occurred "
                "while connecting to the server: "
                f"{e}",
                Colors.red_to_yellow, interval=0.01
            )
            self.client.close()
            sys.exit(1)
        else:
            Write.Print(
                "\n\n[*] Successfully connected to "
                "the server",
                Colors.red_to_yellow, interval=0.01
            )

        if self.data:
            Write.Print(
                "\n\n[*] Trying to send the data...",
                Colors.red_to_yellow, interval=0.01
            )
            self.send()
        else:
            Write.Print(
                "\n\n[*] You does\'\t typed any data, "
                "so the script will try to receive "
                "response from the server...",
                Colors.red_to_yellow, interval=0.01
            )
            self.receive()

    def send(self):
        try:
            self.client.send(self.data)
        except Exception as e:
            Write.Print(
                "\n\n[*] An error occurred while "
                f"sending data: {e}",
                Colors.red_to_yellow, interval=0.01
            )
            self.client.close()
            sys.exit(1)
        else:
            Write.Print(
                "\n\n[*] Data successfully sent..."
                "\n\n[*] Now trying to get response "
                "from the server",
                Colors.red_to_yellow, interval=0.01
            )
            self.receive()

    def receive(self):
        try:
            data = self.client.recv(self.bytes_to_recv)
            data = data.decode("utf-8")
        except Exception as e:
            Write.Print(
                "\n\n[*] An error occurred while "
                f"receiving data: {e}",
                Colors.red_to_yellow, interval=0.01
            )
        else:
            Write.Print(
                f"\n\n[*] Data received: \n{data}",
                Colors.red_to_yellow, interval=0.01
            )
            Write.Print(
                "\n\n[*] Thank you for using the program..."
                "\n\n[*] Bye, gl!",
                Colors.red_to_yellow, interval=0.01
            )
            self.client.close()
            sys.exit(0)


if __name__ == "__main__":
    System.Title("Made by clqwnless (NairLxrd, pos 1 or feed, clqwnless)")
    print(Colorate.Horizontal(Colors.red_to_yellow, banner))
    Write.Print(
        "\n\n[*] Made by NairLxrd.",
        Colors.red_to_yellow, interval=0.01
    )
    Write.Print(
        "\n\n[*] If you want to close program, "
        "press ctrl + c or ctrl + break\n",
        Colors.red_to_yellow, interval=0.01
    )
    obj_parser = Parser(additional_info)
    obj_parser.parse_args()
