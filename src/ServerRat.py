import socket
import argparse


class ServerRat:

    def __init__(self, listen_host, listen_port):
        self.listen_host = listen_host
        self.listen_port = int(listen_port)

    def create_server_socket(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.listen_host, self.listen_port))
            server_socket.listen(1)
            print("Waiting for a connection...")
            connection, address = server_socket.accept()
            print("Connection established!")
            with connection:
                print("Connection received from: ", address)
                while True:
                    # TODO - Need to figure out how to receive the command and then execute it
                    #   Also need to figure out how to receive the quit command and exit properly
                    data = connection.recv(1024)


def main(args):
    server_rat = ServerRat(args.listen_address, args.listen_port)
    server_rat.create_server_socket()


def _arg_parse():
    parser = argparse.ArgumentParser(description="ServerRat is the server side of the command-line based Python "
                                                 "Remote Access Tool")
    parser.add_argument("-l", "--listen-address", help="The listening address")
    parser.add_argument("-p", "--listen-port", help="The listening port")
    return parser.parse_args()


if __name__ == "__main__":
    args = _arg_parse()
    main(args)
