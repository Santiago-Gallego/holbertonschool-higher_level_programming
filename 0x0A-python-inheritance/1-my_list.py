#!/urs/bin/python3
""" class myList """


class MyList(list):
    """ method print sort list """
    def print_sorted(self):
        List = self[:]
        sorted(List)
        print(List)
