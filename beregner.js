// Fil: beregner.js (Simpel og robust løsning til Grader)

// --- 1. Vi definerer vores egne 'Grader' funktioner først ---
// Disse funktioner tager grader som input og returnerer et svar i radianer,
// som JavaScripts 'Math.sin' forstår.
function sind(grader) { return Math.sin(grader * Math.PI / 180); }
function cosd(grader) { return Math.cos(grader * Math.PI / 180); }
function tand(grader) { return Math.tan(grader * Math.PI / 180); }

// Disse funktioner returnerer svaret i GRADER
function asind(værdi) { return Math.asin(værdi) * (180 / Math.PI); }
function acosd(værdi) { return Math.acos(værdi) * (180 / Math.PI); }
function atand(værdi) { return Math.atan(værdi) * (180 / Math.PI); }

// En nem genvej til kvadratrod (så de ikke skal skrive Math.sqrt)
function sqrt(x) { return Math.sqrt(x); }
function abs(x) { return Math.abs(x); }
// Osv. for andre funktioner du vil gøre lette

function lynBeregn() {
    let input = document.getElementById('regner').value;
    const svarFelt = document.getElementById('svar');
    
    // Nulstil hvis tomt
    if (input.trim() === "") {
        svarFelt.innerText = "0";
        return;
    }

    try {
        // --- 2. Grundlæggende brugervenlighed ---
        input = input.replace(',', '.');       // Komma til punktum
        input = input.replace('^', '**');      // ^ til **
        input = input.replace(/pi/gi, 'Math.PI'); // pi til Math.PI

        // --- 3. Beregn ---
        // Nu tager Function() elevens input. Da vi definerede funktionerne
        // som 'sind', 'cosd' osv. helt oppe i toppen af filen, ved
        // JavaScript nu præcis, hvad den skal gøre, når den møder 'sind(90)'.
        const resultat = Function('"use strict";return (' + input + ')')();
        
        // --- 4. Vis svar ---
        if (isFinite(resultat)) {
            // Runder af til 4 decimaler for pænere output
            svarFelt.innerText = Number(resultat.toFixed(4));
        } else {
            svarFelt.innerText = "?"; // Division med 0
        }
    } catch (e) {
        // Mens de taster, viser vi '...'
        svarFelt.innerText = "...";
    }
}