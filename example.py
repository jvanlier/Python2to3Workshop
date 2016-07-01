# example.py
"""An example Python 2 file to practice conversion to Python 3."""
import sys


class SomeException(Exception):
    def __init__(self, message):
        super(SomeException, self)
        self.message = message


def hello_world():
    return u"hello world!"


def ni_hao_world():
    return b'\xe4\xbd\xa0\xe5\xa5\xbd' + " world"


def split_dollar_bills(n_persons, n_bills):
    """
    Calculate the amount of dollar bills everyone gets, should you need to
    divide them equally over a fixed number of persons, without splitting them
    up (and it's okay to discard any remainder).

    :param n_persons: number of persons
    :param n_bills: total number of 1 dollar bills available
    :return: the amount of bills everyone gets (integer)
    """
    bills_per_person = n_bills / n_persons
    print "Dividing {n_bills} bills over {num_persons} persons, I get to " \
          "keep {keep} bills!"\
        .format(n_bills=n_bills, num_persons=n_persons,
                keep=n_bills - bills_per_person * n_persons)
    return bills_per_person


def dont_pass_42(v):
    """Function that will happily accept anything except 42
    :raises SomeException if argument is 42.
    """
    if v == 42:
        raise SomeException, "Argh! Not 42 :("


def zip_it(list1, list2):
    return zip(list1, list2)


def main():
    print "#1: Bytes/Strings"
    print hello_world()
    print ni_hao_world()

    print "\n#2: Integers"
    bills_per_person = split_dollar_bills(n_persons=8, n_bills=90l)
    print "Bills per person:", bills_per_person

    print "\n#3: Exception syntax"
    try:
        dont_pass_42(42)
    except SomeException, e:
        pass
    print >>sys.stderr, "Caught exception with message \"{}\"".format(e.message)

    print "\n#4: Views and iterators instead of lists"
    zipped = zip_it([1, 2, 3], ["one", "two", "three"])
    print "After zipping, we got", zipped, " and its type is ", type(zipped)
    assert(type(zipped) == list)

if __name__ == "__main__":
    main()
