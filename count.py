import json
#increment the VisitCounter's variable
op = open('./count.json', 'r')
l_file = json.load(op)
l_file["vcount"] += 1
op = open('./count.json', 'w')
json.dump(l_file, op, indent=4)
