"""modulo per leggere metadati da immagine"""

# librerie
from exif import Image  #libreria python per lettura metadati immagini
import os
import shutil
import time

# settaggio variabili
listOfImage = 0
listOfScanned = 0
counter = 1

# scansione cartelle per verificare presenza file

scanned_path = os.chdir("C:/Users/met/Documents/PYTHON/DeskApp/src/util/scannedfolder/") # cartella dove vengono spostante le immagini lette
listOfScanned = os.listdir(scanned_path)    # legge tutte le immagini presenti
print("Verifico presenza foto nelle cartelle.")
print("Scansione in corso", end="")
time.sleep(1)
print(".", end="")
time.sleep(1)
print(".", end="")
time.sleep(1)
print(".")
time.sleep(1)
totalScanned = len(listOfScanned)      # numero di foto presenti nella cartella
if totalScanned == 0:
    print("Non sono presenti foto nella cartella dei file analizzati")
elif totalScanned == 1:
    print("E' presente 1 foto nella cartella dei file analizzati")
    counter = totalScanned + 1
else:
    print("Sono presenti", totalScanned, "foto nella cartella dei file analizzati." )
    counter = totalScanned + 1

image_path = os.chdir("C:/Users/met/Documents/PYTHON/DeskApp/src/util/imagefolder")  # posizionarsi nella cartella dove inserire immagini da leggere
listOfImage = os.listdir(image_path)    # legge tutte le immagini presenti
totalImage = len(listOfImage)     # numero di foto presenti nella cartella
if totalImage == 0:
    print("Non sono presenti foto nella cartella dei file da analizzare; attendo inserimento file.")
elif totalImage == 1:
    print("E' presente 1 foto nella cartella dei file da analizzare")
    time.sleep(1)
    print("Ora procedo ad eseguire analisi\n")
    time.sleep(1)
else:
    print("Sono presenti", totalImage, "foto nella cartella dei file da analizzare." )
    time.sleep(1)
    print("Ora procedo ad eseguire analisi\n")
    time.sleep(1)

f = open("C:/Users/met/Documents/PYTHON/DeskApp/src/util/doc/Database.txt", 'w')  # apri file txt per salvare tutti i dati estratti

for name in listOfImage:
    # standardizzazione/rinomina foto, copia la foto nella cartella scannedfolder e cancella foto nella cartella imagefolder
    x = str("image" + str(counter) + ".jpg")
    os.rename(name, x)
    print("Original name: ", name)
    print("Deskapp name: ", x)
    shutil.copy("C:/Users/met/Documents/PYTHON/DeskApp/src/util/imagefolder/" + x, "C:/Users/met/Documents/PYTHON/DeskApp/src/util/scannedfolder/")
    os.remove("C:/Users/met/Documents/PYTHON/DeskApp/src/util/imagefolder/" + x)

    os.chdir("C:/Users/met/Documents/PYTHON/DeskApp/src/util/scannedfolder") # cartella dove vengono spostante le immagini lette


    with open(x, 'rb') as img_file:
        img = Image(img_file)

    # print(img.has_exif)

    # List all EXIF tags contained in the image
    sorted(img.list_all())


    f.write(f'Original name: {name}\n')
    f.write(f'Deskapp name: {x}\n')

    # Make of device which captured image
    print(f'Make: {img.get("make")}')
    f.write(f'Make: {img.get("make")}\n')

    # Model of device which captured image
    print(f'Model: {img.get("model")}')
    f.write(f'Model: {img.get("model")}\n')

    # Software involved in uploading and digitizing image
    print(f'Software: {img.get("software")}')
    f.write(f'Software: {img.get("software")}\n')

    # Name of photographer who took the image
    print(f'Artist: {img.get("artist")}')
    f.write(f'Artist: {img.get("artist")}\n')

    # Original datetime that image was taken (photographed)
    print(f'DateTime (Original): {img.get("datetime_original")}')
    f.write(f'DateTime (Original): {img.get("datetime_original")}\n')

    # Details of flash function
    print(f'Flash Details: {img.get("flash")}')
    f.write(f'Flash Details: {img.get("flash")}\n')

    # getting the Longitude and latitude data
    print(f' Longitude data: {img.get("gps_longitude")}')
    print(f' latitude data: {img.get("gps_latitude")}')
    f.write(f' Longitude data: {img.get("gps_longitude")}\n')
    f.write(f' latitude data: {img.get("gps_latitude")}\n')

    # getting the Longitude  and latitude Reference data is also very important when converting the Decimal degrees formen
    print(f' Longitude data reference : {img.get("gps_longitude_ref")}')
    print(f' latitude data reference : {img.get("gps_latitude_ref")}')
    f.write(f' Longitude data reference : {img.get("gps_longitude_ref")}\n')
    f.write(f' latitude data reference : {img.get("gps_latitude_ref")}\n')

    # Larghezza
    print(f'Larghezza: {img.get("pixel_x_dimension")}')
    f.write(f'Larghezza: {img.get("pixel_x_dimension")}\n')

    # altezza
    print(f'Altezza: {img.get("pixel_y_dimension")}')
    f.write(f'Altezza: {img.get("pixel_y_dimension")}\n')

    # risoluzione
    print(f'Risoluzione: {img.get("x_resolution")}')
    f.write(f'Risoluzione: {img.get("x_resolution")}\n')

    print(f'Dimensione file (in byte): {os.path.getsize(x)}\n')
    f.write(f'Dimensione file (in byte): {os.path.getsize(x)}\n\n')



    counter = counter + 1

    os.chdir("C:/Users/met/Documents/PYTHON/DeskApp/src/util/imagefolder/")  # posizionarsi nella cartella dove inserire immagini da leggere


f.close()
