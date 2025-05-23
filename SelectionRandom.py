from random import uniform,sample
from count import comptage

def Selection(R, S,I):
    RegAleat = sample(R, k=8)
    couples_ordonnais = 0
    for i in range(1,8):
        if RegAleat[i]>RegAleat[i-1] : couples_ordonnais += 1
    SancAleat = sample(S, k=couples_ordonnais)
    return RegAleat, SancAleat

