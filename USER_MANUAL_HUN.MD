# Felhasználói útmutató


Majdnem minden oldal az 'Actions' fülből lenyíló  

## Reigsztráció

A felhasználó a nabbarban lévő 'Register' gombbal tud átnavigálni a regisztrációs oldalra, ahol a form kitöltésével tud regisztrálni.

a felhasználónévnek legalább 8, legfeljebb 16 karakternek kell lennie.

## Bejelentkezés

A 'Login' gombra kattintva tud átnavigálni a bejelentkezéshez, Ahol a felhasználónév és jelszó megadásával tud bejelentkezni (admin itt nem tud bejelentkezni). Ha a jelszót rosszul adja meg, de a felhasználónév helyes akkor tajékoztatja a felhasználót hány lehetősége maradt, 5 rossz jelszó után zárolja a fiókot a rendszer. Ha nem létező felhasználónevet ad meg, akkor csak kiírja, hogy "Unsuccessful login".

Fiók feloldását a navbarban lévő 'Request unlock gomb' megnyomása után lehet kérni, a felhasználónév megadásával.


Bejelentkezés után az 'Actions' fülből lehet minden lényeges oldalt elérni.

## Autó adatbázis

Navbarban az 'Actions' fülből lenyíló 'Car database' gombbal lehet idenavigálni 

Itt a felhasználó a lenyíló fülbők tud filterezni, milyen gyártótól szeretne autókat listázni

A tábla 'Add to faourites' gombjával tudja hozzáadni az autót a kedvenceihez

A grombra kattintás után meg kell adni az évjáratot, színt és az üzemanyag típust. 

```Figyelem! Ha már szerepel a kedvencek között autó ugyanazzal a gyártóval, típussal és évjárattal, akkor nem fogja engedni hozzáadni, mivel úgy veszi a program, hogy az autó már a kedvencek között van.```

A másik módja új kevenc autó hozzáadásához az az 'Add favourite car' gomb megnyomásával tehető meg, ahol viszont meg kell határozni mindent (gyártó, típus, évjárat, szín, üzemanyag típus). Ha a típus nem létezik még az adatbázisban, hozzáadja azt és később látható lesz az autó adatbázisban mindenki számára.


## Kedvenc autók

Navbarban az 'Actions' fülből lenyíló 'Favourite cars' gombbal lehet idenavigálni 

Kedvenc autókat is lehet filterezni gyártó alapján.

'Add favourite car' ugyanúgy működik mint a Car database-nél

A "Remove from favourites" oszlopban lévő gombbal lehet eltávolítani az autót a kedvencek közül.


Az 'Update' gombbal lehet frissíteni a kedvenc autót, és képeket feltölteni az autóhoz.

## Úgy gyártó kérelem

Navbarban az 'Actions' fülből lenyíló 'Request new manufacturer' gombbal lehet idenavigálni.

Gyártó nevének megadásával lehet továbbítani a kérést az adminok felé

## Gyártó törlése kérelem

Navbarban az 'Actions' fülből lenyíló 'Request delete of amunfacturer' gombbal lehet idenavigálni.

A legürdölő menüből ki lehet választani a törölni kívánt gyártót és továbbítani az adminnak a kérelmet.


## Fiók törlési kérelem

Két eset:

- Fiók törlésének kérelme: értesíti az adminokat a törlési szándékról
- Fiók törlési kérelem már el van küldve: Ilyenkor a gombra kattintva törli a törlési kérelmet (fiók nem lesz törölve)
