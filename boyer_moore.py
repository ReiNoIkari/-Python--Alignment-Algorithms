#!/usr/bin/env python
import sys
"""
Inspired and adaptated from 
http://www.mathcs.emory.edu/~cheung/Courses/323/Syllabus/Text/Matching-Boyer-Moore1.html
http://www8.cs.umu.se/kurser/TDBA59/VT01/mom3/slides/BM-alg.html
https://stackoverflow.com/questions/6207819/boyer-moore-algorithm-understanding-and-example  see btilly explication post

Simplified Boyer-Moore from Goodrich
That don't use good suffix heuristic but instead
Slide 1 character down and start matching again           
"""
 
def lastOccurrence(string, size):
    """
    Preprocessing for the bad character heuristic
    """ 
    number_characters = 256
    badChar = [-1]*number_characters
    for i in range(size):
        badChar[ord(string[i])] = i
    return badChar
 
def boyerSearch(motif,sequence):
    """
    Boyer Moore approach
    """
    badChar = lastOccurrence(motif, len(motif)) 
    shift = 0
    while shift <= len(sequence)-len(motif):
        j = len(motif)-1
        while j>=0 and motif[j] == sequence[shift+j]:
            j -= 1
        if j<0:
            print("Match found at pos: %d" % (shift))
            shift += (len(motif)-badChar[ord(sequence[shift+len(motif)])] if shift+len(motif)<len(sequence) else 1)
        else:
            shift += max(1, j-badChar[ord(sequence[shift+j])])
 
#MAIN

SEQUENCE= open(sys.argv[2], "r").read()
MOTIF=str(sys.argv[1])
print("Finding MOTIF in SEQUENCE:")
print("SEQUENCE = ", SEQUENCE)
print("MOTIF = ", MOTIF)
print("Boyer Moore algorithm result:")
boyerSearch(MOTIF, SEQUENCE)