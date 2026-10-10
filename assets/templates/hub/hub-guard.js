/* Loaded just before hub-data.js. If hub-data.js has a typing mistake (a missing comma, quote or bracket),
   the browser stops reading it. This records what the browser said so hub.js can show it on the page.
   On a file opened from your computer, browsers often hide the details ("Script error."); on a published
   link they usually show the line number. */
window.__hubErrors = [];
window.addEventListener("error", function (e) {
  window.__hubErrors.push({ line: e && e.lineno, col: e && e.colno, msg: e && e.message, file: e && e.filename });
});
