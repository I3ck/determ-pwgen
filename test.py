"""
    Copyright (c) 2014 - 2015 I3ck (Martin Buck)
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation the rights to
    use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
    and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
    DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
    OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


import unittest

from inc.Password import Password
import inc.settings as settings
from inc.DetermPwgen import *


class DetermPwgenTest(unittest.TestCase):

    def test_only_numbers_letters(self):
        self.assertTrue(Password._only_numbers_letters("aasdasd"))
        self.assertTrue(Password._only_numbers_letters("48989844"))
        self.assertTrue(Password._only_numbers_letters("asuidauidjhu37485357"))

        self.assertFalse(Password._only_numbers_letters("aasdasd!"))
        self.assertFalse(Password._only_numbers_letters("aasdasd\""))
        self.assertFalse(Password._only_numbers_letters("aasdasd."))
        self.assertFalse(Password._only_numbers_letters("aasdasd-"))
        self.assertFalse(Password._only_numbers_letters("aasdasd,"))

    def test_mixed_case(self):
        self.assertEqual(Password._mixed_case("ahsdahdusa"), "Ahsdahdusa")
        self.assertEqual(Password._mixed_case("Ahsdahdusa"), "Ahsdahdusa")
        self.assertEqual(Password._mixed_case("ASDSADASDASD"), "aSDSADASDASD")
        self.assertEqual(Password._mixed_case("aSDSADASDASD"), "aSDSADASDASD")

    def test_special_chars(self):
        self.assertEqual(Password._with_special("ahsdahdusa!"), "ahsdahdusa!")
        self.assertFalse(Password._with_special("ahsdahdusa") == "ahsdahdusa")

    def test_password_types(self):
        password = Password("nospecialalllower")
        self.assertEqual(password.PWLONG, "Nospecialalllowe#")
        self.assertEqual(password.PWLONG_NO_SPECIAL, "Nospecialalllowe")
        self.assertEqual(password.PWSHORT, "Nospecialalllow[")
        self.assertEqual(password.PWSHORT_NO_SPECIAL, "Nospecialalllowe")

    def test_password_generation_v5(self):
        seed = "a"
        username = "a"
        hostname = "a"
        determpwgen = DetermPwgen(seed)
        pw = determpwgen.generate_password(hostname, username, settings.HASHING_ROUNDS)
        self.assertEqual(pw.PWLONG, "4g+b9DXlgGTV1d0QHBeCSl3Fh/+GKuxk6HOU+K+D7ioFmE73kLgPrVAzvq+IGif5zukWpO74zyuT77KhjYMU2g==")
        self.assertEqual(pw.PWLONG_NO_SPECIAL, "4gb9DXlgGTV1d0QHBeCSl3FhGKuxk6HOUKD7ioFmE73kLgPrVAzvqIGif5zukWpO74zyuT77KhjYMU2g")
        self.assertEqual(pw.PWSHORT, "4g+b9DXlgGTV1d0Q")
        self.assertEqual(pw.PWSHORT_NO_SPECIAL, "4gb9DXlgGTV1d0QH")


if __name__ == "__main__":
    unittest.main()
