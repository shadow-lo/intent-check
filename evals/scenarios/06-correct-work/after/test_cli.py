import io
import unittest
from contextlib import redirect_stdout
from cli import main


class T(unittest.TestCase):
    def test_hello(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            main(["Ada"])
        self.assertEqual(buf.getvalue(), "Hello, Ada!\n")

    def test_verbose(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            main(["--verbose", "Ada"])
        self.assertIn("[verbose]", buf.getvalue())
        self.assertTrue(buf.getvalue().endswith("Hello, Ada!\n"))


if __name__ == "__main__":
    unittest.main()
