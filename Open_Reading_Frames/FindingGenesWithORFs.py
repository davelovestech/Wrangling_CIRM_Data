#!/usr/bin/python
# https://github.com/niemasd/Algorithm-Problem-Solutions/blob/master/ROSALIND%20Solutions/Bioinformatics%20Armory/15%20-%20ORFR%20-%20Finding%20Genes%20with%20ORFs/FindingGenesWithORFs.py
from Bio.Seq import translate
from Bio.Seq import reverse_complement
dna = "TTCCGGTATTTAGAGGATCGGGGCCAGTAATGCGAAGGTGATTGTGCCTTCGCGCAGTTGAATGCGAAAGCATTGTCACCTTATAGGTTTGCGGATCATCAGCTTGATTTGAATACGCTTTGTCCTGCCCCCCTTGATACGATGAAACAGGATTTACTGCTGACAACTCAGAATGGAAAGCAAGGTATGATGCGCTGACTTGGTTAGAACGACCGGATCATCGAGATGGCGGTGAATTATTCAGACGTAACGTCGGGAAGCTTCACTTCCTACTGGCTACGCGATTTAAAACTCACTGCCGGTGTATGACCATATTATACATCGGATATCTGTATCGCTGTTTGTGCCGCGGTTATACGCCACTTGTTGCTAATGGTTATCTACTATTCTGCACAGATAGAGAGCATTTGATGTGGAAATGGGGAAAGGCGCTTTTCTAGCTAGAAAAGCGCCTTTCCCCATTTCCACATGCGGTATTTCTCAATGGAAACTTTCATGTAATCTGTCCCTTGAACAGAGCCGTTCAGTACAGCCCTACTCAAACGCATTTGCTCTGTTCACACCCTAGTGCAACATAAACTAGGGGATGTGAGTTACTCGCCTGTGAACCGAGGTCCTCTTTCATATCTTGGTATTAAAAACTCCCTTATGGCGTGCATCAATGAACTTTGCACTTACGGAAGCTGACTTGAATCCTCCCAGCCCGCATTGTATTGCGTTAGACACAGGTGTCGAATGCTGCAACCATCTAGCCGCTTAAGTCGTACCACCCTGCCGCGCAGGGTTACATATTTACTTATTGTTCTTACTACGATCGCAAGCTCAATTAGCTTCCCTGCATCCAAAGCAAAGGGCTCGGACGAGCAGCAGCCCATGACCA"
initial = []
for start in xrange(0,3):
    initial.append(translate(dna[start:-(3-start)]))
    initial.append(translate(reverse_complement(dna)[start:-(3-start)]))
longest = 0
best = ""
for j in xrange(len(initial)):
    init = initial[j]
    st = len(init)
    for i in range(len(init)-1,-1,-1):
        if(init[i] == '*'):
            st = i+1
            break
    initial[j] = init[:st]
best = ""
for init in initial:
    frames = init.split("*")
    for frame in frames:
        st = -1
        for i in range(len(frame)):
            if frame[i] == 'M':
                st = i
                break
        if st != -1 and len(frame[st:]) > len(best):
            best = frame[st:]
print best
