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

# This looks really good. A couple of comments: when you pull out the last
# "n_lines" lines from your list, you don't need anything after the colon. This
# indicates "to the end of the list". The "None" will throw an error. Also,
# because you already get the last n_lines lines from the list, you don't need 
# to use counter to keep track of the number of lines printed. Two comments 
# about readability. Including blank lines to break up function chunks of code
# makes it easier to read and follow. Also, don't forget to add comments! It
# will help others to read and understand your code, but also help you should
# you take a break and come back to it later. Overall, though, this looks great.
# Keep it up! - Mike