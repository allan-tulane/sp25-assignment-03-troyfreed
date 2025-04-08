import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
    # Top-down memoized edit distance
    if MED is None:
        MED = {}
    if (S, T) in MED:
        return MED[(S, T)]
    if S == "":
        MED[(S, T)] = len(T)
    elif T == "":
        MED[(S, T)] = len(S)
    elif S[0] == T[0]:
        MED[(S, T)] = fast_MED(S[1:], T[1:], MED)
    else:
        # Only insertion and deletion (no substitution)
        MED[(S, T)] = 1 + min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED))
    return MED[(S, T)]


def fast_align_MED(S, T, MED=None):
    # Top-down memoized edit distance with alignment
    if MED is None:
        MED = {}

    if (S, T) in MED:
        return MED[(S, T)]

    if S == "":
        MED[(S, T)] = (len(T), ('-' * len(T), T))

    elif T == "":
        MED[(S, T)] = (len(S), (S, '-' * len(S)))

    elif S[0] == T[0]:
        dist, (a1, a2) = fast_align_MED(S[1:], T[1:], MED)
        MED[(S, T)] = (dist, (S[0] + a1, T[0] + a2))

    else:
        insert_dist, (insert_a1, insert_a2) = fast_align_MED(S, T[1:], MED)
        delete_dist, (delete_a1, delete_a2) = fast_align_MED(S[1:], T, MED)
        sub_dist, (sub_a1, sub_a2) = fast_align_MED(S[1:], T[1:], MED)

        choice = [
            (1 + insert_dist, ('-' + insert_a1, T[0] + insert_a2)),     # Insert
            (1 + delete_dist, (S[0] + delete_a1, '-' + delete_a2)),     # Delete
            (1 + sub_dist,    (S[0] + sub_a1, T[0] + sub_a2))           # Substitute
        ]
        MED[(S, T)] = min(choice, key=lambda x: x[0])

    return MED[(S, T)]