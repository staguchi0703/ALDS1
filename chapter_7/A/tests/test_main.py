import unittest

import sys
from io import StringIO
from contextlib import redirect_stdout

from .test_A import main

class Main_test(unittest.TestCase):
    def test_main(self):
        #コマンドライン引数を再現する
        sys.argv.clear()
        sys.argv.append('./main.py')

        #mainの標準出力をioにリダイレクト
        io = StringIO()
        with redirect_stdout(io):
            main.main()


        out_path = __file__.rsplit('/', 2)[0] + '/output.txt'
        f=open(out_path, 'r', encoding="utf-8")
        self.assertEqual(io.getvalue(), f)

if __name__ == "__main__":
    unittest.main()
