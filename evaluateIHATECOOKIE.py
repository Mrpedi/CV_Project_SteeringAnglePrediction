import sys
import pickle
import math
import csv
results = csv.reader(open(sys.argv[1]))

evaluation_data = {}
try:
	evaluation_data = pickle.load(open("eval.p", "rb"))
except:
	eval_csv = csv.reader(open("eval.csv"))
	for l in eval_csv:
		frame_id, angle = l[0], l[1]
		if frame_id == "frame_id":
			continue
		evaluation_data[frame_id] = float(angle)
		pickle.dump(evaluation_data, open("eval.p", "wb"))
error = 0
n = 0
for l in results:
	if "Filename" in l:
		continue
	frame_id, angle = l[0], l[1]
	if frame_id == "frame_id":
		continue
	frame_id = frame_id+'.jpg'
	error += (evaluation_data[frame_id]*100 - float(angle))**2  # (evaluation_data[frame_id] - float(angle))
	n += 1
final_error = math.sqrt(error/n)
print final_error/10000.00
