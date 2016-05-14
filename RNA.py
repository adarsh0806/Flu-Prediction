# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 15:25:29 2015

@author: rohankoodli
"""

dna = input("Enter a DNA strand sequence: ")
dna1 = dna.lower()

#for char in dna1:
    #print (char)

if not len(dna) % 3 == 0:
    print("Error: Number of bases must be multiple of 3")
else:
    
    rna = []

    for char in dna1:
        if char == "a":
            rna.append("U")
        elif char == "t":
            rna.append("A")
        elif char == "g":
            rna.append("C")
        elif char == "c":
            rna.append("G")
    print(rna)

    rna1 = (rna[::3])
    rna2 = (rna[1::3])
    rna3 = (rna[2::3])

    print (rna1)
    print (rna2)
    print (rna3)
    
    protein = []
    
    i = 0
    amino_acid = []
    
    for i in range(len(rna1)):
        codon = (rna1[i],rna2[i],rna3[i])
        amino_acid.append(codon)
        print(codon)
    
    print(amino_acid)
    
    j = 0
    for list in amino_acid:
        if list[j] == "U":
            if list[j+1] == "U":
                if list[j+2] == "U" or list[j+2] == "C":
                    print("Phe")
                else:
                    print("Leu")
            elif list[j+1] == "G":
                if list[j+2] == "U" or list[j+2] == "C":
                    print("Cys")
                elif list[j+2] == "A":
                    print("Stop")
                elif list[j+2] == "G":
                    print("Trp")
            elif list[j+1] == "A":
                if list[j+2] == "U" or list[j+2] == "C":
                    print("Tyr")
                else:
                    print("Stop")
            elif list[j+1] == "C":
                print("Ser")
        elif list[j] == "G":
            if list[j+1] == "U":
                print("Val")
            elif list[j+1] == "G":
                print("Gly")
            elif list[j+1] == "A":
                if list[j+2] == "U" or list[j+2] == "C":
                    print("Asp")
                else:
                    print("Glu")
            elif list[j+1] == "C":
                print("Ala")
        elif list[j] == "A":
            if list[j+1] == "U":
                if list[j+2] == "G":
                    print("Met(Start)")
                else:
                    print("Ile")
            elif list[j+1] == "G":
                if list[j+2] == "U" or list[j+2] == "C":
                    print("Ser")
                else:
                    print("Arg")
            elif list[j+1] == "A":
                if list[j+2] == "U" or list[j+2] == "C":
                    print("Asn")
                else:
                    print("Lys")
            elif list[j+1] == "C":
                print("Thr")
        elif list[j] == "C":
            if list[j+1] == "U":
                print("Leu")
            elif list[j+1] == "G":
                print("Arg")
            elif list[j+1] == "A":
                if list[j+2] == "U" or list[j+2] == "C":
                    print("His")
                else:
                    print("Gln")
            elif list[j+1] == "C":
                print("Pro")
                
                
                
            