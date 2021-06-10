import re

#correct dates
dates=""""03/09/1994","30/12/1993", "03/07/2021"""

#incorrect dates
in_dates=""""30/02/2004", "31/11/2000", "43/15/1934"""

#no dates
no_dates="""Jest już godzina 17/46"""


sentences = """Milena Sikorska urodziła się w dniu 03/09/1994. 
Mateusz Kubiak urodził się natomiast 30/12/1993. 
Ich ślub będzie miał miejsce 03/07/2021 i było to niesamowite wydarzenie!
Ich pierwsze dziecko już się narodziło i było to w dniu 43/14/2001 """

def detectDates(tekst):
	regex = re.compile(r'[\s\'",\.](\d{2})/(\d{2})/(\d{4})[\s\'",\.]')
	return regex.findall(tekst)

def printDates(tablica, daty):
	if daty:
		print(f"{tablica} \n\nOdnalazłem {len(daty)} dat(y).\nSą to:")
		for d in daty:
			print(f"Dzień: {d[0]}, Miesiąc: {d[1]}, Rok: {d[2]}")
		print('')
	else:
		print(f"W tekście >>{tablica}<< nie odnalazłem żadnych dat!\n")
	pass

def printDates2(daty):
	print("Z czego tylko te istnieją naprawdę:")
	for d in daty:
		print(f"Dzień: {d[0]}, Miesiąc: {d[1]}, Rok: {d[2]}")
	print('')
	pass

def validateDates(daty):
	validated = []
	long_months = [1,3,5,7,8,10,12]
	short_montths = [4,6,9,11]
	for d in daty:
		if int(d[2])%4 == 0 and not int(d[2])%100 == 0:
			if int(d[1]) in long_months:
				if int(d[0])>=1 and int(d[0])<=31:
					validated.append(d)
			elif int(d[1]) ==2:
				if int(d[0])>=1 and int(d[0])<=29:
					validated.append(d)
			else:
				if int(d[0])>=1 and int(d[0])<=30:
					validated.append(d)
		else:
			if int(d[1]) in long_months:
				if int(d[0])>=1 and int(d[0])<=31:
					validated.append(d)
			elif int(d[1]) ==2:
				if int(d[0])>=1 and int(d[0])<=28:
					validated.append(d)
			else:
				if int(d[0])>=1 and int(d[0])<=30:
					validated.append(d)
	return validated

#printDates(dates, detectDates(dates))
#printDates(in_dates, detectDates(in_dates))
#printDates(no_dates, detectDates(no_dates))
print('\n')
printDates(sentences, detectDates(sentences))
printDates2(validateDates(detectDates(sentences)))