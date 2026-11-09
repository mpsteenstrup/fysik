# Fysik 1.g - Regler for udvikling af opgavesider

## Generelle principper
- **Sprog:** Alt brugerfladetekst, opgavebeskrivelser, hints og feedback skal være på dansk.
- **Tone:** Hjælpsom, pædagogisk og orienteret mod fysisk forståelse og fænomenforklaring.
- **Tilgængelighed:** Brug semantisk HTML, og sørg for at inputfelter og tekstområder har tydelige labels.
- **Hints:** Hints skal hjælpe eleven på vej til forståelsen eller formlen uden at give det endelige svar eller den fulde forklaring.
- **Enheder:** Alle beregningsopgaver og formler skal inkludere og fremhæve relevante fysiske enheder (f.eks. $\text{m/s}$, $\text{J}$, $\text{Hz}$, $^\circ\text{C}$).

---

## Pædagogisk Progression
Opgaverne på en side skal opbygges efter følgende faste progression:
1. **Forståelse (Kvalitativ/Konceptuel):** Multipel choice / valg af rigtige udsagn eller sortering af fænomener. Ingen tunge beregninger.
2. **Forklaring (Skriftlig formulering):** Tekstfelt hvor eleven selv skal formulere en fysisk forklaring (f.eks. "Forklar hvorfor..."), som efterfølgende sammenlignes med en udskreven mønsterløsning ("Sammenlign med løsning").
3. **Beregning (Simple taleksempler):** Simple beregningsopgaver med formelindsættelse. Fokus er på at kende størrelserne og bruge de rigtige enheder.
4. **Perspektivering / Krævende opgave (Til de hurtige):** Kobling til hverdagsfænomener, fejlkildeanalyse eller kombination af to begreber.

---

## Teknisk Standard
- **Fysik og Matematik:** Brug MathJax til alle formler og fysiske størrelser. 
    - Inline: `\( v = 343 \text{ m/s} \)`
    - Blok: `$$ v = \frac{s}{t} $$`
- **Interaktivitet:** 
    - `checkMultipleChoice(qId, correctOptionIndex)`: Til forståelsesopgaver med svarmuligheder.
    - `checkAnswer(qId, correctVal, tolerance)`: Til simple numeriske beregninger med enheder.
    - `toggleBox(boxId)`: Til at vise/skjule hints og fold-ud sammenligningsløsninger.
    - Feedback vises i et element med klassen `.feedback`.

---

## HTML Header-struktur
Den øverste del af HTML-dokumentet skal indeholde følgende (med `XX` udskiftet med titlen på emnet):

```html
<!DOCTYPE html>
<html lang="da">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>XX - Fysik 1.g</title>
    <!-- Link til ekstern style.css -->
    <link rel="stylesheet" href="../../style_opgaver.css">
    <!-- MathJax til fysik- og matematikvisning -->
    <script src="[https://polyfill.io/v3/polyfill.min.js?features=es6](https://polyfill.io/v3/polyfill.min.js?features=es6)"></script>
    <script id="MathJax-script" async src="[https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js](https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js)"></script>
</head>