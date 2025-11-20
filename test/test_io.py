from os import path as op
import unittest

import pha_tools
from pha_tools.io import (
    gather_data_filenames, load_donation_data_from_filenames
)

test_data_dir = op.join(op.dirname(op.dirname(pha_tools.__file__)), 'data')


class TestIO(unittest.TestCase):
    def test_gather_data_filenames(self):
        glob_txt = r'transactions*.xlsx'

        filenames = gather_data_filenames(test_data_dir, glob_txt)
        self.assertEqual(len(filenames), 4)

    def test_load_donations(self):
        glob_txt = r'transactions*.xlsx'

        filenames = gather_data_filenames(test_data_dir, glob_txt)
        donations = load_donation_data_from_filenames(filenames)
        # sample data files have 1000 files each
        self.assertEqual(len(donations), 1000 + 1300 + 1500 + 800)


if __name__ == '__main__':
    unittest.main()