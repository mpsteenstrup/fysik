# Bestemmelse af lysets bølgelængde

## Formål
Bestemmelse af lysets fra en lasers bølgelængde med optisk gitter.

## Teori
Gitterligningen giver sammenhængen mellem afstanden mellem spalterne $d$ i et gitter og bølgelængden af lyset $\lambda$, ordnen $n$, og den n'te ordens afbøjdningsvinklen $\theta_n$

$$
\sin(\theta_n) = \frac{n\cdot\lambda}{d}
$$

* Angiv enheden for $\lambda$ og $d$.
* Hvad menes der med ordnen $n$ og har den en enhed?
* Isoler bølgelængden i ligningen.


På vores gitre står der hvor mange spalter der er per mm, men vi har brug for at vide hvor langt der er mellem spalterne. Omregningen er,

$$
d = \frac{1}{\text{antal spalter per meter}}
$$

### Øvelse
Udregn $d$ når

* Der er $10$ spalter per meter.
* Der er $10$ spalter per mm.
* Det er $100$ spalter per mm.

## Materialer
Laser, Gitter, lineal

## Udførsel
Forsøget laves med minimue en farve laser, men gerne flere.

figuren viser forsøgsopstillingen hvor gitteret placeres en afstand $a$ fra en en skærm, væg, og vinklen for de forskellige ordner med konstruktiv interferens måles.

![laserdiffraktion](/billeder/diffraktion1.png)

### Måling af vinklen
Vi skal bruge vores viden om retvinklede trekanter til at måle vinklen.

![vinkelmåling](/billeder/diffraktion2.png)

Vi måler afstanden $a$ til skærmen, og afstanden $x_n$ til den n'te orden. Fra trigonometri ved vi at

$$
tan(\theta_n) = \frac{x_n}{a} .
$$

Vi kan isolere vinklen ved at bruge den inverse tangens,

$$
\theta_n = arcTan(\frac{x_n}{a})
$$

* Overvej hvordan man kan gøre målingen af vinklen så præcis som mulig.

## Måledata
Udfyld tabellen og vis ved eksempelberegning hvordan I kommer frem til bølgelængden.
|       | n=1  | n=2  | n=3  | n=4  | n=-1 | n=-2 | n=-3 | n=-4 |
|-------|------|------|------|------|------|------|------|------|
| $a$ [m] |      |      |      |      |      |      |      |      |
| $x_n$ [m] |      |      |      |      |      |      |      |      |
| $θ_n$ [grader] |      |      |      |      |      |      |      |      |
| $d$ [m] |      |      |      |      |      |      |      |      |
| $λ$ [m] |      |      |      |      |      |      |      |      |

## Databehandling
Beregn den gennemsnitlige bølgelængde og sammenlign med app, [lys og bølgelængde](https://www.mpsteenstrup.dk/spektrum/spektrum.html), [wikipedia](https://en.wikipedia.org/wiki/Laser_pointer), eller spektrometer måling

![spektrometer måling af laser bølgelængde](/billeder/laser_boelgelaengde.png)

## Udvidet databehandling
Formålet med den udvidede databehandling er at kunne estimere præcisionen og identificere fejlkiler.

* Plot $(n,\sin(\theta_n))$ ind i et koordinatsystem og lav lineær regression.

Den estimered heldningskoefficient er $a = \frac{\lambda}{d}$

* Brug resultaterne til at finde en ny værdi for bølgelængden.
* Omregn til $nm$ og lav procentvis afvigelse fra tabelværdi.
* Er der afvigelse og hvor kommer den fra?

## Tillægsforsøg
En glødepærer udsender lys ved at blive opvarmet. I skal lave et kvalitativt forsøg med en lampe og et gitter.

## Materialer
Gitter, 12V lampe, strømforsyning

## Udførsel
* Se på lyset som sendes gennem gittret.
* Forklar hvorfan farven bliver slitter op
* Brug din viden om intergerens til at forklare hvorfor rød er yderst mens violet er inderst.
* Tror I at det er sådan en regnbue bliver dannet?
* Hvis I tror det, hvad danner gitteret?

## Tillægsforsøg, mål tykkelsen af et hår
I kan bruge jeres viden om bølgelængde og gitre til at finde tykkelsen på et hår.

## Teori
Håret virker som en dobbeltspalte, så der dannes interferensmønster, så gitterligningen kan bruges igen.

* Isoler d i ligningen

## Udførsel

* Placer et hår i en holder og send laserlys gennem det.
* Mål afbøjningsvinklen til minimum 3. orden.
* Brug målingerne til at bestemme tykkelsen af håret.
* Find en reference og sammenlign.