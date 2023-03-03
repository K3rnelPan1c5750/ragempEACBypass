import os
import psutil
from shutil import rmtree
import time

os.system("mode con: cols=65 lines=10")
os.system("title RAGE:MP - EAC Bypass by K3rnelPan1c#5750")
def checkexerunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

 def delcert():
    os.chdir(dir)
    time.sleep(2)
    i = 0
    while i == 0:
        if os.path.exists(rf"{dir}\EasyAntiCheat\Certificates"):
            rmtree(rf"{dir}\EasyAntiCheat\Certificates")
            i = 1
        else:
            print("Certificados eliminados correctamente")
            input("Pulsa Enter para continuar...")
        
 if os.path.isfile("ragedir.txt"):
    db = open("ragedir.txt","r")
    datos = []
    with db as fname:
        ln = fname.readlines()
        for lineas in ln:
            datos.append(lineas.strip('\n'))
    dir = datos[1]
else:
    db = open("ragedir.txt","w")
    print("="*18, "Creado por K3rnelPan1c#5750", "="*18);
    dir = str(input("Introduce la ruta de RAGEMP: "))
    db.write("DON'T DELETE THIS FILE\n")
    db.write (dir)
    db.close()
    print (f"Directorio de RAGEMP asignado: {dir}")
    time.sleep(3)

if checkexerunning('ragemp_v'):
    os.system("cls")
    print("="*18, "Creado por K3rnelPan1c#5750", "="*18);
    print("- RAGE:MP en ejecucion.")
    print("-- Eliminando certificados de EasyAntiCheat...")
    if os.path.exists(rf"{dir}\EasyAntiCheat\Certificates"):
        rmtree(rf"{dir}\EasyAntiCheat\Certificates")
        print("Los certificados fueron eliminados.")
        input("Pulsa 'Enter' para continuar.")
    else:
        print("Los certificados ya estan eliminados.\n")
        input("Pulsa 'Enter' para continuar.")
else:
    os.system("cls")
    print("="*18, "Creado por K3rnelPan1c#5750", "="*18);
    print ("Ejecutando RAGE:MP")
    os.chdir(dir)
    time.sleep(2)
    os.system(rf'"{dir}\ragemp_v.exe"')
    time.sleep(5)
    t = 0
    while t == 0:
        if checkexerunning('ragemp_v'):
            print("- RAGE:MP en ejecucion")
            print("-- Eliminando certificados de EasyAntiCheat...")
            delcert()
            t=1