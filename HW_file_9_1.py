import json

infile = open("US_fires_9_1.json", "r")
outfile = open("readable_fi_data.json", "w")

fi_data = json.load(infile)
json.dump(fi_data, outfile, indent=4)

list_of_fis = fi_data

print(list_of_fis)