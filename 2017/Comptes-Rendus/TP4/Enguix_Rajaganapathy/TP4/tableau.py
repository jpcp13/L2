from module import *

cols = 10
rows = 20

s = "\\begin{tabular}{" + "|c|c" *2 + "|>{\columncolor{yellow}}c"+"|c|c"*2 +">{\columncolor{yellow}}c}\n"
s+= '\\hline \n'

for i in range(rows):
	for j in range(cols):
		if j < cols - 1 :
			finir = '&'
		else:
			finir = '\\\\ \\hline \n'
		nb = cols * i + j + 1
	
		if is_prime(nb):
			s+= '\\textbf{'+ str(nb)+'}' + finir
		else : 
			if nb == 1:
				s+='\\cellcolor{red}'

			if nb % 2 == 0:
				s+='\\color{red}'

				if nb % 3 == 0:
					s+='\\cellcolor{cyan}'

					if nb % 7 == 0:
						s+='\\color{green}'

						if nb % 11 == 0:
							s+= '\\color[RGB]{255,0,186}'

			else :
				if nb % 3 == 0:
					s+= '\\cellcolor{cyan}'

					if nb % 7 == 0 :
						s+='\\color{green}'
					
						if nb % 11 == 0:
							s+='\\color[RGB]{255,0,186}'

				else :
					if nb % 7 == 0 :
						s+='\\color{green}'
					
						if nb % 11 == 0:
							s+='\\color[RGB]{255,0,186}'
					
					else:
						if nb % 11 == 0:
							s+= '\\color[RGB]{255,0,186}'

					
						else:
							if nb % 13 == 0:
								s+= '\\color[RGB]{150,0,186}'

			s+= str(nb) + finir

s+= '\n\end{tabular}'

with open('table.txt','w') as file :
	file.write(s)
