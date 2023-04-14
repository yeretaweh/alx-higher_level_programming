#!/usr/bin/python3

class MyList(list):
"""Inherits from list"""
def print_sorted(self):
"""Prints the list sorted in ascending order"""
sorted_list = self.copy()
sorted_list.sort()
print(sorted_list)
