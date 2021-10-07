import argparse
import socket
import ssl


class ClientRat:

    def __init__(self, target_host, target_port):
        self.target_host = target_host
        self.target_port = int(target_port)
        self.quit_flag = False

    def create_socket(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.target_host, self.target_port))

            while not self.quit_flag:
                command = self.read_command()
                self.send_command(client_socket, command)
                self.recv_command_output(client_socket)

    def create_encrypted_socket(self):
        context = ssl.create_default_context()
        context.check_hostname = False
        context.load_verify_locations('cert.pem')

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            with context.wrap_socket(client_socket) as secure_client_socket:
                secure_client_socket.connect((self.target_host, self.target_port))

                while not self.quit_flag:
                    command = self.read_command()
                    self.send_command(secure_client_socket, command)
                    self.recv_command_output(secure_client_socket)

    def read_command(self):
        user_command = input("simplePyRat# ")

        if user_command == "quit":
            self.quit_flag = True
            print("Exiting!")

        return user_command

    def send_command(self, client_socket, command):
        client_socket.send(command.encode())

    def recv_command_output(self, client_socket):
        print(client_socket.recv(1024).decode())


def main(args):
    client_rat = ClientRat(args.target, args.port)

    if args.ssl_encrypt is False:
        client_rat.create_socket()
    else:
        client_rat.create_encrypted_socket()


def _arg_parse():
    parser = argparse.ArgumentParser(description="ClientRat is the client side of the command-line based "
                                                 "Python Remote Access Tool")
    parser.add_argument("-t", "--target", help="The target address")
    parser.add_argument("-p", "--port", help="The target port")
    parser.add_argument("-s", "--ssl-encrypt", action="store_true", help="Use ssl encryption")
    return parser.parse_args()


if __name__ == "__main__":
    args = _arg_parse()
    main(args)
