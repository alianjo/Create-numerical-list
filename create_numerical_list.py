#!/usr/bin/env python3
from colorama import Fore
class Listcreator:
    def __init__(self, number_length, path):
        self.number_length = number_length
        self.path = path

    def addziros(self, value):
        """we add ziros to the first part of number"""
        if len(str(value)) < self.number_length:
            ziros = self.number_length - len(str(value))
            return ziros * '0' + str(value)
        else:
            return str(value)

    def write_list(self):
        """write the numbers line by line in the file"""
        with open(self.path, 'w') as file:
            for i in map(self.addziros, range(1, int(str(1) + self.number_length * '0') + 1)):
                file.write(i + '\n')
            file.close()


if '__main__' == __name__:
    A = Listcreator(int(input(Fore.RED + "[*]" + " Enter number length :")), input(Fore.RED + "[*]" + " Enter the Path :"))
    A.write_list()
