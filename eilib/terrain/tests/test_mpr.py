import os
import unittest

from eilib.res.resfile import ResFile
from eilib.terrain import mpr

TESTDATA_DIR = os.path.dirname(__file__)


class TestMpr(unittest.TestCase):

    def test_mp(self):

        mp = mpr.MpFile()
        with ResFile(os.path.join(TESTDATA_DIR, 'data', 'zonemainmenunew.mpr')) as res:
            mp_name = ''
            for info in res.iter_files():
                if info.name.lower().endswith('.mp'):
                    with res.open(info.name) as file:
                        mp.read(file)
                        mp_name = info.name
                        break
            else:
                self.fail(".mpr file doesn't have .mp file")

            sec_format = f'{os.path.splitext(mp_name)[0]}{{:03d}}{{:03d}}.sec'
            for x in range(mp.sectors_x_count):
                for y in range(mp.sectors_y_count):
                    sec_name = sec_format.format(x, y)
                    with res.open(sec_format.format(x, y)) as file:
                        sec = mpr.SecFile()
                        sec.read(file)
                    sec.write(open(sec_name, 'wb'))

        mp.write(open('test.mp', 'wb'))


if __name__ == '__main__':
    unittest.main(module='test_mpr')
