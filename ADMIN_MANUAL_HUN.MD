# Admin útmutató


## Bejelentkezés

Az adminoknak külön bejelentkezési lehetősége van, ezt a navbarban az Admin login gombbal lehet elérni. Itt jelszó és felhasználónév megadásával tud belépni.


## Használat

Bejelentkezés után két fül van a navbarban az Admin Sites és a Car, amiknek linkkén keresztül tud elérni olyan oldalakat, amiken keresztül tud változásokat eszközölni a szerveren

## Admin

### Felhasználó lista

Az Admin Sites dropdownból lenyíló első fül a 'Users' gomb, ami az admint egy felhasználókat listázó oldalra visz el. Itt egy tábla gondoskodik a felhasználók megfelelő megjelenítéséről.

Sorok színkódjai:
 - Kék: A felhasználó admin
 - Fehér: Általános user
 - Sárga: Általános user aki feloldást kért account zárolást követően
 - Piros: Általános felhasználó, aki a fiókja törlését kérte

A delete account oszlopban megjelent gombokra kattintva törölhető a felhasználó.

Az Admin oszlpba megjelenő gombbal tud az admin admin jogot adni vagy elvenni.

Az update account gombbal fedig frissíteni tudja a felhasználó adatait.

A tábla felett balra lévő gombra kattintva tud az admin új felhasználót kreálni.

```
Az adminnak szabadkezet adtam a felhasználó adatait illetően, bármilyen felhasználónevet adhat (ami nem létezik), bármilyen összetételű és hosszúságú jelszóval egy új/frissített felhasználónak.
```

### Gyártók listája

A 'Car manufacturers' lenyíló gombból lehet elérni.

Kilistázza az gyártók nevét, A piros gombbal lehet törölni az összes relációjával együtt.

A tábla felett lévő zöld gombbal lehet hozzáadni gyártót az adatbázishoz.


### Gyártó hozzáadási kérések

A 'Car manufacturers request' lenyíló gombból lehet elérni.


Az első oszlop a kért gyártók nevét tartalmazza.

Elfogadni a kérést az Accept requesst gombbal lehet.

- Ha az gyártó már fel van véve az adatbázisba, akkor szimplán törli a kérést
- Ha nem létezik még a gyártó az adatbázisban, akkor csak hozzáadja a gyártót a kérésben megfogalmazott névvel, és törli a kérést

A kérés törlését a 'Delete request' gombbal lehet törölni

A tábla felett lévő 'Accept all requests' és 'Delete all requests' gombokkal lehet teljesíteni vagy törölni az összes kérést.

### Gyártó törlési kérelmek

 ``` 
 "ha valamilyen autó márka nincs, akkor valamilyen módszerrel képes értesíteni az admin-t, hogy az vegyen fel új márkát (5 pont)
 (a törlés és ez a funkció lehet ugyanazon a logikán alapulva)"
```

A feladat ezt a részét úgy értelmeztem, hogy gyártó törlését is kezdeményezhet a felhasználó


Ezen az oldalon lehet a gyártó törlési kéréseket teljesíteni, vagy elutasítani. Elfogadni a 'Fulfill request' gombbal, elutasítani a 'Delete request' gombbal lehet.

### Fiók feloldási kérelmek

Kérelmek a zárolt fiókok feloldására.

A 'Account unlock requests' lenyíló gombból lehet elérni.

Zöld gomb oldja fel a felhasználó fiókját.

Az 'Unlock all' gomb feloldja az összeset.


### Fiók törlési kérelmek

A 'Account delete requests' lenyíló gombból lehet elérni.

A piros 'X' gombbal lehet törölni a felhasználót.

A 'Delete all' törli az összes fiókot, ahol kérve van a törlés.


Ezeken kívül az összes többi felhasználói funkció elérhető az adminok számára, kivéve

- Fiók törlési kérelem
- Új gyártói kérelem
- Gyártó törlési kérelem
  

  