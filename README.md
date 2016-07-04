Python2to3 workshop
==================

Try to convert both example.py and test.py to Python 3!

1. Start with excellent test coverage
2. Make sure it runs fine on the latest Python 2.7.x version of Python
3. Run Python 2 with the `-3` command line switch. This enables warnings about features that will be removed (or change) in 3. Run your test suite again, and fix code that you get warnings about until there are no warnings left, and all your tests still pass. 
4. Run the `2to3` source-to-source translator over your source code tree. Run the result of the translation under Python 3. Manually fix up any remaining issues, fixing problems until all tests pass again.

## Running unit tests
`python -m unittest test`

Or (easier): `pip install nose` (in both your Python 2 and Python 3 environment) and just run `nosetests` when you're in the directory of this repo.

