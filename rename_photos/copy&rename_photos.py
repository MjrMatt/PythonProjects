import os, shutil, re

show_logs = True
indir = 'todo'
outdir= 'renamed'
pattern = r'(?:[\w]*\d\d)(\d{2})(\d{2})(\d{2})(?:[\w]*)(\.[\w\d]{3,4})'
dates = {}

if os.path.isdir(outdir):
    print('WARNING: Folder '+outdir+' już istnieje!\n' if show_logs else '', end='')
    print('LOG: Usuwam folder '+outdir+' wraz z zawartością\n' if show_logs else '', end='')
    shutil.rmtree(outdir)
print('LOG: Tworzę pusty folder '+outdir+'\n' if show_logs else '', end='')
os.mkdir(outdir)

print('LOG: Sprawdzam istnienie folderu '+indir+'... ' if show_logs else '', end='')
try:
    if not os.path.isdir(indir):
        print('\nERROR: Folder '+indir+' nie istnieje!\n' if show_logs else '', end='')
        raise RuntimeError('Input data does not exist!')
except RuntimeError:
    print('Należy utworzyć folder o nazwie \''+indir+'\' i umieścić w nim dane wejściowe (zdjęcia), a następnie uruchomić skrypt ponownie.')
    quit('Wrong input!')
print('OK!\n' if show_logs else '', end='')

print('LOG: Odczytuję pliki z folderu '+indir+'\n' if show_logs else '', end='')
files = os.scandir(r'ToDo')
for file in files:
    if file.is_file():
        print('LOG: Znaleziono plik '+file.name+'\n' if show_logs else '', end='')
        m = re.match(pattern, file.name)
        if not m==None:
            date=m.group(1)+'-'+m.group(2)+'-'+m.group(3)
            if date not in dates:
                num = 1
                dates[date] = '1'
            else:
                num = int(dates[date])+1
                dates[date] = str(num)
            newname = date+'_'+f'{num:02d}'+m.group(4)
            print('LOG: Proponowana nowa nazwa to '+newname+'\n' if show_logs else '', end='')
        else:
            print('WARNING: Nie odnaleziono daty w nazwie pliku: ' + file.name)
            newname = 'ACTION NEEDED ' + file.name

        print('LOG: Kopiuję plik do folderu '+outdir+'\n'if show_logs else '', end='')
        shutil.copy2(r'./'+indir+'/'+file.name, r'./'+outdir)
        print('LOG: Nadaję mu nazwę '+newname+'\n'if show_logs else '', end='')
        os.rename(r'./'+outdir+'/'+file.name, r'./'+outdir+'/'+newname)

print('Zakończono kopiowanie plików sukcesem!')


