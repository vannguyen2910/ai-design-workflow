/* Checkpoint prototype: Delivery App first-order flow (fictional). Three screens. Built on the starter design system.
   Known gaps are listed in README.md; they are for week 6. */
(function () {
  var app = document.getElementById("app");
  var state = { day: "", home: true, confirmed: false };
  var DAYS = [
    { id: "s12", title: "12:00 to 12:30", detail: "Arrives within the half hour" },
    { id: "s18", title: "18:30 to 19:00", detail: "Arrives within the half hour" },
    { id: "s19", title: "19:30 to 20:00", detail: "Arrives within the half hour" }
  ];
  function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;"); }
  function steps(n) {
    var names = ["Start", "Time", "Confirm"];
    return '<ol class="steps" aria-label="Progress">' + names.map(function (t, i) {
      return "<li" + (i === n ? ' aria-current="step"' : i < n ? ' class="done"' : "") + ">" + t + "</li>";
    }).join("") + "</ol>";
  }
  var screens = {
    welcome: function () {
      return steps(0) + '<div class="stack"><h1 id="h">Your first order, in three steps</h1>' +
        '<p>Here is what to expect.</p><div class="card"><ol><li>Choose a delivery time</li><li>Pick your dishes</li><li>Know how to cancel or change</li></ol></div>' +
        '<a class="btn btn--block" href="#day">Start</a></div>';
    },
    day: function (error) {
      var cards = DAYS.map(function (d) {
        return '<label class="radio-card"><input type="radio" name="day" value="' + d.id + '"' + (state.day === d.id ? " checked" : "") + '><span><span class="radio-card__title">' + d.title + '</span><span class="radio-card__detail">' + d.detail + "</span></span></label>";
      }).join("");
      return steps(1) + '<div class="stack"><h1 id="h">Choose your delivery time</h1>' +
        '<p>You can change this until 15 minutes before your slot. After that it is locked for this order.</p>' +
        (error ? '<div class="alert alert--error" role="alert">Choose a time to continue.</div>' : "") +
        '<fieldset style="border:0;padding:0;margin:0" class="stack"><legend class="visually-hidden">Delivery time</legend>' + cards + "</fieldset>" +
        '<label class="radio-card"><input type="checkbox" id="away"' + (state.home ? "" : " checked") + '><span><span class="radio-card__title">I will not be home</span><span class="radio-card__detail">We will leave the order in a safe place you choose later</span></span></label>' +
        '<button class="btn btn--block" id="go" type="button">Continue</button></div>';
    },
    confirm: function () {
      var d = DAYS.filter(function (x) { return x.id === state.day; })[0] || DAYS[0];
      return steps(2) + '<div class="stack"><h1 id="h">' + (state.confirmed ? "You are set" : "Check your first order") + "</h1>" +
        (state.confirmed ? '<div class="alert" role="status">Your first order is placed. We will remind you 30 minutes before the cut-off.</div>' : "") +
        '<div class="card"><h2>Delivery</h2><p>' + esc(d.title) + (state.home ? "" : ", left in a safe place") + '</p><span class="badge">Change until 15 minutes before</span></div>' +
        '<div class="card"><h2>Need to cancel?</h2><p>Go to Orders, then "Cancel order". You can cancel until the restaurant accepts your order.</p></div>' +
        (state.confirmed ? '<a class="btn btn--secondary btn--block" href="#welcome">Start again</a>' :
          '<button class="btn btn--block" id="ok" type="button">Confirm my first order</button><a class="btn btn--secondary btn--block" href="#day">Change the time</a>') + "</div>";
    }
  };
  function show(name, error) {
    if (!screens[name]) name = "welcome";
    app.innerHTML = screens[name](error);
    var h = document.getElementById("h"); if (h) { h.setAttribute("tabindex", "-1"); h.focus(); }
    var go = document.getElementById("go");
    if (go) go.addEventListener("click", function () {
      var sel = document.querySelector('input[name="day"]:checked');
      state.home = !document.getElementById("away").checked;
      if (!sel) { show("day", true); return; }
      state.day = sel.value; location.hash = "#confirm";
    });
    var ok = document.getElementById("ok");
    if (ok) ok.addEventListener("click", function () { state.confirmed = true; show("confirm"); });
  }
  window.addEventListener("hashchange", function () { show(location.hash.slice(1)); });
  show(location.hash.slice(1));
})();
