#USAGE: python scriptname.py input_filename [number_lines_to_display]
import sys
filename = sys.argv[1]
if len(sys.argv) > 2:
	n_lines = int(sys.argv[2])
else:
	n_lines = 10
counter = 0
line_list = []
for line in open(filename):
    if not line.startswith("#"):
        line_list.append(line.strip('\r\n'))
last_lines = line_list[-n_lines:None]
for line in last_lines:
    if counter < n_lines:
        print(line)
        counter = counter + 1