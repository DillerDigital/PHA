import glob
import logging
import os.path as op

import pandas as pd

logger = logging.getLogger(__name__)


def gather_data_filenames(data_dir, glob_txt):
    return glob.glob(op.join(data_dir, glob_txt))


def load_donation_data_from_filenames(filenames, column_filter={}):
    if isinstance(filenames, str):
        filenames = [filenames]
    donations = []
    for name in filenames:
        df = pd.read_excel(name)
        logger.debug(f'Loaded {len(df)} records from {name!r}')
        donations.append(df)
    return pd.concat(donations, axis=0)


def normalize_name(name):
    return ' '.join(s.capitalize() for s in name.split())