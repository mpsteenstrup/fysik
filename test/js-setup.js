// 1. Konfiguration af MathJax (skal ligge øverst)
window.MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    displayMath: [['$$', '$$'], ['\\[', '\\]']],
    processEscapes: true
  }
};

// 2. Gør formler kopierbare til Google Docs
document.addEventListener('copy', function (event) {
  const selection = window.getSelection();
  if (!selection.rangeCount) return;

  const container = document.createElement('div');
  for (let i = 0; i < selection.rangeCount; i++) {
    container.appendChild(selection.getRangeAt(i).cloneContents());
  }

  container.querySelectorAll('mjx-container').forEach(mjx => {
    const assistiveMml = mjx.querySelector('mjx-assistive-mml');
    if (assistiveMml) {
      const span = document.createElement('span');
      span.textContent = ' ' + assistiveMml.textContent.trim() + ' ';
      mjx.replaceWith(span);
    }
  });

  event.clipboardData.setData('text/html', container.innerHTML);
  event.clipboardData.setData('text/plain', container.innerText);
  event.preventDefault();
});

// 3. Auto-gem af elevsvar og klargøring til PDF-print
document.addEventListener('DOMContentLoaded', () => {
  const pageKey = 'fysik_svar_' + window.location.pathname;
  const savedData = JSON.parse(localStorage.getItem(pageKey) || '{}');

  // Hent gemte svar ind i felterne ved indlæsning
  document.querySelectorAll('input[id], textarea[id]').forEach(el => {
    if (savedData[el.id]) {
      el.value = savedData[el.id];
    }

    // Opdater spejl-div hvis det er et textarea
    const mirror = el.parentElement?.querySelector('.print-mirror');
    if (mirror) mirror.textContent = el.value;

    // Gem automatisk når eleven skriver
    el.addEventListener('input', () => {
      savedData[el.id] = el.value;
      localStorage.setItem(pageKey, JSON.stringify(savedData));
      if (mirror) mirror.textContent = el.value;
    });
  });
});

// Tilføj en "Gem som PDF / Print"-knap og en "Nulstil felter"-knap nederst på siden
window.addEventListener('load', () => {
  const controls = document.createElement('div');
  controls.className = 'no-print';
  controls.style.marginTop = '30px';
  controls.innerHTML = `
    <button onclick="window.print()">Gem besvarelse som PDF</button>
    <button onclick="nulstilBesvarelse()" style="margin-left:10px;">Ryd alle felter</button>
  `;
  document.body.appendChild(controls);
});

function nulstilBesvarelse() {
  if (confirm('Er du sikker på, at du vil slette alle dine indtastede svar på denne side?')) {
    const pageKey = 'fysik_svar_' + window.location.pathname;
    localStorage.removeItem(pageKey);
    document.querySelectorAll('input[id], textarea[id]').forEach(el => el.value = '');
    document.querySelectorAll('.print-mirror').forEach(m => m.textContent = '');
  }
}