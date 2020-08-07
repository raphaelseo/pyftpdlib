from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# TODO fix
basedir = "/Users/sangwonseo/dev_projects/ftp_directory"

authorizer = DummyAuthorizer()
# TODO add sets
for client_id, client_secret in [
    ("34b9476441fe499ea653", "32c2ab2debcceed03589a7d66f482ca638e1bbb8")
]:
    authorizer.add_user(client_id, client_secret, basedir, perm="elr")
handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 21), handler)
server.serve_forever()
