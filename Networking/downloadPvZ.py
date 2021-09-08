# Enlace de: https://www.mediafire.com/file/8yxaysu9eqo3dsr/Plantas_vs._Zombies_por_JimmyTutoriales.rar/file
import urllib.request

game = urllib.request.urlopen("https://download1493.mediafire.com/kbq70sprzmgg/8yxaysu9eqo3dsr/Plantas+vs.+Zombies+por+JimmyTutoriales.rar")
# Aunque lo malo es que los enlaces de mediafire son temporales

size = 0

with open("Networking/PvZ.rar","ab") as file:
    while True:
        info = game.read(500000)
        if len(info)<1: break
        size += len(info)
        file.write(info)
        print("Se han descargado {0:.2f} MB".format(size/1000000))

print("Archivo descargado y guardado con exito")

# La descarga fue exitosa :D
"""
·Salida:

Se han descargado 0.50 MB
Se han descargado 1.00 MB
Se han descargado 1.50 MB
Se han descargado 2.00 MB
Se han descargado 2.50 MB
Se han descargado 3.00 MB
Se han descargado 3.50 MB
Se han descargado 4.00 MB
Se han descargado 4.50 MB
Se han descargado 5.00 MB
Se han descargado 5.50 MB
Se han descargado 6.00 MB
Se han descargado 6.50 MB
Se han descargado 7.00 MB
Se han descargado 7.50 MB
Se han descargado 8.00 MB
Se han descargado 8.50 MB
Se han descargado 9.00 MB
Se han descargado 9.50 MB
Se han descargado 10.00 MB
Se han descargado 10.50 MB
Se han descargado 11.00 MB
Se han descargado 11.50 MB
Se han descargado 12.00 MB
Se han descargado 12.50 MB
Se han descargado 13.00 MB
Se han descargado 13.50 MB
Se han descargado 14.00 MB
Se han descargado 14.50 MB
Se han descargado 15.00 MB
Se han descargado 15.50 MB
Se han descargado 16.00 MB
Se han descargado 16.50 MB
Se han descargado 17.00 MB
Se han descargado 17.50 MB
Se han descargado 18.00 MB
Se han descargado 18.50 MB
Se han descargado 19.00 MB
Se han descargado 19.50 MB
Se han descargado 20.00 MB
Se han descargado 20.50 MB
Se han descargado 21.00 MB
Se han descargado 21.50 MB
Se han descargado 22.00 MB
Se han descargado 22.50 MB
Se han descargado 23.00 MB
Se han descargado 23.50 MB
Se han descargado 24.00 MB
Se han descargado 24.50 MB
Se han descargado 25.00 MB
Se han descargado 25.50 MB
Se han descargado 26.00 MB
Se han descargado 26.50 MB
Se han descargado 27.00 MB
Se han descargado 27.50 MB
Se han descargado 28.00 MB
Se han descargado 28.50 MB
Se han descargado 29.00 MB
Se han descargado 29.50 MB
Se han descargado 30.00 MB
Se han descargado 30.50 MB
Se han descargado 31.00 MB
Se han descargado 31.50 MB
Se han descargado 32.00 MB
Se han descargado 32.50 MB
Se han descargado 33.00 MB
Se han descargado 33.50 MB
Se han descargado 34.00 MB
Se han descargado 34.50 MB
Se han descargado 35.00 MB
Se han descargado 35.50 MB
Se han descargado 36.00 MB
Se han descargado 36.43 MB
Archivo descargado y guardado con exito
"""