# 2023 Analiza `mlxtend` biblioteke

Ovaj repozitorijum namenjen je za izradu samostalnog praktičnog seminarskog rada u okviru kursa Verifikacija softvera na master studijama Matematičkog fakulteta u Beogradu. Cilj rada je analizirati i verifikovati softverski projekat otvorenog koda, sa fokusom na identifikaciju potencijalnih grešaka i eventualno poboljšanje performansi koda.

**Autor:** Mladen Canović 1098/2020

## Opis projekta mlxtend
`mlxtend` (Machine Learning Library Extensions) je *Python* biblioteka koja pruža korisne alate za svakodnevne zadatke u oblasti *Data Science*-a. Ova biblioteka uključuje alate za izbor atributa, klasifikaciju, regresiju, obradu podataka, evaluaciju modela i vizualizaciju. Razvija se kako bi proširila mogućnosti postojećih biblioteka za mašinsko učenje, poput [scikit-learn](https://scikit-learn.org)-a i sličnih. `mlxtend` nudi jednostavan i lako proširiv skup alata koji mogu olakšati rad kako istraživačima tako i ljudima u industriji.

### Autor biblioteke

`mlxtend` biblioteku je kreirao i održava **Sebastian Raschka**, profesor statistike na Univerzitetu Wisconsin-Madison i autor nekoliko izuzetno dobro prihvaćenih knjiga o mašinskom učenju, uključujući "[Machine Learning with PyTorch and Scikit-Learn](https://www.amazon.com/Machine-Learning-PyTorch-Scikit-Learn-learning-ebook/dp/B09NW48MR1)" i "[Build a Large Language Model (From Scratch)](https://www.manning.com/books/build-a-large-language-model-from-scratch)" (trenutno u izradi, poglavlje po poglavlje). Raschka je prepoznat kao jedan od uticajnijih stručnjaka u oblasti *data science*-a i mašinskog učenja.

Više informacija o `mlxtend` biblioteci možete pronaći na [zvaničnoj GitHub stranici projekta](https://github.com/rasbt/mlxtend).

## Sadržaj projekta

Analiza je vršena nad `main` granom projekta [mlxtend](https://github.com/rasbt/mlxtend) ([commit SHA](https://github.com/rasbt/mlxtend/tree/d9713eaa9fcc466dd9b4a999962eb57a061ab746)). 

- [`ProjectAnalysisReport.md`](ProjectAnalysisReport.md) - Detaljan izveštaj o analizi projekta i zaključci.

Korišćeni su sledeći alati:
- [`pytest`](pytest/README.md)
    - Jedinično testiranje
    - Integraciono testiranje
    - [`coverage.py`](pytest/README.md#praćenje-pokrivenosti) je korišćen za praćenje pokrivenosti koda
- [`pylint`](pylint/README.md)
    - Statička analiza kvaliteta koda
- [`cProfile`](cProfile/README.md)
    - Prvi alat korišćen za profajliranje
    - [`SnakeViz`](ProjectAnalysisReport.md#cprofile--snakeviz) je alat koji je korišćen za vizualizaciju
- [`py-spy`](py-spy/README.md) je takođe korišćen za profajliranje

## Preporuka za instalaciju alata

Iako je za svaki od alata dato uputstvo za instalaciju u odgovarajućem folderu, preporuka je da se prethodno kreira radno okruženje korišćenjem alata `pipenv` (postoje i drugi alati za kreiranje i upravljanje izolovanim okruženjima, ali u ovom projektu korišćen je `pipenv`), kako se ne bi zagadilo globalno *Python*, odnosno `pip` okruženje. Dakle, pokretanjem sledećeg niza komandi se ostvaruje kreiranje preporučenog radnog okruženja (podrazumeva se da je na samom sistemu instaliran alat `pipenv` i odgovarajuća verzija *Python*-a).

```bash
pipenv install --python 3.11 (inicijalizacija okruženja)
pipenv shell (aktiviranje okruženja)
pip install -r requirements.txt (instalacija svih potrebnih paketa)
```

Tokom razvoja projekta, biblioteka `mlxtend` je instalirana sa opcijom `-e`, kako bi se promene te biblioteke odmah registrovale u sistemu što umnogome olakšava rad:

```bash
pip install -e mlxtend
```