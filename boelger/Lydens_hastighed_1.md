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

# Forsøgsvejledning: Bestemmelse af lydens hastighed (Manuel metode)

## Formål
At bestemme lydens hastighed i luft ved manuel tidtagning med stopur over en kendt afstand og sammenligne resultatet med den teoretiske tabellerværdi.

---

## Apparatur og Materialer
* Balloner (kraftige farver)
* Knappenål eller sikkerhedsnål
* Målebånd, målehjul eller GPS/opmåling på $100\text{ m}$
* Stopure (f.eks. på mobiltelefoner)
* Termometer (til måling af luftens temperatur)

---

## Teori

### Lydens hastighed
Lyd spreder sig gennem luften som trykbølger. Da lysets hastighed er ekstremt høj ($\approx 300.000\text{ km/s}$), ser vi ballonen sprænge øjeblikkeligt. Lydens hastighed $v$ er væsentligt langsommere og kan beregnes ved formlen:

$$v = \frac{s}{t}$$

hvor:
* $s$ er afstanden i meter ($\text{m}$)
* $t$ er den målte tid i sekunder ($\text{s}$)
* $v$ er lydens hastighed i meter pr. sekund ($\text{m/s}$)

### Teoretisk sammenligning
Lydens hastighed i tør luft afhænger af luftens temperatur $T$ i Celsius og kan beregnes teoretisk med formlen:

$$v_{\text{teoretisk}} = 331{,}3 \text{ m/s} + 0{,}6 \cdot T$$

---

## Fremgangsmåde

1. **Opmåling:** Mål en præcis strækning på $s = 100\text{ m}$ op udendørs på et fladt område.
2. **Placering:**
   * **Gruppe A (Afsender):** Står ved $0\text{ m}$ med ballon og nål.
   * **Gruppe B (Modtagere):** Står ved $100\text{ m}$ med stopure klar og direkte udsyn til Gruppe A.
3. **Måling af temperatur:** Mål luftens temperatur $T$ i $^\circ\text{C}$ og noter den i skemaet.
4. **Udførelse:**
   * Gruppe A rækker ballonen op i luften.
   * Gruppe A stikker nålen i ballonen.
   * Gruppe B **starter** stopuret i det øjeblik, de **ser** ballonen sprænge.
   * Gruppe B **stopper** stopuret i det øjeblik, de **hører** braget.
5. Gentag forsøget minimum 3–5 gange for at reducere usikkerheden fra den menneskelige reaktionstid.

---

## Databehandling og Beregninger

### 1. Datamålinger (Måleskema)

Registrer jeres målinger fra de enkelte forsøg i tabellen herunder:

| Forsøg nr. | Afstand, $s$ [$\text{m}$] | Målt tid, $t$ [$\text{s}$] |
| :--- | :--- | :--- |
| **1** | | |
| **2** | | |
| **3** | | |
| **4** | | |
| **5** | | |

---

### 2. Beregning af gennemsnitstid

For at reducere reaktionstidens indvirkning beregnes gennemsnittet af de målte tider:

$$t_{\text{gennemsnit}} = \frac{t_1 + t_2 + t_3 + t_4 + t_5}{5}$$

| Afstand, $s$ [$\text{m}$] | Gennemsnitstid, $t_{\text{gennemsnit}}$ [$\text{s}$] |
| :--- | :--- |
| $100$ | |

---

### 3. Beregning af lydens forsøgshastighed

Når I kender afstanden og gennemsnitstiden, kan I beregne lydens hastighed ud fra:

$$v_{\text{forsøg}} = \frac{s}{t_{\text{gennemsnit}}}$$

| Afstand, $s$ [$\text{m}$] | Gennemsnitstid, $t_{\text{gennemsnit}}$ [$\text{s}$] | Lydens hastighed, $v_{\text{forsøg}} = \frac{s}{t}$ [$\text{m/s}$] |
| :--- | :--- | :--- |
| &nbsp; | | |

---

### 4. Sammenligning med den teoretiske værdi

Mål luftens temperatur $T$ og beregn den teoretiske hastighed:

$$v_{\text{teoretisk}} = 331{,}3 + 0{,}6 \cdot T$$

| Temperatur, $T$ [$^\circ\text{C}$] | Teoretisk lydhastighed, $v_{\text{teoretisk}}$ [$\text{m/s}$] | Målt hastighed $v$|
| :--- | :--- | :--- |
| &nbsp;|  | |

---

### 5. Afvigelse i procent

Beregning af den procentvise afvigelse mellem jeres forsøgsresultat og den teoretiske værdi:

$$\text{Procentvis afvigelse} = \frac{|v_{\text{forsøg}} - v_{\text{teoretisk}}|}{v_{\text{teoretisk}}} \cdot 100\%$$

| Forsøgsværdi, $v_{\text{forsøg}}$ [$\text{m/s}$] | Teoretisk værdi, $v_{\text{teoretisk}}$ [$\text{m/s}$] | Procentvis afvigelse [$\%$] |
| :--- | :--- | :--- |
|&nbsp; | | |

---

## Konklusion & Fejlkilder
1. Sammenlign jeres forsøgsresultat med den teoretiske værdi. Hvor tæt kom I på?
2. Hvilken rolle spiller den menneskelige reaktionstid for usikkerheden i dette forsøg?
3. Hvordan påvirker vindforholdene (medvind/modvind) det endelige resultat?
4. Kom med et bud på hvorfor temperaturen betyder noget for lydens hastighed.