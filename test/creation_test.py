import unittest
from pathlib import Path

from smart_open import open as so

from vrt import Corpus, Text, P, S


class MyTestCase(unittest.TestCase):
    def test_something(self):
        with Corpus("~", "mycorpus", 4, "textname", "author") as c:
            with Text(c, textname="Demotext2", author="Frank_N") as _:
                with P(c) as _:
                    for _ in range(10):
                        with S(c) as s:
                            s.writep("Das", "PDS", "PRON", "der")
                            s.writep("hier", "ADV", "ADV", "hier")
                with P(c) as _:
                    with S(c) as s:
                        s.writep("Unplausibel", "PDF", "PRON", "plausibel")

        mypath = Path("~/mycorpus.vrt.gz").expanduser().resolve()
        self.assertTrue(mypath.exists())
        with so(mypath) as f:
            text = [line.strip() for line in f]
        self.assertIn("<", text[0])
        self.assertIn("<", text[-1])
        self.assertGreater(len(text), 1)


if __name__ == '__main__':
    unittest.main()
