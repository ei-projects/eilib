import io
import os
import unittest

from eilib.res.resfile import ResFile

TESTDATA_DIR = os.path.dirname(__file__)


class TestResFile(unittest.TestCase):

    def test_resfile_is_readble(self):
        with ResFile(os.path.join(TESTDATA_DIR, 'data', 'z3q1.mq')) as res:
            for info in res.iter_files():
                with res.open(info.name) as file:
                    self.assertEqual(len(file.read()), info.file_size)

    def test_resfile_writing(self):
        # Test empty resfile
        resfile = io.BytesIO()
        with ResFile(resfile, 'w'):
            pass
        self.assertEqual(resfile.getvalue(), b'<\xe2\x9c\x01' + b'\0' * 12)

        # Test resfile consistency
        test_files = {'foo': b'1234567', 'bar': b'hello world', 'rab': b'aaaabbbbaaaabbbb'}
        resfile.seek(0)
        with ResFile(resfile, 'w') as res:
            for name, data in test_files.items():
                with res.open(name, 'w') as file:
                    file.write(data)
        self.check_resfile_content(resfile, test_files)

        # Test append mode
        test_files_upd = {
            'foo': b'fooooo-old', # Update old file
            'foo-new': b'foooooo-new',  # New file
        }
        resfile.seek(0)
        with ResFile(resfile, 'a') as res:
            for name, data in test_files_upd.items():
                with res.open(name, 'w') as file:
                    file.write(data)
        self.check_resfile_content(resfile, {**test_files, **test_files_upd})

    def check_resfile_content(self, resfile, test_files):
        resfile.seek(0)
        with ResFile(resfile) as res:
            for name, data in test_files.items():
                with res.open(name) as file:
                    self.assertEqual(file.read(), data)


if __name__ == '__main__':
    unittest.main(module='test_resfile')
