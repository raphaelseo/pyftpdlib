import unittest
from ftplib import FTP, error_perm


class FtpTestCase(unittest.TestCase):

    def test_connect(self):
        ftp = FTP('127.0.0.1')
        ftp.quit()

    def test_login(self):
        ftp = FTP('127.0.0.1')
        ftp.login('34b9476441fe499ea653', '32c2ab2debcceed03589a7d66f482ca638e1bbb8')
        ftp.quit()

    def test_list(self):
        ftp = FTP('127.0.0.1')
        ftp.login('34b9476441fe499ea653', '32c2ab2debcceed03589a7d66f482ca638e1bbb8')
        result = ftp.retrlines('LIST')
        self.assertEqual(result, '226 Transfer complete.')
        ftp.quit()

    def test_change_directory(self):
        ftp = FTP('127.0.0.1')
        ftp.login('34b9476441fe499ea653', '32c2ab2debcceed03589a7d66f482ca638e1bbb8')
        result = ftp.cwd('/linkedin_company')
        self.assertEqual(result, '250 "/linkedin_company" is the current directory.')
        ftp.quit()

    def test_download(self):
        ftp = FTP('127.0.0.1')
        ftp.login('34b9476441fe499ea653', '32c2ab2debcceed03589a7d66f482ca638e1bbb8')
        ftp.cwd('/linkedin_company')
        filename = "2020-08-01.csv"
        with open(filename, 'wb') as fp:
            result = ftp.retrbinary("RETR " + filename , fp.write)
        self.assertEqual(result, '226 Transfer complete.')
        ftp.quit()

    def test_upload(self):
        with self.assertRaises(error_perm):
            ftp = FTP('127.0.0.1')
            ftp.login('34b9476441fe499ea653', '32c2ab2debcceed03589a7d66f482ca638e1bbb8')
            ftp.cwd('/linkedin_company')
            filename = './setup.py'
            with open(filename, 'r') as f:  
                ftp.storbinary('STOR %s' % filename, f)  
            ftp.quit()

    def test_make_direcotry(self):
        with self.assertRaises(error_perm):
            ftp = FTP('127.0.0.1')
            ftp.login('34b9476441fe499ea653', '32c2ab2debcceed03589a7d66f482ca638e1bbb8')
            ftp.rmd('new_linkedin_company')
        ftp.quit()

    def test_remove_direcotry(self):
        with self.assertRaises(error_perm):
            ftp = FTP('127.0.0.1')
            ftp.login('34b9476441fe499ea653', '32c2ab2debcceed03589a7d66f482ca638e1bbb8')
            ftp.rmd('linkedin_company')
        ftp.quit()

    def test_rename_file(self):
        with self.assertRaises(error_perm):
            ftp = FTP('127.0.0.1')
            ftp.login('34b9476441fe499ea653', '32c2ab2debcceed03589a7d66f482ca638e1bbb8')
            ftp.cwd('/linkedin_company')
            ftp.rename("2020-08-01.csv", "new_2020-08-01.csv")
        ftp.quit()

    def test_delete_file(self):
        with self.assertRaises(error_perm):
            ftp = FTP('127.0.0.1')
            ftp.login('34b9476441fe499ea653', '32c2ab2debcceed03589a7d66f482ca638e1bbb8')
            ftp.cwd('/linkedin_company')
            ftp.delete("2020-08-01.csv")
        ftp.quit()


if __name__ == '__main__':
    unittest.main()
