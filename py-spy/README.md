# Profajliranje koda korišćenjem `py-spy` alata

## py-spy

`py-spy` je alat za profajliranje koji omogućava snimanje i analizu performansi Python aplikacija u realnom vremenu. Jedna od ključnih prednosti `py-spy` alata je mogućnost profajliranja aplikacija koje su već u toku izvršavanja, što omogućava lakše otkrivanje uskih grla i performansnih problema u produkcionim okruženjima. 

Na primer, tokom treniranja modela mašinskog učenja, py-spy može pomoći da se identifikuju delovi koda koji najviše troše resurse, omogućavajući optimizaciju procesa treniranja. Ovo je posebno korisno kada je potrebno optimizovati trening na velikim skupovima podataka.

Detaljnije informacije o ovom alatu, kao i njegovoj primeni na izabranim delovima projekta `mlxtend`, možete pročitati u izveštaju [`ProjectAnalysisReport.md`](../ProjectAnalysisReport.md).

## Instalacija alata

*Pročitati preporuke za instalaciju i korišćenje alata za kreiranje izolovanih okruženja u glavnom [README.md](../README.md#preporuka-za-instalaciju-alata) dokumentu.*

Instalacija `py-spy` alata može se izvršiti korišćenjem `pip` paketa:

```bash
pip install py-spy
```

## Korišćenje alata

`py-spy` se može koristiti za profajliranje Python procesa direktno iz komandne linije. Ovaj alat podržava snimanje *call stack*-a i generisanje ***flame graph***-ova, što omogućava vizuelnu analizu performansi. Primer pokretanja `py-spy` alata za praćenje performansi skripte, nakon pokretanja skripte za treniranje u drugom terminalu:

```bash
py-spy top --pid $(pgrep -f path/to/training_script.py)
```

Može se desiti da postoje određeni problemi s pravima pristupa, pa je neophodno pokretanje na sledeći način:

```bash
sudo $(which py-spy) top --pid $(pgrep -f path/to/training_script.py)
```

Ova komanda će prikazati interaktivni prikaz u terminalu sa informacijama o potrošnji *CPU*-a po funkcijama. Da bi se generisao *flame graph* za dublju analizu, može se koristiti sledeća komanda, sa konkretnim primerom za trening *MLP* modela:

```bash
py-spy record -o py-spy/flame_graphs/output_file.svg --pid $(pgrep -f profiling_scripts/train_mlp.py)
```

Opet, može se desiti da postoje određeni problemi s pravima pristupa, pa je neophodno pokretanje na sledeći način:

```bash
sudo $(which py-spy) record -o py-spy/flame_graphs/output_file.svg --pid $(pgrep -f profiling_scripts/train_mlp.py)
```

## Profili

Profajliranje je izvršeno na skriptama koje treniraju različite modele mašinskog učenja u okviru `mlxtend` biblioteke. Rezultati profajliranja u vidu *flame graph*-ova nalaze se u folderu [flame_graphs](flame_graphs/)..
