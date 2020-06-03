#!/usr/bin/python3
"""
MyList - subclass of list
"""


class MyList(list):
    """ public method: print sorted list """
    def print_sorted(self):
        """ sorts list and then print """
        new_list = self[:]
        new_list.sort()
        print(new_list)
