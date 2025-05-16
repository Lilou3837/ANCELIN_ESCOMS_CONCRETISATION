####
####  TOUS LES STR SONT EN MINUSCULES ET AU SINGULIER ET SANS ACCENT NULLE PART
####

class Card:
    def __init__ (self, 
                  couleur: str, 
                  nuit: int, 
                  indice: int,
                  merveille: dict, 
                  score: dict, 
                  condition: dict):
        """
        couleur : str
        nuit : int, 0 ou 1
        indice : int, 0 ou 1
        merveille : même chose que condition
        score : dictionnaire avec attribut : int (nb de points) et clé : par cartes ... qqch
                quand y'a des points dans tous les cas, la clé est 'a'
                si pas de points, disctionnaire vide
        condition : dictionnaire avec clé : str (merveille) et attribut : int (quantité nécessaire)
        """
        self.couleur = couleur
        self.nuit = nuit
        self.indice = indice
        self.merveille = merveille
        self.score = score
        self.condition = condition

    def __repr__(self):
        return self.couleur+str(self.nuit)+str(self.indice)+str(self.merveille)+str(self.score)+str(self.condition)

T=[None for _ in range(146)]
# Les indices sont les vraties valeurs utilisées par les cartes, il n'y a donc pas de carte 0 etc
# Aussi y'a rien en plein milieu du coup heh 

T[1] = Card('r', 0, 0, {'p': 1, 'chi': 1}, {}, {})
T[2] = Card('b', 0, 0, {'p': 2}, {}, {})
T[3] = Card('v', 0, 0, {}, {'a': 4}, {})
T[4] = Card('r', 0, 0, {'p': 1, 'cha': 1}, {}, {})
T[5] = Card('v', 0, 0, {'chi': 1}, {'a': 2}, {})
T[6] = Card('b', 0, 1, {'p': 1}, {}, {})
T[7] = Card('r', 0, 0, {'chi': 1, 'cha':1}, {}, {})
T[8] = Card('v', 0, 1, {'chi': 1}, {}, {})
T[9] = Card('b', 0, 0, {}, {'a': 5}, {})
T[10] = Card('r', 0, 0, {}, {'n': 3}, {})
T[11] = Card('v', 0, 0, {}, {'i': 2}, {})
T[12] = Card('j', 0, 1, {'cha': 1}, {}, {})
T[13] = Card('b', 0, 0, {}, {'p': 2}, {})
T[14] = Card('r', 0, 0, {'cha': 1}, {'n': 2}, {})
T[15] = Card('v', 0, 1, {}, {'chi': 2}, {})
T[16] = Card('r', 0, 0, {'chi': 1}, {'chi': 2}, {})
T[17] = Card('b', 0, 0, {'p': 1}, {'p': 3}, {'chi' : 2})
T[18] = Card('v', 0, 0, {'chi': 1}, {'e': 10}, {})
T[19] = Card('r', 0, 0, {'cha': 1}, {'cha': 2}, {})
T[20] = Card('v', 1, 1, {}, {'n': 2}, {'p' : 1})
T[21] = Card('b', 1, 0, {}, {'a': 8}, {'p' : 2})
T[22] = Card('v', 1, 1, {}, {'i': 1}, {})
T[23] = Card('r', 1, 0, {'p': 1, 'chi': 1}, {'e': 10}, {})
T[24] = Card('b', 1, 0, {'p': 1}, {'n': 2}, {'chi' : 1})
T[25] = Card('j', 1, 0, {}, {'j': 1, 'v':1}, {})
T[26] = Card('r', 1, 0, {'chi': 1}, {'cha': 3}, {})
T[27] = Card('j', 1, 0, {}, {'j': 1, 'b': 1}, {})
T[28] = Card('r', 1, 0, {'p': 1}, {'chi': 3}, {})
T[29] = Card('j', 1, 0, {'cha': 1}, {'cha': 2}, {})
T[30] = Card('r', 1, 0, {'p': 1}, {'p': 2}, {})
T[31] = Card('j', 1, 0, {}, {'j': 1, 'r': 1}, {})
T[32] = Card('r', 1, 0, {'p': 1, 'chi': 1}, {'a': 7}, {'p' : 3})
T[33] = Card('j', 1, 1, {}, {'cha': 3}, {})
T[34] = Card('v', 1, 0, {'chi': 1}, {'chi': 3}, {'p' : 2})
T[35] = Card('j', 1, 0, {'chi': 1}, {'e': 10}, {})
T[36] = Card('r', 1, 0, {}, {'cha': 4}, {'chi' : 2})
T[37] = Card('j', 1, 0, {}, {'n': 3}, {'cha' : 1})
T[38] = Card('v', 1, 0, {'p': 1}, {'i': 3}, {'chi' : 1, 'cha': 1})
T[39] = Card('r', 1, 0, {'p': 1, 'cha': 1}, {'a': 9}, {'chi' : 2})
T[40] = Card('b', 1, 0, {}, {'n' : 3}, {'p' : 1, 'chi' : 1, 'cha' : 1})
T[41] = Card('v', 0, 0, {'cha' : 1}, {'n' : 4}, {'p' : 2, 'chi' : 1})
T[42] = Card('j', 0, 0, {}, {'j' : 2, 'v' : 2}, {'p' : 1, 'chi' : 1})
T[43] = Card('b', 0, 0, {'p' : 1}, {'e' : 10}, {})
T[44] = Card('j', 0, 0, {}, {'j' : 2, 'b' : 2}, {'p' : 1, 'cha' : 1})
T[45] = Card('v', 0, 0, {'p' : 1}, {'a' : 13}, {'chi' : 3})
T[46] = Card('b', 0, 1, {}, {'a' : 10}, {'p' : 2, 'chi' : 1})
T[47] = Card('j', 0, 0, {}, {'j' : 2, 'r' : 2}, {'chi' : 1, 'cha' : 1})
T[48] = Card('r', 0, 0, {'chi' : 1}, {'p' : 3}, {})
T[49] = Card('b', 0, 1, {}, {'a' : 12}, {'p' : 2, 'cha' : 1})
T[50] = Card('j', 0, 0, {'p' : 1}, {'v' : 4}, {'cha' : 2})
T[51] = Card('b', 0, 0, {'p' : 1}, {'a' : 14}, {'p' : 4})
T[52] = Card('r', 0, 0, {}, {'chi' : 4}, {'p' : 3})
T[53] = Card('j', 0, 0, {'chi' : 1}, {'r' : 4}, {'cha' : 2})
T[54] = Card('v', 0, 0, {'chi' : 1}, {'i' : 4}, {'cha' : 2})
T[55] = Card('b', 0, 1, {'p' : 1}, {'p' : 3}, {'chi' : 1, 'cha' : 2})
T[56] = Card('j', 0, 0, {'cha' : 1}, {'b' : 4}, {'p' : 1, 'chi' : 2})
T[57] = Card('r', 0, 0, {}, {'p' : 4}, {'cha' : 3})
T[58] = Card('v', 0, 1, {}, {'i' : 3}, {'chi' : 3})
T[59] = Card('j', 0, 1, {}, {'j' : 3, 'r' : 3}, {'p' : 1, 'chi' : 3})
T[60] = Card('b', 0, 1, {}, {'a' : 16}, {'p' : 2, 'chi' : 2})
T[61] = Card('v', 0, 0, {'cha' : 1}, {'a' : 17}, {'chi' : 4})
T[62] = Card('j', 0, 1, {}, {'j' : 3, 'b' : 3}, {'cha' : 3})
T[63] = Card('v', 0, 1, {}, {'a' : 15}, {'chi' : 2, 'cha' : 1})
T[64] = Card('b', 0, 1, {}, {'a' : 18}, {'p' : 2, 'cha' : 2})
T[65] = Card('j', 0, 1, {}, {'j' : 3, 'v' : 3}, {'cha' : 3})
T[66] = Card('b', 0, 0, {}, {'a' : 20}, {'p' : 4})
T[67] = Card('v', 0, 1, {}, {'a' : 19}, {'chi' : 2, 'cha' : 2})
T[68] = Card('b', 0, 0, {}, {'a' : 24}, {'p' : 5})

T[101] = Card('', 0, 0, {'p' : 1}, {'p' : 1}, {})
T[102] = Card('', 0, 0, {},{'p' : 2}, {})
T[103] = Card('', 0, 0, {'chi' : 1}, {'chi' : 1}, {})
T[104] = Card('', 0, 0,{}, {'chi' : 2},{})
T[105] = Card('', 0, 0, {'cha' : 1}, {'cha' : 1}, {})
T[106] = Card('', 0, 0, {}, {'cha' : 2}, {})
T[107] = Card('', 0, 1, {'p' : 1}, {}, {})
T[108] = Card('', 0, 1, {'chi' : 1}, {}, {})
T[109] = Card('', 0, 1, {'cha' : 1}, {}, {})
T[110] = Card('', 0, 0, {'p' : 1}, {'i' : 1}, {})
T[111] = Card('', 0, 0, {'chi' : 1}, {'i' : 1}, {})
T[112] = Card('', 0, 1, {}, {'i' : 1}, {})
T[113] = Card('', 0, 0, {}, {'i' : 2}, {})
T[114] = Card('', 0, 0, {}, {'r' : 1, 'b' : 1}, {})
T[115] = Card('', 0, 0, {}, {'r' : 1, 'v' : 1}, {})
T[116] = Card('', 0, 0, {}, {'r' : 1, 'j' : 1}, {})
T[117] = Card('', 0, 0, {}, {'b' : 1, 'v' : 1}, {})
T[118] = Card('', 0, 0, {}, {'b' : 1, 'j' : 1}, {})
T[119] = Card('', 0, 0, {}, {'j' : 1, 'v' : 1}, {})
T[120] = Card('', 0, 1, {}, {'e' : 4}, {})
T[121] = Card('', 0, 0, {}, {'a' : 5}, {})
T[122] = Card('', 0, 0, {'p' : 1}, {'n' : 1}, {})
T[123] = Card('', 1, 0, {'p' : 1}, {}, {})
T[124] = Card('', 1, 0, {'chi' : 1}, {}, {})
T[125] = Card('', 1, 0, {'cha' : 1}, {}, {})
T[126] = Card('r', 0, 0, {'p' : 1}, {}, {})
T[127] = Card('r', 0, 0, {'chi' : 1}, {}, {})
T[128] = Card('r', 0, 0, {'cha' : 1}, {}, {})
T[129] = Card('r', 1, 0, {}, {}, {})
T[130] = Card('r', 0, 0, {}, {'r' : 1}, {})
T[131] = Card('b', 0, 0, {'p' : 1}, {}, {})
T[132] = Card('b', 0, 0, {'chi' : 1}, {}, {})
T[133] = Card('b', 0, 0, {'cha' : 1}, {}, {})
T[134] = Card('b', 0, 1, {}, {}, {})
T[135] = Card('b', 0, 0, {}, {'b' : 1}, {})
T[136] = Card('v', 0, 0, {'p' : 1}, {}, {})
T[137] = Card('v', 0, 0, {'chi' : 1}, {}, {})
T[138] = Card('v', 0, 1, {}, {}, {})
T[139] = Card('v', 0, 0, {}, {'n' : 1}, {})
T[140] = Card('v', 0, 0, {}, {'v' : 1}, {})
T[141] = Card('j', 0, 0, {'p' : 1}, {}, {})
T[142] = Card('j', 0, 1, {}, {}, {})
T[143] = Card('j', 0, 0, {}, {'e' : 4}, {})
T[144] = Card('j', 0, 0, {}, {'i' : 1}, {})
T[145] = Card('j', 0, 0, {}, {'j' : 1}, {})

























