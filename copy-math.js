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