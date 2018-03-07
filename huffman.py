import operator
from math import log2 as log
from math import ceil as up
import sys

def_dict = {}

def_dict['a'] = 0.1
def_dict['b'] = 0.1
def_dict['c'] = 0.15
def_dict['d'] = 0.18
def_dict['e'] = 0.2
def_dict['f'] = 0.27


ex1 = {'a': 0.5, 'b': 0.25, 'c': 0.25}
ex2 = {'a': 0.25, 'b': 0.25, 'c': 0.2, 'd': 0.15, 'e': 0.15}
ex3 = {'a': 0.5, 'b': 0.3, 'c': 0.15, 'd': 0.05} #Veszpremi konyvbol 2.3 pelda
ex4 = {'a': 0.3, 'b': 0.19, 'c': 0.16, 'd': 0.03, 'e': 0.12, 'f': 0.11, 'g': 0.09}
ex5 = {'a': 0.7, 'b': 0.1, 'c': 0.15, 'd': 0.03, 'e': 0.02}

def_dict = ex4.copy()




global left_char, right_char
left_char = '0'
right_char = '1'
# print(def_dict)

# d = def_dict
# for w in sorted(d, key=d.get):
#   print(w, d[w])

# dictionary = sorted(def_dict.items(), key=operator.itemgetter(0))
# print(type(dictionary))
# code_dict = {}
# for i in dictionary:
#     print(i)
# # while len(dictionary)>1:

def huffman(p):
    '''Return a Huffman code for an ensemble with distribution p.'''
    assert(abs(sum(p.values()) - 1.0) < 0.000000001) # Ensure probabilities sum to 1

    # Base case of only two symbols, assign 0 or 1 arbitrarily
    if(len(p) == 2):
        # return dict(zip(p.keys(), ['0', '1']))
        return dict(zip(p.keys(), [left_char, right_char]))

    # Create a new distribution by merging lowest prob. pair
    p_prime = p.copy()
    a1, a2 = lowest_prob_pair(p)
    p1, p2 = p_prime.pop(a1), p_prime.pop(a2)
    p_prime[a1 + a2] = p1 + p2

    # Recurse and construct code on new distribution
    c = huffman(p_prime)
    # print("c: ",c)
    ca1a2 = c.pop(a1 + a2)
    # print("ca1a2: ",ca1a2)
    c[a1], c[a2] = ca1a2 + left_char, ca1a2 + right_char
    # print("c_after: ",c)
    # print("")

    return c

def lowest_prob_pair(p):
    '''Return pair of symbols from distribution p with lowest probabilities.'''
    assert(len(p) >= 2) # Ensure there are at least 2 symbols in the dist.

    # sorted_p = sorted(p.items(), key=lambda (i,pi): pi)
    sorted_p = sorted(p.items(), key=lambda i_pi: i_pi[1])
    # print("Sorted: ",sorted_p)
    return sorted_p[0][0], sorted_p[1][0]

def calc_entropy(p):
    entr = 0
    for i in p:
        entr += p[i]*log(1/p[i])
    print("H: ",entr, " bit\t(Entropy)")
    return entr

def calc_avg_code_len(p,d):
    c_len = 0
    for i in d:
        c_len += p[i]*len(d[i])
    print("L: ",c_len, " bit\t(Code Length)")
    return c_len

def calc_efficiency(p,d):
    H=calc_entropy(p)
    L = calc_avg_code_len(p,d)
    h = H/L
    print("h: ",h*100, " %\t(Efficiency)")
    return h,H,L

def create_double_dict(p):
    new_dict = {}
    for i in p:
        for j in p:
            new_dict[i+j]=p[i]*p[j]
    # print (sum(p.values()))
    return new_dict

def naive_code(p):
    new_dict = {}
    code_len = up(log(len(p)))
    c_len = '0'+str(code_len)+'b'
    for i in p:
        digits = [(ord(c)-ord('a')) for c in i]
        zero_padded_BCD_digits = [format(d, c_len) for d in digits]
        new_dict[i] = ''.join(zero_padded_BCD_digits)
    # print(new_dict)
    return new_dict
