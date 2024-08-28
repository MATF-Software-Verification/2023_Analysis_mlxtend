# Profajliranje koda korišćenjem `cProfile` alata

## cProfile

`cProfile` je ugrađeni alat u Python-u za profajliranje, koji omogućava detaljnu analizu performansi koda. Profajliranje je proces merenja vremenskih performansi različitih delova programa, što pomaže u identifikaciji uskih grla i optimizaciji koda. Detaljnije informacije o ovom alatu, kao i njegovoj primeni na izabranim delovima projekta `mlxtend`, možete pročitati u izveštaju [`ProjectAnalysisReport.md`](../ProjectAnalysisReport.md).

## Instalacija alata

*Pročitati preporuke za instalaciju i korišćenje alata za kreiranje izolovanih okruženja u glavnom [README.md](../README.md#preporuka-za-instalaciju-alata) dokumentu.*

`cProfile` je već ugrađen u *Python*, tako da nije potrebna dodatna instalacija. Može se direktno koristiti iz komandne linije ili unutar *Python* skripti.

## Korišćenje alata

Nakon podešavanja skripti za treniranje modela, `cProfile` se može koristiti za profajliranje koda. U ovom slučaju, skripte treniraju modele za logističku regresiju, perceptron i višeslojni perceptron. Primer pokretanja `cProfile` alata za treniranje jednog od modela:

```bash
python -m cProfile -o cProfile/profiles/output_file.prof profiling_scripts/script_name.py
```

`output_file.prof` će sadržati rezultate profajliranja, koje zatim možete analizirati pomoću alata `snakeviz` da se ne bi analiziralo u komandnoj liniji.

## Vizualizacija rezultata profajliranja sa `snakeviz`

`snakeviz` je alat koji omogućava vizualizaciju rezultata dobijenih profajliranjem, što olakšava interpretaciju i analizu uskih grla u kodu.

### Instalacija alata `snakeviz`

*Pročitati preporuke za instalaciju i korišćenje alata za kreiranje izolovanih okruženja u glavnom [README.md](../README.md#preporuka-za-instalaciju-alata) dokumentu.*

```bash
pip install snakeviz
```

### Korišćenje alata `snakeviz`

Nakon što je profajliranje izvršeno i generisan je `.prof` fajl, `snakeviz` se koristi za vizualizaciju rezultata:

```bash
snakeviz output_file.prof
```

Ova komanda otvara interaktivni prikaz u pregledaču, gde se mogu istraživati različiti aspekti performansi koda, identifikovati delovi koji najviše opterećuju sistem i koji možda mogu biti optimizovani.

## Profili

Profajliranje je izvršeno na skriptama koje treniraju različite modele mašinskog učenja u okviru `mlxtend` biblioteke. Izabran je veliki broj epoha, kako bi se osiguralo da izvršavanje traje dovoljno dugo za značajnu analizu. Primarni cilj nije bio razvoj optimalnih modela, već analiza performansi koda. Rezultati profajliranja se nalaze u folderu [profiles](profiles/). Uz gore opisani postupak, oni se mogu vizualizovati korišćenjem alata `snakeviz`.
