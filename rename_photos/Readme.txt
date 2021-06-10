COPY AND RENAME - Instrukcja:
1. Utwórz folder o nazwie "todo" i umieść w nim zdjęcia, którym chcesz zmienić nazwę.
2. Umieść skrypt "copy&rename_photos.py" w folderze nadrzędnym do folderu "todo". 
3. Uruchom skrypt poprzez dwukrotne kliknięcie*
4. GOTOWE! Zdjęcia ze zmienionymi nazwami pojawią się w folderze "renamed". Jeśli skrypt nie potrafi odnaleźć daty w nazwie pliku - nada mu przedrostek "ACTION NEEDED"

RENAME - Instrukcja:
1. Utwórz folder o nazwie "todo" i umieść w nim zdjęcia, którym chcesz zmienić nazwę.
2. Umieść skrypt "rename_photos.py" w folderze nadrzędnym do folderu "todo". 
3. Uruchom skrypt poprzez dwukrotne kliknięcie*
4. GOTOWE! Zdjęcia folderze "todo" mają już zmienione nazwy. Jeśli skrypt nie potrafi odnaleźć daty w nazwie pliku - nada mu przedrostek "ACTION NEEDED"



*UWAGA! Do poprawnego działania wymagany jest interpreter Python w wersji co najmniej 3.8.

Skrypt wyszukuje daty w nazwie pliku i używa ich do nadania nowych nazw, opartych na datach - w formacie YY-MM-DD_XX, gdzie xx to numer od 01 do 99 oznaczjący kolejne zdjęcia z tego samego dnia.

Obsługiwane formaty:

- IMG_YYYYMMDD_00000.jpg
- IMG_YYYYMMDD_00000.jpeg
- VID_YYYYMMDD_00000.mp4