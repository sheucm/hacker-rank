#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#


class Node:
    def __init__(self, ch):
        self.ch = ch
        self.children = {}  # ch, node
        self.is_word = False

def noPrefix(words):
    # Write your code here
    # print(words)
    
    root = Node('#')
    
    for w in words:
        curr = root
        for idx, ch in enumerate(w):
            
            if ch in curr.children:
                if curr.children[ch].is_word:
                    print("BAD SET")
                    print(w)
                    return
                if idx == len(w) - 1:
                    print("BAD SET")
                    print(w)
                    return
                
                curr = curr.children[ch]
                
            else:
                # Create new node
                curr.children[ch] = Node(ch)
                if idx == len(w) - 1:
                    curr.children[ch].is_word = True
                curr = curr.children[ch]
    
    print("GOOD SET")

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
