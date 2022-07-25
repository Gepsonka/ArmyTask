# Telepítés

## Linux (Debian alapú)

 - Telepítse a Python 3.10-es verzióját
 - Telepítse a pip csomagkezelőt
 - Telepítse a virtualenv csomagot a ``` 
  python3 -m pip install virtualenv``` paranccsal.
 - Colneozza a https://github.com/Gepsonka/ArmyTask.git repot. (vagy szimplán csomagolja ki a fájlt amit kapott az emailben)
 - Futtassa az install.sh scriptet és kövesse az instrukciókat
 
```Ha esetlen nem futnának le a migrationök akkor törölje a migration fileokat a projektmappák migrations mappáiból (minden fájl a migrations mappákban az __init__.py fileokon kívül)```

Sikeres telepítés után futassa a szervert a runserver.sh script segítségével


## Windows

 - Telepítse a python 3.10-es verzióját
 - Colneozza a https://github.com/Gepsonka/ArmyTask.git repot. (vagy szimplán csomagolja ki a fájlt, amit küldtem az emailben)

 Tepelpítse a virtualenv csomagot a (OPCIONÁLIS)

  ```bash
  python3 -m pip install virtualenv
  ``` 
  vagy a
  
  ```bash
  python -m pip install virtualenv
  ``` 
 paranccsal.


 Hozzon létre egy python virtuális környezetet (OPCIONÁLIS):

 ```bash
 python3 -m venv <környezet_neve>
 ```

 vagy a 

 ```bash
 python -m venv <környezet_neve>
 ```
 parancsokkal.

 Aktiválja a környezetet:

 ```bash
 <környezet_neve>/Scripts/activate
 ```

 Telepítse a függőségeket:

 ```bash
 python3 -m pip install -r requirements.txt
 ```

 Hozzon létre egy .env fájlt a CarDatabase mappába (nem abba, ahol a settings.py van), ahova bemásolja a következőt:

 ```
 DJANGO_SECRET=q_l$q-x@bea68#zogx=wmsr7ix(7rs@@vqmb+@ks&ur7b&((ob 
 ```
(A https://djecrety.ir/ oldalon tud generálni másik secretet)

 Futtassa le az adatbázis migrációkat:

 ```bash
 python3 CarDatabase/manage.py makemigrations
 ```

 ```bash
 python3 CarDatabase/manage.py migrate
 ```

Hozzon létre admin felhasználót:

 ```bash
 python3 CarDatabase/manage.py createsuperuser
 ```

és kövesse az instrukciókat.


Amint ezeket a lépéseket elvégezte futtassa a szervert

 ```bash
  python3 CarDatabase/manage.py runserver <port>
 ```

 (Alapértelmezett port: 8000)

 READY TO USE


# MacOS

 Mivel nem rendelkezek olyan eszközzel, ami MacOS-t futtat, nem tudok útmutatást adni a telepítéshez. 