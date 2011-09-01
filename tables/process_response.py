import csv
f = open('reporting_ranks_qualitative.csv', 'rUb') 
dr = csv.DictReader(f)
outlist = []
outfile = open('response.csv', 'w')
outfields = ['State']
for row in dr:
	outrow = {}
	outrow['State'] = row['State']
	for field in row:
		if field[-5:] == " Rank":
			rank = row[field]
			hidden_rank = rank
			if hidden_rank == 'N':
				hidden_rank = 999
			if field[:-5] not in outfields:
				outfields.append(field[:-5])
			submission_key = field[:-5] + " Submission Timeline"
			if row.has_key(submission_key):
				outrow[field[:-5]] = "<span style='display: none;'>%s</span><img src=http://assets.news21.com/2011/response/images/%sred.png title='%s' width='20' height='20'>" % (hidden_rank, rank, row[submission_key])
			else:
				print "No %s" % submission_key
	outlist.append(outrow)

outwriter = csv.DictWriter(outfile, outfields)
outwriter.writeheader()
outwriter.writerows(outlist)