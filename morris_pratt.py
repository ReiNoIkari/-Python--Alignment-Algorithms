import sys

SEQUENCE = "ATGGCGATGGACAGCATGTTAGTCAGTGACAGATCGTGCAGCAGAT"
MOTIF = "AGAT"


def pre_calcul(motif):
    """
    Index table
    """
    j = 0
    board= [-1] * len(motif)
    for i in range(1, len(motif)):
        while j >- 1 and motif[i] != motif[j]:
            j = board[j]
        j += 1
        board[i] = j
    return board

def recherche(motif, sequence, board):
    """
    Morris Pratt table
    """
    j = 0
    for i in range(1, len(sequence) ):
        while j >- 1 and sequence[i] != motif[j]:
            j = board[j]
        j += 1
        if j == len(motif):
            print("Match found at pos: %d" % (i-len(motif)+1))
            j = board[j-1]


#MAIN
SEQUENCE= open(sys.argv[2], "r").read()
MOTIF=str(sys.argv[1])
print("Finding MOTIF in SEQUENCE:")
print("SEQUENCE = ", SEQUENCE)
print("MOTIF = ", MOTIF)
print("Morris Pratt algorithm result:")
BOARD=pre_calcul(MOTIF)
recherche(MOTIF, SEQUENCE, BOARD)