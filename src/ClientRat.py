import argparse
import socket


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
                # TODO - need to figure out how to send the command
                client_socket.send()

    def read_command(self):
        user_command = input("simplePyRat# ")

        if user_command == "quit":
            self.quit_flag = True
            print("Exiting!")

        return user_command


def main(args):
    client_rat = ClientRat(args.target, args.port)
    client_rat.create_socket()


def _arg_parse():
    parser = argparse.ArgumentParser(description="ClientRat is the client side of the command-line based "
                                                 "Python Remote Access Tool")
    parser.add_argument("-t", "--target", help="The target address")
    parser.add_argument("-p", "--port", help="The target port")
    return parser.parse_args()


if __name__ == "__main__":
    args = _arg_parse()
    main(args)
