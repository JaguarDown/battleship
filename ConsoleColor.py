#!/usr/bin/python

# TODO: Change functionality to just return a string so you can print it how
# you want to.

class ConsoleColor:
    OKGREEN = '\033[92m'
    FAILRED = '\033[91m'
    ENDC = '\033[0m'
    OKBLUE = '\033[94m'

    def ok(self):
        return "[" + self.OKGREEN + "OK" + self.ENDC + "]"

    def fail(self):
        return "[" + self.FAILRED + "FAIL" + self.ENDC + "]"

    def blue(self, text):
        return self.OKBLUE + text + self.ENDC

    def red(self, text):
        return self.FAILRED + text + self.ENDC