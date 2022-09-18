#!/usr/bin/env python3

import numpy as np
import sys
from fasta import readFASTA

# #opening fasta file
# input_sequences = readFASTA(open("CTCF_38_M27_AA.faa"))
#
# #taking the sequnces and not the headers from each file, setting gap penalty
# seq1_id, sequence1 = input_sequences[0]
# seq2_id, sequence2 = input_sequences[1]
# gap_penalty = -10
#
# #creating a dictionary, taking my input file, hardcoding a scoring matrix and a corresponding matrix with the letter values
# sd = {}
# dna_score = sys.argv[1]
# hoxd = np.loadtxt(open(dna_score), object, skiprows=1)
# s1 = np.array(hoxd[:,0])
# s1a = np.array(hoxd[:,1:]).astype(float)
#
# for i, nt in enumerate(s1):
#     sd[nt] = i
#
# #creating my two matrices
# F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))
# T_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))
# for i in range(len(sequence1)+1):
#     F_matrix[i,0] = i * gap_penalty
# for j in range(len(sequence2)+1):
#     F_matrix[0,j] = j * gap_penalty
#
# #initializing the rows in my t-matrix
# for i in range(len(sequence1)+1):
#     T_matrix[i,0] = 1
# for j in range(len(sequence2)+1):
#     T_matrix[0,j] = 2
# for x in range(len(sequence1)+1):
#     T_matrix[0,0] = 0
#
# #Running needleman wunsch equations for matches/mismatches
# for i in range(1, len(sequence1)+1):
#     for j in range(1, len(sequence2)+1):
#         match_score = s1a[sd[sequence1[i-1]], sd[sequence2[j-1]]]
#         d = F_matrix[i-1,j-1] + match_score
#         h = F_matrix[i,j-1] + gap_penalty
#         v = F_matrix[i-1,j] + gap_penalty
#         F_matrix[i,j] = max(d, h, v)
#
#         if F_matrix[i,j] == d:
#             T_matrix[i,j] = 0
#
#         elif F_matrix[i,j] == h:
#             T_matrix[i,j] = 1
#
#         elif F_matrix[i,j] == v:
#             T_matrix[i,j] = 2
#
# #generating score
# score = F_matrix[len(sequence1), len(sequence2)]
# print(score)
# # print(T_matrix)
#
# #creating lists and preparing to assign values to my T-matrix
# align1 = []
# align2 = []
# T_list = []
# i = len(sequence1)
# j = len(sequence2)
# #assigning values to T-matrix based on d, h, or v.
# while i > 0 and j > 0:
#     T_list.append(T_matrix[i,j])
#     if T_matrix[i,j] == 0:
#         i -= 1
#         j -= 1
#     elif T_matrix[i,j] == 1:
#         j -= 1
#     elif T_matrix[i,j] == 2:
#         i -= 1
#
# # print(T_list)
# #Matching the vaues in the T-matrix to their correspong AAs and assinging those values to new lists.
# i = 0
# j = 0
# T_list.reverse()
# for val in T_list:
#     if val == 0:
#         align1.append(sequence1[i])
#         align2.append(sequence2[j])
#         i += 1
#         j += 1
#     elif val == 1:
#         align1.append('-')
#         align2.append(sequence2[j])
#         j += 1
#     elif val == 2:
#         align1.append(sequence1[i])
#         align2.append('-')
#         i += 1
#
# #counting gaps
# counter = 0
# for gap in align1:
#     if gap == '-':
#         counter += 1
# print(counter)
# print(align1)
# print(align2)

input_sequences = readFASTA(open("CTCF_38_M27_DNA.fna"))

seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]
gap_penalty = -300


sd = {}
dna_score = sys.argv[1]
hoxd = np.loadtxt(open(dna_score), object, skiprows=1)
s1 = np.array(hoxd[:,0])
s1a = np.array(hoxd[:,1:]).astype(float)

for i, nt in enumerate(s1):
    sd[nt] = i
    
F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))
T_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))
for i in range(len(sequence1)+1):
    F_matrix[i,0] = i * gap_penalty
for j in range(len(sequence2)+1):
    F_matrix[0,j] = j * gap_penalty
    
for i in range(len(sequence1)+1):
    T_matrix[i,0] = 1
for j in range(len(sequence2)+1):
    T_matrix[0,j] = 2  
for x in range(len(sequence1)+1):
    T_matrix[0,0] = 0

for i in range(1, len(sequence1)+1):
    for j in range(1, len(sequence2)+1):
        match_score = s1a[sd[sequence1[i-1]], sd[sequence2[j-1]]]
        d = F_matrix[i-1,j-1] + match_score
        h = F_matrix[i,j-1] + gap_penalty
        v = F_matrix[i-1,j] + gap_penalty
        F_matrix[i,j] = max(d, h, v)
        
        if F_matrix[i,j] == d:
            T_matrix[i,j] = 0
            
        elif F_matrix[i,j] == h:
            T_matrix[i,j] = 1
            
        elif F_matrix[i,j] == v:
            T_matrix[i,j] = 2
            
score = F_matrix[len(sequence1), len(sequence2)]
print(score)
# print(T_matrix)

align1 = []
align2 = []
T_list = []
i = len(sequence1)
j = len(sequence2)

while i > 0 and j > 0:
    T_list.append(T_matrix[i,j])
    if T_matrix[i,j] == 0:
        i -= 1
        j -= 1
    elif T_matrix[i,j] == 1:
        j -= 1
    elif T_matrix[i,j] == 2:
        i -= 1

# print(T_list)

i = 0
j = 0
T_list.reverse()        
for val in T_list:
    if val == 0:
        align1.append(sequence1[i])
        align2.append(sequence2[j])
        i += 1
        j += 1
    elif val == 1:
        align1.append('-')
        align2.append(sequence2[j])
        j += 1
    elif val == 2:
        align1.append(sequence1[i])
        align2.append('-') 
        i += 1
counter = 0
for gap in align1:
    if gap == '-':
        counter += 1
counters = 0
for gaps in align2:
    if gaps == '-':
        counters +=1
print(counter)
print(counters)
print(align1)
print(align2)