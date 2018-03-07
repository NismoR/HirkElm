import huffman as huf

# A valószínűségek összegének 0-nak kell lennie!
ex0 = {'a': 0.1, 'b': 0.1, 'c': 0.15, 'd': 0.18, 'e': 0.2, 'f': 0.27}
ex1 = {'a': 0.5, 'b': 0.25, 'c': 0.25}
ex2 = {'a': 0.25, 'b': 0.25, 'c': 0.2, 'd': 0.15, 'e': 0.15}
ex3 = {'a': 0.5, 'b': 0.3, 'c': 0.15, 'd': 0.05} #Veszpremi konyvbol 2.3 pelda
ex4 = {'a': 0.3, 'b': 0.19, 'c': 0.16, 'd': 0.03, 'e': 0.12, 'f': 0.11, 'g': 0.09}
ex5 = {'a': 0.7, 'b': 0.1, 'c': 0.15, 'd': 0.03, 'e': 0.02}

def_dict = ex4.copy()   # Teszt szett kiválasztása
N=2                     # Forráskiterjesztés száma (ne emeld 4 fölé)



def coding(p):          # Kommenttel állítható Naív vagy Huffman kódolás
    return huf.huffman(p)
    # return huf.naive_code(p)












print("---------------- CALCULATIONS FOR ORIGINAL DATASET ----------------")
o_code=coding(def_dict)
oh,oH,oL=huf.calc_efficiency(def_dict,o_code)


print("")
print("---------------- CALCULATIONS FOR ",N,"x DATASET ----------------")
for i in range (N-1):
    def_dict=huf.create_double_dict(def_dict)

n_code=coding(def_dict)
nh,nH,nL=huf.calc_efficiency(def_dict,n_code)
dh=nh-oh
print("")
print("efficiency growth: ", dh, " %")
print("Shannon I. for old_h:     1 >= ", oh, " > ",1-1/(oH+1))
print("Shannon I. for new_h:     1 >= ", nh, " > ",1-1/(nH*N+1))
print("")
print("----------------          GENERATED CODES         ----------------")
print("Original code:", o_code)
print("New code:", n_code)