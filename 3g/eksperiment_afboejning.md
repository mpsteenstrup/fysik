# Forsøgsbeskrivelse: Accelerationsspændingens Betydning for Elektronafbøjning

## 1. Formål

Formålet med dette eksperiment er at undersøge, hvordan elektronernes starthastighed (styret af accelerationsspændingen $U_{\text{acc}}$) påvirker den samlede afbøjning $y$ i et konstant homogent elektrisk felt. 

Eksperimentet tester den teoretiske omvendte proportionalitet mellem $y$ og $U_{\text{acc}}$.

---

## 2. Teori

Når elektroner accelereres over en spændingsforskel $U_{\text{acc}}$, omsættes den potentielle elektriske energi til kinetisk energi:

$$e \cdot U_{\text{acc}} = \frac{1}{2} m v_x^2 \implies v_x^2 = \frac{2 e U_{\text{acc}}}{m}$$

Elektronerne sendes derefter ind mellem to parallelle plader med længden $L$ og afstanden $d$. Mellem pladerne påtrykkes en konstant afbøjningsspænding $U_{\text{afb}}$, hvilket skaber et elektrisk felt $E = \frac{U_{\text{afb}}}{d}$.

### Udledning af afbøjningen $y$

* **Opholdstid i feltet ($t$):** Den tid, elektronen er mellem pladerne af længde $L$:
  $$t = \frac{L}{v_x}$$

* **Lodret acceleration ($a_y$):**
  $$a_y = \frac{e \cdot E}{m} = \frac{e \cdot U_{\text{afb}}}{m \cdot d}$$

* **Lodret afbøjning ved pladeudgangen ($y$):**
  $$y = \frac{1}{2} a_y t^2 = \frac{1}{2} \left( \frac{e \cdot U_{\text{afb}}}{m \cdot d} \right) \left( \frac{L}{v_x} \right)^2 = \frac{e \cdot U_{\text{afb}} \cdot L^2}{2 \cdot m \cdot d \cdot v_x^2}$$

Indsættes udtrykket for $v_x^2$ i afbøjningsligningen:

$$y = \frac{e \cdot U_{\text{afb}} \cdot L^2}{2 \cdot m \cdot d \cdot \left( \frac{2 e U_{\text{acc}}}{m} \right)}$$

Ved at forkorte $e$ og $m$ reduceres udtrykket til:

$$y = \left( \frac{U_{\text{afb}} \cdot L^2}{4 \cdot d} \right) \cdot \frac{1}{U_{\text{acc}}}$$

### Konklusion på teorien
Da $U_{\text{afb}}$, $L$ og $d$ holdes konstante under forsøget, kan udtrykket skrives som:

$$y = k \cdot \frac{1}{U_{\text{acc}}} \quad \text{hvor} \quad k = \frac{U_{\text{afb}} \cdot L^2}{4 \cdot d}$$

Afbøjningen $y$ er altså **omvendt proportional** med accelerationsspændingen $U_{\text{acc}}$. Det vil sige, at en højere accelerationsspænding giver højere fart, kortere opholdstid i feltet og dermed en mindre afbøjning.

---

## 3. Apparatur og Opstilling

* Elektronstrålerør / Fintstrålerør med afbøjningsplader
* Højspændingsforsyning til accelerationsspænding ($U_{\text{acc}}$)
* Regulær spændingsforsyning til afbøjningsspænding ($U_{\text{afb}}$)
* Precision voltmetre til måling af $U_{\text{acc}}$ og $U_{\text{afb}}$
* Lineal / Indbygget mm-skala på røret til aflæsning af afbøjningen $y$ ved en fast position $x = L$

---

## 4. Udførelse

1. **Opstilling:** Opstil kredsløbet til elektronstrålerøret. Kontrollér polariteten på afbøjningspladerne.
2. **Fasthold afbøjningsspænding:** Indstil afbøjningsspændingen $U_{\text{afb}}$ til en fast, passende værdi (f.eks. $1500 \text{ V}$ eller $2000 \text{ V}$). Denne spænding skal holdes konstant under hele dataindsamlingen.
3. **Måleserie:**
   * Indstil accelerationsspændingen $U_{\text{acc}}$ til den første værdi (f.eks. $2{,}0 \text{ kV}$).
   * Mål og notér elektronstrålens lodrette afbøjning $y$ ved pladernes udgang eller på skærmen ved en valgt fast afstand $x$.
   * Øg $U_{\text{acc}}$ trinvist (f.eks. i skridt af $0{,}5 \text{ kV}$ op til $5{,}0 \text{ kV}$) og mål den tilhørende afbøjning $y$ for hver indstilling.
   * Notér mindst 6–8 sammenhørende målinger af $(U_{\text{acc}}, y)$.

---

## 5. Databehandling og Analyse

1. **Datatabel:** Opret en tabel over dine måledata indeholdende:
   * $U_{\text{acc}}$ (i Volt)
   * $\frac{1}{U_{\text{acc}}}$ (i $\text{V}^{-1}$)
   * Afbøjning $y$ (i meter)

2. **Grafisk afbildning:**
   * Opret et scatterplot med $\frac{1}{U_{\text{acc}}}$ på $x$-aksen og afbøjningen $y$ på $y$-aksen.
   * Udfør en **lineær regression** ($y = a \cdot x + b$) på datapunkterne.

3. **Sammenligning med teorien:**
   * Tjek om skæringspunktet $b$ er tæt på $0$.
   * Sammenlign den eksperimentelt fundne hældning $a_{\text{eksperiment}}$ med den teoretiske konstant:
     $$k_{\text{teoretisk}} = \frac{U_{\text{afb}} \cdot L^2}{4 \cdot d}$$
   * Beregn den procentvise afvigelse:
     $$\text{Afvigelse} = \frac{\vert a_{\text{eksperiment}} - k_{\text{teoretisk}} \vert}{k_{\text{teoretisk}}} \cdot 100\%$$

---

## 6. Fejlkilder og Diskussion

* Hvorfor falder afbøjningen $y$, når accelerationsspændingen $U_{\text{acc}}$ øges?
* Hvordan påvirker det målingerne, hvis afbøjningsspændingen $U_{\text{afb}}$ fluktuerede under forsøget?
* Hvilken pædagogisk/fysisk forklaring er der på, at elektrodernes masse $m$ og ladning $e$ overhovedet ikke indgår i den endelige formel for $y$?