/* Checkpoint prototype: Kitchen Crate first-box flow (fictional). Three screens. Built on the starter design system.
   Known gaps are listed in README.md; they are for week 7. */
(function () {
  var app = document.getElementById("app");
  var state = { day: "", home: true, confirmed: false };
  var DAYS = [
    { id: "wed", title: "Wednesday", detail: "Arrives between 8 am and 12 pm" },
    { id: "fri", title: "Friday", detail: "Arrives between 8 am and 12 pm" },
    { id: "sat", title: "Saturday", detail: "Arrives between 10 am and 2 pm" }
  ];
  function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;"); }
  function steps(n) {
    var names = ["Start", "Day", "Confirm"];
    return '<ol class="steps" aria-label="Progress">' + names.map(function (t, i) {
      return "<li" + (i === n ? ' aria-current="step"' : i < n ? ' class="done"' : "") + ">" + t + "</li>";
    }).join("") + "</ol>";
  }
  var screens = {
    welcome: function () {
      return steps(0) + '<div class="stack"><h1 id="h">Your first box, in three steps</h1>' +
        '<p>Here is what to expect.</p><div class="card"><ol><li>Choose a delivery day</li><li>Pick your meals</li><li>Know how to skip or pause</li></ol></div>' +
        '<a class="btn btn--block" href="#day">Start</a></div>';
    },
    day: function (error) {
      var cards = DAYS.map(function (d) {
        return '<label class="radio-card"><input type="radio" name="day" value="' + d.id + '"' + (state.day === d.id ? " checked" : "") + '><span><span class="radio-card__title">' + d.title + '</span><span class="radio-card__detail">' + d.detail + "</span></span></label>";
      }).join("");
      return steps(1) + '<div class="stack"><h1 id="h">Choose your delivery day</h1>' +
        '<p>You can change this until Monday 6 pm. After that it is locked for that box.</p>' +
        (error ? '<div class="alert alert--error" role="alert">Choose a day to continue.</div>' : "") +
        '<fieldset style="border:0;padding:0;margin:0" class="stack"><legend class="visually-hidden">Delivery day</legend>' + cards + "</fieldset>" +
        '<label class="radio-card"><input type="checkbox" id="away"' + (state.home ? "" : " checked") + '><span><span class="radio-card__title">I will not be home</span><span class="radio-card__detail">We will leave the box in a safe place you choose later</span></span></label>' +
        '<button class="btn btn--block" id="go" type="button">Continue</button></div>';
    },
    confirm: function () {
      var d = DAYS.filter(function (x) { return x.id === state.day; })[0] || DAYS[0];
      return steps(2) + '<div class="stack"><h1 id="h">' + (state.confirmed ? "You are set" : "Check your first box") + "</h1>" +
        (state.confirmed ? '<div class="alert" role="status">Your first box is booked. We will remind you on Monday before the cut-off.</div>' : "") +
        '<div class="card"><h2>Delivery</h2><p>' + esc(d.title) + (state.home ? "" : ", left in a safe place") + '</p><span class="badge">Change until Monday 6 pm</span></div>' +
        '<div class="card"><h2>Need to skip a week?</h2><p>Go to Home, then "Skip this week". You can skip until Monday 6 pm before each delivery.</p></div>' +
        (state.confirmed ? '<a class="btn btn--secondary btn--block" href="#welcome">Start again</a>' :
          '<button class="btn btn--block" id="ok" type="button">Confirm my first box</button><a class="btn btn--secondary btn--block" href="#day">Change the day</a>') + "</div>";
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
