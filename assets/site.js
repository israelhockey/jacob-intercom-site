(function () {
  // Open every page at the top, unless the link points to a section (#quote etc.).
  try { if ('scrollRestoration' in history) { history.scrollRestoration = 'manual'; } } catch (e) {}
  var toTop = function () { if (!location.hash) { window.scrollTo(0, 0); } };
  toTop();
  window.addEventListener('load', toTop);
  window.addEventListener('pageshow', toTop);

  // Phone menu
  var toggle = document.querySelector('.menu-toggle'), nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', open ? 'false' : 'true');
      nav.classList.toggle('open', !open);
    });
  }

  // Buzzer panel troubleshooter (home page)
  var panel = document.querySelector('[data-panel]');
  if (panel) {
    var out = {
      title: panel.querySelector('[data-out="title"]'),
      cause: panel.querySelector('[data-out="cause"]'),
      price: panel.querySelector('[data-out="price"]'),
      link: panel.querySelector('[data-out="link"]')
    };
    var buttons = panel.querySelectorAll('button[data-id]');
    var show = function (btn) {
      buttons.forEach(function (b) { b.setAttribute('aria-pressed', b === btn ? 'true' : 'false'); });
      out.title.textContent = btn.dataset.title;
      out.cause.textContent = btn.dataset.cause;
      out.price.textContent = btn.dataset.price;
      out.link.textContent = btn.dataset.linktext;
      if (btn.dataset.href) { out.link.setAttribute('href', btn.dataset.href); }
    };
    buttons.forEach(function (b) { b.addEventListener('click', function () { show(b); }); });
  }

  // Cost estimators. Edit the figures here; a value in [BRACKETS] is still waiting on Jacob.
  var REPAIR = {
    station: ['$100 to $300', 'Usually a new apartment station, fitted in under an hour.'],
    strike: ['$100 to $300', 'Adjusting or repairing the strike. A new strike costs more: [STRIKE PRICE].'],
    audio: ['$100 to $300', 'A new speaker or microphone in the panel, or a station repair.'],
    video: ['[VIDEO REPAIR RANGE]', 'Depends on the system and whether the camera, monitor or power has failed.'],
    panel: ['[PANEL RANGE]', 'From a few buttons to a full new panel on the existing wiring.'],
    amp: ['[AMPLIFIER RANGE]', 'Usually the power supply or amplifier. One repair brings every apartment back.'],
    wiring: ['[WIRING REPAIR RANGE]', 'A fault on a shared riser wire, traced and repaired.']
  };
  var INSTALL = {
    s: { audio: '[PRICE]', video: '[PRICE]', phone: '[PRICE]' },
    m: { audio: '[PRICE]', video: '[PRICE]', phone: '[PRICE]' },
    l: { audio: '[PRICE]', video: '[PRICE]', phone: '[PRICE]' },
    xl: { audio: 'Quoted after a site visit', video: 'Quoted after a site visit', phone: 'Quoted after a site visit' }
  };
  var TYPE_NOTE = { audio: 'No monthly fee.', video: 'No monthly fee. Often runs on the existing wire.', phone: 'Usually carries a monthly service fee on top.' };
  var mark = function (el, text) {
    el.textContent = text;
    el.classList.toggle('todo', /^\[/.test(text));
  };
  document.querySelectorAll('[data-calc]').forEach(function (box) {
    var range = box.querySelector('[data-out="range"]'), note = box.querySelector('[data-out="note"]');
    var selects = box.querySelectorAll('select');
    var update = function () {
      if (box.dataset.calc === 'repair') {
        var r = REPAIR[selects[0].value]; mark(range, r[0]); note.textContent = r[1];
      } else {
        mark(range, INSTALL[selects[0].value][selects[1].value]); note.textContent = TYPE_NOTE[selects[1].value];
      }
    };
    selects.forEach(function (s) { s.addEventListener('change', update); });
    update();
  });

  // Quote forms: not connected to a mailbox yet, so say so instead of pretending to send.
  document.querySelectorAll('form[data-quote]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var msg = form.querySelector('.form-msg');
      msg.hidden = false;
      msg.textContent = 'Preview only: this form is not connected yet. Call 718-252-2730 for now.';
    });
  });
})();
