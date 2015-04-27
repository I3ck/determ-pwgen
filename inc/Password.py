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

import random
import string
from inc.settings import LENGTH_SHORT


class Password:
    def __init__(self, pwlong):
        self.PWLONG = self._mixed_case(self._with_special(pwlong))

        self.PWLONG_NO_SPECIAL = self._mixed_case(''.join(c for c in self.PWLONG if c.isalnum()))

        self.PWSHORT = self._mixed_case(self._with_special(self.PWLONG[:LENGTH_SHORT]))

        self.PWSHORT_NO_SPECIAL = self._mixed_case(self.PWLONG_NO_SPECIAL[:LENGTH_SHORT])

    @staticmethod
    def _mixed_case(pw):
        allupper = True
        alllower = True

        for c in pw:
            if not allupper and not alllower:
                return pw
            elif c.isalpha():
                if c.isupper():
                    alllower = False
                elif c.islower():
                    allupper = False

        # either allupper or alllower
        # swap case for first alphanumeric char
        for i, c in enumerate(pw):
            if c.isalpha():
                pw[i].swapcase()
                return pw

        return pw

    @staticmethod
    def _with_special(pw):
        if not Password._only_numbers_letters(pw):
            return pw

        # use pw as seed for random (to always get the same choice for the same password)
        random.seed(pw)

        newchar = random.choice(string.punctuation)

        out = ""
        for i, c in enumerate(pw):
            if i == len(pw)-1:
                out += newchar
            else:
                out += c

        return out

    @staticmethod
    def _only_numbers_letters(pw):
        allowed = string.ascii_letters + string.digits
        return all(c in allowed for c in pw)



