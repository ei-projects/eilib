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
        self.check_resfile_content(resfile, {})

        # Test resfile consistency
        test_files = {'foo': b'1234567', 'bar': b'hello world', 'rab': b'aaaabbbbaaaabbbb'}
        with ResFile(resfile, 'w') as res:
            for name, data in test_files.items():
                with res.open(name, 'w') as file:
                    file.write(data)
        self.check_resfile_content(resfile, test_files)

        # Test append mode
        test_files_upd = {
            'foo': b'fooooo-old',  # Update old file
            'foo-new': b'foooooo-new',  # New file
        }
        with ResFile(resfile, 'a') as res:
            for name, data in test_files_upd.items():
                with res.open(name, 'w') as file:
                    file.write(data)
        self.check_resfile_content(resfile, {**test_files, **test_files_upd})

    def test_inner_resfile(self):
        resfile_out = io.BytesIO()

        # Create archive.
        with (
            ResFile(resfile_out, "w") as res_out,
            res_out.open("inner.res", "w") as resfile_in,
            ResFile(resfile_in, "w") as res_in,
            res_in.open("file.txt", "w") as file,
        ):
            file.write(b"hello world")

        # Check content.
        with (
            ResFile(resfile_out, "r") as res_out,
            res_out.open("inner.res", "r") as resfile_in,
            ResFile(resfile_in, "r") as res_in,
            res_in.open("file.txt", "r") as file,
        ):
            self.assertEqual(file.read(), b"hello world")

    def check_resfile_content(self, resfile, test_files):
        resfile.seek(0)
        with ResFile(resfile) as res:
            for name, data in test_files.items():
                with res.open(name) as file:
                    self.assertEqual(file.read(), data)
            for info in res.iter_files():
                self.assertIn(info.name, test_files)
        resfile.seek(0)


if __name__ == '__main__':
    unittest.main(module='test_resfile')
