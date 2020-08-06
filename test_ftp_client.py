from ftplib import FTP
ftp = FTP('127.0.0.1')
ftp.login('34b9476441fe499ea653', '32c2ab2debcceed03589a7d66f482ca638e1bbb8')

# TODO 1. direcoty list
rows = []
ftp.dir(rows.append)
for row in rows:
    print (row)

# TODO 2. change directory
rows = []
ftp.cwd('/linkedin_company')
ftp.dir(rows.append)
for row in rows:
    print (row)

# TODO 3. download files
filename = "2020-08-01.csv"
ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)

# TODO 4. try upload

# TODO 5. try remove

# TODO. Login




# from ftplib import FTP_TLS
# ftps = FTP_TLS('ftp.python.org')
# ftps.login()           # login anonymously before securing control channel
# ftps.prot_p()          # switch to secure data connection
# ftps.retrlines('LIST') # list directory content securely