
import logging
from unittest import defaultTestLoader, TextTestRunner
from tests.test_pass import TestPass

def full_suite():
    suite = defaultTestLoader.loadTestsFromTestCase(TestPass)
    return suite

def main():
    logging.basicConfig(level=logging.ERROR)
    suite = full_suite()
    TextTestRunner().run(suite)
    return

if __name__ == "__main__":
    main()