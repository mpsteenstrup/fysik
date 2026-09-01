# Guide: Lav dit eget Fysik Escape Room

Velkommen til projektet! I skal bygge jeres eget interaktive Escape Room i HTML og JavaScript. I behøver ikke kunne programmere for at I kan få det til at virke.

Først skal I prøve om I kan klare om I kan komme fri: [https://mpsteenstrup.github.io/fysik/escaperoom/index.html](https://mpsteenstrup.github.io/fysik/escaperoom/index.html)

Her er opskriften på, hvordan I arbejder med koden lokalt på jeres computer, så I kan se ændringer med det samme.

##  Sådan kommer I i gang

1.  **Download projektet:** Download mappen fra linket: [template.zip](https://github.com/mpsteenstrup/fysik/raw/refs/heads/main/escaperoom/template.zip).
2.  **Åbn spillet:** Højreklik på `index.html` og vælg **Åbn med...** -> **Google Chrome** (eller Edge/Safari). Nu kan I se spillet køre.
3.  **Rediger opgaverne:** Højreklik på filen `opgaver.js` og vælg **Åbn med...**:
    * **Windows:** Vælg **Notesblok** (Notepad).
    * **Mac:** Vælg **TextEdit**. (Vigtigt: Tryk `Shift + Cmd + T` for at gøre teksten til "Ren tekst", ellers virker koden ikke!).
    * **Alternativ:** Brug [vscode.dev](https://vscode.dev) i din browser og åbn mappen derfra.
4.  **Se ændringer:** Hver gang I har rettet noget i `opgaver.js`, skal I **Gemme** filen (`Ctrl + S` / `Cmd + S`), gå tilbage til browseren og trykke på **Opdater** (`F5` / `Cmd + R`).

---

## Sådan redigerer I `opgaver.js`

I skal kun rette i listen `levels`. Hvert "level" (rum) er indrammet af krøllede parenteser `{ }`.

```javascript
const levels = [
    {
        title: "Level 1: Overskrift",
        description: "Her skriver I opgaveteksten. Husk at bruge fysik-betegnelser!",
        answer: "42",        // Svaret skal stå i gåseøjne
        image: "billede1.jpg", // Filnavnet på jeres billede i mappen
        music: "lyd1.mp3",     // (Valgfrit) Filnavn på jeres baggrundsmusik
        pdf: "bilag1.pdf"      // (Valgfrit) Filnavn på jeres PDF-dokument
    },
    // Næste level herunder...
];
```

---

## Gode råd til fysik-gåderne

* **Billeder:** Brug billeder i god kvalitet. I kan gemme små tal eller spor i hjørnerne, som spillerne skal zoome ind for at finde.
* **Enheder:** Bestem selv om svaret skal være med eller uden enheder (f.eks. "5" eller "5 m/s"). Skriv det tydeligt i opgaven!
* **Fysik-PDF:** I kan lave en PDF med formler, grafer eller datatabeller, som spillerne skal bruge for at regne koden ud.
* **Lyd:** Find gratis musik og lydeffekter på **Pixabay.com**. Det giver den helt rigtige stemning!
* **Vigtigt:** Tjek at alle filnavne er stavet præcis ens i koden og i mappen (husk at der er forskel på store og små bogstaver på GitHub, hold jer til små bogstaver!).
---

## Når I er færdige

Når spillet virker perfekt på jeres computer:
1.  Lav en zip-fil og send den til din lærer.

## Online på Github
Github til hosting af websider

Github er et online sted hvor udviklere lægger programmer, data og meget mere. Det er et versionsstyringsværktøj lavet til at arbejde på forskellige version af samme software. Vi kommer ikke til at bruge denne feature men kun bruge det til at have vores websider liggenden.

Det anbefales generelt ikke at bruge specialtegn, æøå og mellemrum i filnavne.

Guide til github

* Gå ind på siden [www.github.com](www.github.com).
* Opret en konto, det er gratis.
* Tryk på **+** for at oprette et *repository*.
* Vælg "uploading an existing file".
* Vælg alle filerne i din mappe, drag and drop.
* Vælg mappen billeder, drag and drop.
* Scroll nederst og vælg "commit changes".

Nu er dine filer online, men github har ikke lavet hjemmesiden endnu.

Opgætning af webpage

* Vælg "Settings" til højre, ikke helt øverst.
* Vælg "Pages" ude til venstre.
* Under "Branch" og skift fra "NONE" til "main" og vælg "Save".

Nu loader github hjemmesiden. Det kan tage et par minutter og man kan med fordel trykke reload en gang i mellem. Når linket kommer frem kan man jo se om det virker. 

### Flere escaperooms

Hvis der er flere escaperooms fra elever er det letteste at uploade hele mappen fra eleverne. Her er det vigtigt at. 
