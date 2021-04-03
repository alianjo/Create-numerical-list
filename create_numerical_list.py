#!/usr/bin/env python3


def addZiros(value):
    ''' we add ziros to the first part of number'''
    if len(str(value)) < number_length :
        ziros = number_length - len(str(value))
        return (ziros * '0' + str(value))
    else :
        return str(value)

def write_list(path):
    with open(path,'w') as file:
        for i in map(addZiros,range( 1 , int(str(1) +  number_length  * '0') + 1 )):
            file.write(i + '\n')
        file.close()

if '__main__' == __name__:
    number_length =int(input("Entre you numer of digits :"))
    path = input("Enter your path to save : ")
    write_list(path)
