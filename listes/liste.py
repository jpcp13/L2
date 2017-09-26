with open('emails.txt', 'w') as emails_file:
	with open('liste.txt', 'r') as students_file:
		for line in students_file:
			ls = line.split()
			if ';' in ls:
				emails_file.write(ls[-1]+',\n')
