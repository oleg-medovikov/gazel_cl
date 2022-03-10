from config import ROOT
from value import VIEW_PROJECT, VIEW_REFERENCE
import os

import hashlib


def get_hash_md5(filename):
    with open(filename, 'rb') as f:
        m = hashlib.md5()
        while True:
            data = f.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()


def reference_files():
    REFERENCE_CATALOG = VIEW_REFERENCE.r_level1 + '_' + VIEW_REFERENCE.r_level2 + '_' + VIEW_REFERENCE.r_level3

    PATH = ROOT / VIEW_PROJECT.p_name / REFERENCE_CATALOG

    if not os.path.exists(testpath):
        os.makedirs(PATH)
    else:
        for path in list(PATH.glob('*')):
            if path.is_file():
                get_hash_md5(path)
