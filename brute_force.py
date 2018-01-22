#!/usr/bin/env python
"""
Naive Algorithm implementation
"""

SEQUENCE = "ATGGCGATGGACAGCATGTTAGTCAGTGACAGATCGTGCAGCAGAT"
MOTIF = "AGAT"

def naive(sequence, motif):
    """
    Naive approach
    """
    motif_lenght = len(MOTIF)
    for i in range(1, len(sequence) - len(motif) + 1):
        j = 0
        while j < motif_lenght:
            if sequence[i + j] == motif[j]:
                j += 1
                if j == motif_lenght:
                    print("Match found at pos: %d" % (i))
            else:
                break

#MAIN
print("Finding MOTIF in SEQUENCE:")
print("SEQUENCE = ", SEQUENCE)
print("MOTIF = ", MOTIF)
print("Naive algorithm result:")
naive(SEQUENCE, MOTIF)
