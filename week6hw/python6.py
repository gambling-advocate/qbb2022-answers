#!/usr/bin/env python

import sys

import numpy
import matplotlib.pyplot as plt
import matplotlib.colors as colors

# in1_fname should be ddCTCF
# in2_fname should be dCTCF
# bin_fname should be bed file with bin locations

def remove_dd_bg(mat):
     N = mat.shape[0]
     mat2 = numpy.copy(mat)
     for i in range(N):
         bg = numpy.mean(mat[numpy.arange(i, N), numpy.arange(N - i)])
         mat2[numpy.arange(i, N), numpy.arange(N - i)] -= bg
         if i > 0:
             mat2[numpy.arange(N - i), numpy.arange(i, N)] -= bg
     return mat2

def smooth_matrix(mat):
    N = mat.shape[0]
    invalid = numpy.where(mat[1:-1, 1:-1] == 0)
    nmat = numpy.zeros((N - 2, N - 2), float)
    for i in range(3):
        for j in range(3):
            nmat += mat[i:(N - 2 + i), j:(N - 2 + j)]
    nmat /= 9
    nmat[invalid] = 0
    return nmat

in1_fname, in2_fname, in3_fname, bin_fname, out_fname = sys.argv[1:6]
data1 = numpy.loadtxt(in1_fname, dtype=numpy.dtype([
    ('F1', int), ('F2', int), ('score', float)]))
data2 = numpy.loadtxt(in2_fname, dtype=numpy.dtype([
    ('F1', int), ('F2', int), ('score', float)]))
data3 = numpy.loadtxt(in3_fname, dtype=numpy.dtype([
    ('F1', int), ('F2', int), ('score', float)]))   
frags = numpy.loadtxt(bin_fname, dtype=numpy.dtype([
    ('chr', 'S5'), ('start', int), ('end', int), ('bin', int)]))

chrom = b'chr15'
start = 11170245
end = 12070245
start_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                     (frags['start'] <= start) &
                                     (frags['end'] > start))[0][0]]
end_bin = frags['bin'][numpy.where((frags['chr'] == chrom) &
                                   (frags['start'] <= end) &
                                   (frags['end'] > end))[0][0]] + 1
print(start_bin)
print(end_bin)


#setting the range
#monday = numpy.where((data1["F1"] >= start_bin) & (data1["F2"] < end_bin))
# tuesday = numpy.where((data2["F1"] >= start_bin) & (data2["F2"] < end_bin))
# #filtering out of the range
# filter_data1 = (data1[monday])
# filter_data2 = (data2[tuesday])
#
#
# #logging the scores
# filter_data1['score'] = numpy.log(filter_data1['score'])
# filter_data2['score'] = numpy.log(filter_data2['score'])
# #setting the values to start from zero
# filter_data1['F1'] = filter_data1['F1'] - start_bin
# filter_data1['F2'] = filter_data1['F2'] - start_bin
# print(filter_data1)
#
# filter_data2['F1'] = filter_data2['F1'] - start_bin
# filter_data2['F2'] = filter_data2['F2'] - start_bin
# filter_data1['score'] = filter_data1['score'] - numpy.min(filter_data1['score'])
# filter_data2['score'] = filter_data2['score'] - numpy.min(filter_data2['score'])

wednesday = numpy.where((data3['F1'] >= 54878) & (data3['F2'] <= 54951))
filter_data3 = (data3[wednesday])
filter_data3['score'] = numpy.log(filter_data3['score'])
filter_data3['F1'] = filter_data3['F1'] - 54878
filter_data3['F2'] = filter_data3['F2'] - 54878
filter_data3['score'] =  filter_data3['score'] - numpy.min(filter_data3['score'])

mat3 = numpy.zeros( [54951 - 54878 + 1, 54951 - 54878 + 1] )
mat3[filter_data3['F1'], filter_data3['F2']] = filter_data3['score']
mat3[filter_data3['F2'], filter_data3['F1']] = filter_data3['score']


# mat1 = numpy.zeros([end_bin - start_bin + 1, end_bin - start_bin +1])
# print(mat1.shape)
# print(filter_data1['F2'])
# mat1[filter_data1['F1'], filter_data1["F2"]] = filter_data1['score']
# mat1[filter_data1['F2'], filter_data1['F1']] = filter_data1['score']
#
# mat2 = numpy.zeros([end_bin - start_bin + 1, end_bin - start_bin +1])
# mat2[filter_data2['F1'], filter_data2["F2"]] = filter_data2['score']
# mat2[filter_data2['F2'], filter_data2['F1']] =filter_data2['score']


# fig, ax = plt.subplots(3)
# ax[0].imshow(mat1, cmap ='magma')
# ax[0].set_title('dCTCF')
#
# ax[1].imshow(mat2, cmap= 'magma')
# ax[1].set_title('ddCTCF')
#
# # plt.show()
#
# ax[2].imshow(smooth_matrix(remove_dd_bg(mat1)) - smooth_matrix(remove_dd_bg(mat2)), cmap = 'seismic')
# plt.show()
# plt.savefig("Nonanalyzed.png")

insulation_scores = []
nt_list = []
for i in range(5, 54951 - 54878 + 1) :
    insulation_scores.append(numpy.mean(mat3[(i - 5):i, i:(i + 5)]))
    #print(insulation_scores)
nt_list = numpy.linspace(10400000, 13400000, len(insulation_scores))
fig, ax = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, figsize=(5,6.25))
ax[0].axis('off')
plt.margins(x=0)
ax[1].set_xlim(10400000, 13400000)
plt.subplots_adjust(left=0.15, bottom=0.1, right=1.0, top=1.0, wspace=0.4, hspace=0.0)
ax[0].imshow(mat3,cmap='magma')
#ax[0].imshow(mat1, vmin = 0, vmax = 1, cmap='magma')
ax[0].set_title('dCTCF 40000')
ax[1].scatter(nt_list, insulation_scores)
ax[1].set_xlabel("nucleotide pos")
ax[1].set_ylabel("insulation score")
ax[1].set_title("insulation score")
fig.tight_layout()
plt.show()
fig.savefig( "insulationscore.png" )

