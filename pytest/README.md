# Testiranje koda korišćenjem Pytest alata

## Pytest

`Pytest` je popularan alat za testiranje koda napisanog u programskom jeziku *Python*. Omogućava jednostavno pisanje i izvršavanje testova, kao i generisanje detaljnih izveštaja o rezultatima testiranja. Detaljnije informacije o ovom alatu i njegovoj upotrebi u testiranju izabranih delova projekta `mlxtend` se mogu pročitati u izveštaju [`ProjectAnalysisReport.md`](../ProjectAnalysisReport.md).

## Instalacija alata

*Pročitati preporuke za instalaciju i korišćenje alata za kreiranje izolovanih okruženja u glavnom [README.md](../README.md#preporuka-za-instalaciju-alata) dokumentu.*

Da bi se omogućilo korišćenje ovog alata jednostavno je potrebno instalirati ga na sledeći način:

```bash
pip install pytest
```

## Korišćenje alata

Nakon instalacije, `pytest` se može pokrenuti u komandnoj liniji kako bi izvršio sve napisane testove na sledeći način:

```bash
pytest pytest/unit_tests/tests pytest/integration_tests/tests
```

Rezultati testiranja prikazuju koje su funkcionalnosti ispravno implementirane, a koji testovi nisu prošli, odnosno da li je došlo do greške ili nas sistem samo upozorava na potencijalne probleme na šta je takođe neophodno obratiti pažnju zarad podizanja kvaliteta, ali i sigurnosti koda. 

## Praćenje pokrivenosti

Da bi testovi u potpunosti imali smisla potrebno je pratiti i koje delove koda oni pokrivaju, odnosno koliki procenat koda je pokriven testovima. Alat koji je korišćen za praćenje pokrivenosti je `coverage.py`. Uzimajući u obzir obim projekta, nije se pristupilo testiranju celokupnog projekta već je odabrano nekoliko funkcionalnosti. Detaljnije o pokrivenosti koda se takođe može pročitati u glavnom izveštaju [`ProjectAnalysisReport.md`](../ProjectAnalysisReport.md).

### Instalacija alata `coverage.py`

*Pročitati preporuke za instalaciju i korišćenje alata za kreiranje izolovanih okruženja u glavnom [README.md](../README.md#preporuka-za-instalaciju-alata) dokumentu.*

```bash
pip install coverage
```

### Korišćenje alata `coverage.py`

Nakon instalacije, `coverage.py` se može pokrenuti u komandnoj liniji. Ovaj alat se koristi u kombinaciji sa alatom `pytest`, odnosno pokreće se izvršavanje testova tokom čijeg izvršavanja se prati pokrivenost. Potrebno je pokrenuti analizu, a zatim narednom komandom generisati izveštaj u čitljivijem, `html` formatu, umesto korišćenja standardnog izlaza:

```bash
coverage run -m pytest pytest/unit_tests/tests/ pytest/integration_tests/tests/
coverage html
```

Oba izveštaja o pokrivenosti koda se nalaze u direktorijumu [coverage_reports](coverage_reports/). Ova analiza pokrenuta je pre i posle ispravki te se rezultat za svaku od ovih analiza nalazi u odgovarajućem folderu.
