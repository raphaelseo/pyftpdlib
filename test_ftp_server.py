# difference between sftp and ftp
# https://pyftpdlib.readthedocs.io/en/latest/install.html
# https://github.com/giampaolo/pyftpdlib

# Login
# Dataset List
# Date List of dataset
# Download

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("34b9476441fe499ea653", "32c2ab2debcceed03589a7d66f482ca638e1bbb8", "/Users/sangwonseo/dev_projects/ftp_directory", perm="elr")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 21), handler)
server.serve_forever()



# from thinknum import History
# h = History(
#     client_id='34b9476441fe499ea653',
#     client_secret='32c2ab2debcceed03589a7d66f482ca638e1bbb8',
# )
# h.get_presigned_url(dataset_id='store', history_date='2020-08-01')
# h.get_dataset_list()
# h.get_history_list(dataset_id='store')
# h.get_history_metadata(
#     dataset_id='store',
#     history_date='2020-03-09'
# )
# h.download(
#     dataset_id='store',
#     history_date='2020-03-09'
# )

# import requests
# response = requests.get(
#     'https://data.thinknum.com/datasets/linkedin_company/history/2020-02-01',
#     headers={
#         "Authorization": "token 7fa9f98ca042bd40d743cda8309641b3",
#         "X-API-Version": "20151130",
#         "Accept": "text/csv"
#     }, 
#     allow_redirects=False
# )
# for resp in response.history:
#     print(resp.status_code, resp.url)

# import re
# root = '/Users/sangwonseo/dev_projects/ftp_directory'
# path = '/Users/sangwonseo/dev_projects/ftp_directory/linkedin_company'
# z = re.match(
#     '^{root}/[a-z_]+$'.format(root=root),
#     path
# )
# bool(z)