# O sajtu

**granice.udobakorone.live** skenira podatke direktno sa vladinog sajta i prikazuje ih u uređenoj tabeli.

## Kako doprineti projektu

Projekat koristi **Scrapy** za skrejpovanje i **Svelte** za frontend.

---
### Da radiš na frontendu:


```
cd foolder_root
npm install
npm run dev
```

Otvori **localhost:5000** u brauzeru.


---
### Da radiš na skeniranju informacija i generisanju .csv i .json fajla:

1. Ako nemaš instaliran pipenv `pip install pipenv`
2. `cd folder_root/scraper/`
3. `pipenv install && pipenv shell`
4. `cd granice/`
5. Otvori u svom omiljenom editoru i lociiraj spider u `granice/spiders/zemlje.py`, uglavnom je sav kod tu.
6. Da pokreneš spider i smestiš fajl u svelte static folder uradi ovu komandu 

```
rm -rf ../../src/static/data/zemlje.json && scrapy crawl zemlje -t json -o ../../src/static/data/zemlje.json
```
7. Ako ti treba i csv fajl pokreni ovu komandu
```
scrapy crawl zemlje -t csv -o ../../src/static/data/zemlje.csv
```

Fajlovi sa podacima se nalaze u 
```
folder_root/src/static/data/zemlje.csv
```