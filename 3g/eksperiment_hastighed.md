<link rel="stylesheet" href="../style.css">
<script>
  window.MathJax = {
    tex: {
      inlineMath: [['$', '$'], ['\\(', '\\)']],
      displayMath: [['$$', '$$'], ['\\[', '\\]']],
      processEscapes: true
    }
  };
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# Forsøgsbeskrivelse: Bestemmelse af Elektroners Hastighed i et Homogent Elektrisk Felt

## 1. Formål
Formålet med dette eksperiment er at undersøge elektroners bevægelse i et homogent elektrisk felt (en fladkondensator) og bestemme elektronernes faktiske hastighed $v_x$ ud fra banens kasteparabel. 

Den fundne hastighed sammenlignes efterfølgende med den teoretiske hastighed beregnet ud fra accelerationsspændingen $U_{\text{acc}}$.

---

## 2. Teori

### Bevægelse i det homogene felt
Når en elektron med ladning $e$ og masse $m$ træder ind i et homogent elektrisk felt med feltstyrke $E$, påvirkes den af en konstant lodret kraft $F_e = e \cdot E$. 

* **Vandret retning ($x$-akse):** Ingen kræfter virker i denne retning. Hastigheden $v_x$ er derfor konstant:
  $$x(t) = v_x \cdot t \implies t = \frac{x}{v_x}$$

* **Lodret retning ($y$-akse):** Elektronen accelereres lodret med $a_y = \frac{e \cdot E}{m}$. Den lodrette afbøjning $y$ til tiden $t$ er:
  $$y(t) = \frac{1}{2} a_y t^2 = \frac{1}{2} \left( \frac{e \cdot E}{m} \right) t^2$$

### Parabelligningen
Indsæt \( t = \frac{x}{v_x} \) i ligningen for $y(t)$, og vis at det giver:

$$y(x) = \frac{1}{2} \cdot \left( \frac{e}{m} \right) \cdot \frac{E}{v_x^2} \cdot x^2$$

Dette har formen af en parabel $y = a \cdot x^2$, hvor parabelkoefficienten $a$ er givet ved:

$$a = \frac{\left( \frac{e}{m} \right) \cdot E}{2 \cdot v_x^2}$$

### Bestemmelse af hastigheden $v_x$
Feltstyrken mellem plader med afstand $d$ og afbøjningsspænding $U_{\text{afb}}$ er $E = \frac{U_{\text{afb}}}{d}$. 

Når koefficienten $a$ bestemmes ved en kvadratisk regression på eksperimentelle $(x,y)$-data, og tabelværdien for den specifikke ladning ($\frac{e}{m} \approx 1{,}7588 \times 10^{11} \text{ C/kg}$) benyttes, kan den faktiske hastighed $v_x$ beregnes som:

$$v_x = \sqrt{\frac{\left( \frac{e}{m} \right) \cdot E}{2 \cdot a}}$$

### Teoretisk sammenligning
Den teoretiske hastighed $v_{\text{teo}}$ opnået fra accelerationsspændingen $U_{\text{acc}}$ beregnes ved energibevarelse ($E_{\text{kin}} = E_{\text{pot}}$):

* Vis at når $E_{pot} = e\cdot U$ og $E_{kin} = 1/2\cdot m \cdot v^2$ bliver

$$v_{\text{teo}} = \sqrt{2 \cdot \left( \frac{e}{m} \right) \cdot U_{\text{acc}}}$$

---

## 3. Apparatur og Opstilling

* Fintstrålerør eller elektronstrålerør med afbøjningsplader
* Højspændingsforsyning til accelerationsspænding ($U_{\text{acc}}$)
* Spændingsforsyning til afbøjningsspænding ($U_{\text{afb}}$)
* Voltmetre / Måleudstyr til spænding
* Lineal eller gitter/kamera-opstilling til måling af $(x, y)$-koordinater
* Sikkerhedskabler

---

## 4. Udførelse

1. **Opstilling:** Tilslut elektronstrålerøret i henhold til sikkerhedsinstruktionerne. Sørg for korrekt jordforbindelse og polaritet på afbøjningspladerne.
2. **Accelerationsindstilling:** Tænd for glødespændingen og indstil accelerationsspændingen $U_{\text{acc}}$ til en fast værdi (f.eks. $3{,}9 \text{ kV}$). Mål og noter værdien.
3. **Afbøjningsindstilling:** Påtryk en konstant afbøjningsspænding $U_{\text{afb}}$ (f.eks. $2000 \text{ V}$) over pladerne. Notér pladeafstanden $d$.
4. **Dataindsamling:** Mål sammenhørende værdier af den vandrette position $x$ og den lodrette afbøjning $y$ langs elektronstrålens bane. Registrer mindst 6–8 punkter med god spredning.

---

## 5. Databehandling og Analyse

1. **Regression:** Indtast de målte koordinater $(x, y)$ i meter og udfør en kvadratisk regression af formen $y = a \cdot x^2 + b \cdot x + c$. Hvis I regner i meter er enheden for $a=[\frac{1}{\text{m}}]$. 
2. **Feltstyrke:** Beregn den elektriske feltstyrke $E = \frac{U_{\text{afb}}}{d}$.
3. **Eksperimentel hastighed:** Indsæt den udlæste værdi for $a$ og beregn $v_x$:
   $$v_x = \sqrt{\frac{(e/m) \cdot E}{2 \cdot a}}$$
4. **Teoretisk hastighed:** Beregn $v_{\text{teo}} = \sqrt{2 \cdot 1{,}7588 \times 10^{11} \cdot U_{\text{acc}}}$.
5. **Afvigelse:** Beregn den procentvise afvigelse mellem den eksperimentelle hastighed $v_x$ og den teoretiske hastighed $v_{\text{teo}}$:
   $$\text{Afvigelse} = \frac{|v_x - v_{\text{teo}}|}{v_{\text{teo}}} \cdot 100\%$$

---

## 6. Fejlkilder og Diskussion

Overvej og diskuter følgende punkter i din rapport:
* Hvilken effekt har elektriske **randfelter** (hvor feltet strækker sig ud over pladernes fysiske grænser) på den målte parabelkoefficient $a$?
* Hvordan påvirker usikkerheden i målingen af $x$ og $y$ den endelige værdi for $v_x$?
* Hvorfor ville det **ikke** være muligt at bestemme brøken $e/m$ udelukkende ved brug af et elektrisk felt, hvis $v_x$ blev antaget at være præcis lig med $v_{\text{teo}}$?