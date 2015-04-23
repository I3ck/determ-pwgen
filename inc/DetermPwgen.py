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


import hashlib
import base64
from inc.settings import MASTER_SALT
from inc.Password import Password


class DetermPwgen:

    def __init__(self, seed):
        self._seed = seed

    @staticmethod
    def multi_hash(text):
        text = hashlib.md5(text).digest()
        text = hashlib.sha1(text).digest()
        text = hashlib.sha224(text).digest()
        text = hashlib.sha256(text).digest()
        text = hashlib.sha384(text).digest()
        text = hashlib.sha512(text).digest()

        return text

    def generate_password(self, hostname, username, rounds):
        pw = (MASTER_SALT + self._seed + hostname + username).encode("UTF-8")

        for i in range(rounds):
            pw = self.multi_hash(pw)

        pw = base64.b64encode(pw)

        pw = pw.decode("UTF-8")

        return Password(pw)
