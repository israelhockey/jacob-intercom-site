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

  // Dropdown menus: click or tap to open, Escape or click elsewhere to close
  var groups = [].slice.call(document.querySelectorAll('.nav-group'));
  function closeAll(except) {
    groups.forEach(function (g) { if (g !== except) { g.classList.remove('open'); g.querySelector('.nav-top').setAttribute('aria-expanded', 'false'); } });
  }
  groups.forEach(function (g) {
    var btn = g.querySelector('.nav-top');
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = !g.classList.contains('open');
      closeAll(g);
      g.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });
  document.addEventListener('click', function (e) { if (!e.target.closest('.nav-group')) closeAll(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeAll(); });

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
    station: ['$200 to $400', 'Usually a new apartment station.'],
    strike: ['$200 to $400', 'Adjusting or repairing the strike. A new strike: contact for price.'],
    audio: ['$200 to $400', 'A new speaker or microphone in the panel, or a station repair.'],
    video: ['Contact for price', 'Depends on the system and whether the camera, monitor or power has failed.'],
    panel: ['Contact for price', 'From a few buttons to a full new panel on the existing wiring.'],
    amp: ['Contact for price', 'Usually the power supply or amplifier. One repair brings every apartment back.'],
    wiring: ['Contact for price', 'A fault on a shared riser wire, traced and repaired.']
  };
  var INSTALL = {
    s: { audio: 'Contact for price', video: 'Contact for price', phone: 'Contact for price' },
    m: { audio: 'Contact for price', video: 'Contact for price', phone: 'Contact for price' },
    l: { audio: 'Contact for price', video: 'Contact for price', phone: 'Contact for price' },
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

  // Quote forms: every submission is emailed to jacobintercom@gmail.com through FormSubmit.
  var FORM_ENDPOINT = 'https://formsubmit.co/ajax/jacobintercom@gmail.com';
  document.querySelectorAll('form[data-quote]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var msg = form.querySelector('.form-msg');
      var btn = form.querySelector('button[type="submit"]');
      var val = function (n) { var f = form.elements[n]; return f ? f.value.trim() : ''; };
      msg.hidden = false;
      if (val('_honey')) { msg.textContent = 'Thanks, we got your request.'; return; }
      if (!val('name') || !(val('phone') || val('email'))) {
        msg.textContent = 'Please add your name and a phone number or email so we can get back to you.';
        return;
      }
      var data = {};
      new FormData(form).forEach(function (v, k) { if (k !== '_honey' && String(v).trim()) data[k] = v; });
      data._subject = 'New quote request from jacobintercom.com' + (val('company') ? ' (' + val('company') + ')' : '');
      data._template = 'table';
      data._captcha = 'false';
      if (val('email')) data._replyto = val('email');
      data.page = document.title + ' (' + location.pathname + ')';
      btn.disabled = true;
      msg.textContent = 'Sending...';
      fetch(FORM_ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify(data)
      }).then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) {
          if (!res.ok || String(res.j.success) === 'false') throw new Error('send failed');
          form.reset();
          msg.textContent = 'Thanks! Your request was sent to Jacob Intercom. We will get back to you shortly. For anything urgent, call 718-252-2730.';
        })
        .catch(function () {
          msg.textContent = 'Sorry, that did not send. Please call 718-252-2730 or email jacobintercom@gmail.com.';
        })
        .then(function () { btn.disabled = false; });
    });
  });
})();
