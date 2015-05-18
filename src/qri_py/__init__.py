import socket
import binascii

import msgpack


class QriPython:

    def __init__(self, host=None, port=None):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.sock.connect((host, port))
        except socket.error, msg:
            print "Server {0}:{1} unreachable: {2}".format(host, port, msg)

    def send(self, peer="123", message="ololo"):
        checksum = binascii.crc32(peer)
        packed_data = msgpack.packb([peer, checksum, message])

        try:
            self.sock.send(packed_data)
        except socket.error, msg:
            print "Error occurred during sending: {0}".format(msg)

    def close(self):
        self.sock.close()

qri = QriPython(host="127.0.0.1", port=5679)
qri.send(peer="123", message=b"101Hello Qri")
qri.close()

