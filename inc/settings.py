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


"""
number of iterations used to generate the passwords
altering this will change all generated passwords
and render old ones incompatible
"""
ROUNDS = 1000000

"""
master seed that is used for the generation of passwords
do not alter this or determ-pwgen will generate incompatible passwords
"""
MASTER_SEED = "MasterSeed for determ-pwgen by I3ck (Martin Buck)." \
              "This enhances or at least doesn't lower security. NK3FE28Z7MGAED5RMN9YBPU5KPWCG7Q0DVY0NWEX4WVGY6Y98B"

"""
the path to the json file in which the accounts shall be saved / loaded
"""
PATH_ACCOUNTS_FILE = "accounts.json"
