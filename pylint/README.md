# Analiza koda korišćenjem Pylint alata

## Pylint

`Pylint` je statički alat za analizu koda napisanog u programskom jeziku *Python*. Ovaj alat se koristi za proveru potencijalnih grešaka u kodu, za proveru ispravnosti stila pisanja, detekciju neupotrebljenog koda, optimizaciju i uopšteno, za poboljšanje kvaliteta koda. U nastavku sledi uputstvo za korišćenje, a detaljnije informacije o ovom alatu, ali i njegovoj upotrebi u analizi projekta `mlxtend` se može pročitati u izveštaju [`ProjectAnalysisReport.md`](ProjectAnalysisReport.md).

## Instalacija alata

*Pročitati preporuke za instalaciju i korišćenje alata za kreiranje izolovanih okruženja u glavnom [README.md](../README.md#preporuka-za-instalaciju-alata) dokumentu.*

Da bi se omogućilo korišćenje ovog alata jednostavno je potrebno instalirati ga na sledeći način:

```bash
pip install pylint
```

## Korišćenje alata

Prilikom korišćenja alata glavna stvar o kojoj treba voditi računa je nad kojim folderom se pokreće analiza. Pokretanje analize mlxtend biblioteke se može izvršiti na sledeći način, ukoliko je korisnik pozicioniran u korenom direktorijumu projekta `2023_Analysis_mlxtend`:

```bash
pylint mlxtend/mlxtend > pylint/reports/00_pylint_initial_report.txt
```

Ili korišćenjem *flegova*:

```bash
pylint \
    --extension-pkg-whitelist=numpy \
    mlxtend/mlxtend \
    > pylint/reports/yet_another_report.txt
```

Ovakvim pokretanjem dobićemo kompletan izveštaj, koji ukazuje na sva potencijalna upozorenja, sve stilske preporuke, ali i ono najvažnije, ukazivanje na potencijalne greške u kodu. Na kraju, dobićemo i ocenu celokupnog koda, uzimajući sve prethodno navedene parametre u obzir. Npr. inicijalnim pokretanjem dobijamo ocenu `7.1/10`.

U ovom projektu korišćeni su sledeće opcije (eng. *flags*) prilikom pokretanja:

```
--errors-only
--extension-pkg-whitelist=numpy
```

Razlozi za korišćenje tih opcija, kao i celokupan proces statičke analize i zaključci detaljnije su opisani u izveštaju [`ProjectAnalysisReport.md`](../ProjectAnalysisReport.md).

Svi generisani izveštaji čuvaju se u folderu [reports](reports/).
