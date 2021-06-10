import random
from scipy.stats import shapiro

color=['black','black','black','Niebieskie','Zielone','Czerwone']
tura=0
barbarian =0
barbarian_limit=8
zliczanko={'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0}

#definiowalne
gracze=['Milena','Monia','Miki','Mati']

def zeruj(co):
	for c in co:
		co[c]=0
		
def drukuj(co, zera):
	mask='{:>'+str(zera+1)+'}'
	macierz=[]
	for i, z in enumerate(co):
		macierz.append(co[z])
	stats, p = shapiro(macierz)
	for x in range(2, 13):
		print(mask.format(str(x)), end=',')
	print('\n')
	for z in co:
		print(mask.format(str(co[z])), end=',')
	print('\n')
	if(p>0.05):
		print('Rozkład jest normalny! p: '+str(p)+', stats: '+str(stats))
	else:
		print('Rozkład nie jest normalny! Porażka...😢'+' Parametr p wynosi jedynie '+str(p))

def test(times):
	while(times>0):
		a=random.randint(1,6)
		b=random.randint(1,6)
		suma=a+b
		zliczanko[str(suma)]+=1
		times-=1
	drukuj(zliczanko, 4)
	zeruj(zliczanko)
	
def poczatek():
	start=random.randint(0,3)
	zaczyna=gracze[start]
	kolejno=list(gracze[start:]+gracze[:start])
	print('INSTRUKCJA: Naciskaj Enter aby kontynuować. \nWpisanie \'e\' i zatwierdzenie Enterem spowoduje wyjście z aplikacji.\nWpisanie \'s\' w dowolnej turze wyświetla statystyki rzutów.')
	print('\nCzy chcesz przetestować pseudolosowość tego urządzenia? [t/n] :')
	key=input()
	if(key=='t'):
		print('Podaj próbkę (liczbę rzutów) :')
		test(int(input()))
	print('\n\nGrę rozpocznie '+zaczyna+'!\n\n')
	for g in kolejno:
	   print(g+', ustaw na planszy osadę oraz drogę.')
	   if (input()=='e'):
	   	break
	for g in kolejno[::-1]:
		print(g+', ustaw na planszy miasto, drogę i pobierz zasoby.')
		if (input()=='e'):
		   break
	print('\nRozpoczynajmy grę!\n\n')	
	return(kolejno)

def nextround(nowi, tura, barbarian):
	print('Tura '+str(tura+1)+': Rzuca '+nowi[tura%4]+'\n')
	znaczaca=random.randint(1,6)
	zwykla=random.randint(1,6)
	kolorowa=color[random.randint(0,4)]
	suma=zwykla+znaczaca
	zliczanko[str(suma)]+=1
	if (kolorowa=='black'):
		barbarian+=1
		gdzie=barbarian%barbarian_limit
		if (gdzie==0):
			print('Następuje najazd BARBARZYŃCÓW!')
		else:
			print('Barbarzyńcy przybliżają się i zaatakują za '+str(barbarian_limit-gdzie)+' ruchów.')
	else:
		print(kolorowa+ ' '+str(znaczaca)+'! Pobierzcie karty ROZWOJU!')
	if(suma==7 and barbarian>=barbarian_limit):
		print('Wypadło 7! '+nowi[tura%4]+', przestaw ZŁODZIEJA! Sprawdźcie LIMIT kart!')
	elif(suma==7):
		print('Wypadło 7. Złodziej nieaktywny. Sprawdźcie LIMIT kart!')
	else:
		print('Pobierzcie zasoby z '+str(suma)+'.')
	return(barbarian)
		  	
kolejno=poczatek()
while(True):
	barbarian=nextround(kolejno,tura, barbarian)
	tura+=1
	key=input()
	if (key=='e'):
		break
	elif(key=='s'):
		drukuj(zliczanko, 2)