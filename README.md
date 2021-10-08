# SimplePyRat
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/brease568/SimplePyRat)

SimpleRat is a command-line based client / server paired Java Remote Access Tool (RAT). SimpleRat can be used to enable remote command execution and supports SSL encryption.

# Prerequisites

- Python 3
- Ability to run programs from the command line

# Dependencies

See the provided requirements.txt file.

# Modules Used

- socket
- subprocess
- ssl
- argparse

# Usage - without SSL Encryption

## To execute the server and client without SSL encryption:
- Execute the server and specify a port to listen on.
- Execute the client and specify a target IP address and a port to connect to.

ServerRat:
```bash
python3 ServerRat.py -l {listening_ip} -p {listening_port}
Waiting for a connection...
```

ClientRat:
```bash
python3 ClientRat.py -t {target_ip} -p {target_port}
simplePyRat#
```

# Usage - with SSL Encryption

To execute the server and client with SSL encryption you must do two things:

- First, you need a certificate. To generate a self-signed certificate run the following command:

```bash
openssl req -new -x509 -days 30 -nodes -out cert.pem -keyout cert.pem
```

- Second, execute the server and client with the '-s' switch option.

ServerRat:
```bash
python3 ServerRat.py -l {listening_ip} -p {listening_port} -s
Waiting for a secure connection...
```

ClientRat:
```bash
python3 ClientRat.py -t {target_ip} -p {target_port} -s
simplePyRat#
```

# Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Currently, there are no contributors.

# License

[MIT](https://choosealicense.com/licenses/mit/)
