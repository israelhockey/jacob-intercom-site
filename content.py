"""Page content for jacobintercom.com.

[[path/|text]] links to another page (plain text until that page is built).
[CAPITALISED] marks a fact still needed from Jacob; it renders highlighted.
"""

PAGES = []


def page(**kw):
    PAGES.append(kw)


def symptom(path, nav, title, desc, h1, lead, notice, causes, checks, fix, cost, replace, faqs, related):
    cause_html = "".join(f"<li><strong>{n}.</strong> {t}</li>" for n, t in causes)
    check_html = "".join(f"<li>{c}</li>" for c in checks)
    body = f"""
<h2>What you'll notice</h2>
{notice}
<h2>The usual causes</h2>
<ul>{cause_html}</ul>
<h2>What you can safely check yourself</h2>
<ul>{check_html}</ul>
<p>Don't open the lobby panel or the amplifier cabinet yourself. The wiring is low voltage, but the power supply that feeds it is not, and a crossed wire can take out every apartment on the line.</p>
<h2>How we fix it</h2>
{fix}
<h2>What it costs</h2>
{cost}
<h2>Repair or replace?</h2>
{replace}
"""
    page(path=path, nav=nav, title=title, desc=desc, h1=h1, lead=lead,
         facts=["<b>35 years</b> repairing New York intercoms", "Most repairs <b>$100 to $300</b>", "Price given <b>before</b> work starts"],
         body=body, faqs=faqs, related=related)


# ───────────────────────────── Home ─────────────────────────────

HOME = """
<section class="hero" id="top"><div class="wrap row" style="gap:48px;align-items:flex-start">
<div class="col stack" style="gap:22px;flex-basis:420px">
<h1>New York's intercoms, repaired and installed for 35 years.</h1>
<p class="lead">Buzzers, door releases, video entry and the Lee-Dan systems other companies won't touch. All five boroughs. Most repairs run $100 to $300.</p>
<div class="btn-row"><a class="btn btn-brass" href="tel:+17182522730">Call 718-252-2730</a><a class="btn btn-ghost" href="#quote">Text us a photo of your panel</a></div>
<p class="fine">Rated 4.7 from 23 Google reviews. Licensed and insured, [LICENCE NO.].</p>
</div>
<div class="panel col" data-panel style="flex-basis:460px">
<div class="panel-head"><h2>What's wrong? Press a button.</h2><div class="grille" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div></div>
<div class="panel-buttons">
<button type="button" aria-pressed="true" data-id="ring" data-title="Buzzer won't ring in the apartment" data-cause="Usually a failed apartment station, a broken wire in the riser, or a tired amplifier. If several apartments are dead, it is almost always the amplifier or the power supply." data-price="Most repairs: $100 to $300." data-linktext="How we fix dead buzzers" data-href="{{u:intercom-repair/door-buzzer/}}">Buzzer won't ring</button>
<button type="button" aria-pressed="false" data-id="door" data-title="It buzzes, but the door stays locked" data-cause="The electric strike in the door frame is worn or misaligned, or the release relay or transformer has failed. The intercom itself is often fine." data-price="Most repairs: $100 to $300." data-linktext="Door release repair" data-href="{{u:intercom-repair/door-release/}}">Door won't unlock</button>
<button type="button" aria-pressed="false" data-id="audio" data-title="No sound, static, or only one side can hear" data-cause="A corroded speaker or microphone in the lobby panel, crossed wires, or a failing amplifier. Outdoor panels take the most weather." data-price="Most repairs: $100 to $300." data-linktext="Audio faults explained" data-href="{{u:intercom-repair/no-audio/}}">No sound or static</button>
<button type="button" aria-pressed="false" data-id="video" data-title="The screen is blank or frozen" data-cause="A failed camera module, a weak power supply, or on newer systems a network problem. We test each before replacing anything." data-price="Price depends on the system. Call for a range." data-linktext="Video intercom repair" data-href="{{u:intercom-repair/video/}}">No video</button>
<button type="button" aria-pressed="false" data-id="panel" data-title="The entry panel is broken or vandalised" data-cause="Buttons, name strips and faceplates can usually be replaced on the existing wiring without touching the apartments." data-price="Price depends on the panel. Send us a photo." data-linktext="Entry panel repair" data-href="{{u:intercom-repair/entry-panel/}}">Panel damaged</button>
<button type="button" aria-pressed="false" data-id="new" data-title="Time for a new system" data-cause="We look at the building, test the existing wire, and give you options in writing, from a like-for-like swap to video on your phone." data-price="Written quote after a site visit." data-linktext="All intercom repairs" data-href="{{u:intercom-repair/}}">I need a new system</button>
</div>
<div class="panel-out" aria-live="polite">
<h3 data-out="title">Buzzer won't ring in the apartment</h3>
<p data-out="cause">Usually a failed apartment station, a broken wire in the riser, or a tired amplifier. If several apartments are dead, it is almost always the amplifier or the power supply.</p>
<p class="price" data-out="price">Most repairs: $100 to $300.</p>
<div class="btn-row" style="align-items:center"><a class="btn btn-dark" href="tel:+17182522730">Call about this</a><a data-out="link" href="{{u:intercom-repair/door-buzzer/}}" style="font-weight:600">How we fix dead buzzers</a></div>
</div>
</div>
</div></section>

<section class="strip" aria-label="Why Jacob Intercom"><div class="wrap"><span>35 years in business</span><span>4.7 stars from 23 Google reviews</span><span>Licensed and insured</span><span>All five boroughs, plus Long Island, Westchester and New Jersey</span></div></section>

<section class="section"><div class="wrap">
<h2>Whatever is on the wall, we work on it.</h2>
<div class="row">
<div class="col col-rule stack">
<h3>Repair</h3>
<p>One apartment or the whole building. We find the fault before we quote, and we fix what can be fixed instead of selling you a new system.</p>
<ul class="linklist">
<li>[[intercom-repair/door-buzzer/|Buzzer not ringing]]</li>
<li>[[intercom-repair/door-release/|Door release and electric strike]]</li>
<li>[[intercom-repair/no-audio/|No sound, static or one-way audio]]</li>
<li>[[intercom-repair/video/|Video not working]]</li>
<li>[[intercom-repair/entry-panel/|Damaged entry panel]]</li>
<li>[[intercom-repair/emergency/|Emergency repair]]</li>
</ul>
</div>
<div class="col col-rule stack">
<h3>Installation and replacement</h3>
<p>New systems for brownstones, walk-ups, co-ops, condos and offices. Where the old wire is good, we reuse it and save you the cost of opening walls.</p>
<ul class="linklist">
<li>[[intercom-installation/video/|Video intercoms]]</li>
<li>[[intercom-installation/wireless/|Wireless and smartphone entry]]</li>
<li>[[intercom-installation/telephone-entry/|Audio and telephone entry]]</li>
<li>[[intercom-replacement/|Replacing an old buzzer system]]</li>
<li>[[access-control/|Access control and key fobs]]</li>
</ul>
</div>
<div class="col" style="flex-basis:300px">{{img:1}}</div>
</div>
</div></section>

<section class="section band-dark"><div class="wrap row" style="align-items:center;gap:48px">
<div class="col" style="flex-basis:300px;max-width:420px">{{img:25}}</div>
<div class="col stack" style="flex-basis:480px;gap:18px">
<h2>Got a Lee-Dan? We still fix them.</h2>
<p style="font-size:1.12rem;max-width:32em">Thousands of New York buildings still run on Lee-Dan intercoms. Most companies will only quote you a replacement. We repair them, source the parts, and tell you plainly when replacing really is the better money.</p>
<ul class="linklist grid2">
<li>[[lee-dan-intercom-systems/|Lee-Dan repair and service]]</li>
<li>[[lee-dan-intercom-systems/ir-203/|IR-203 apartment stations]]</li>
<li>[[lee-dan-intercom-systems/ir-204/|IR-204 four-wire systems]]</li>
<li>[[lee-dan-intercom-systems/ir-205/|IR-205 five-wire systems]]</li>
<li>[[lee-dan-intercom-systems/pk-543-amplifier/|PK-543 amplifiers]]</li>
<li>[[lee-dan-intercom-systems/troubleshooting/|Troubleshooting guide]]</li>
</ul>
</div>
</div></section>

<section class="section"><div class="wrap">
<h2 style="margin-bottom:8px">Recent jobs</h2>
<p style="color:var(--muted);margin-bottom:32px">Sample entries shown for layout. Each will be replaced with one of Jacob's real jobs and its photos.</p>
<div class="jobs">
<article><div class="slot">Real job photo</div><p class="sample">Sample</p><h3>[BUILDING TYPE], [NEIGHBORHOOD]: dead buzzers on two floors</h3><p style="color:var(--muted);margin-top:8px">What was wrong, what we found, what we replaced, and how long it took. Three or four sentences in Jacob's words.</p></article>
<article><div class="slot">Real job photo</div><p class="sample">Sample</p><h3>[CO-OP], [NEIGHBORHOOD]: Lee-Dan system kept running</h3><p style="color:var(--muted);margin-top:8px">The board had a replacement quote. What we repaired instead, and what it saved.</p></article>
<article><div class="slot">Real job photo</div><p class="sample">Sample</p><h3>[WALK-UP], [NEIGHBORHOOD]: buzzer upgraded to video</h3><p style="color:var(--muted);margin-top:8px">New video entry on the existing wire, and how the tenants were shown to use it.</p></article>
</div>
</div></section>

<section class="section tight" style="padding-top:0"><div class="wrap row" style="gap:48px">
<div class="col stack">
<h2 style="font-size:clamp(1.6rem,3vw,2.3rem)">For managing agents, supers and boards</h2>
<p style="color:var(--muted)">One call for every building you look after. We send the insurance certificate before we arrive, quote in writing, and keep a record of what is installed where.</p>
<ul><li>Certificate of insurance on request</li><li>Yearly maintenance contracts, [CONTRACT PRICE]</li><li>One invoice across multiple buildings</li></ul>
<div><a class="btn btn-dark" href="#quote">Request a building quote</a></div>
</div>
<div class="col stack">
<h2 style="font-size:clamp(1.6rem,3vw,2.3rem)">Brands we service</h2>
<p style="color:var(--muted)">Fifteen makes, old and new. Each is getting its own page with models, common faults and what repairs cost.</p>
<ul class="linklist" style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0 20px">
<li>[[lee-dan-intercom-systems/|Lee-Dan]]</li><li>[[brands/aiphone/|Aiphone]]</li><li>[[brands/butterflymx/|ButterflyMX]]</li>
<li>[[brands/comelit/|Comelit]]</li><li>[[brands/akuvox/|Akuvox]]</li><li>[[brands/tektone/|Tektone]]</li>
<li>[[brands/mircom/|Mircom]]</li><li>[[brands/siedle/|Siedle]]</li><li>[[brands/elvox/|Elvox]]</li>
<li>[[brands/doorbird/|DoorBird]]</li><li>[[brands/2n/|2N]]</li><li>[[brands/doorking/|DoorKing]]</li>
<li>[[brands/alpha-communications/|Alpha]]</li><li>[[brands/pacific-electronics/|Pacific]]</li><li>[[brands/nutone/|NuTone]]</li>
</ul>
</div>
</div></section>
"""

page(path="", nav="Home", title="Intercom Repair & Installation NYC | Jacob Intercom",
     desc="Intercom repair and installation across New York for 35 years. Buzzers, door releases, video entry and Lee-Dan systems. Most repairs $100 to $300. Call 718-252-2730.",
     h1="New York's intercoms, repaired and installed for 35 years.", html=HOME)

# ───────────────────────────── Repair hub ─────────────────────────────

page(path="intercom-repair/", nav="Intercom repair",
     title="Intercom Repair NYC: Buzzers, Door Release, Audio & Video | Jacob Intercom",
     desc="Intercom repair in New York for apartment buildings, brownstones and offices. We find the fault and price it before work starts. Most repairs $100 to $300.",
     h1="Intercom repair in New York City",
     lead="One dead apartment or a silent building: we find what failed, tell you the price, and fix it. Most repairs take one visit and cost $100 to $300.",
     facts=["<b>35 years</b> repairing New York intercoms", "Most repairs <b>$100 to $300</b>", "<b>15 brands</b>, including Lee-Dan", "Price given <b>before</b> work starts"],
     body="""
<h2>Start with what it's doing</h2>
<p>Almost every intercom call we get is one of six problems. Pick yours for the likely causes, what you can check yourself, and what the repair usually costs.</p>
<div class="tablebox"><table>
<thead><tr><th scope="col">The problem</th><th scope="col">Where the fault usually is</th><th scope="col">Typical price</th></tr></thead>
<tbody>
<tr><th scope="row">[[intercom-repair/door-buzzer/|The buzzer doesn't ring]]</th><td>Apartment station, riser wire or amplifier</td><td>$100 to $300</td></tr>
<tr><th scope="row">[[intercom-repair/door-release/|It buzzes but the door stays locked]]</th><td>Electric strike, release relay or transformer</td><td>$100 to $300</td></tr>
<tr><th scope="row">[[intercom-repair/no-audio/|No sound, static or one-way audio]]</th><td>Panel speaker or microphone, wiring, amplifier</td><td>$100 to $300</td></tr>
<tr><th scope="row">[[intercom-repair/video/|The video screen is blank]]</th><td>Camera module, power supply or network</td><td>[VIDEO REPAIR RANGE]</td></tr>
<tr><th scope="row">[[intercom-repair/entry-panel/|The entry panel is damaged]]</th><td>Buttons, faceplate or the whole panel</td><td>[PANEL RANGE]</td></tr>
<tr><th scope="row">[[intercom-repair/not-working/|Nothing works at all]]</th><td>Power supply, amplifier or a main wiring fault</td><td>[AMPLIFIER RANGE]</td></tr>
</tbody></table></div>
<p>The $100 to $300 range covers the common single-fault repairs. Parts for older or discontinued systems, long wiring runs and full panel replacements cost more, and we tell you so before starting.</p>

<h2>How an intercom system fails</h2>
<p>A building intercom is four things joined by wire: the <strong>entry panel</strong> at the front door, an <strong>amplifier and power supply</strong> usually in the basement or a closet, a <strong>station in each apartment</strong>, and the <strong>electric strike</strong> that unlocks the door. A fault in any one of them looks different from the apartment.</p>
<ul>
<li><strong>One apartment has the problem.</strong> The fault is in that apartment's station or the wire run to it. This is the quickest and cheapest repair.</li>
<li><strong>A vertical line of apartments has it.</strong> The riser wire they share is broken or shorted somewhere between floors.</li>
<li><strong>Everyone has it.</strong> The amplifier, the power supply or the entry panel has failed. The rest of the system is usually fine.</li>
<li><strong>Talking works but the door won't open.</strong> The intercom is fine. The door hardware has failed.</li>
</ul>
<p>Knowing which of these you have before you call saves a visit. Ask a neighbour above or below you whether theirs works.</p>

<h2>What happens when you call</h2>
<ol>
<li><strong>You tell us what it's doing.</strong> A photo of the entry panel and of the apartment station tells us the make and usually the age.</li>
<li><strong>We test before we touch.</strong> We check power at the amplifier, then the panel, then the line to the affected apartments, so we replace the part that failed and nothing else.</li>
<li><strong>You get the price.</strong> We tell you what it is and what it costs before any work starts.</li>
<li><strong>We repair it.</strong> Most single faults are fixed on the first visit. If a part has to be ordered, we say how long.</li>
<li><strong>We test every affected apartment</strong> before we leave.</li>
</ol>

<h2>The systems we repair</h2>
<p>We work on audio and video intercoms, old and new: [[lee-dan-intercom-systems/|Lee-Dan]], [[brands/aiphone/|Aiphone]], [[brands/comelit/|Comelit]], [[brands/akuvox/|Akuvox]], [[brands/butterflymx/|ButterflyMX]], [[brands/tektone/|Tektone]], [[brands/mircom/|Mircom]], [[brands/siedle/|Siedle]], [[brands/elvox/|Elvox]], [[brands/doorbird/|DoorBird]], [[brands/2n/|2N]], [[brands/doorking/|DoorKing]], [[brands/alpha-communications/|Alpha Communications]], [[brands/pacific-electronics/|Pacific Electronics]] and [[brands/nutone/|NuTone]].</p>
<p>Older systems are a large part of our work. Many New York buildings have intercoms that were installed decades ago and still have years in them. If a company tells you your system is too old to repair, get a second opinion before you pay for a new one.</p>

<h2>Repair or replace?</h2>
<p>We repair when the fault is in one part and the rest of the system is sound. We recommend replacing when the same system keeps failing in different places, when parts are no longer made, or when the repair would cost a large share of a new system.</p>
<p>When replacing is the better choice, the existing wire can often stay. That is the expensive part of any installation, and reusing it keeps the cost down. See [[intercom-replacement/|intercom replacement and upgrades]].</p>

<h2>Warranty</h2>
<p>[WARRANTY TERMS]</p>
""",
     faqs=[("How much does intercom repair cost in NYC?", "Most single-fault repairs cost $100 to $300. Repairs needing discontinued parts, long wiring runs or a new entry panel cost more. We give you the price before starting."),
           ("Can you fix an intercom another company installed?", "Yes. We repair systems from 15 manufacturers regardless of who installed them."),
           ("Do I call you, or does my landlord?", "In a rental the building owner is normally responsible for the intercom, so tell your landlord or super first. Owners, supers and managing agents can call us directly at {{tel}}."),
           ("Can you repair just one apartment?", "Yes. If only your apartment is affected, the repair is usually the station on your wall or the wire to it, and it's the quickest job we do."),
           ("How fast can you come?", "We're open Monday to Thursday 9 to 5 and Friday 8 to 4. Call {{tel}} for the next opening. After hours: [AFTER-HOURS LINE].")],
     related=[("intercom-repair/emergency/", "Emergency intercom repair"), ("lee-dan-intercom-systems/", "Lee-Dan systems"), ("pricing/", "Pricing"), ("contact/", "Contact us")])

# ───────────────────────────── Symptom pages ─────────────────────────────

symptom(
    "intercom-repair/door-buzzer/", "Door buzzer repair",
    "Door Buzzer Repair NYC: Buzzer Not Ringing | Jacob Intercom",
    "Apartment buzzer not ringing? The usual causes, what to check yourself, and what repair costs in New York. Most buzzer repairs $100 to $300.",
    "Door buzzer repair",
    "Visitors press your button and nothing happens upstairs. Here is why that happens and what it takes to fix.",
    """<p>Someone presses your button at the front door and your apartment stays silent. Deliveries leave. Guests call your phone from the sidewalk. Sometimes the buzzer is faint, or rings only now and then.</p>
<p>The first thing to find out is whether it's only you. If the apartments above and below you have the same problem, the fault is in the wiring you share. If the whole building is silent, it is at the amplifier or the entry panel.</p>""",
    [("The apartment station has failed", "The buzzer or speaker inside the unit on your wall wears out. This is the most common cause when only one apartment is affected."),
     ("A wire is broken or loose", "Renovations, a new kitchen, or a painter pulling the station off the wall can break a connection. A break in the riser takes out every apartment on that line."),
     ("The button at the door is worn", "Entry panel buttons take weather and thousands of presses. A dead button means the signal never leaves the lobby."),
     ("The amplifier or power supply is failing", "If every apartment is quiet or faint, the unit that powers the system has usually failed."),
     ("The station was switched off or turned down", "Some stations have a volume wheel or a mute switch on the side or underneath.")],
    ["Look for a volume wheel or switch on your apartment station and turn it up.",
     "Check that the handset is seated properly on its hook, if you have one. A handset left off the hook can stop the buzzer.",
     "Ask a neighbour on your line and one on another line whether theirs rings.",
     "Have someone press your button while you listen at the station for a click or hum. Any sound means the signal is arriving and the station itself is the problem."],
    """<p>We test from the door inward: the button, the panel, the power at the amplifier, then the line to your apartment. That tells us which part failed.</p>
<p>A failed station is replaced with a matching or compatible unit, usually in under an hour. A broken wire is traced and repaired at the break. A worn button is replaced in the panel. A failed amplifier or power supply is repaired or replaced, which brings the whole building back at once.</p>""",
    """<p>Most buzzer repairs cost <strong>$100 to $300</strong>. A single apartment station is at the low end. Tracing a break inside a wall, or replacing an amplifier, costs more: [WIRING AND AMPLIFIER RANGE]. You get the price before we start.</p>""",
    """<p>A dead buzzer in one apartment is always a repair. If stations are failing one after another across the building, the system is at the end of its life and it is cheaper to plan a replacement than to keep paying for visits. We will tell you which situation you are in.</p>""",
    [("Why does my buzzer work sometimes and not others?", "An intermittent buzzer usually means a loose connection or a worn button at the door. It tends to get worse, and it's easier to find while it's still happening."),
     ("My buzzer rings but I can't hear the visitor. Is that the same fault?", "No. That is an audio fault. See [[intercom-repair/no-audio/|no sound, static or one-way audio]]."),
     ("Can I replace the apartment station myself?", "The replacement has to match the system's wiring, and older stations are wired differently from the ones sold online. A wrong unit can short the line for your neighbours."),
     ("Who pays, me or my landlord?", "In a rental, the owner is normally responsible for keeping the intercom working. Report it to your landlord or super in writing.")],
    [("intercom-repair/", "All intercom repairs"), ("intercom-repair/door-release/", "Door won't unlock"), ("intercom-repair/no-audio/", "No sound or static"), ("intercom-repair/not-working/", "Nothing works at all")])

symptom(
    "intercom-repair/door-release/", "Door release repair",
    "Door Release & Electric Strike Repair NYC | Jacob Intercom",
    "Buzzer sounds but the door won't unlock? Electric strike and door release repair in New York. Causes, checks and costs. Most repairs $100 to $300.",
    "Door release and electric strike repair",
    "You press the door button, maybe even hear the buzz, and the front door stays locked. The intercom is usually fine. The fault is at the door.",
    """<p>You can hear and talk to your visitor, but pressing the door button doesn't let them in. Sometimes the door buzzes and still won't push open. Sometimes it opens only if the visitor leans on it at the right moment. The opposite fault matters too: a door that no longer locks after it has been buzzed is a security problem for the whole building.</p>""",
    [("The electric strike is worn or misaligned", "The strike is the powered latch plate in the door frame. Doors sag and frames shift, and a strike that is a few millimetres out will buzz without releasing."),
     ("The strike has burned out", "Strikes held open too long, or fed the wrong voltage, fail completely. There is no buzz at the door at all."),
     ("The transformer or release relay has failed", "The strike has its own power feed. If that fails, every apartment loses door release at once."),
     ("The door button in one apartment has failed", "If your neighbours can open the door and you can't, the fault is in your station."),
     ("The door closer or the latch is the real problem", "A door that doesn't close fully never latches, and a stiff latch won't retract. Neither is an intercom fault, but both get reported as one.")],
    ["Have someone stand at the door while you press the button. Ask whether they hear a buzz or click at the frame.",
     "If it buzzes, have them push the door firmly while it's buzzing. If that works, the strike is misaligned.",
     "Ask a neighbour to try their door button. If theirs works, the fault is in your apartment station.",
     "Watch the door close on its own. If it stops short of latching, the closer needs adjusting."],
    """<p>We check for power at the strike while the button is pressed, which separates an electrical fault from a mechanical one in a few minutes.</p>
<p>A misaligned strike is adjusted or refitted. A burned-out strike is replaced with one matched to the door, the frame and the system voltage. A failed transformer or relay is replaced at the amplifier. If the door closer or lock is the cause, we tell you, and we can fit door hardware where it is part of the entry system.</p>""",
    """<p>Most door release repairs cost <strong>$100 to $300</strong>. A new electric strike costs more, depending on the door and frame: [STRIKE PRICE]. You get the price before we start.</p>""",
    """<p>Door release faults are almost always repairs. The strike and its power supply are separate from the intercom, so a failed strike is never a reason to replace the system.</p>""",
    [("The door buzzes but doesn't open. Is the intercom broken?", "Usually not. A buzz means power is reaching the strike. The strike is misaligned or worn, or the latch is binding."),
     ("Our front door doesn't lock after someone is buzzed in. Is that urgent?", "Yes. A strike that sticks open leaves the building unlocked. Call {{tel}}."),
     ("Can you fit a new strike to an old door?", "In most cases, yes. Old wood and steel frames both take modern strikes, though some need the frame cut or a surface-mounted strike."),
     ("Do you repair magnetic locks?", "Yes. We service magnetic locks and the exit buttons and sensors that go with them. See [[access-control/electric-strikes-maglocks/|electric strikes and magnetic locks]].")],
    [("intercom-repair/", "All intercom repairs"), ("intercom-repair/door-buzzer/", "Buzzer not ringing"), ("intercom-repair/entry-panel/", "Damaged entry panel"), ("access-control/", "Access control")])

symptom(
    "intercom-repair/no-audio/", "No sound or static",
    "Intercom No Sound, Static or One-Way Audio: Repair NYC | Jacob Intercom",
    "Can't hear your visitor, or they can't hear you? Intercom audio repair in New York: the causes of silence, static and one-way sound, and what it costs to fix.",
    "No sound, static or one-way audio",
    "The buzzer rings, but the conversation doesn't work. One side can't hear, both are drowned in static, or there's a loud hum.",
    """<p>Audio faults come in a few forms: you can hear the visitor but they can't hear you, or the other way round; both sides get crackle or a loud hum; the sound is so faint it's useless; or you hear your neighbours' visitors as well as your own.</p>
<p>Which form you have points to where the fault is, so it helps to note it before you call.</p>""",
    [("The speaker or microphone in the entry panel has corroded", "The panel sits outdoors or in a damp vestibule. When visitors can't be heard by anyone in the building, this is the usual cause."),
     ("Your apartment station's speaker or microphone has failed", "If only your apartment has the problem, the fault is in the unit on your wall or its handset cord."),
     ("Wires are crossed or shorted", "Hearing other apartments' conversations, or a hum that starts when a button is pressed, means two wires are touching somewhere."),
     ("The amplifier is failing", "Faint sound across the whole building, or sound that fades in and out, points to the amplifier."),
     ("Something is interfering", "A loud steady hum can come from a failing power supply or from intercom wire run alongside power cable.")],
    ["Note which direction fails: you can't hear them, they can't hear you, or both.",
     "If you have a handset, check the coiled cord is pushed fully in at both ends.",
     "Turn up the volume control on your station if it has one.",
     "Ask a neighbour whether visitors are clear on theirs. If nobody can hear visitors, the fault is at the entry panel."],
    """<p>We test the entry panel's speaker and microphone first, because one failed part there affects every apartment. Then we check the amplifier output and the line to the affected stations.</p>
<p>Panel speakers and microphones are replaced inside the existing panel. A failed station or handset is replaced. Crossed wires are traced and separated. A weak amplifier is repaired or replaced.</p>""",
    """<p>Most audio repairs cost <strong>$100 to $300</strong>. Tracing crossed wires through a building can take longer and cost more: [WIRING REPAIR RANGE]. You get the price before we start.</p>""",
    """<p>A corroded panel speaker or a dead handset is a repair. If the panel is corroded throughout, replacing the panel on the existing wiring is often better value than replacing its parts one at a time.</p>""",
    [("Why can I hear other apartments on my intercom?", "Two lines are touching, usually where wires share a conduit or at a station that was wired wrongly. It's a privacy problem as well as a nuisance, so it's worth fixing promptly."),
     ("The intercom hums all the time. Is that dangerous?", "It isn't dangerous, but a constant hum usually means the power supply is failing, and the system may stop altogether."),
     ("Visitors say I sound far away. What causes that?", "A weak microphone in your station, or a failing amplifier if your neighbours get the same complaint."),
     ("Does rain affect the intercom?", "Yes. Water in an outdoor panel causes crackle and silence that come and go with the weather. The fix is to replace the damaged parts and reseal the panel.")],
    [("intercom-repair/", "All intercom repairs"), ("intercom-repair/door-buzzer/", "Buzzer not ringing"), ("intercom-repair/entry-panel/", "Damaged entry panel"), ("intercom-repair/video/", "Video not working")])

symptom(
    "intercom-repair/video/", "Video intercom repair",
    "Video Intercom Repair NYC: Blank or Frozen Screen | Jacob Intercom",
    "Video intercom screen blank, frozen or dark? Repair in New York for wired and IP video intercoms and smartphone entry systems. Causes, checks and costs.",
    "Video intercom repair",
    "The sound works but the picture doesn't, or the screen is dark, frozen or too poor to recognise anyone.",
    """<p>Video faults look like this: a black or blue screen when someone calls; a picture that freezes or breaks up; an image too dark to see a face at night; or, on systems that ring your phone, calls that arrive late or not at all.</p>
<p>Wired video systems and network-based ones fail in different ways, so the first thing we establish is which you have.</p>""",
    [("The camera in the entry panel has failed", "If no apartment gets a picture, the camera module is the first suspect. Cameras facing the sun or the weather age fastest."),
     ("The power supply is weak", "Video needs more power than audio. A tired power supply will run the sound and drop the picture."),
     ("The monitor in the apartment has failed", "If only your screen is blank, the fault is in your monitor or its connection."),
     ("The network is down, on IP and smartphone systems", "These systems depend on the building's internet connection, a network switch and often a cloud service. A fault in any of them stops the video."),
     ("The night lighting has failed", "Panels light the visitor with small LEDs. When they fail, the picture is fine by day and black at night.")],
    ["Check whether the picture fails for every apartment or only yours.",
     "Note whether it fails only after dark.",
     "On a smartphone system, check the app is updated, notifications are allowed, and your phone has a signal.",
     "If the building has its own internet router for the intercom, check whether its lights are on. Don't reset it without asking the building manager."],
    """<p>On wired systems we test the camera, the power supply and the video line in turn. On network systems we check the panel's connection, the switch and the service account before touching hardware, because many faults are in the settings and not the equipment.</p>
<p>Cameras and monitors are replaced with matching parts. Power supplies are replaced. Network faults are corrected at the switch or router, and app and account problems are fixed with the building's administrator.</p>""",
    """<p>Video repairs vary more than audio ones, because the parts range from a small camera module to a full touchscreen panel: [VIDEO REPAIR RANGE]. Faults in settings or the network are often fixed in a single short visit. You get the price before we start.</p>""",
    """<p>Replace the part when the system is current and supported. If the manufacturer no longer supplies parts or software updates, repairs become temporary, and a planned replacement costs less over a few years. Much of the existing wiring can usually be reused.</p>""",
    [("The video works but calls don't reach my phone. Can you fix that?", "Usually, yes. It's most often a setting in the app, the phone's notification permissions, or the building's account with the service."),
     ("Can you add video to an audio-only intercom?", "Often, and sometimes on the wire that's already there. See [[intercom-installation/video/|video intercom installation]]."),
     ("Which video systems do you repair?", "Aiphone, Comelit, Akuvox, ButterflyMX, DoorBird, 2N, Siedle, Elvox and others. See [[brands/|the brands we service]]."),
     ("The picture is fine in the day and black at night. Why?", "The panel's night lighting has failed, or the camera has lost its low-light sensitivity. Either can be replaced.")],
    [("intercom-repair/", "All intercom repairs"), ("intercom-repair/no-audio/", "No sound or static"), ("intercom-installation/video/", "Video intercom installation"), ("brands/", "Brands we service")])

symptom(
    "intercom-repair/entry-panel/", "Entry panel repair",
    "Intercom Entry Panel Repair & Replacement NYC | Jacob Intercom",
    "Broken, vandalised or worn intercom entry panel? Button, faceplate and full panel replacement in New York, on your existing wiring where possible.",
    "Damaged entry panel repair",
    "Buttons that stick, names nobody can read, a cracked faceplate, or a panel someone has forced open.",
    """<p>The entry panel is the hardest-working part of the system and the only part exposed to the street. The signs are familiar: buttons that stay in or do nothing; a directory with half the names missing; a cracked or dented face; exposed wires; or a panel that has been pried off the wall.</p>
<p>A damaged panel is also a security problem. Exposed wiring at the door can be used to trigger the door release.</p>""",
    [("Button wear", "Each button is a small switch pressed thousands of times a year. They fail one at a time, starting with the busiest apartments."),
     ("Weather", "Water and salt get behind the faceplate and corrode the contacts, the speaker and the microphone."),
     ("Vandalism or forced entry", "Panels are kicked, pried and burned. The face may be destroyed while the wiring behind it is untouched."),
     ("Age", "Name strips fade, plastic lenses yellow and crack, and metal faces pit.")],
    ["Photograph the panel straight on and from the side, and any maker's name or model number on it.",
     "Count the buttons and note which ones don't work.",
     "Check whether the panel is flush in the wall or mounted on the surface.",
     "If wires are exposed, tell the super or managing agent the same day."],
    """<p>We open the panel and test the wiring behind it. In most cases the wiring is sound and only what you can see needs replacing.</p>
<p>Single buttons are replaced in the panel. A worn or broken face is replaced with a new faceplate. When the whole panel is beyond repair, we fit a new one sized to cover the old opening, connect it to the existing wires, and relabel every apartment.</p>""",
    """<p>Replacing a few buttons is a small job. A new panel is priced by the number of apartments, the finish, and whether it is audio or video: [PANEL RANGE]. Send a photo and we can usually give a range the same day.</p>""",
    """<p>The panel can be replaced without replacing the system. If the apartments are working, a new panel on the old wiring gives the building a new front door for a fraction of a full installation. It is also a good moment to move to video or to a vandal-resistant panel.</p>""",
    [("Can you match the old panel?", "Often, and when the original is discontinued we fit a panel sized to cover the same opening so the wall doesn't need repairing."),
     ("Can you update the names on the directory?", "Yes. We relabel as part of any panel repair, and can do it as a job by itself."),
     ("Is there a panel that's harder to vandalise?", "Yes. Heavy-gauge stainless panels with tamper-resistant fixings and protected buttons are made for exactly this."),
     ("Our panel was forced and the door now opens for anyone. What should we do?", "Treat it as urgent. Call {{tel}}. See [[intercom-repair/emergency/|emergency intercom repair]].")],
    [("intercom-repair/", "All intercom repairs"), ("intercom-repair/door-release/", "Door won't unlock"), ("intercom-repair/no-audio/", "No sound or static"), ("intercom-repair/emergency/", "Emergency repair")])

symptom(
    "intercom-repair/not-working/", "Intercom not working",
    "Intercom Not Working? What to Check and Who to Call in NYC | Jacob Intercom",
    "Whole-building intercom not working? The causes of a dead system, what to check before you call, and repair costs in New York.",
    "Intercom not working",
    "No buzz, no sound, no door release. When the whole system goes quiet, the cause is usually one failed part, and it is usually in the basement.",
    """<p>Nothing happens when a visitor presses any button. No apartment rings, nobody can talk, and the door can't be released from upstairs. It may have stopped suddenly, or grown fainter for weeks first.</p>
<p>A system that fails everywhere at once has almost always lost power or lost its amplifier. That is better news than it sounds: one repair brings every apartment back.</p>""",
    [("The power supply or transformer has failed", "This is the most common cause of a completely dead system. Transformers run hot for decades and then stop."),
     ("The amplifier has failed", "The amplifier is the centre of an older system. When it goes, every apartment goes with it."),
     ("A breaker has tripped or the unit was unplugged", "Work in the basement, a tripped breaker or a moved plug can switch the system off."),
     ("The main wiring has been cut", "Construction, a new boiler, or a cable installer working in the same space can cut the intercom's trunk wiring."),
     ("Water has reached the equipment", "A leak or a flooded basement will take out an amplifier quickly.")],
    ["Confirm it is the whole building: ask two neighbours on different floors.",
     "Ask the super whether any work was done in the basement, meter room or lobby recently.",
     "Have the super check the breaker panel for a tripped breaker and reset it once. If it trips again, leave it off.",
     "Find the intercom amplifier if you can, usually a metal box near the electric meters, and see whether it is plugged in. Don't open it."],
    """<p>We go straight to the power supply and amplifier and measure what is coming out. If there's no power, we replace the transformer or supply. If there's power but no signal, we repair or replace the amplifier. If the equipment is healthy, we trace the trunk wiring for a cut or a short.</p>
<p>Once the system is live again we test at the door and in a sample of apartments on every line.</p>""",
    """<p>A tripped breaker or a loose plug costs a service call. A new power supply or amplifier costs more, depending on the make: [AMPLIFIER RANGE]. Even so, it is the best-value repair there is, because it restores every apartment at once. You get the price before we start.</p>""",
    """<p>A failed amplifier in an otherwise sound system should be repaired or replaced like for like. If the amplifier is discontinued and no compatible unit exists, that is the point at which replacing the system makes sense, and the existing wiring can often be reused.</p>""",
    [("Is a dead intercom an emergency?", "It depends on the building. If residents can't let in home-care workers or deliveries, or the door has been propped open as a workaround, it's urgent. See [[intercom-repair/emergency/|emergency repair]]."),
     ("How long does a whole-building repair take?", "A power supply or amplifier swap is usually done in one visit when the part is in stock. If a part must be ordered, we tell you how long."),
     ("Our system is a Lee-Dan. Can it still be fixed?", "Yes. See [[lee-dan-intercom-systems/|Lee-Dan repair and service]]."),
     ("The intercom died after the power went out. Why?", "A surge when power returns can blow a transformer or fuse. It is a common and usually simple repair.")],
    [("intercom-repair/", "All intercom repairs"), ("intercom-repair/emergency/", "Emergency repair"), ("lee-dan-intercom-systems/", "Lee-Dan systems"), ("intercom-replacement/", "Replacement and upgrades")])

# ───────────────────────────── Emergency ─────────────────────────────

page(path="intercom-repair/emergency/", nav="Emergency repair",
     title="Emergency Intercom Repair NYC | Jacob Intercom",
     desc="Front door won't lock, or the whole building's intercom is down? Emergency intercom repair in New York. What counts as urgent and what to do first.",
     h1="Emergency intercom repair",
     lead="Some intercom faults can wait a few days. A front door that won't lock, or a building where nobody can be let in, can't.",
     facts=["Office hours <b>Mon to Thu 9 to 5, Fri 8 to 4</b>", "After hours: [AFTER-HOURS LINE]", "<b>35 years</b> in business"],
     body="""
<div class="note"><p><strong>If someone is in danger or there has been a break-in, call 911 first.</strong> We repair the equipment. We can't secure a building against an intruder.</p></div>
<h2>What counts as an emergency</h2>
<ul>
<li><strong>The front door won't lock.</strong> A strike stuck open, or a panel that has been forced, leaves the building open to anyone.</li>
<li><strong>The whole building is down</strong> and residents who rely on visitors can't let them in: home-care workers, medical deliveries, people who can't get down the stairs.</li>
<li><strong>Exposed or damaged wiring at the entrance,</strong> which can be used to trigger the door.</li>
<li><strong>The door won't release at all</strong> and there is no other way for residents' visitors to enter.</li>
</ul>
<p>A single apartment with a dead buzzer, or a crackly line, is a normal repair. Those are booked for the next opening. See [[intercom-repair/|intercom repair]].</p>
<h2>What to do right now</h2>
<ol>
<li><strong>If the door won't lock,</strong> have the super lock it with the key or deadbolt if the door has one, and post a notice for residents. Don't wedge it shut in a way that blocks the exit.</li>
<li><strong>If the door won't open,</strong> give residents a way to let visitors in by coming down, and tell anyone who depends on deliveries.</li>
<li><strong>Don't prop the door open.</strong> It solves the intercom problem by creating a worse one.</li>
<li><strong>Photograph the panel and any damage,</strong> and note the make if you can see it.</li>
<li><strong>Call {{tel}}.</strong> Tell us it's urgent and why.</li>
</ol>
<h2>When we can come</h2>
<p>During office hours, urgent calls go to the front of the schedule. Our hours are Monday to Thursday 9 to 5 and Friday 8 to 4.</p>
<p>Evenings, weekends and holidays: [AFTER-HOURS LINE AND TERMS].</p>
<h2>What an emergency visit covers</h2>
<p>The aim of the first visit is to make the entrance secure and usable again. That usually means freeing or replacing a stuck strike, restoring power to the system, or making a damaged panel safe. If a full repair needs a part we don't have with us, we leave the door secure and working and return with the part.</p>
<h2>What it costs</h2>
<p>During office hours, emergency repairs are priced like any other repair, most between $100 and $300. After-hours rates: [AFTER-HOURS RATE]. You get the price before we start.</p>
""",
     faqs=[("Do you offer 24-hour service?", "[AFTER-HOURS LINE AND TERMS]"),
           ("The door is stuck open. Can I fix it myself for now?", "If the door has a key lock or deadbolt, use that. Don't force the strike or cut wires, which can turn a simple repair into a larger one."),
           ("We manage several buildings. Can we get priority service?", "Yes, through a maintenance contract. See [[intercom-maintenance-contract/|maintenance contracts]] or call {{tel}}.")],
     related=[("intercom-repair/", "All intercom repairs"), ("intercom-repair/door-release/", "Door release repair"), ("intercom-repair/not-working/", "Intercom not working"), ("contact/", "Contact us")])

# ───────────────────────────── Lee-Dan hub ─────────────────────────────

page(path="lee-dan-intercom-systems/", nav="Lee-Dan",
     title="Lee-Dan Intercom Repair, Parts & Service NYC | Jacob Intercom",
     desc="Lee-Dan intercom repair in New York: IR-203, IR-204 and IR-205 apartment stations, PK-543 amplifiers and lobby panels. Repair, parts and upgrades on existing wiring.",
     h1="Lee-Dan intercom repair and service",
     lead="Lee-Dan systems are in buildings all over New York, and most of them can be repaired. We fix them, find the parts, and tell you plainly when replacing is the better money.",
     facts=["<b>IR-203, IR-204, IR-205</b> stations", "<b>PK-543</b> amplifiers", "Lobby panels and parts", "<b>35 years</b> in business"],
     aside={"head": "Got a Lee-Dan that's stopped working?", "text": "Send a photo of the apartment station and the lobby panel. We can usually tell you the model and the likely fault from the picture."},
     body="""
<div class="note"><p><strong>For Jacob to confirm before launch:</strong> the technical details on this page are drawn from published Lee-Dan product information. Fault patterns, parts availability and prices need his review. Dealer status: [AUTHORISED DEALER OR NOT].</p></div>
<h2>Why so many New York buildings have one</h2>
<p>Lee-Dan Communications is a Long Island manufacturer that has supplied apartment intercoms to the New York market for decades. Its systems were fitted in walk-ups, pre-war elevator buildings, co-ops and small multi-family houses across the five boroughs, and a great many are still in daily use.</p>
<p>The design is simple and the parts are sturdy, which is why they last. It is also why a Lee-Dan that has stopped working is usually worth repairing.</p>
<h2>How to tell if yours is a Lee-Dan</h2>
<ul>
<li>The apartment station is a plain wall unit with <strong>Talk</strong>, <strong>Listen</strong> and <strong>Door</strong> buttons.</li>
<li>Look for the Lee-Dan name, or a model number such as IR-204, on the unit or on a label behind it.</li>
<li>The lobby panel is a metal plate with a column of push buttons, a speaker grille and a name directory.</li>
<li>The amplifier is a metal box, often in the basement near the electric meters.</li>
</ul>
<p>Not sure? Send us a photo. We can tell from the picture.</p>
<h2>The models we service</h2>
<div class="tablebox"><table>
<thead><tr><th scope="col">Model</th><th scope="col">What it is</th><th scope="col">Where you find it</th></tr></thead>
<tbody>
<tr><th scope="row">[[lee-dan-intercom-systems/ir-203/|IR-203]]</th><td>Three-wire apartment station</td><td>Buildings upgraded from an old bell-and-buzzer system, reusing the original wiring</td></tr>
<tr><th scope="row">[[lee-dan-intercom-systems/ir-204/|IR-204]]</th><td>Four-wire apartment station</td><td>The economical standard in many walk-ups and small buildings</td></tr>
<tr><th scope="row">[[lee-dan-intercom-systems/ir-205/|IR-205]]</th><td>Five-wire apartment station</td><td>Older five-wire systems and buildings with more than one entrance</td></tr>
<tr><th scope="row">[[lee-dan-intercom-systems/pk-543-amplifier/|PK-543]]</th><td>Amplifier and power unit</td><td>The centre of the system, usually in the basement</td></tr>
<tr><th scope="row">[[lee-dan-intercom-systems/lobby-panels/|Lobby panels]]</th><td>Entry panel with buttons, speaker and directory</td><td>At the front door or in the vestibule</td></tr>
</tbody></table></div>
<p>The wire count matters. A three-wire, four-wire and five-wire station look alike on the wall and are not interchangeable. Fitting the wrong one is the most common mistake we are called to correct. See the [[lee-dan-intercom-systems/wiring/|Lee-Dan wiring guide]].</p>
<h2>What goes wrong</h2>
<ul>
<li><strong>One apartment stops working.</strong> The station has failed or a wire behind it has come loose. [[intercom-repair/door-buzzer/|More on dead buzzers]].</li>
<li><strong>Everyone can listen but nobody can talk, or the reverse.</strong> This points to the amplifier or to the speaker and microphone in the lobby panel. [[intercom-repair/no-audio/|More on audio faults]].</li>
<li><strong>The whole building is silent.</strong> The amplifier or its power supply has failed. [[intercom-repair/not-working/|More on dead systems]].</li>
<li><strong>It talks, but the door won't open.</strong> The fault is at the door strike or its power feed, not the intercom. [[intercom-repair/door-release/|More on door release]].</li>
<li><strong>Buttons at the door don't call.</strong> The lobby panel's buttons are worn. [[intercom-repair/entry-panel/|More on panel repair]].</li>
</ul>
<p>[JACOB: THE THREE FAULTS HE SEES MOST ON LEE-DAN SYSTEMS, AND WHAT CAUSES THEM]</p>
<h2>Repair, parts and replacement</h2>
<h3>Repair</h3>
<p>We test the amplifier, the lobby panel and the affected lines, replace the part that has failed, and test every affected apartment before leaving. Most single-apartment repairs take one visit.</p>
<h3>Parts</h3>
<p>Lee-Dan stations, amplifiers and panel components are still sold. [PARTS JACOB STOCKS]. See [[lee-dan-intercom-systems/parts/|Lee-Dan parts]].</p>
<h3>Replacement and upgrade</h3>
<p>When a system has reached the end of its life, the existing wiring can often carry a newer one, including video. That avoids opening walls, which is most of the cost of a new installation. See [[lee-dan-intercom-systems/replacement/|Lee-Dan replacement and upgrades]].</p>
<h2>What it costs</h2>
<p>Most single-fault Lee-Dan repairs fall in our usual range of <strong>$100 to $300</strong>. Amplifier and lobby panel replacements cost more: [LEE-DAN AMPLIFIER AND PANEL PRICES]. You get the price before we start.</p>
<h2>"We were told it can't be fixed"</h2>
<p>We hear this often. Sometimes it's true: the wiring has failed throughout, or the building wants features the old system can't provide. More often the company that said it doesn't work on older systems. If you've been quoted a full replacement for a Lee-Dan with one fault, call us before you sign.</p>
""",
     faqs=[("Does anyone still repair Lee-Dan intercoms in NYC?", "Yes. We repair Lee-Dan apartment stations, amplifiers and lobby panels across all five boroughs."),
           ("Are Lee-Dan parts still available?", "Yes. Lee-Dan stations, amplifiers and panel parts are still sold by the manufacturer and its distributors."),
           ("Can I replace a Lee-Dan apartment station myself?", "Only with the exact wire-count match. An IR-203, IR-204 and IR-205 look similar and are wired differently, and the wrong unit can disable the line for your neighbours."),
           ("Can a Lee-Dan system be upgraded to video?", "Often, and sometimes on the existing wiring. It depends on how many wires run to each apartment and their condition, which we test on site."),
           ("How much does a Lee-Dan repair cost?", "Most single-fault repairs cost $100 to $300. Amplifiers and lobby panels cost more. We give you the price before starting.")],
     related=[("intercom-repair/", "All intercom repairs"), ("intercom-repair/not-working/", "Intercom not working"), ("brands/", "Other brands we service"), ("contact/", "Contact us")])

# ───────────────────────────── Contact ─────────────────────────────

page(path="contact/", nav="Contact",
     title="Contact Jacob Intercom: Call, Text or Send a Photo",
     desc="Call 718-252-2730 or 212-837-2147, or send a photo of your intercom panel for a price range. 209 Avenue F, Brooklyn. Serving all five boroughs.",
     h1="Contact Jacob Intercom",
     lead="The quickest way to a price is a photo of the entry panel and the apartment station. Or call, and a person will answer during office hours.",
     facts=["<b>718-252-2730</b>", "<b>212-837-2147</b>", "Mon to Thu 9 to 5, Fri 8 to 4"], no_reviews=True,
     aside={"head": "Is it urgent?", "text": "If the front door won't lock or the whole building is down, see [[intercom-repair/emergency/|emergency repair]] and call {{tel}}."},
     body="""
<h2>Call or text</h2>
<p><strong>{{tel}}</strong></p>
<p><strong>{{tel2}}</strong></p>
<p>Email: <a href="mailto:jacobintercom@gmail.com">jacobintercom@gmail.com</a></p>
<p>Text a photo to: [NUMBER THAT ACCEPTS TEXTS]</p>
<h2>Hours</h2>
<div class="tablebox"><table>
<thead><tr><th scope="col">Day</th><th scope="col">Hours</th></tr></thead>
<tbody>
<tr><th scope="row">Monday to Thursday</th><td>9:00 am to 5:00 pm</td></tr>
<tr><th scope="row">Friday</th><td>8:00 am to 4:00 pm</td></tr>
<tr><th scope="row">Saturday and Sunday</th><td>Closed</td></tr>
<tr><th scope="row">After hours</th><td>[AFTER-HOURS LINE]</td></tr>
</tbody></table></div>
<h2>Where we are</h2>
<p>Jacob Intercom<br>209 Avenue F<br>Brooklyn, NY 11218</p>
<p>We travel to you. Our technicians cover Brooklyn, Manhattan, Queens, the Bronx and Staten Island, and take jobs on Long Island, in Westchester and in New Jersey.</p>
<h2>What to send us</h2>
<p>These four things let us give you a price range before anyone drives out:</p>
<ol>
<li>A photo of the entry panel at the front door.</li>
<li>A photo of the station inside an apartment.</li>
<li>What it's doing, and whether it affects one apartment or all of them.</li>
<li>The building's address and how many apartments it has.</li>
</ol>
<h2>Property managers and boards</h2>
<p>We send a certificate of insurance before the first visit and quote in writing. For several buildings, ask about one invoice across the portfolio and a yearly maintenance contract. See [[property-managers/|property managers]].</p>
""",
     related=[("intercom-repair/", "Intercom repair"), ("lee-dan-intercom-systems/", "Lee-Dan systems"), ("intercom-repair/emergency/", "Emergency repair")])

# ───────────────────────────── Lee-Dan section ─────────────────────────────

LD = "lee-dan-intercom-systems/"
LD_RELATED = [(LD, "Lee-Dan repair and service"), (LD + "troubleshooting/", "Lee-Dan troubleshooting"),
              (LD + "parts/", "Lee-Dan parts"), (LD + "replacement/", "Replacement and upgrades")]
LD_ASIDE = {"head": "Got a Lee-Dan that's stopped working?",
            "text": "Send a photo of the apartment station and the lobby panel. We can usually tell you the model and the likely fault from the picture."}
REVIEW = '<div class="note"><p><strong>For Jacob to review before launch.</strong> Specifications here come from published Lee-Dan product data. Fault patterns and prices are his to confirm.</p></div>'


def ld(slug, nav, title, desc, h1, lead, body, faqs, facts=None):
    page(path=LD + slug + "/", nav=nav, title=title, desc=desc, h1=h1, lead=lead,
         facts=facts or ["<b>Lee-Dan</b> specialists", "Most repairs <b>$100 to $300</b>", "<b>35 years</b> in business"],
         aside=LD_ASIDE, body=REVIEW + body, faqs=faqs, related=LD_RELATED)


def station(slug, model, wires, commons, where, extra):
    ld(slug, model, f"Lee-Dan {model} Intercom Station: Repair & Replacement NYC | Jacob Intercom",
       f"Lee-Dan {model} {wires}-wire apartment intercom station: how to identify it, what goes wrong, and repair or replacement in New York.",
       f"Lee-Dan {model} apartment station",
       f"The {model} is Lee-Dan's {wires}-wire apartment station. {where}",
       f"""
<h2>What the {model} is</h2>
<p>The {model} is the unit on the apartment wall: a speaker, and three push buttons marked <strong>Talk</strong>, <strong>Listen</strong> and <strong>Door</strong>. When a visitor presses your button at the entrance, it sounds a tone. You hold Talk to speak, Listen to hear the reply, and press Door to let them in.</p>
<p>It connects with <strong>{wires} wires</strong>: {commons} shared by every apartment on the system, and one that is yours alone and carries your call signal.</p>
{extra}
<h2>How to tell which model you have</h2>
<p>The IR-203, IR-204 and IR-205 look the same from the front. The difference is the number of wires behind them. The model number is printed on the unit, usually on the back or inside. If you can't find it, we identify it by taking the station off the wall and counting the connected wires.</p>
<div class="tablebox"><table>
<thead><tr><th scope="col">Model</th><th scope="col">Wires</th><th scope="col">Shared</th><th scope="col">Your own</th></tr></thead>
<tbody>
<tr><th scope="row">[[{LD}ir-203/|IR-203]]</th><td>3</td><td>2</td><td>1</td></tr>
<tr><th scope="row">[[{LD}ir-204/|IR-204]]</th><td>4</td><td>3</td><td>1</td></tr>
<tr><th scope="row">[[{LD}ir-205/|IR-205]]</th><td>5</td><td>4</td><td>1</td></tr>
</tbody></table></div>
<h2>What goes wrong</h2>
<ul>
<li><strong>No tone when a visitor calls.</strong> The speaker has failed, or your own call wire is broken or loose.</li>
<li><strong>You can hear but can't be heard, or the reverse.</strong> The Talk or Listen button contacts are worn.</li>
<li><strong>The Door button does nothing.</strong> The button contact has failed, or the fault is at the door. Ask a neighbour to try theirs.</li>
<li><strong>It stopped after painting or renovation.</strong> A wire was pulled off its terminal, or the station was put back on the wrong wires.</li>
</ul>
<p>[JACOB: THE FAULTS HE SEES MOST ON THE {model}]</p>
<h2>Repair or replace the station?</h2>
<p>A station with a failed speaker or worn buttons is replaced, not repaired. The part is inexpensive and the swap is quick. What matters is fitting the right model: a station with the wrong wire count will not work and can disable the line for other apartments.</p>
<p>The current version is the {model}E, which is also sold as a direct replacement for the matching TekTone station.</p>
<h2>What it costs</h2>
<p>Replacing one apartment station usually falls at the low end of our <strong>$100 to $300</strong> repair range. Several stations in one visit cost less each: [PER-STATION PRICE]. You get the price before we start.</p>
""",
       [(f"Can I swap an {model} for a different Lee-Dan model?", "Only if the building's wiring supports it. The three models use different numbers of wires, so they are not interchangeable on the same line."),
        (f"Is the {model} still made?", f"Yes. The current version is the {model}E, sold by Lee-Dan and its distributors."),
        ("Can I fit one myself?", "The wires must go back on the same terminals they came off. If they are mixed up, your station won't work and your neighbours' may stop too. If you do it yourself, photograph the wiring before disconnecting anything."),
        ("Mine works, but the plastic has yellowed and cracked. Can it be replaced?", "Yes. A new station on the same wires takes a few minutes per apartment.")],
       facts=[f"<b>{wires}-wire</b> apartment station", "Talk, Listen and Door buttons", "Most repairs <b>$100 to $300</b>"])


station("ir-203", "IR-203", 3, "two", "It is the one fitted when an old bell-and-buzzer system was upgraded to voice without running new wire.",
        "<p>That short wire count is the point of the IR-203. Buildings that had only a bell and a door buzzer already had enough wire in the walls for a three-wire intercom, so they could gain a voice system without opening the walls.</p>")
station("ir-204", "IR-204", 4, "three", "It is the most common Lee-Dan station in New York walk-ups and small apartment buildings.",
        "<p>The IR-204 is the standard choice and the one we replace most. The current IR-204E has a 2&frac12;-inch speaker, a white impact-resistant case about 7 inches tall and 5 wide, Braille markings on the buttons, and fits a standard single electrical box or mounts on the wall surface.</p>")
station("ir-205", "IR-205", 5, "four", "It is found on older five-wire systems and in buildings with more than one entrance.",
        "<p>The extra wire is what older five-wire systems and some multi-entrance buildings need. If your building was wired for five, a four-wire station will not do the job.</p>")

ld("pk-543-amplifier", "PK-543 amplifier",
   "Lee-Dan PK-543 Amplifier Repair & Replacement NYC | Jacob Intercom",
   "The Lee-Dan PK-543A amplifier powers the whole building's intercom. Signs it has failed, what can be adjusted, and replacement in New York.",
   "Lee-Dan PK-543 amplifier",
   "The PK-543 is the centre of a Lee-Dan system. When the whole building goes quiet, this is usually where the fault is.",
   """
<h2>What the PK-543 does</h2>
<p>The PK-543A is a small power-pack amplifier, about the size of a paperback, usually fixed to a wall in the basement, a meter room or a lobby closet. One unit does three jobs for the whole building:</p>
<ul>
<li><strong>It amplifies the voice</strong> between the entrance panel and every apartment.</li>
<li><strong>It makes the call tone</strong> each apartment hears when a visitor presses a button.</li>
<li><strong>It switches the door release</strong> when a resident presses Door.</li>
</ul>
<p>It works with three-wire, four-wire and five-wire apartment stations, which is why the same amplifier is found behind IR-203, IR-204 and IR-205 systems. It runs from a separate 16-volt transformer.</p>
<h2>Signs the amplifier has failed</h2>
<ul>
<li>No apartment gets a tone, and nobody can talk or listen.</li>
<li>Sound is very faint in every apartment, or fades in and out.</li>
<li>Talking works but no apartment can release the door.</li>
<li>A constant hum on every station.</li>
</ul>
<p>If only some apartments are affected, the amplifier is probably fine and the fault is in the wiring or the stations. See [[lee-dan-intercom-systems/troubleshooting/|Lee-Dan troubleshooting]].</p>
<h2>It may only need adjusting</h2>
<p>The PK-543A has two adjustments on its front, set with a small screwdriver: one for voice volume and one for tone volume. If the whole building is faint but working, or the call tone is too quiet, the setting may have been turned down. That is a short visit, not a replacement.</p>
<p>It also has a switch that sets how long the door stays released after the button is pressed, and it can drive the door strike on AC or DC. A door that releases for too short a time to push open can sometimes be fixed here.</p>
<h2>Check the transformer first</h2>
<p>The amplifier gets its power from a separate transformer. A dead system is as often a failed transformer or a tripped breaker as a failed amplifier. We test the supply before condemning the amplifier, because the transformer is the cheaper part.</p>
<h2>Replacement</h2>
<p>The PK-543A is still sold, and it is interchangeable with the TekTone amplifier of the same number. The unit plugs into a wired connector, so in many buildings a replacement is quick and the building's wiring is not disturbed.</p>
<p>Buildings with more than one entrance use an additional unit, the PK-502B, alongside it.</p>
<h2>What it costs</h2>
<p>An adjustment or a transformer replacement is at the lower end. A new amplifier, fitted and tested: [PK-543 REPLACEMENT PRICE]. It restores every apartment at once, which makes it the best-value repair on a Lee-Dan system. You get the price before we start.</p>
""",
   [("Where is the amplifier in my building?", "Usually in the basement near the electric meters, in a utility closet, or in the lobby ceiling or a closet near the front door. The super normally knows."),
    ("Can a PK-543 be repaired, or only replaced?", "Adjustments and connection faults are repaired. A unit that has failed internally is replaced, which is quicker and more reliable than a bench repair."),
    ("Will a new amplifier fix a system that's been getting worse for years?", "If the gradual decline was the amplifier, yes. If stations and wiring have been failing too, the amplifier is only part of it. We test before recommending."),
    ("Is the PK-543A the same as the TekTone PK543A?", "They are sold as interchangeable replacements for each other.")],
   facts=["Powers the <b>whole building</b>", "Works with <b>3, 4 and 5-wire</b> stations", "Still available"])

ld("lobby-panels", "Lobby panels",
   "Lee-Dan Lobby Panel Repair & Replacement NYC | Jacob Intercom",
   "Lee-Dan lobby panel repair in New York: worn buttons, corroded speakers, faded directories and full panel replacement on existing wiring.",
   "Lee-Dan lobby panels",
   "The panel at the front door takes the weather, the wear and the abuse. It is also the part of a Lee-Dan system that is easiest to renew.",
   """
<h2>What the lobby panel does</h2>
<p>The lobby panel is the metal plate at the entrance with a push button for each apartment, a speaker and microphone behind a grille, and a directory of names. Pressing a button sends the call signal up that apartment's own wire. The speaker and microphone carry the conversation through the amplifier.</p>
<h2>What goes wrong</h2>
<ul>
<li><strong>Some buttons don't call.</strong> The switch behind each button wears out. The busiest apartments fail first.</li>
<li><strong>Nobody upstairs can hear visitors, or visitors can't hear residents.</strong> The panel's speaker or microphone has corroded. Because every apartment shares it, one failed part affects the whole building.</li>
<li><strong>Crackle that comes and goes with the weather.</strong> Water is getting behind the faceplate.</li>
<li><strong>The directory is unreadable.</strong> Name strips fade and the lens over them yellows.</li>
<li><strong>The panel has been forced or damaged.</strong> See [[intercom-repair/entry-panel/|damaged entry panel repair]].</li>
</ul>
<h2>Repairing the panel</h2>
<p>Buttons, the speaker and the microphone can each be replaced inside the existing panel. We also reseal panels that are letting water in and relabel the directory.</p>
<h2>Replacing the panel</h2>
<p>When the face is corroded or damaged throughout, a new panel is better value than replacing its parts one at a time. Lee-Dan panels are made in stainless steel and brass, flush or surface mounted, in sizes from two buttons up. We fit one that covers the old opening, connect it to the existing wires, and label every apartment.</p>
<p>The apartments are not touched. If the stations upstairs work, a new panel gives the building a new front door without a new system.</p>
<p>[JACOB: PANEL SIZES AND FINISHES HE STOCKS OR CAN GET QUICKLY]</p>
<h2>What it costs</h2>
<p>A few buttons or a speaker fall in our usual <strong>$100 to $300</strong> range. A new panel is priced by the number of buttons and the finish: [LEE-DAN PANEL PRICES]. Send a photo for a range.</p>
""",
   [("Can you add a button for a new apartment?", "If the panel has a spare position and there is a wire to that apartment, yes. If not, the panel is replaced with a larger one."),
    ("Can a Lee-Dan audio panel be replaced with a video panel?", "Yes, as part of an upgrade. See [[lee-dan-intercom-systems/replacement/|Lee-Dan replacement and upgrades]]."),
    ("Do you update the names on the directory?", "Yes, as part of a repair or as a job by itself.")])

ld("wiring", "Wiring guide",
   "Lee-Dan Intercom Wiring Explained: 3, 4 and 5 Wire Systems | Jacob Intercom",
   "How Lee-Dan intercom wiring works: common and selective wires, the difference between 3, 4 and 5-wire systems, and why the wire count matters for repairs and upgrades.",
   "Lee-Dan wiring guide",
   "Almost every mistake made on a Lee-Dan system comes down to the wire count. Here is how the wiring works, in plain terms.",
   """
<h2>Common wires and selective wires</h2>
<p>A Lee-Dan system uses two kinds of wire.</p>
<ul>
<li><strong>Common wires</strong> run to every apartment. They carry the things everyone shares: the voice in each direction and the door release.</li>
<li><strong>A selective wire</strong> runs to one apartment only. It carries that apartment's call signal from its button at the door.</li>
</ul>
<p>So each apartment station has several common wires plus one selective wire of its own.</p>
<div class="tablebox"><table>
<thead><tr><th scope="col">System</th><th scope="col">Station</th><th scope="col">Common wires</th><th scope="col">Selective wire</th><th scope="col">Total at each station</th></tr></thead>
<tbody>
<tr><th scope="row">Three-wire</th><td>[[lee-dan-intercom-systems/ir-203/|IR-203]]</td><td>2</td><td>1</td><td>3</td></tr>
<tr><th scope="row">Four-wire</th><td>[[lee-dan-intercom-systems/ir-204/|IR-204]]</td><td>3</td><td>1</td><td>4</td></tr>
<tr><th scope="row">Five-wire</th><td>[[lee-dan-intercom-systems/ir-205/|IR-205]]</td><td>4</td><td>1</td><td>5</td></tr>
</tbody></table></div>
<p>The cable running up the building carries the common wires plus one selective wire for every apartment on that line. A ten-apartment riser on a four-wire system needs at least thirteen conductors: three common and ten selective.</p>
<h2>Why the difference shows up as faults</h2>
<ul>
<li><strong>A fault on a selective wire affects one apartment.</strong> That apartment's buzzer stops and everyone else is fine.</li>
<li><strong>A fault on a common wire affects everyone on that line.</strong> A whole column of apartments loses voice or door release together.</li>
<li><strong>Two selective wires touching</strong> makes two apartments ring together.</li>
</ul>
<p>This is why the first question we ask is how many apartments are affected. The answer usually tells us which kind of wire has failed before we arrive.</p>
<h2>Why the wire count matters when replacing a station</h2>
<p>The three station models look alike and are built for different wire counts. A four-wire station on a three-wire line has a terminal with nothing to connect to, and it will not work. Putting a wire on the wrong terminal can short a common wire and take out the whole line.</p>
<p>If you are replacing a station yourself, photograph the wires on their terminals before you remove anything, and fit the same model that came off.</p>
<h2>Why it matters for upgrades</h2>
<p>Wire that is already in the walls is the most valuable part of an old system. Newer video intercoms, including Lee-Dan's own 2Easy range, run on two wires. A building wired for a three, four or five-wire Lee-Dan often has enough good conductors to carry one, which means video without opening walls. We test the existing wire before quoting. See [[lee-dan-intercom-systems/replacement/|replacement and upgrades]] and [[lee-dan-intercom-systems/2easy/|Lee-Dan 2Easy]].</p>
<h2>Diagrams</h2>
<p>[WIRING DIAGRAMS TO BE DRAWN FOR THE SITE AND CHECKED BY JACOB]</p>
""",
   [("How do I know if my building is three, four or five-wire?", "Count the wires connected to the back of an apartment station, or read the model number on it: IR-203 is three, IR-204 is four, IR-205 is five."),
    ("Is intercom wiring dangerous to touch?", "The wiring to the stations is low voltage. The transformer that feeds the amplifier is connected to mains power and should be left to an electrician or intercom technician."),
    ("Can old intercom wire be reused for a new system?", "Often. It depends on how many conductors there are and their condition, which we test on site.")],
   facts=["<b>3, 4 and 5-wire</b> systems explained", "Common and selective wires", "Why the count matters"])

ld("troubleshooting", "Troubleshooting",
   "Lee-Dan Intercom Troubleshooting Guide | Jacob Intercom",
   "Lee-Dan intercom not working? Match the symptom to the likely part: apartment station, lobby panel, PK-543 amplifier, transformer, wiring or door strike.",
   "Lee-Dan troubleshooting guide",
   "Match what the system is doing to the part that has most likely failed. Two questions narrow it down: how many apartments are affected, and which function has stopped.",
   """
<h2>Start with how many apartments are affected</h2>
<div class="tablebox"><table>
<thead><tr><th scope="col">Who has the problem</th><th scope="col">Where the fault usually is</th></tr></thead>
<tbody>
<tr><th scope="row">One apartment</th><td>That apartment's station, or its own selective wire</td></tr>
<tr><th scope="row">A column of apartments, one above another</th><td>A common wire in the riser they share</td></tr>
<tr><th scope="row">Two apartments ring together</th><td>Their two selective wires are touching</td></tr>
<tr><th scope="row">The whole building</th><td>The transformer, the PK-543 amplifier, or the lobby panel</td></tr>
</tbody></table></div>
<h2>Then by symptom</h2>
<div class="tablebox"><table>
<thead><tr><th scope="col">What it does</th><th scope="col">Most likely cause</th><th scope="col">Read more</th></tr></thead>
<tbody>
<tr><th scope="row">No tone in one apartment</th><td>Failed station speaker, or a broken selective wire</td><td>[[lee-dan-intercom-systems/ir-204/|Apartment stations]]</td></tr>
<tr><th scope="row">No tone anywhere</th><td>No power: transformer or breaker. Then the amplifier.</td><td>[[lee-dan-intercom-systems/pk-543-amplifier/|PK-543 amplifier]]</td></tr>
<tr><th scope="row">One lobby button doesn't call</th><td>Worn button in the lobby panel</td><td>[[lee-dan-intercom-systems/lobby-panels/|Lobby panels]]</td></tr>
<tr><th scope="row">Residents can't hear visitors, building-wide</th><td>Lobby panel microphone, or the amplifier</td><td>[[lee-dan-intercom-systems/lobby-panels/|Lobby panels]]</td></tr>
<tr><th scope="row">Visitors can't hear residents, building-wide</th><td>Lobby panel speaker, or the amplifier</td><td>[[lee-dan-intercom-systems/lobby-panels/|Lobby panels]]</td></tr>
<tr><th scope="row">One resident can't be heard</th><td>Worn Talk button in that station</td><td>[[lee-dan-intercom-systems/ir-204/|Apartment stations]]</td></tr>
<tr><th scope="row">Everything is faint</th><td>Amplifier volume setting, or a failing amplifier</td><td>[[lee-dan-intercom-systems/pk-543-amplifier/|PK-543 amplifier]]</td></tr>
<tr><th scope="row">Constant hum</th><td>Failing transformer or amplifier, or a shorted common wire</td><td>[[lee-dan-intercom-systems/wiring/|Wiring guide]]</td></tr>
<tr><th scope="row">Talking works, door won't release for anyone</th><td>Door strike, its power feed, or the amplifier's release circuit</td><td>[[intercom-repair/door-release/|Door release repair]]</td></tr>
<tr><th scope="row">Door releases too briefly to open</th><td>Release timing on the amplifier, or a misaligned strike</td><td>[[lee-dan-intercom-systems/pk-543-amplifier/|PK-543 amplifier]]</td></tr>
<tr><th scope="row">Stopped working after renovation or painting</th><td>Wires off their terminals, or back on the wrong ones</td><td>[[lee-dan-intercom-systems/wiring/|Wiring guide]]</td></tr>
</tbody></table></div>
<h2>What residents and supers can check</h2>
<ul>
<li>Ask neighbours above, below and across the hall whether theirs works. This is the most useful thing you can tell us.</li>
<li>Have the super check for a tripped breaker and reset it once.</li>
<li>Check that the amplifier's transformer is plugged in, if it is the plug-in type.</li>
<li>Photograph the apartment station, the lobby panel and the amplifier.</li>
</ul>
<h2>What to leave alone</h2>
<p>Don't swap wires between terminals to see what happens. A shorted common wire can take out the whole line and can damage the amplifier. Don't open the transformer or anything connected to mains power.</p>
<p>[JACOB: ANY LEE-DAN FAULT HE SEES OFTEN THAT ISN'T IN THIS TABLE]</p>
""",
   [("My Lee-Dan works for everyone but me. What is it?", "Your station or your own call wire. It is the quickest Lee-Dan repair."),
    ("The whole building went dead at once. Is the system finished?", "Almost never. A sudden building-wide failure is usually the transformer or the amplifier, and replacing either brings every apartment back."),
    ("Can you diagnose it from a photo?", "A photo tells us the model and often narrows the fault. We confirm on site before quoting.")],
   facts=["Match the <b>symptom</b> to the part", "One apartment or the whole building?", "<b>35 years</b> of Lee-Dan work"])

ld("repair", "Lee-Dan repair",
   "Lee-Dan Intercom Repair NYC | Jacob Intercom",
   "Lee-Dan intercom repair across New York's five boroughs. Apartment stations, PK-543 amplifiers, lobby panels and wiring. Most repairs $100 to $300.",
   "Lee-Dan intercom repair",
   "If you have been told nobody fixes Lee-Dan any more, that isn't true. We repair them every week.",
   """
<h2>What we repair</h2>
<ul>
<li><strong>Apartment stations:</strong> [[lee-dan-intercom-systems/ir-203/|IR-203]], [[lee-dan-intercom-systems/ir-204/|IR-204]] and [[lee-dan-intercom-systems/ir-205/|IR-205]], replaced like for like.</li>
<li><strong>Amplifiers:</strong> the [[lee-dan-intercom-systems/pk-543-amplifier/|PK-543]], adjusted, reconnected or replaced, along with its transformer.</li>
<li><strong>Lobby panels:</strong> [[lee-dan-intercom-systems/lobby-panels/|buttons, speakers, microphones and whole panels]].</li>
<li><strong>Wiring:</strong> broken, shorted and crossed wires between the panel, the amplifier and the apartments.</li>
<li><strong>Door release:</strong> the strike and its power feed. See [[intercom-repair/door-release/|door release repair]].</li>
</ul>
<h2>How a Lee-Dan repair goes</h2>
<ol>
<li><strong>You tell us how many apartments are affected</strong> and what has stopped: the tone, the voice, or the door.</li>
<li><strong>We test power first,</strong> at the transformer and the amplifier.</li>
<li><strong>Then the lobby panel,</strong> because one fault there affects everyone.</li>
<li><strong>Then the line</strong> to the affected apartments, and the stations themselves.</li>
<li><strong>You get the price,</strong> we make the repair, and we test every affected apartment before leaving.</li>
</ol>
<h2>Why these systems are worth repairing</h2>
<p>A Lee-Dan system is a handful of simple parts. The stations are inexpensive, the amplifier is a single small unit, and all of it is still sold. When one part fails, replacing that part restores the system. A full replacement is only worth considering when the wiring has failed throughout or the building wants video or phone entry.</p>
<h2>What it costs</h2>
<p>Most single-fault repairs cost <strong>$100 to $300</strong>. Amplifier and lobby panel replacements cost more: [LEE-DAN AMPLIFIER AND PANEL PRICES]. You get the price before we start.</p>
<h2>Where we work</h2>
<p>Brooklyn, Manhattan, Queens, the Bronx and Staten Island, and we take Lee-Dan jobs on Long Island, in Westchester and in New Jersey.</p>
""",
   [("Does anyone still repair Lee-Dan intercoms?", "Yes. We do, across all five boroughs."),
    ("How long does a Lee-Dan repair take?", "A single apartment station is usually done in under an hour. An amplifier replacement is usually one visit."),
    ("Another company quoted us a whole new system. Should we get a second opinion?", "Yes, if the system has one fault. Call {{tel}} before you sign."),
    ("Do you work on TekTone systems too?", "Yes. Many TekTone and Lee-Dan parts are interchangeable. See [[brands/tektone/|TekTone]].")])

ld("replacement", "Replacement and upgrades",
   "Lee-Dan Intercom Replacement & Upgrade NYC | Jacob Intercom",
   "Replacing or upgrading a Lee-Dan intercom in New York: like-for-like renewal, a new lobby panel, or video on the existing wiring. How to choose.",
   "Lee-Dan replacement and upgrades",
   "When repair is no longer the right answer, there are three ways forward. Which one fits depends on the wiring and on what the building wants.",
   """
<h2>When to stop repairing</h2>
<p>Repair is the right choice while faults are isolated. It stops being the right choice when:</p>
<ul>
<li>Different parts keep failing, month after month.</li>
<li>The wiring itself is failing in several places.</li>
<li>The building wants something the system can't do: seeing who is at the door, or answering from a phone.</li>
<li>The entrance is being renovated anyway.</li>
</ul>
<h2>Three ways forward</h2>
<div class="tablebox"><table>
<thead><tr><th scope="col">Option</th><th scope="col">What changes</th><th scope="col">Best when</th></tr></thead>
<tbody>
<tr><th scope="row">Renew like for like</th><td>New stations, amplifier and panel of the same type, on the same wires</td><td>The wiring is sound and the building is happy with audio</td></tr>
<tr><th scope="row">New lobby panel only</th><td>A new panel at the door. Apartments untouched.</td><td>The stations work and the entrance looks tired or is damaged</td></tr>
<tr><th scope="row">Upgrade to video</th><td>A video panel and a monitor in each apartment, often on the existing wires</td><td>The building wants to see visitors, and the wiring tests well</td></tr>
</tbody></table></div>
<h2>Reusing the wire</h2>
<p>Running new cable through finished walls is the most expensive and disruptive part of any intercom job. A Lee-Dan building already has three, four or five wires to every apartment. Many newer systems need only two.</p>
<p>That means a video upgrade is often possible without opening a single wall. We test every line first, because old wire can be broken or corroded where you can't see it, and we tell you which apartments, if any, would need new cable.</p>
<h2>What we check before quoting</h2>
<ol>
<li>How many wires reach each apartment, and whether each one is intact.</li>
<li>The condition of the riser cable and any junction boxes.</li>
<li>The size of the opening behind the lobby panel.</li>
<li>Where the amplifier and power supply are, and whether a new system needs more power there.</li>
<li>What the door strike is, and whether it should be replaced at the same time.</li>
</ol>
<h2>Systems we install in place of an old Lee-Dan</h2>
<p>Lee-Dan's own [[lee-dan-intercom-systems/2easy/|2Easy two-wire video range]], and systems from [[brands/aiphone/|Aiphone]], [[brands/comelit/|Comelit]], [[brands/akuvox/|Akuvox]] and [[brands/butterflymx/|ButterflyMX]]. [JACOB: WHICH HE RECOMMENDS MOST OFTEN, AND WHY]</p>
<h2>What it costs</h2>
<p>Price depends on the number of apartments and entrances and on how much wire can be reused: [REPLACEMENT PRICE RANGE BY BUILDING SIZE]. We give a written quote after testing the wiring.</p>
""",
   [("Can we keep our Lee-Dan apartment stations and just change the panel?", "Yes, if the stations work. A new panel on the existing wiring is the least expensive way to renew the entrance."),
    ("Can a Lee-Dan be upgraded to video without rewiring?", "Often. Newer two-wire video systems can run on the wire already in the walls, if it tests well."),
    ("How long does a replacement take?", "[TYPICAL DURATION BY BUILDING SIZE]"),
    ("Will residents be without an intercom during the work?", "We plan the changeover so the old system stays working until the new one is ready, apartment by apartment where possible.")],
   facts=["Reuse the <b>existing wiring</b> where possible", "Audio renewal or <b>video upgrade</b>", "Written quote after testing"])

ld("parts", "Lee-Dan parts",
   "Lee-Dan Intercom Parts: Stations, Amplifiers & Panels | Jacob Intercom",
   "Lee-Dan intercom parts: IR-203E, IR-204E and IR-205E stations, the PK-543A amplifier, transformers and lobby panel components. What each part is and what it does.",
   "Lee-Dan parts",
   "Lee-Dan parts are still sold. Here is what each one is, what it replaces, and when it's worth fitting yourself.",
   """
<h2>The parts in a Lee-Dan system</h2>
<div class="tablebox"><table>
<thead><tr><th scope="col">Part</th><th scope="col">What it is</th><th scope="col">Notes</th></tr></thead>
<tbody>
<tr><th scope="row">IR-203E</th><td>Three-wire apartment station</td><td>[[lee-dan-intercom-systems/ir-203/|About the IR-203]]</td></tr>
<tr><th scope="row">IR-204E</th><td>Four-wire apartment station</td><td>The most common. [[lee-dan-intercom-systems/ir-204/|About the IR-204]]</td></tr>
<tr><th scope="row">IR-205E</th><td>Five-wire apartment station</td><td>[[lee-dan-intercom-systems/ir-205/|About the IR-205]]</td></tr>
<tr><th scope="row">PK-543A</th><td>Amplifier and control unit for the building</td><td>[[lee-dan-intercom-systems/pk-543-amplifier/|About the PK-543]]</td></tr>
<tr><th scope="row">PK-502B</th><td>Add-on unit for buildings with more than one entrance</td><td>Used alongside the PK-543A</td></tr>
<tr><th scope="row">16-volt transformer</th><td>Powers the amplifier</td><td>A common cause of a dead system</td></tr>
<tr><th scope="row">Lobby panel</th><td>Buttons, speaker, microphone and directory at the door</td><td>[[lee-dan-intercom-systems/lobby-panels/|About lobby panels]]</td></tr>
</tbody></table></div>
<p>Lee-Dan and TekTone stations and amplifiers with the same model numbers are sold as direct replacements for each other, which widens the supply.</p>
<h2>What the parts cost</h2>
<p>The parts themselves are not expensive. In November 2026, distributors listed the IR-204E station at about $30 and the PK-543A amplifier at about $125. Most of the cost of a repair is finding the fault and fitting the part correctly.</p>
<h2>Parts we keep</h2>
<p>[PARTS JACOB STOCKS, AND TYPICAL LEAD TIME FOR THE REST]</p>
<h2>Fitting parts yourself</h2>
<p>A like-for-like apartment station is within reach of a careful owner: photograph the wires, move them one at a time to the same terminals on the new unit, and test. Make sure the model matches the one that came off.</p>
<p>Leave the amplifier, the transformer and the lobby panel to a technician. A mistake there affects the whole building, and the transformer is connected to mains power.</p>
<h2>We supply and fit</h2>
<p>We bring the part, fit it, test it, and stand behind it: [WARRANTY TERMS]. Call {{tel}}.</p>
""",
   [("Where can I buy Lee-Dan parts?", "From Lee-Dan's distributors and from security-equipment suppliers. We also supply any part as part of a repair."),
    ("Are TekTone parts compatible with Lee-Dan?", "Stations and amplifiers with matching model numbers are sold as direct replacements for each other."),
    ("Do you sell parts without fitting them?", "[PARTS-ONLY SALES: YES OR NO]")],
   facts=["Stations, amplifiers, panels", "Still <b>available</b>", "Supplied and fitted"])

ld("2easy", "Lee-Dan 2Easy",
   "Lee-Dan 2Easy Video Intercom Installation NYC | Jacob Intercom",
   "Lee-Dan 2Easy two-wire colour video intercoms in New York: what the system is, why it suits older buildings, and installation on existing wiring.",
   "Lee-Dan 2Easy video intercoms",
   "2Easy is Lee-Dan's two-wire colour video intercom. For a building with an old audio system, it is often the shortest route to video.",
   """
<h2>What 2Easy is</h2>
<p>2Easy is a colour video intercom that runs on two wires. A camera panel at the door shows each visitor on a monitor in the apartment, and the resident talks and releases the door from the monitor.</p>
<p>It is sold as kits sized by the number of apartments, from a single apartment up to eight, and as separate parts for larger buildings.</p>
<h2>The parts</h2>
<ul>
<li><strong>Door panels,</strong> with a camera and a call button for each apartment. [[dt-607entry-panels/|DT-607 entry panels]] and the larger DMR11 lobby panels are in this range.</li>
<li><strong>Apartment monitors.</strong> The [[dx-471-monitor/|DX-471]] is a 7-inch colour touchscreen. Smaller monitors are also made.</li>
<li><strong>A power supply</strong> that feeds the system over the same two wires.</li>
</ul>
<h2>Why it suits older New York buildings</h2>
<p>A building with a three, four or five-wire Lee-Dan audio system already has more wire in the walls than 2Easy needs. If that wire tests well, the video system can run on it, and no walls are opened. See the [[lee-dan-intercom-systems/wiring/|wiring guide]].</p>
<p>It also suits brownstones and small buildings, where a kit for two, three or four apartments covers the whole house.</p>
<h2>How an installation goes</h2>
<ol>
<li>We test the existing wire to every apartment.</li>
<li>We fit the door panel, sized to cover the old panel's opening where possible.</li>
<li>We fit a monitor in each apartment in place of the old station.</li>
<li>We connect the power supply and the door release, and test every apartment.</li>
<li>We show each resident how to use it.</li>
</ol>
<h2>What it costs</h2>
<p>Price depends on the number of apartments and how much of the existing wiring can be used: [2EASY PRICE RANGE]. We give a written quote after testing the wiring.</p>
<p>[JACOB: HOW MANY 2EASY SYSTEMS HE HAS INSTALLED, AND WHERE IT WORKS BEST]</p>
""",
   [("Can 2Easy run on our old intercom wiring?", "Often. It needs two wires per apartment, and older Lee-Dan systems have three to five. We test the wire first."),
    ("Does 2Easy work with a phone app?", "[CONFIRM WHICH 2EASY MONITORS SUPPORT PHONE ANSWERING]"),
    ("Is 2Easy only for small buildings?", "Kits cover one to eight apartments, and larger buildings are built from separate panels and monitors.")],
   facts=["<b>Two-wire</b> colour video", "Often on <b>existing wiring</b>", "Kits for 1 to 8 apartments"])

# ───────────────────────────── Installation ─────────────────────────────

INST = "intercom-installation/"
INST_FACTS = ["<b>35 years</b> installing in New York", "Existing wiring <b>reused</b> where possible", "Written quote after a site visit"]
INST_ASIDE = {"head": "Planning a new intercom?", "text": "Tell us the number of apartments and entrances, and send a photo of the current panel. We'll tell you what is realistic before anyone visits."}
INST_RELATED = [(INST, "Intercom installation"), ("intercom-replacement/", "Replacement and upgrades"), ("pricing/", "Pricing"), ("property-managers/", "Property managers")]


def inst(slug, nav, title, desc, h1, lead, body, faqs):
    page(path=(INST + slug + "/") if slug else INST, nav=nav, title=title, desc=desc, h1=h1, lead=lead,
         facts=INST_FACTS, aside=INST_ASIDE, body=body, faqs=faqs, related=INST_RELATED)


inst("", "Intercom installation",
     "Intercom Installation NYC: Apartment Buildings, Brownstones & Offices | Jacob Intercom",
     "Intercom installation across New York for 35 years. Audio, video, wireless and smartphone entry. We test the existing wire first so you don't pay to open walls you don't need to.",
     "Intercom installation in New York City",
     "A new intercom is mostly a wiring decision. We test what is already in the walls first, because reusing it is the difference between a two-day job and a two-week one.",
     """
<h2>Choosing a system</h2>
<p>There are five kinds of intercom we install. The right one depends on the building, the wiring and how residents want to answer the door.</p>
<div class="tablebox"><table>
<thead><tr><th scope="col">System</th><th scope="col">How residents answer</th><th scope="col">Suits</th></tr></thead>
<tbody>
<tr><th scope="row">[[intercom-installation/audio/|Audio]]</th><td>A wall station: talk, listen, door</td><td>Buildings that want it simple and inexpensive</td></tr>
<tr><th scope="row">[[intercom-installation/video/|Video]]</th><td>A wall monitor that shows the visitor</td><td>Most apartment buildings today</td></tr>
<tr><th scope="row">[[intercom-installation/ip-smartphone/|IP and smartphone]]</th><td>An app on their phone, from anywhere</td><td>Buildings with good internet and many deliveries</td></tr>
<tr><th scope="row">[[intercom-installation/wireless/|Wireless]]</th><td>A phone or a wireless monitor</td><td>Buildings where the wiring has failed or never existed</td></tr>
<tr><th scope="row">[[intercom-installation/telephone-entry/|Telephone entry]]</th><td>Their own phone rings</td><td>Offices, gated properties, large buildings</td></tr>
</tbody></table></div>
<h2>What the job involves</h2>
<ol>
<li><strong>Site visit.</strong> We count apartments and entrances, look at the door and frame, find where the old equipment is, and test the existing wire to each apartment.</li>
<li><strong>Options in writing.</strong> Usually two or three, with what each includes and costs.</li>
<li><strong>Scheduling.</strong> We agree access with the super and give residents notice of when we need to enter each apartment.</li>
<li><strong>Installation.</strong> Entry panel, power and control equipment, apartment stations, door release.</li>
<li><strong>Testing and handover.</strong> Every apartment is tested from the door. Residents are shown how it works.</li>
</ol>
<h2>By building type</h2>
<ul>
<li>[[apartment-building-intercom/|Apartment buildings]]</li>
<li>[[brownstone-intercom/|Brownstones and two to four family houses]]</li>
<li>[[co-op-condo-intercom/|Co-ops and condos]]</li>
<li>[[commercial-intercom/|Offices and stores]]</li>
</ul>
<h2>The door matters as much as the intercom</h2>
<p>An intercom is only as good as the door it controls. If the strike is worn, the closer is weak or the frame has shifted, a new intercom will buzz a door that still doesn't open properly. We check the door hardware on every site visit and include it in the quote where it needs work.</p>
<h2>What it costs</h2>
<p>Installation is priced by the number of apartments and entrances, the type of system, and how much existing wire can be reused: [INSTALL PRICE RANGES BY BUILDING SIZE]. See [[pricing/|pricing]].</p>
<h2>Warranty</h2>
<p>[INSTALLATION WARRANTY TERMS]</p>
""",
     [("How long does an intercom installation take?", "[TYPICAL DURATION BY BUILDING SIZE]"),
      ("Do you need to get into every apartment?", "Yes, to fit and test each station. We schedule this with the super and give residents notice."),
      ("Can the old wiring be reused?", "Often. We test it during the site visit and tell you which lines are good."),
      ("Which brands do you install?", "Aiphone, Comelit, Akuvox, ButterflyMX, Lee-Dan and others. See [[brands/|brands]].")])

inst("video", "Video intercoms",
     "Video Intercom Installation NYC | Jacob Intercom",
     "Video intercom installation for New York apartment buildings, brownstones and offices. Wall monitors or phone answering, often on existing wiring.",
     "Video intercom installation",
     "Seeing who is at the door changes how a building feels. In many older buildings it can be added on the wire that is already there.",
     """
<h2>What a video intercom adds</h2>
<p>A camera at the entrance shows each visitor on a screen before the resident answers or opens the door. Residents stop buzzing in strangers, deliveries are easier to manage, and the building has a record of who was let in on systems that keep one.</p>
<h2>The two kinds</h2>
<ul>
<li><strong>Wired video.</strong> A camera panel at the door and a monitor on each apartment wall, connected by two or more wires. It does not depend on the internet and keeps working when the Wi-Fi doesn't.</li>
<li><strong>Network video.</strong> The panel connects to the building's internet and calls residents on a phone app, a wall tablet, or both. See [[intercom-installation/ip-smartphone/|IP and smartphone intercoms]].</li>
</ul>
<h2>Adding video to an older building</h2>
<p>Many wired video systems need only two wires per apartment. A building with an old audio intercom usually has three to five. If those wires test well, the video system runs on them and no walls are opened.</p>
<p>Where some lines have failed, we replace only those, or use a wireless link for those apartments.</p>
<h2>What to decide</h2>
<ul>
<li><strong>Monitor or phone?</strong> Wall monitors suit residents who don't want an app. Phones suit people who are often out.</li>
<li><strong>How many entrances?</strong> Each needs its own camera panel.</li>
<li><strong>Buttons or a directory screen?</strong> A button per apartment is simplest. A scrolling directory suits larger buildings.</li>
<li><strong>Access for residents.</strong> Many panels also take key fobs or codes. See [[access-control/|access control]].</li>
</ul>
<h2>What it costs</h2>
<p>[VIDEO INSTALL RANGE BY BUILDING SIZE]. The largest variable is whether existing wire can be reused.</p>
""",
     [("Can video be added without rewiring?", "Often, if the existing wire tests well. We check during the site visit."),
      ("Does a video intercom record visitors?", "Some systems keep a photo or clip of each call. It depends on the model."),
      ("Does it work in the dark?", "Yes. Panels have built-in lighting for night use."),
      ("What happens if the internet goes down?", "A wired video system keeps working. A network system depends on the connection, so we recommend a wired or backup path for the door release.")])

inst("wireless", "Wireless intercoms",
     "Wireless Intercom Installation for NYC Apartment Buildings | Jacob Intercom",
     "Wireless intercom installation in New York for buildings where the wiring has failed or was never there. How it works, where it fits, and its limits.",
     "Wireless intercom installation",
     "When the wire in the walls is finished, or was never there, a wireless system avoids opening them. It has trade-offs worth knowing first.",
     """
<h2>What "wireless" means here</h2>
<p>A wireless intercom still has a wired, powered panel at the door. What it removes is the cable to each apartment. The panel reaches residents over the cellular network or the building's internet, and they answer on their own phone or on a wireless monitor.</p>
<h2>When it is the right choice</h2>
<ul>
<li>The old riser wiring has failed in many places and replacing it would mean opening finished walls.</li>
<li>The building never had an intercom.</li>
<li>A landmark or newly renovated building where running cable is not acceptable.</li>
<li>A few apartments have dead lines and the rest are fine. Those apartments can go wireless while the others stay wired.</li>
</ul>
<h2>The trade-offs</h2>
<ul>
<li><strong>It depends on a signal.</strong> A cellular or internet outage affects it. We check signal strength at the door before recommending it.</li>
<li><strong>There is usually a monthly fee</strong> for the cellular or cloud service.</li>
<li><strong>Residents need a phone,</strong> or a wireless monitor for those who don't want to use one.</li>
</ul>
<p>Where the existing wire is good, a wired system is usually cheaper over time and has fewer things to go wrong. We test the wire first and tell you which way the numbers fall.</p>
<h2>What it costs</h2>
<p>[WIRELESS INSTALL RANGE AND TYPICAL MONTHLY FEE]</p>
""",
     [("Do residents need a smartphone?", "For most wireless systems, yes, though many can also ring an ordinary phone or a wireless wall monitor."),
      ("Is there a monthly charge?", "Usually, for the cellular or cloud service. We include it in the quote so there are no surprises."),
      ("Can part of the building be wireless and part wired?", "Yes. That is often the cheapest fix when only some lines have failed.")])

inst("ip-smartphone", "IP and smartphone intercoms",
     "IP & Smartphone Intercom Installation NYC | Jacob Intercom",
     "IP and smartphone intercom installation in New York. Answer the door from your phone, give delivery codes, manage residents online. What the building needs first.",
     "IP and smartphone intercoms",
     "The door calls your phone, wherever you are. For buildings with reliable internet and a lot of deliveries, this is where intercoms have gone.",
     """
<h2>How it works</h2>
<p>The entry panel is a small networked computer with a camera, a touchscreen or buttons, and a connection to the building's internet. When a visitor calls an apartment, the resident's phone rings with video. They talk and open the door from the app.</p>
<h2>What it makes possible</h2>
<ul>
<li>Answering the door when you aren't home.</li>
<li>One-time or scheduled codes for deliveries, cleaners and guests.</li>
<li>Adding and removing residents online, without visiting the panel.</li>
<li>A log of entries, on systems that keep one.</li>
</ul>
<h2>What the building needs</h2>
<ul>
<li><strong>A reliable internet connection at the entrance,</strong> wired to the panel where possible.</li>
<li><strong>Power at the door,</strong> usually over the network cable.</li>
<li><strong>Someone to manage the resident list.</strong> The super, the managing agent, or us under a service agreement.</li>
<li><strong>A plan for residents without smartphones.</strong> Most systems can ring a landline or a wall tablet.</li>
</ul>
<h2>Costs to plan for</h2>
<p>These systems usually carry a monthly or yearly service fee per building or per apartment, on top of the installation. We set out both in the quote so the board or owner can compare it fairly with a wired system that has no ongoing fee.</p>
<p>[IP INSTALL RANGE AND TYPICAL SERVICE FEES]</p>
<h2>Systems we install</h2>
<p>[[brands/butterflymx/|ButterflyMX]], [[brands/akuvox/|Akuvox]], [[brands/aiphone/|Aiphone]], [[brands/2n/|2N]], [[brands/doorbird/|DoorBird]] and [[brands/comelit/|Comelit]].</p>
""",
     [("What if the internet goes down?", "Calls to phones stop until it returns. Residents can still use fobs or codes, and we recommend keeping a way in that doesn't depend on the connection."),
      ("Is a smartphone intercom secure?", "Reputable systems encrypt calls and log entries. The main risk is codes being shared, which is why one-time and expiring codes are worth using."),
      ("Can it work alongside our old intercom during the changeover?", "Yes. We plan the switch so residents are not left without a way to answer the door.")])

inst("telephone-entry", "Telephone entry systems",
     "Telephone Entry System Installation NYC | Jacob Intercom",
     "Telephone entry system installation in New York for offices, gated properties and large buildings. How it works and when it beats a wired intercom.",
     "Telephone entry systems",
     "A telephone entry system rings the resident's own phone. There is no equipment in the apartment at all.",
     """
<h2>How it works</h2>
<p>The visitor finds a name on the panel's directory and presses a code or button. The system dials that person's phone. They answer, talk, and press a key on their phone to release the door.</p>
<h2>Where it fits</h2>
<ul>
<li><strong>Offices and commercial buildings,</strong> where tenants change and nobody wants to rewire for each one.</li>
<li><strong>Gates and parking entrances,</strong> far from the units they serve.</li>
<li><strong>Large residential buildings,</strong> where wiring every apartment would be a major project.</li>
<li><strong>Buildings with no usable intercom wiring.</strong></li>
</ul>
<h2>What to know</h2>
<ul>
<li>It needs a phone line or a cellular connection at the panel, which usually means a monthly cost.</li>
<li>Changing a tenant means changing a phone number in the directory, not visiting an apartment.</li>
<li>Basic systems are audio only. Many newer ones add a camera and an app, which makes them close to an [[intercom-installation/ip-smartphone/|IP intercom]].</li>
</ul>
<h2>What it costs</h2>
<p>[TELEPHONE ENTRY INSTALL RANGE]</p>
<p>[JACOB: WHICH TELEPHONE ENTRY SYSTEMS HE INSTALLS]</p>
""",
     [("Do residents need a special phone?", "No. It rings whatever number is on file: a mobile or a landline."),
      ("Can it open a gate as well as a door?", "Yes. Gates and parking barriers are a common use.")])

inst("audio", "Audio intercoms",
     "Audio Intercom System Installation NYC | Jacob Intercom",
     "Audio intercom installation in New York: simple talk, listen and door systems for apartment buildings and brownstones. Reliable, inexpensive and easy to maintain.",
     "Audio intercom systems",
     "Talk, listen, door. An audio intercom does one job, costs the least to install, and can run for decades.",
     """
<h2>Why buildings still choose audio</h2>
<ul>
<li><strong>It is the least expensive system to install and to repair.</strong></li>
<li><strong>It has no monthly fee,</strong> no app and no internet connection.</li>
<li><strong>Every resident can use it</strong> without being shown how.</li>
<li><strong>Parts are simple and widely available.</strong></li>
</ul>
<p>For a small building where residents mostly know who is calling, audio is often all that is needed.</p>
<h2>What it consists of</h2>
<p>An entry panel with a button per apartment, an amplifier and power supply, a station in each apartment, and the door strike. See [[lee-dan-intercom-systems/wiring/|how the wiring works]].</p>
<h2>Renewing an old audio system</h2>
<p>If the wiring is sound, the panel, amplifier and stations can all be replaced on it in a day or two for a small building. Residents get a system that looks and sounds new for a fraction of the cost of going to video.</p>
<h2>When to choose video instead</h2>
<p>If residents are buzzing in people they can't identify, or the building gets many deliveries, video is worth the difference. It can often run on the same wires. See [[intercom-installation/video/|video intercom installation]].</p>
<h2>What it costs</h2>
<p>[AUDIO INSTALL RANGE BY BUILDING SIZE]</p>
""",
     [("Is an audio intercom still worth installing?", "Yes, for small buildings that want something simple and inexpensive with no ongoing fee."),
      ("Can we add video later?", "Often, on the same wiring. Tell us at the start and we'll choose equipment with that in mind."),
      ("Which audio systems do you install?", "[[lee-dan-intercom-systems/|Lee-Dan]], [[brands/aiphone/|Aiphone]], [[brands/tektone/|TekTone]] and others.")])

page(path="intercom-replacement/", nav="Replacement and upgrades",
     title="Intercom Replacement & Upgrade NYC | Jacob Intercom",
     desc="Replacing an old intercom in New York: when it's time, what the options are, and how reusing the existing wiring keeps the cost down.",
     h1="Intercom replacement and upgrades",
     lead="Most old intercoms can be repaired. When yours can't, or the building wants more from it, here is how to replace it without paying for more than you need.",
     facts=INST_FACTS, aside=INST_ASIDE, related=INST_RELATED,
     body="""
<h2>Is it time?</h2>
<p>Replace when one of these is true:</p>
<ul>
<li>You have paid for several repairs in a year and different parts keep failing.</li>
<li>Parts for the system are no longer made and no compatible substitute exists.</li>
<li>The wiring is failing in many places.</li>
<li>The building wants video, phone answering or delivery codes.</li>
</ul>
<p>One failed part is not a reason to replace. If you have been quoted a new system for a single fault, get a second opinion.</p>
<h2>The four levels of replacement</h2>
<div class="tablebox"><table>
<thead><tr><th scope="col">Level</th><th scope="col">What is replaced</th><th scope="col">Disruption</th></tr></thead>
<tbody>
<tr><th scope="row">Entry panel only</th><td>The panel at the door</td><td>A few hours. No apartment access.</td></tr>
<tr><th scope="row">Like-for-like renewal</th><td>Panel, amplifier and stations, same type, same wires</td><td>A short visit to each apartment</td></tr>
<tr><th scope="row">Upgrade on existing wire</th><td>A newer system, often video, on the old wiring</td><td>A short visit to each apartment</td></tr>
<tr><th scope="row">New system with new wiring</th><td>Everything, including cable</td><td>The most work. Sometimes walls are opened.</td></tr>
</tbody></table></div>
<p>We always price the lower levels first. Most buildings that think they need the fourth turn out to need the second or third.</p>
<h2>Testing the wire</h2>
<p>Before quoting, we test the wire to every apartment. That tells us how many conductors are intact and which lines, if any, need new cable. It is the single biggest factor in the price, and it is why a quote given without a site visit is a guess.</p>
<h2>Keeping the building running</h2>
<p>We plan the changeover so the old system works until the new one is ready. Where that isn't possible, we tell residents exactly when the door will need to be answered in person.</p>
<h2>What it costs</h2>
<p>[REPLACEMENT PRICE RANGE BY LEVEL AND BUILDING SIZE]. See [[pricing/|pricing]].</p>
""",
     faqs=[("Should we repair or replace?", "Repair when one part has failed and the rest is sound. Replace when faults keep moving around the system or parts are no longer available."),
           ("Can we replace only the panel at the door?", "Yes, if the apartment stations work. It is the least expensive way to renew an entrance."),
           ("Do you remove the old equipment?", "Yes, and we cover or patch the openings old stations leave behind where the new ones are a different size.")])

# ───────────────────────────── Pricing, property managers, about ─────────────────────────────

page(path="pricing/", nav="Pricing",
     title="Intercom Repair & Installation Prices in NYC | Jacob Intercom",
     desc="What intercom repair and installation cost in New York. Most repairs $100 to $300. Prices by problem and by building size, given before work starts.",
     h1="Pricing",
     lead="You get the price before any work starts. Here is what jobs usually cost, so you know what to expect before you call.",
     facts=["Most repairs <b>$100 to $300</b>", "Price given <b>before</b> work starts", "Written quotes for installations"],
     body="""
<div class="note"><p><strong>For Jacob to complete before launch.</strong> Only the $100 to $300 repair range comes from his current site. Every highlighted figure below is waiting on his real numbers. A full table like this is something no competitor publishes.</p></div>
<h2>Repairs</h2>
<div class="tablebox"><table>
<thead><tr><th scope="col">Job</th><th scope="col">Typical price</th></tr></thead>
<tbody>
<tr><th scope="row">Service call and diagnosis</th><td>[DIAGNOSIS FEE, AND WHETHER IT IS CREDITED TO THE REPAIR]</td></tr>
<tr><th scope="row">[[intercom-repair/door-buzzer/|Apartment station replaced]]</th><td>$100 to $300</td></tr>
<tr><th scope="row">[[intercom-repair/door-release/|Door release adjusted or repaired]]</th><td>$100 to $300</td></tr>
<tr><th scope="row">[[intercom-repair/no-audio/|Panel speaker or microphone replaced]]</th><td>$100 to $300</td></tr>
<tr><th scope="row">New electric strike, fitted</th><td>[STRIKE PRICE]</td></tr>
<tr><th scope="row">Amplifier or power supply replaced</th><td>[AMPLIFIER RANGE]</td></tr>
<tr><th scope="row">Wiring fault traced and repaired</th><td>[WIRING REPAIR RANGE]</td></tr>
<tr><th scope="row">[[intercom-repair/entry-panel/|New entry panel on existing wiring]]</th><td>[PANEL RANGE]</td></tr>
<tr><th scope="row">[[intercom-repair/video/|Video intercom repair]]</th><td>[VIDEO REPAIR RANGE]</td></tr>
<tr><th scope="row">After-hours call</th><td>[AFTER-HOURS RATE]</td></tr>
</tbody></table></div>
<h2>Installations</h2>
<div class="tablebox"><table>
<thead><tr><th scope="col">Building</th><th scope="col">Audio</th><th scope="col">Video</th></tr></thead>
<tbody>
<tr><th scope="row">Brownstone, 2 to 4 apartments</th><td>[PRICE]</td><td>[PRICE]</td></tr>
<tr><th scope="row">Small building, 5 to 12 apartments</th><td>[PRICE]</td><td>[PRICE]</td></tr>
<tr><th scope="row">Medium building, 13 to 30 apartments</th><td>[PRICE]</td><td>[PRICE]</td></tr>
<tr><th scope="row">Large building, over 30 apartments</th><td>Quoted</td><td>Quoted</td></tr>
</tbody></table></div>
<p>Installation prices assume the existing wiring can be reused. New cable adds to the cost, and we tell you by how much after testing.</p>
<h2>What changes the price</h2>
<ul>
<li><strong>How many apartments are affected.</strong> One station is quick. A fault on a shared wire takes longer to find.</li>
<li><strong>The age and make of the system.</strong> Parts for discontinued systems cost more and can take time to source.</li>
<li><strong>Access.</strong> Wire inside finished walls costs more to reach than wire in a basement.</li>
<li><strong>The door.</strong> A worn strike or closer is often part of the problem and part of the price.</li>
</ul>
<h2>Maintenance contracts</h2>
<p>For owners and managing agents, a yearly contract covers inspection and priority service: [CONTRACT PRICE]. See [[intercom-maintenance-contract/|maintenance contracts]].</p>
<h2>How we quote</h2>
<p>For repairs, we find the fault and tell you the price on site, before starting. For installations and replacements, you get a written quote after a site visit. The price we quote is the price you pay unless the job changes, and if it does we stop and tell you first.</p>
""",
     faqs=[("Is there a charge to come out and look?", "[DIAGNOSIS FEE, AND WHETHER IT IS CREDITED TO THE REPAIR]"),
           ("Do you give prices over the phone?", "We can usually give a range from a photo and a description. The firm price comes once we've tested the system."),
           ("Do you charge more for older systems?", "Labour is the same. Parts for discontinued systems can cost more."),
           ("How do I pay?", "[PAYMENT METHODS AND TERMS]")],
     related=[("intercom-repair/", "Intercom repair"), (INST, "Intercom installation"), ("intercom-maintenance-contract/", "Maintenance contracts"), ("contact/", "Contact us")])

page(path="property-managers/", nav="Property managers",
     title="Intercom Service for NYC Property Managers, Supers & Boards | Jacob Intercom",
     desc="Intercom repair, installation and maintenance for New York managing agents, supers and co-op and condo boards. Insurance certificate, written quotes, one invoice.",
     h1="For managing agents, supers and boards",
     lead="You need a contractor who shows up, sends the paperwork without being chased, and doesn't sell a new system when a part will do.",
     facts=["Certificate of insurance <b>on request</b>", "Written quotes", "One invoice across buildings"],
     aside={"head": "Looking after several buildings?", "text": "Send us the addresses and what each has. We'll tell you what we can cover and what a maintenance contract would cost."},
     body="""
<h2>What you get</h2>
<ul>
<li><strong>Insurance paperwork first.</strong> We send a certificate of insurance naming the building and managing agent before the first visit. Licence: [LICENCE NO.]. Coverage: [INSURANCE LIMITS].</li>
<li><strong>Written quotes</strong> a board can vote on, with options where there are options.</li>
<li><strong>One point of contact</strong> and one invoice across every building you manage.</li>
<li><strong>A record of each building:</strong> the make and model of the system, where the amplifier is, what has been replaced and when.</li>
<li><strong>Repair first.</strong> We tell you when a part will do and when it won't.</li>
</ul>
<h2>For supers</h2>
<p>Call or text us what the system is doing and how many apartments are affected. A photo of the panel and of the amplifier gets you a faster answer. We work around your schedule for apartment access, and we leave the equipment labelled so the next fault is easier to describe. See the [[intercom-repair/|repair guide by symptom]].</p>
<h2>For co-op and condo boards</h2>
<p>Replacing an intercom is a capital decision. We test the existing wiring, set out two or three options with costs, and explain the difference in plain terms at a board meeting if that helps. Residents are given notice, shown how the new system works, and not left without a way to answer the door. See [[intercom-replacement/|replacement and upgrades]].</p>
<h2>For owners</h2>
<p>A working intercom is part of keeping a building habitable and secure, and tenants notice quickly when it isn't. We keep older systems running for as long as that is the sensible choice, and tell you in advance when it is time to budget for a replacement. [LEGAL REQUIREMENTS: TO BE CHECKED BEFORE PUBLISHING]</p>
<h2>Maintenance contracts</h2>
<p>A yearly contract covers a scheduled inspection of every building and priority response when something fails. See [[intercom-maintenance-contract/|maintenance contracts]].</p>
<h2>Buildings we look after</h2>
<p>[CLIENTS OR BUILDING TYPES JACOB CAN NAME, WITH PERMISSION]</p>
""",
     faqs=[("Can you send a certificate of insurance before the job?", "Yes, naming the building owner and managing agent as required."),
           ("Do you work with building staff schedules for apartment access?", "Yes. We agree access with the super and give residents notice."),
           ("Can you attend a board meeting to explain the options?", "[YES OR NO, AND ANY CHARGE]"),
           ("Do you offer payment terms for managing agents?", "[PAYMENT TERMS FOR ACCOUNTS]")],
     related=[("intercom-maintenance-contract/", "Maintenance contracts"), ("intercom-replacement/", "Replacement and upgrades"), ("pricing/", "Pricing"), ("contact/", "Contact us")])

page(path="intercom-maintenance-contract/", nav="Maintenance contracts",
     title="Intercom Maintenance Contracts NYC | Jacob Intercom",
     desc="Yearly intercom maintenance contracts for New York buildings: scheduled inspection, priority service and a record of every system.",
     h1="Intercom maintenance contracts",
     lead="Most intercom failures give warning. A yearly inspection finds the weak transformer and the corroded panel before the building goes quiet.",
     facts=["Yearly <b>inspection</b>", "<b>Priority</b> response", "One invoice across buildings"],
     aside={"head": "Want a contract price?", "text": "Tell us how many buildings, how many apartments in each, and what systems they have. We'll send a price."},
     body="""
<div class="note"><p><strong>For Jacob to decide before launch.</strong> This page describes a contract he does not offer online today. The terms below are a proposal for him to adjust, price or drop.</p></div>
<h2>What a contract covers</h2>
<ul>
<li><strong>A scheduled inspection</strong> of each building: [INSPECTIONS PER YEAR].</li>
<li><strong>Testing</strong> of the entry panel, amplifier, power supply, door release and a sample of apartments on every line.</li>
<li><strong>Cleaning and resealing</strong> of the entry panel.</li>
<li><strong>Directory updates</strong> for new residents.</li>
<li><strong>Priority response</strong> when something fails: [RESPONSE COMMITMENT].</li>
<li><strong>A written report</strong> after each inspection, with anything that is likely to fail soon.</li>
</ul>
<h2>What it doesn't cover</h2>
<p>[PARTS, VANDALISM, AFTER-HOURS CALLS: INCLUDED OR EXTRA]</p>
<h2>Why it pays</h2>
<p>Two emergency calls in a year usually cost more than a contract. The inspection also catches the failures that take out a whole building, a weak transformer or a panel taking in water, while they are still inexpensive to fix.</p>
<h2>What it costs</h2>
<p>[CONTRACT PRICE BY BUILDING SIZE]. Several buildings under one contract are priced together.</p>
<h2>Who it suits</h2>
<p>Managing agents with several buildings, co-op and condo boards that want predictable costs, and owners of buildings with older systems. See [[property-managers/|property managers]].</p>
""",
     faqs=[("Are parts included?", "[PARTS INCLUDED OR EXTRA]"),
           ("Can we cancel?", "[CANCELLATION TERMS]"),
           ("Do you take over systems another company installed?", "Yes. We inspect first and tell you what condition the system is in.")],
     related=[("property-managers/", "Property managers"), ("pricing/", "Pricing"), ("intercom-repair/emergency/", "Emergency repair"), ("contact/", "Contact us")])

page(path="about/", nav="About",
     title="About Jacob Intercom: 35 Years of Intercom Work in New York",
     desc="Jacob Intercom has repaired and installed intercoms across New York for 35 years, from a base at 209 Avenue F in Brooklyn.",
     h1="About Jacob Intercom",
     lead="Thirty-five years of repairing and installing intercoms in New York, from Avenue F in Brooklyn.",
     facts=["<b>35 years</b> in business", "Based in <b>Brooklyn</b>", "Licensed and insured"],
     body="""
<div class="note"><p><strong>For Jacob to write or approve.</strong> This page should be in his words. The structure and the confirmed facts are in place. The rest is marked for him.</p></div>
<figure class="portrait"><img src="{{a:img/jacob.webp}}" alt="Jacob of Jacob Intercom, holding a tool bag and answering his phone" width="600" height="900" fetchpriority="high"><figcaption>Jacob, founder of Jacob Intercom. [JACOB: CONFIRM HOW HE WANTS TO BE NAMED]</figcaption></figure>
<h2>How we started</h2>
<p>[JACOB: HOW AND WHEN HE STARTED, AND WHAT THE WORK WAS LIKE THEN]</p>
<h2>What we do</h2>
<p>We repair and install intercoms, and the door hardware, access control and cameras that go with them. Most of our work is in apartment buildings, brownstones, co-ops and condos, with offices and stores alongside.</p>
<p>A large part of it is keeping older systems running. New York has thousands of intercoms that were fitted decades ago and still have years in them, and we would sooner repair one than replace it. We are known for [[lee-dan-intercom-systems/|Lee-Dan systems]] in particular.</p>
<h2>How we work</h2>
<ul>
<li>We find the fault before we quote.</li>
<li>We give the price before we start.</li>
<li>We repair when repair is the sensible choice, and say so when it isn't.</li>
<li>We test every affected apartment before we leave.</li>
</ul>
<h2>The team</h2>
<p>[NAMES AND ROLES, WITH PERMISSION]. One of our Google reviewers wrote: &ldquo;Marina is the person to go to!&rdquo;</p>
<h2>Licences and insurance</h2>
<p>Licence: [LICENCE NO. AND TYPE]. Insurance: [INSURER AND LIMITS]. A certificate of insurance is available to managing agents and boards on request.</p>
<h2>Where we work</h2>
<p>Our office is at 209 Avenue F, Brooklyn, NY 11218. We cover Brooklyn, Manhattan, Queens, the Bronx and Staten Island, and take jobs on Long Island, in Westchester and in New Jersey.</p>
""",
     related=[("intercom-repair/", "Intercom repair"), (INST, "Intercom installation"), ("lee-dan-intercom-systems/", "Lee-Dan systems"), ("contact/", "Contact us")])

# ───────────────────────────── Building types ─────────────────────────────

BT_RELATED = [(INST, "Intercom installation"), ("intercom-repair/", "Intercom repair"), ("property-managers/", "Property managers"), ("pricing/", "Pricing")]


def btype(path, nav, title, desc, h1, lead, body, faqs):
    page(path=path, nav=nav, title=title, desc=desc, h1=h1, lead=lead,
         facts=["<b>35 years</b> in New York buildings", "Repair and installation", "Existing wiring <b>reused</b> where possible"],
         aside=INST_ASIDE, body=body, faqs=faqs, related=BT_RELATED)


btype("apartment-building-intercom/", "Apartment buildings",
      "Apartment Building Intercom Systems NYC: Repair & Installation | Jacob Intercom",
      "Intercom systems for New York apartment buildings: how they work, which type suits your building, and what repair and installation involve.",
      "Apartment building intercom systems",
      "A building intercom has to work for every resident, every day, for years. Here is how to choose one, keep it running, and replace it when the time comes.",
      """
<h2>What a building system has to do</h2>
<ul>
<li>Let a visitor call any apartment from the front door.</li>
<li>Let the resident talk to them, and see them on video systems.</li>
<li>Let the resident open the door without going downstairs.</li>
<li>Lock the door again behind the visitor.</li>
</ul>
<p>Everything else, from phone answering to delivery codes, is added on top. The first four must work every time.</p>
<h2>Choosing a system by building size</h2>
<div class="tablebox"><table>
<thead><tr><th scope="col">Building</th><th scope="col">What usually fits</th></tr></thead>
<tbody>
<tr><th scope="row">Up to 12 apartments</th><td>Button panel, audio or two-wire video, on the existing wire</td></tr>
<tr><th scope="row">12 to 40 apartments</th><td>Button or directory panel, wired video or a phone-based system</td></tr>
<tr><th scope="row">Over 40 apartments</th><td>Directory panel with a scrolling list or keypad, phone-based or IP system, access control at every door</td></tr>
<tr><th scope="row">More than one entrance</th><td>A panel at each, all calling the same apartments</td></tr>
</tbody></table></div>
<h2>The parts, and where they are</h2>
<ul>
<li><strong>Entry panel</strong> at the front door or in the vestibule.</li>
<li><strong>Amplifier or controller and power supply,</strong> usually in the basement, a meter room or a closet near the entrance.</li>
<li><strong>Riser cable</strong> running up through the building, one per vertical line of apartments.</li>
<li><strong>Apartment stations or monitors</strong> on each apartment wall.</li>
<li><strong>Electric strike or magnetic lock</strong> on the entrance door.</li>
</ul>
<p>Knowing where your controller is saves time on every repair. If nobody knows, we label it on the first visit.</p>
<h2>Keeping it running</h2>
<p>Most building-wide failures start at the power supply or the entry panel, and most give warning: fading volume, crackle in wet weather, buttons that need a second press. A yearly inspection catches these early. See [[intercom-maintenance-contract/|maintenance contracts]].</p>
<h2>When it fails</h2>
<p>Start with [[intercom-repair/|intercom repair by symptom]]. The first question is always how many apartments are affected.</p>
<h2>Replacing it</h2>
<p>Most buildings can reuse the riser cable already in the walls. That keeps a replacement to a short visit per apartment. See [[intercom-replacement/|replacement and upgrades]].</p>
""",
      [("Who is responsible for a building intercom?", "The building owner, through the super or managing agent. Residents should report faults to them in writing."),
       ("Can a building have different systems for different entrances?", "It is possible but harder to maintain. We recommend one system with a panel at each door."),
       ("How long does a building intercom last?", "Wired systems commonly run for decades with parts replaced along the way. Network systems are usually replaced sooner, when software support ends.")])

btype("brownstone-intercom/", "Brownstones and 2 to 4 family",
      "Brownstone & Two-Family Intercom Systems NYC | Jacob Intercom",
      "Intercoms for New York brownstones, townhouses and two to four family houses: repair, replacement and video, without damaging original detail.",
      "Brownstone and two to four family intercoms",
      "A brownstone intercom is a small system with particular problems: original doors, decorative ironwork, plaster walls and owners who live upstairs.",
      """
<h2>What is different about a brownstone</h2>
<ul>
<li><strong>Two front doors.</strong> Many have an outer door under the stoop or at the top of it, and an inner vestibule door. The intercom may need to release one or both.</li>
<li><strong>Original doors and frames.</strong> Fitting a strike to a hundred-year-old door needs care so the wood and hardware aren't damaged.</li>
<li><strong>Plaster walls.</strong> Running new cable is slow and messy, so reusing the old wire matters more here than anywhere.</li>
<li><strong>Few apartments.</strong> Two to four units means a small, inexpensive system, often a kit.</li>
<li><strong>Landmark districts.</strong> A panel visible from the street may need to suit the facade.</li>
</ul>
<h2>Common setups</h2>
<div class="tablebox"><table>
<thead><tr><th scope="col">Setup</th><th scope="col">When it fits</th></tr></thead>
<tbody>
<tr><th scope="row">Audio panel and stations</th><td>Simple, inexpensive, no monthly fee</td></tr>
<tr><th scope="row">Two-wire video kit</th><td>Video on the existing wire. Kits come sized for two, three or four apartments.</td></tr>
<tr><th scope="row">Video doorbell-style panel with phone app</th><td>Owner-occupied houses where residents want to answer from anywhere</td></tr>
</tbody></table></div>
<p>Lee-Dan's [[lee-dan-intercom-systems/2easy/|2Easy kits]] and [[brands/aiphone/|Aiphone]]'s small multi-tenant kits are both common choices.</p>
<h2>The door</h2>
<p>Old doors sag, and a strike that worked when it was fitted can drift out of line. If yours buzzes without opening, see [[intercom-repair/door-release/|door release repair]]. For heavy original doors, a magnetic lock or a surface strike sometimes suits better than cutting the frame.</p>
<h2>Repair</h2>
<p>Most brownstone repairs are a single station, a worn button, or the strike. They are usually done in one visit, at the low end of our $100 to $300 range.</p>
<h2>What a new system costs</h2>
<p>[BROWNSTONE INSTALL RANGE, AUDIO AND VIDEO]</p>
<p>[JACOB: A BROWNSTONE JOB TO FEATURE, WITH PHOTOS]</p>
""",
      [("Can you fit an intercom without damaging the original door?", "Yes. We choose a strike or lock that suits the door, and fit it to the frame with as little cutting as possible."),
       ("Do we need permission in a landmark district?", "Work visible from the street on a landmarked building may need approval. Check with the Landmarks Preservation Commission before replacing a street-facing panel."),
       ("Can one apartment have video and the others audio?", "On some systems, yes. It is usually simpler to put the whole house on one system.")])

btype("co-op-condo-intercom/", "Co-ops and condos",
      "Co-op & Condo Intercom Systems NYC: Repair, Replacement & Board Quotes | Jacob Intercom",
      "Intercom repair and replacement for New York co-ops and condos. Written options a board can vote on, insurance paperwork, and resident notice handled.",
      "Co-op and condo intercoms",
      "In a co-op or condo, an intercom replacement goes through a board, a managing agent and every shareholder's front door. We plan for all three.",
      """
<h2>How the decision usually goes</h2>
<ol>
<li><strong>The managing agent or super reports a problem</strong> or a system that is costing too much to keep repairing.</li>
<li><strong>We inspect and test the wiring,</strong> and send a written report.</li>
<li><strong>The board gets two or three options,</strong> with what each includes, costs and changes for residents.</li>
<li><strong>The board decides,</strong> often after a presentation at a meeting.</li>
<li><strong>We schedule the work</strong> with the managing agent, and residents get notice.</li>
<li><strong>Residents are shown the new system,</strong> with a printed guide for those who want one.</li>
</ol>
<h2>What boards ask, and our answers</h2>
<ul>
<li><strong>Can we keep the old wiring?</strong> Usually. We test it and tell you which lines are sound.</li>
<li><strong>What will it cost each year to run?</strong> Wired systems have no ongoing fee. Phone-based systems usually have one. We set out both.</li>
<li><strong>What happens for residents without a smartphone?</strong> Every system we recommend has a way for them to answer.</li>
<li><strong>How long will residents be without an intercom?</strong> We plan the changeover to keep that to a minimum.</li>
</ul>
<h2>Paperwork</h2>
<p>A certificate of insurance naming the corporation or condominium and the managing agent, sent before the first visit. Written quotes and an itemised invoice. Licence: [LICENCE NO.].</p>
<h2>Shareholders and unit owners</h2>
<p>In most co-ops and condos the building intercom is a common element, and the apartment station is often treated as part of it. Check your proprietary lease or bylaws, or ask the managing agent, before arranging a repair to your own station.</p>
<p>[JACOB: A CO-OP JOB TO FEATURE, WITH THE BOARD'S PERMISSION]</p>
""",
      [("Will you present the options at a board meeting?", "[YES OR NO, AND ANY CHARGE]"),
       ("Can the new system tie into our key fobs?", "Many can. See [[access-control/key-fob/|key fob systems]]."),
       ("Do you work with our managing agent directly?", "Yes. Most of our co-op and condo work is arranged through the managing agent.")])

btype("commercial-intercom/", "Offices and stores",
      "Commercial & Office Intercom Systems NYC | Jacob Intercom",
      "Intercom and door entry systems for New York offices, stores and mixed-use buildings. Video entry, telephone entry and access control, installed and repaired.",
      "Office and commercial intercoms",
      "In an office or store, the intercom is part of how you run the business: who gets in, when, and how fast.",
      """
<h2>What businesses need</h2>
<ul>
<li><strong>Reception or staff answering the door,</strong> often from a desk or a phone.</li>
<li><strong>Deliveries let in without someone walking to the door.</strong></li>
<li><strong>Different access for staff and visitors,</strong> usually by fob or code.</li>
<li><strong>Several tenants in one building,</strong> each answering their own calls.</li>
<li><strong>Work done outside business hours,</strong> so the business isn't disrupted.</li>
</ul>
<h2>Common setups</h2>
<div class="tablebox"><table>
<thead><tr><th scope="col">Business</th><th scope="col">What usually fits</th></tr></thead>
<tbody>
<tr><th scope="row">Single office or store</th><td>Video door station answered on a desk monitor or a phone</td></tr>
<tr><th scope="row">Multi-tenant office building</th><td>[[intercom-installation/telephone-entry/|Telephone entry]] or an IP directory panel</td></tr>
<tr><th scope="row">Back door or loading entrance</th><td>Audio or video station with a strike, often alongside a fob reader</td></tr>
<tr><th scope="row">Mixed-use with apartments above</th><td>Separate entrances, or one panel with residential and commercial listings</td></tr>
</tbody></table></div>
<h2>Access control alongside the intercom</h2>
<p>Most commercial jobs combine an intercom for visitors with fobs or codes for staff. See [[access-control/|access control]] and [[access-control/electric-strikes-maglocks/|electric strikes and magnetic locks]].</p>
<h2>Cameras</h2>
<p>A camera over the door complements the intercom and covers the times nobody answers. See [[security-cameras/|security cameras]].</p>
<h2>What it costs</h2>
<p>[COMMERCIAL INSTALL RANGE]</p>
""",
      [("Can you work before we open or after we close?", "[AFTER-HOURS SCHEDULING AND ANY SURCHARGE]"),
       ("Can the intercom ring our office phones?", "Yes, with a telephone entry or IP system."),
       ("Can different tenants have their own buttons?", "Yes. Each tenant gets a listing that calls their own station or phone.")])

# ───────────────────────────── Brands ─────────────────────────────

BRAND_ASIDE = {"head": "Need service on your system?", "text": "Send a photo of the panel and an apartment station. The model number tells us the parts and the likely fault."}


def brand(slug, name, title, desc, lead, body, faqs, facts):
    disclaimer = f'<p class="soon" style="font-size:.92rem">Jacob Intercom is an independent installer and repair company. We are not affiliated with or endorsed by {name}. Product names belong to their owners.</p>'
    page(path=f"brands/{slug}/", nav=name, title=title, desc=desc, h1=f"{name} intercom service in New York",
         lead=lead, facts=facts, aside=BRAND_ASIDE, body=body + disclaimer, faqs=faqs,
         related=[("brands/", "All brands we service"), ("intercom-repair/", "Intercom repair"), (INST, "Installation"), ("pricing/", "Pricing")])


page(path="brands/", nav="Brands",
     title="Intercom Brands We Repair & Install in NYC | Jacob Intercom",
     desc="We repair and install intercoms from 15 manufacturers: Lee-Dan, Aiphone, ButterflyMX, Comelit, Akuvox, TekTone, Mircom, Siedle, Elvox, DoorBird, 2N, DoorKing and more.",
     h1="Intercom brands we service",
     lead="Fifteen makes, old and new. Whatever is on your wall, there is a good chance we have repaired one like it.",
     facts=["<b>15</b> manufacturers", "Old and current systems", "Repair, parts and installation"],
     body="""
<h2>The brands</h2>
<div class="tablebox"><table>
<thead><tr><th scope="col">Brand</th><th scope="col">What you'll usually find in New York</th></tr></thead>
<tbody>
<tr><th scope="row">[[lee-dan-intercom-systems/|Lee-Dan]]</th><td>Audio systems in walk-ups and small buildings, and 2Easy two-wire video</td></tr>
<tr><th scope="row">[[brands/aiphone/|Aiphone]]</th><td>GT multi-tenant video, IX and IXG network systems, small kits</td></tr>
<tr><th scope="row">[[brands/butterflymx/|ButterflyMX]]</th><td>Touchscreen panels that call residents' phones</td></tr>
<tr><th scope="row">[[brands/comelit/|Comelit]]</th><td>Two-wire video in apartment buildings, IP systems</td></tr>
<tr><th scope="row">[[brands/akuvox/|Akuvox]]</th><td>Network door phones and indoor monitors</td></tr>
<tr><th scope="row">[[brands/tektone/|TekTone]]</th><td>Audio apartment entry, interchangeable with Lee-Dan</td></tr>
<tr><th scope="row">[[brands/mircom/|Mircom]]</th><td>Telephone entry in larger buildings</td></tr>
<tr><th scope="row">[[brands/siedle/|Siedle]]</th><td>High-end panels in townhouses and luxury buildings</td></tr>
<tr><th scope="row">[[brands/elvox/|Elvox]]</th><td>Italian video systems in apartment buildings</td></tr>
<tr><th scope="row">[[brands/doorbird/|DoorBird]]</th><td>Stainless network door stations in houses and small buildings</td></tr>
<tr><th scope="row">[[brands/2n/|2N]]</th><td>Network intercoms in offices and newer buildings</td></tr>
<tr><th scope="row">[[brands/doorking/|DoorKing]]</th><td>Telephone entry for gates and parking</td></tr>
<tr><th scope="row">[[brands/alpha-communications/|Alpha Communications]]</th><td>Audio and video apartment entry</td></tr>
<tr><th scope="row">[[brands/pacific-electronics/|Pacific Electronics]]</th><td>Older apartment entry systems</td></tr>
<tr><th scope="row">[[brands/nutone/|NuTone]] and [[brands/m-and-s/|M&amp;S]]</th><td>Whole-house intercoms in private homes</td></tr>
</tbody></table></div>
<h2>Don't know the make?</h2>
<p>Look for a name or model number on the entry panel, on the front or back of an apartment station, or on the amplifier in the basement. If there isn't one, send us a photo and we'll identify it.</p>
<h2>Mixed systems</h2>
<p>Many buildings have parts from more than one maker, added over the years. Some are interchangeable, such as Lee-Dan and TekTone stations with the same model number. Others aren't. We test before replacing anything so you don't pay for a part that won't work with the rest of the system.</p>
<p class="soon" style="font-size:.92rem">Jacob Intercom is an independent installer and repair company, not affiliated with any of these manufacturers. Product names belong to their owners.</p>
""",
     related=[("intercom-repair/", "Intercom repair"), (INST, "Intercom installation"), ("lee-dan-intercom-systems/", "Lee-Dan systems"), ("contact/", "Contact us")])

brand("aiphone", "Aiphone", "Aiphone Intercom Repair & Installation NYC: GT, IX, IXG, JO | Jacob Intercom",
      "Aiphone intercom repair and installation in New York. A guide to the GT, IX, IXG, JO and AX series: which is which, what goes wrong, and repair costs.",
      "Aiphone is one of the most common video intercom makers in New York buildings. This is a guide to which Aiphone system you have, what goes wrong with it, and what repairs cost.",
      """
<div class="note"><p><strong>For Jacob to review before launch.</strong> Product line details are from Aiphone's published range. Fault patterns and prices are his to confirm.</p></div>
<h2>About Aiphone</h2>
<p>Aiphone is a Japanese manufacturer that has made intercoms since the late 1940s, with its US company based in Washington State. Its systems are known for being built to last, and many Aiphone installations in New York have run for well over a decade.</p>
<h2>Which Aiphone do you have?</h2>
<p>Aiphone sells several families, each for a different kind of building. The series name is usually printed on the panel or the monitor, or is the first letters of the model number.</p>
<div class="tablebox"><table>
<thead><tr><th scope="col">Series</th><th scope="col">What it is</th><th scope="col">Where you find it</th></tr></thead>
<tbody>
<tr><th scope="row">GT</th><td>Multi-tenant audio and video entry, wired</td><td>Apartment buildings of most sizes</td></tr>
<tr><th scope="row">IXG</th><td>Network multi-tenant system with a phone app</td><td>Newer and upgraded apartment buildings</td></tr>
<tr><th scope="row">IX</th><td>Network intercom for commercial and institutional sites</td><td>Offices, schools, healthcare</td></tr>
<tr><th scope="row">AX</th><td>Larger commercial and security systems</td><td>Institutions, industrial sites</td></tr>
<tr><th scope="row">JO, JP and JK</th><td>Video systems for houses and small offices</td><td>Townhouses and single-family homes</td></tr>
<tr><th scope="row">Older audio lines</th><td>Earlier apartment and door systems</td><td>Buildings that haven't been upgraded</td></tr>
</tbody></table></div>
<h2>What goes wrong</h2>
<ul>
<li><strong>A monitor screen goes dark</strong> or the picture fades. The monitor or its connection has failed. Usually one apartment.</li>
<li><strong>No apartment can see the visitor.</strong> The camera module in the entry panel, or the video power supply.</li>
<li><strong>Some apartments stop ringing.</strong> On GT systems, a fault in the distribution between the panel and those floors.</li>
<li><strong>Phone app calls stop arriving</strong> on IXG systems. Usually the building's network or the app settings, not the hardware.</li>
<li><strong>The door won't release.</strong> As with any make, often the strike rather than the intercom. See [[intercom-repair/door-release/|door release repair]].</li>
</ul>
<p>[JACOB: THE AIPHONE FAULTS HE SEES MOST]</p>
<h2>Repair or upgrade?</h2>
<p>A failed monitor or panel component on a current Aiphone line is replaced like for like. Where a series has been discontinued, compatible parts are often still available for a time, and Aiphone has published upgrade paths from older lines to newer ones. We tell you which applies to your system.</p>
<h2>Adding phone answering</h2>
<p>Buildings with a wired GT system often ask about answering on a phone. That generally means moving to a network-based system such as IXG, sometimes on part of the existing wiring. See [[intercom-installation/ip-smartphone/|IP and smartphone intercoms]].</p>
<h2>What it costs</h2>
<p>Single-apartment repairs usually fall in our $100 to $300 range, plus the part where a monitor is replaced: [AIPHONE MONITOR PRICE RANGE]. Entry panel repairs: [AIPHONE PANEL RANGE].</p>
""",
      [("Does Aiphone repair its own intercoms in NYC?", "Aiphone sells through dealers and installers. Service is done by independent companies like ours."),
       ("Can I mix old and new Aiphone monitors?", "Only within a compatible series. A GT monitor won't work on an IXG system, for example."),
       ("Can Aiphone call my phone?", "The IXG and some other network systems can. Older wired series cannot without an upgrade."),
       ("How long do Aiphone systems last?", "Well-maintained wired Aiphone systems commonly run for many years. Monitors and panel parts are replaced along the way.")],
      ["GT, IXG, IX, AX and JO series", "Monitors, panels and wiring", "Repair and upgrades"])

brand("butterflymx", "ButterflyMX", "ButterflyMX Installation, Repair & Troubleshooting NYC | Jacob Intercom",
      "ButterflyMX installation and repair in New York. How the system works, what it costs to run, common problems with calls, the app and door release, and how to fix them.",
      "ButterflyMX is a phone-based video intercom that started in New York and is now in many of its buildings. This is a plain guide to how it works, what it costs to run, and what to do when it stops working.",
      """
<div class="note"><p><strong>For Jacob to review before launch.</strong> Details are from ButterflyMX's published material. Whether he is a certified ButterflyMX installer: [CERTIFIED OR NOT].</p></div>
<h2>How ButterflyMX works</h2>
<p>A touchscreen panel at the entrance shows a directory of residents. A visitor finds a name and taps to call. The resident's phone rings with video through the ButterflyMX app, and they open the door from the app. There is no equipment inside the apartment.</p>
<p>The system is managed online: residents are added and removed by the building's administrator, and the panel connects to ButterflyMX's cloud service over the building's internet or a cellular link.</p>
<h2>What residents can do</h2>
<ul>
<li>Answer the door with video from anywhere.</li>
<li>Open the door from the app, with a virtual key, or with a PIN at the panel.</li>
<li>Send guests time-limited access codes.</li>
<li>Let couriers in with delivery codes.</li>
</ul>
<h2>What the building pays</h2>
<p>A ButterflyMX installation has two parts: the hardware and installation, and a recurring software subscription paid to ButterflyMX. Boards comparing it with a wired system should compare both over several years. We set out the installation cost in our quote and tell you to confirm the subscription directly with ButterflyMX.</p>
<h2>Common problems and what causes them</h2>
<div class="tablebox"><table>
<thead><tr><th scope="col">What happens</th><th scope="col">Usual cause</th></tr></thead>
<tbody>
<tr><th scope="row">One resident's phone doesn't ring</th><td>App notifications turned off, an old app version, or the resident's number or account details are out of date</td></tr>
<tr><th scope="row">No one's phone rings</th><td>The panel has lost its internet or cellular connection</td></tr>
<tr><th scope="row">The panel screen is black</th><td>Power to the panel, or the panel itself</td></tr>
<tr><th scope="row">Calls connect but the door won't open</th><td>The strike or its relay. The panel can be fine.</td></tr>
<tr><th scope="row">Delivery codes don't work</th><td>Code settings in the building's account</td></tr>
<tr><th scope="row">Calls arrive late</th><td>A weak network at the panel, or the resident's phone signal</td></tr>
</tbody></table></div>
<h2>What residents can check</h2>
<ul>
<li>Update the app and allow its notifications.</li>
<li>Check that the phone number on your account is current with your building administrator.</li>
<li>Try calling yourself from the panel while connected to Wi-Fi and then on mobile data.</li>
</ul>
<p>For account and app problems, your building administrator or ButterflyMX support is the right first call. For a dead panel, a door that won't open or a network fault at the entrance, call us.</p>
<h2>Installing ButterflyMX</h2>
<p>An installation needs power and a network connection at the entrance, a suitable strike or lock on the door, and a mounting position for the panel. We usually fit it in place of the old entry panel. The old apartment stations are left in place or removed, as the building prefers.</p>
<p>See [[intercom-installation/ip-smartphone/|IP and smartphone intercoms]] for how phone-based systems compare.</p>
<h2>What it costs</h2>
<p>Installation: [BUTTERFLYMX INSTALL RANGE]. Repairs to the door hardware, power or network: usually within our $100 to $300 range.</p>
""",
      [("Do residents need the ButterflyMX app?", "To answer with video, yes. Residents without a smartphone can usually be called on an ordinary phone number."),
       ("What happens if the internet goes down?", "Calls to phones stop until the connection returns. Residents can still enter with a PIN or virtual key on most setups."),
       ("Can ButterflyMX use our old intercom wiring?", "The panel needs power and a network connection at the door. The old apartment wiring isn't used."),
       ("Who do I call when ButterflyMX isn't working?", "For app and account problems, your building administrator or ButterflyMX. For the panel, power, network at the door or the door release, call us at {{tel}}."),
       ("Is there a monthly fee?", "Yes, ButterflyMX charges a recurring software subscription. Confirm the current price with them.")],
      ["Phone-based video entry", "Installation and repair", "Door, power and network faults"])

brand("comelit", "Comelit", "Comelit Intercom Repair & Installation NYC | Jacob Intercom",
      "Comelit intercom repair and installation in New York: Simplebus two-wire video and ViP network systems in apartment buildings.",
      "Comelit is an Italian maker whose two-wire video systems are common in New York apartment buildings, including many co-ops that upgraded in the last twenty years.",
      """
<h2>About Comelit</h2>
<p>Comelit has made intercoms in Italy since the 1950s. In New York it is best known for video systems that run on two wires, which made it a popular choice for upgrading older buildings without rewiring.</p>
<h2>Which Comelit do you have?</h2>
<ul>
<li><strong>Simplebus:</strong> two-wire audio and video systems. The most common Comelit in New York apartment buildings.</li>
<li><strong>ViP:</strong> network-based systems, often with app answering.</li>
<li><strong>Entry panels</strong> in several ranges, from button panels to directory panels with keypads.</li>
</ul>
<h2>What goes wrong</h2>
<ul>
<li>A monitor fails in one apartment.</li>
<li>The camera or a button module in the entry panel fails.</li>
<li>The power supply or a distribution module fails, taking out part or all of the building.</li>
<li>App calls stop on network systems.</li>
</ul>
<p>One review on our Google listing comes from a co-op where a Comelit system was upgraded and given app answering. [JACOB: COMELIT JOB DETAILS IF THIS WAS HIS]</p>
<h2>Repair and upgrade</h2>
<p>Comelit parts are modular, so failed panel modules and monitors are replaced individually. Buildings on Simplebus can often add app answering or move to ViP using part of the existing installation.</p>
<h2>What it costs</h2>
<p>[COMELIT REPAIR AND INSTALL RANGES]</p>
""",
      [("Can a Comelit system call my phone?", "Network ViP systems can, and some Simplebus systems can with added equipment."),
       ("Can you replace one Comelit monitor?", "Yes, with a compatible model."),
       ("Is Comelit a two-wire system?", "Simplebus is. That is why it is often used to bring video to buildings with old intercom wiring.")],
      ["Simplebus two-wire video", "ViP network systems", "Repair and upgrades"])

brand("akuvox", "Akuvox", "Akuvox Intercom Installation & Repair NYC | Jacob Intercom",
      "Akuvox intercom installation and repair in New York: network door phones, indoor monitors and app answering for apartment buildings and offices.",
      "Akuvox makes network intercoms: door phones with cameras and touchscreens, indoor monitors, and app answering. We install and service them across New York.",
      """
<h2>About Akuvox</h2>
<p>Akuvox is a manufacturer of network-based intercoms. Its door phones connect to a building's network, call indoor monitors or residents' phones, and often handle access with fobs, codes or face recognition as well.</p>
<h2>What we install</h2>
<ul>
<li><strong>Door phones</strong> from simple button units to large touchscreen directory panels. The [[akuvox-r29/|Akuvox R29]], a door phone with a touchscreen and face recognition, is one we fit.</li>
<li><strong>Indoor monitors</strong> for apartments and offices.</li>
<li><strong>App answering</strong> through Akuvox's cloud service.</li>
<li><strong>Access control</strong> built into the door phone.</li>
</ul>
<h2>What the building needs</h2>
<p>Power and a network connection at each door phone, usually over one network cable, and a network that reaches each indoor monitor. In older buildings we often run the network over a dedicated cable alongside the old intercom riser.</p>
<h2>What goes wrong</h2>
<ul>
<li>Calls stop reaching monitors or phones after a network change.</li>
<li>A door phone loses power when its network switch fails.</li>
<li>Faces or fobs stop being recognised after a settings change.</li>
<li>The door release fails, usually at the strike.</li>
</ul>
<p>Many Akuvox faults are in settings or the network, and are fixed without replacing hardware.</p>
<h2>What it costs</h2>
<p>[AKUVOX INSTALL AND REPAIR RANGES]. Dealer status: [AKUVOX DEALER OR NOT].</p>
""",
      [("Does Akuvox work with phone apps?", "Yes, through Akuvox's cloud service."),
       ("Can Akuvox run on old intercom wiring?", "It needs network cable. Some buildings can reuse existing cable with adapters; most need a new run to the door."),
       ("Do you install the Akuvox R29?", "Yes. See [[akuvox-r29/|the R29 page]].")],
      ["Network door phones", "Indoor monitors and app answering", "Installation and repair"])


def short_brand(slug, name, about, where, works, faqs, facts):
    brand(slug, name, f"{name} Intercom Repair NYC | Jacob Intercom",
          f"{name} intercom repair and service in New York. {where}",
          f"{about} We repair and service {name} systems across the five boroughs.",
          f"""
<h2>About {name}</h2>
<p>{about}</p>
<h2>Where you'll find it</h2>
<p>{where}</p>
<h2>What we do</h2>
{works}
<h2>What it costs</h2>
<p>Most repairs fall in our usual range of $100 to $300, plus parts where a component is replaced: [{name.upper()} PART PRICES]. You get the price before we start.</p>
<p>[JACOB: {name.upper()} FAULTS HE SEES MOST]</p>
""", faqs, facts)


short_brand("tektone", "TekTone",
            "TekTone is an American maker of apartment entry and nurse call systems. Its Tek-ENTRY apartment stations and amplifiers share model numbers with Lee-Dan's, and the two are sold as replacements for each other.",
            "Audio intercoms in walk-ups and small apartment buildings, often mixed with Lee-Dan parts.",
            """<p>We replace TekTone apartment stations, amplifiers and lobby panel parts, and repair the wiring between them. Because TekTone and Lee-Dan parts with the same numbers are interchangeable, much of our [[lee-dan-intercom-systems/|Lee-Dan guide]] applies to TekTone systems too, including the [[lee-dan-intercom-systems/wiring/|wiring guide]] and [[lee-dan-intercom-systems/troubleshooting/|troubleshooting guide]].</p>""",
            [("Are TekTone and Lee-Dan parts interchangeable?", "Stations and amplifiers with the same model numbers, such as the IR-204E and PK-543A, are sold as direct replacements for each other."),
             ("Can a TekTone system be upgraded to video?", "Often, on the existing wiring. See [[intercom-replacement/|replacement and upgrades]].")],
            ["Apartment entry systems", "Interchangeable with <b>Lee-Dan</b>", "Repair and parts"])
short_brand("mircom", "Mircom",
            "Mircom is a Canadian maker of fire alarm, telephone entry and building systems.",
            "Telephone entry panels in larger apartment buildings, where the panel dials each resident's phone.",
            """<p>We service Mircom telephone entry panels: directory updates, keypads, door release, power and the phone line or cellular link. See [[intercom-installation/telephone-entry/|telephone entry systems]].</p>""",
            [("Can you update the names on our Mircom directory?", "Yes, as part of a service visit or by itself."),
             ("Our Mircom panel stopped calling residents. What is it?", "Usually the phone line or cellular service to the panel. We test that first.")],
            ["Telephone entry", "Directory and keypad service", "Door release"])
short_brand("siedle", "Siedle",
            "Siedle is a long-established German maker known for design-led, high-quality door stations.",
            "Townhouses, luxury apartment buildings and architect-designed entrances.",
            """<p>We service Siedle door stations and indoor units, replace modules, and repair door release and wiring. Siedle panels are modular and finished to order, so replacement parts are matched to the existing finish where possible.</p>""",
            [("Can a single Siedle module be replaced?", "Yes. Siedle panels are built from modules that can be changed individually."),
             ("Do you install new Siedle systems?", "[YES OR NO]")],
            ["Design-led door stations", "Module replacement", "Repair and service"])
short_brand("elvox", "Elvox",
            "Elvox is an Italian intercom maker, now part of the Vimar group.",
            "Video and audio systems in apartment buildings, many installed in the 1990s and 2000s.",
            """<p>We repair Elvox entry panels, monitors and handsets, power supplies and wiring. Where an older Elvox line is no longer supported, we advise on compatible replacements or an upgrade on the existing wire.</p>""",
            [("Are Elvox parts still available?", "For current lines, yes. Older lines vary, and we check before quoting."),
             ("Can an Elvox system be replaced without rewiring?", "Often. See [[intercom-replacement/|replacement and upgrades]].")],
            ["Italian video systems", "Repair and parts", "Upgrade advice"])
short_brand("doorbird", "DoorBird",
            "DoorBird is a German maker of network video door stations in stainless steel and bronze, answered on a phone app or an indoor monitor.",
            "Townhouses, single-family homes and small buildings.",
            """<p>We install DoorBird door stations, connect them to door strikes and gate releases, and set up app answering. We also repair power, network and door release faults on existing DoorBird installations. See [[intercom-installation/ip-smartphone/|IP and smartphone intercoms]].</p>""",
            [("Does DoorBird need a network cable?", "Most models are powered and connected over one network cable, which is the most reliable setup."),
             ("Can DoorBird open a gate and a door?", "Yes, with the right relay setup.")],
            ["Network video door stations", "Installation and app setup", "Repair"])
short_brand("2n", "2N",
            "2N is a Czech maker of network intercoms and access control, owned by Axis Communications.",
            "Offices, institutions and newer apartment buildings.",
            """<p>We install and service 2N network intercoms and access units: door stations, keypads, card readers and the door hardware they control. Many 2N faults are in network or software settings and are fixed without replacing equipment.</p>""",
            [("Does 2N work with phone apps?", "Yes, through 2N's mobile and cloud services."),
             ("Can 2N handle access control as well?", "Yes. Many 2N door stations include card, code or Bluetooth access.")],
            ["Network intercoms", "Access control", "Installation and repair"])
short_brand("doorking", "DoorKing",
            "DoorKing is an American maker of telephone entry systems and gate operators.",
            "Gates, parking entrances and buildings with telephone entry.",
            """<p>We service DoorKing telephone entry panels: directory programming, keypads, phone lines and the release of the door or gate. See [[intercom-installation/telephone-entry/|telephone entry systems]].</p>""",
            [("Can you reprogram our DoorKing directory?", "Yes."),
             ("Our gate opens but the entry panel doesn't call anyone. What is it?", "Usually the phone line or cellular service to the panel.")],
            ["Telephone entry", "Gate and door release", "Programming and repair"])
short_brand("alpha-communications", "Alpha Communications",
            "Alpha Communications is an American maker of apartment entry and intercom systems.",
            "Audio and video apartment entry in buildings across the city.",
            """<p>We repair Alpha entry panels, apartment stations, amplifiers and wiring, and replace failed parts with compatible units.</p>""",
            [("Are Alpha parts still available?", "For current lines, yes. We check older models before quoting.")],
            ["Apartment entry systems", "Repair and parts", "Wiring"])
short_brand("pacific-electronics", "Pacific Electronics",
            "Pacific Electronics made apartment entry systems found in older buildings.",
            "Older apartment buildings that haven't replaced their original entry system.",
            """<p>We repair Pacific Electronics entry panels, stations and wiring where parts allow, and advise on compatible replacements where they don't.</p>""",
            [("Can a Pacific Electronics system still be repaired?", "Often, depending on the fault and the part. We test before quoting.")],
            ["Older apartment entry", "Repair where parts allow", "Replacement advice"])
short_brand("nutone", "NuTone",
            "NuTone, now part of Broan-NuTone, made whole-house intercoms that were fitted in many American homes from the 1960s onward. Most are no longer manufactured.",
            "Private houses, with a master station in the kitchen and room stations throughout.",
            """<p>We repair NuTone master and room stations, door speakers and wiring where parts allow, and replace systems that can't be saved. Many houses replace a NuTone with a modern video door station and a phone app, reusing some of the old wiring.</p>""",
            [("Are NuTone intercoms still made?", "Most NuTone whole-house intercoms are no longer manufactured. Parts come from remaining stock and compatible units."),
             ("Can the old NuTone wiring be reused?", "Sometimes, for a new door station. We test it first.")],
            ["Whole-house intercoms", "Repair where parts allow", "Replacement"])
short_brand("m-and-s", "M&S",
            "M&amp;S Systems made whole-house intercom and music systems for private homes.",
            "Private houses, with a master unit and room stations.",
            """<p>We repair M&amp;S master units, room stations and door speakers where parts allow, and replace systems that can no longer be repaired.</p>""",
            [("Can an M&amp;S system still be repaired?", "Often, depending on the part. We test before quoting.")],
            ["Whole-house intercoms", "Repair", "Replacement"])

# ───────────────────────────── Boroughs ─────────────────────────────


def borough(path, name, title, stock, hoods, note):
    hood_list = ", ".join(hoods)
    page(path=path, nav=name[0].upper() + name[1:], title=title,
         desc=f"Intercom repair and installation in {name}. Buzzers, door releases, video entry and Lee-Dan systems. Most repairs $100 to $300. Call 718-252-2730.",
         h1=f"Intercom repair and installation in {name}",
         lead=f"We repair and install intercoms in every kind of building in {name}. Most repairs run $100 to $300, priced before we start.",
         facts=["<b>35 years</b> in New York", "Most repairs <b>$100 to $300</b>", "<b>4.7 stars</b> from 23 Google reviews"],
         body=f"""
<h2>{name} buildings and their intercoms</h2>
{stock}
<h2>What we do in {name}</h2>
<ul>
<li>[[intercom-repair/|Intercom repair]]: [[intercom-repair/door-buzzer/|dead buzzers]], [[intercom-repair/door-release/|doors that won't unlock]], [[intercom-repair/no-audio/|static and silence]], [[intercom-repair/video/|blank video]].</li>
<li>[[lee-dan-intercom-systems/|Lee-Dan]] and [[brands/|14 other brands]], old and new.</li>
<li>[[intercom-installation/|New installations]] and [[intercom-replacement/|replacements]], on the existing wiring where possible.</li>
<li>[[access-control/|Access control]] and [[security-cameras/|cameras]] at the entrance.</li>
</ul>
<h2>Neighborhoods we cover</h2>
<p>{hood_list}, and the rest of {name}.</p>
{note}
<h2>Recent jobs in {name}</h2>
<p class="sample">Sample</p>
<p>[THREE {name.upper()} JOBS WITH NEIGHBORHOOD, BUILDING TYPE, PROBLEM AND PHOTO]</p>
<h2>What it costs</h2>
<p>Most single-fault repairs cost $100 to $300. See [[pricing/|pricing]] for installations and larger repairs.</p>
""",
         faqs=[(f"Do you charge extra to come to {name}?", "[TRAVEL CHARGE BY AREA, IF ANY]"),
               (f"How soon can you get to a building in {name}?", "Call {{tel}} for the next opening. Urgent faults, such as a door that won't lock, go to the front of the schedule.")],
         related=[("intercom-repair/", "Intercom repair"), ("lee-dan-intercom-systems/", "Lee-Dan systems"), (INST, "Installation"), ("contact/", "Contact us")])


borough("intercom-installation-brooklyn/", "Brooklyn", "Intercom Repair & Installation Brooklyn NY | Jacob Intercom",
        """<p>Brooklyn is our home borough: the office is on Avenue F in Kensington. Its housing runs from brownstones and limestone rowhouses in Park Slope, Bed-Stuy and Crown Heights, to pre-war walk-ups and elevator buildings along Ocean Parkway, Eastern Parkway and in Flatbush, to co-ops in Brooklyn Heights and new towers downtown and in Williamsburg.</p>
<p>That means every kind of intercom: [[brownstone-intercom/|two to four family systems]] with outer and vestibule doors, [[lee-dan-intercom-systems/|Lee-Dan]] and TekTone audio in walk-ups, two-wire video in upgraded co-ops, and phone-based systems in new buildings.</p>""",
        ["Kensington", "Flatbush", "Midwood", "Borough Park", "Bay Ridge", "Sheepshead Bay", "Park Slope", "Bed-Stuy", "Crown Heights", "Williamsburg", "Brooklyn Heights", "Bushwick"],
        "<p>Our Google listing ranks first for intercom repair around our office, and we reach most of south and central Brooklyn quickly.</p>")
borough("intercom-installation-manhattan/", "Manhattan", "Intercom Repair & Installation Manhattan NY | Jacob Intercom",
        """<p>Manhattan has the city's densest mix of intercom systems: tenement walk-ups on the Lower East Side and in Harlem, pre-war co-ops on the Upper West and Upper East Sides, converted lofts downtown, townhouses in the Village, and doorman buildings where the intercom calls the front desk.</p>
<p>Older audio systems are still common in walk-ups. [[co-op-condo-intercom/|Co-ops]] are often weighing an upgrade to video or phone answering, and townhouses tend toward high-end panels such as [[brands/siedle/|Siedle]].</p>""",
        ["Upper West Side", "Upper East Side", "Harlem", "Washington Heights", "Midtown", "Chelsea", "Greenwich Village", "East Village", "Lower East Side", "Tribeca", "Financial District"],
        "<p>Manhattan calls can also reach us on 212-837-2147.</p>")
borough("intercom-installation-queens/", "Queens", "Intercom Repair & Installation Queens NY | Jacob Intercom",
        """<p>Queens has a wide range of building types: the garden apartment co-ops of Jackson Heights, six-storey brick apartment houses in Forest Hills, Rego Park and Kew Gardens, two-family attached houses across Astoria, Woodside and Ridgewood, and new towers in Long Island City.</p>
<p>Many Queens co-ops have several entrances around a courtyard, each needing its own panel. Attached two-family houses usually need a [[brownstone-intercom/|small system]] for two apartments.</p>""",
        ["Astoria", "Long Island City", "Jackson Heights", "Elmhurst", "Forest Hills", "Rego Park", "Kew Gardens", "Flushing", "Bayside", "Sunnyside", "Woodside", "Ridgewood", "Jamaica"],
        "")
borough("intercom-installation-bronx/", "the Bronx", "Intercom Repair & Installation Bronx NY | Jacob Intercom",
        """<p>The Bronx has some of the city's finest pre-war apartment buildings, including the art deco blocks along the Grand Concourse, alongside large elevator buildings, garden apartments in Parkchester and Co-op City, and houses in Riverdale and Throgs Neck.</p>
<p>Large buildings here often have long riser runs and several entrances, and many still run on older audio systems that are good candidates for an [[intercom-replacement/|upgrade on the existing wire]].</p>""",
        ["Riverdale", "Kingsbridge", "Fordham", "Grand Concourse", "Mott Haven", "Pelham Bay", "Throgs Neck", "Morris Park", "Parkchester"],
        "<p>Bronx calls can also reach us on 212-837-2147.</p>")
borough("intercom-installation-staten-island/", "Staten Island", "Intercom Repair & Installation Staten Island NY | Jacob Intercom",
        """<p>Staten Island is mostly one and two-family houses, with apartment buildings and co-ops along the North Shore and near the ferry, and garden apartment complexes elsewhere.</p>
<p>That means more [[brownstone-intercom/|two-family systems]], [[brands/nutone/|whole-house intercoms]] in older homes, and video door stations with phone apps in newer ones.</p>""",
        ["St. George", "Stapleton", "Tompkinsville", "New Brighton", "West Brighton", "Port Richmond", "Great Kills", "Tottenville", "New Dorp"],
        "")

# ───────────────────────────── Access control and cameras ─────────────────────────────

AC_RELATED = [("access-control/", "Access control"), ("access-control/key-fob/", "Key fob systems"), ("access-control/electric-strikes-maglocks/", "Strikes and magnetic locks"), ("security-cameras/", "Security cameras")]


def svc(path, nav, title, desc, h1, lead, body, faqs, facts):
    page(path=path, nav=nav, title=title, desc=desc, h1=h1, lead=lead, facts=facts,
         aside={"head": "Securing an entrance?", "text": "Send a photo of the door and frame and tell us how many people need access. We'll suggest what fits."},
         body=body, faqs=faqs, related=AC_RELATED)


svc("access-control/", "Access control",
    "Access Control Installation NYC: Fobs, Codes & Card Readers | Jacob Intercom",
    "Access control for New York apartment buildings and offices: key fobs, codes, card readers and phone access, installed with the door hardware they control.",
    "Access control systems",
    "An intercom lets visitors in. Access control lets residents and staff in, without keys, and keeps a record of who did.",
    """
<h2>The options</h2>
<div class="tablebox"><table>
<thead><tr><th scope="col">Method</th><th scope="col">How it works</th><th scope="col">Good for</th></tr></thead>
<tbody>
<tr><th scope="row">[[access-control/key-fob/|Key fobs and cards]]</th><td>Tap a fob or card on a reader</td><td>Apartment buildings, offices</td></tr>
<tr><th scope="row">Keypads</th><td>Enter a code</td><td>Back doors, staff entrances, deliveries</td></tr>
<tr><th scope="row">Phone access</th><td>Open from an app or with Bluetooth</td><td>Buildings with phone-based intercoms</td></tr>
<tr><th scope="row">Intercom-integrated</th><td>The intercom panel includes the reader</td><td>New installations</td></tr>
</tbody></table></div>
<h2>Why buildings switch from keys</h2>
<ul>
<li>A lost fob is switched off in minutes. A lost key means new locks and new keys for everyone.</li>
<li>Access can be limited to certain doors or times.</li>
<li>Most systems keep a log of entries.</li>
</ul>
<h2>The door hardware</h2>
<p>Every access system ends at a lock that releases: an [[access-control/electric-strikes-maglocks/|electric strike or a magnetic lock]], plus a way out from the inside. Choosing the right one for the door matters as much as the reader. Exits must work without a key or code, under the building and fire codes.</p>
<h2>What it costs</h2>
<p>[ACCESS CONTROL INSTALL RANGE BY NUMBER OF DOORS]</p>
""",
    [("Can access control work with our existing intercom?", "Usually. The reader and the intercom can release the same door."),
     ("Who manages the fobs?", "The super or managing agent, through simple software. We set it up and show them how."),
     ("What happens in a power cut?", "It depends on the lock. Magnetic locks release, strikes can be set to stay locked. Exits must always open from inside.")],
    ["Fobs, codes and phone access", "Installed with the <b>door hardware</b>", "Works alongside the intercom"])
svc("access-control/key-fob/", "Key fob systems",
    "Key Fob Entry Systems for NYC Apartment Buildings | Jacob Intercom",
    "Key fob entry systems for New York apartment buildings: how they work, what they cost, and how to manage lost fobs and new residents.",
    "Key fob entry systems",
    "Residents tap a fob instead of turning a key. When one is lost, it is switched off, not replaced with a new set of locks.",
    """
<h2>How it works</h2>
<p>A reader beside the door reads the fob when it is held close. If the fob is on the building's list, the reader releases the door for a few seconds. The list is kept in a small controller or online, and the super or managing agent adds and removes fobs.</p>
<h2>What to decide</h2>
<ul>
<li><strong>Which doors.</strong> Front door only, or also the back door, laundry, roof, garage and mailroom.</li>
<li><strong>Who manages it.</strong> Software on a computer in the building, or online from anywhere.</li>
<li><strong>Fob or card type.</strong> Some fobs are easy to copy. More secure types cost a little more and are harder to duplicate.</li>
<li><strong>Combined with the intercom.</strong> Many new intercom panels include a fob reader.</li>
</ul>
<h2>Lost fobs and new residents</h2>
<p>A lost fob is deleted from the list and stops working straight away. New residents get a fob programmed in minutes. Buildings usually keep a small stock of blank fobs for this.</p>
<h2>What it costs</h2>
<p>[KEY FOB SYSTEM RANGE AND PRICE PER FOB]</p>
""",
    [("Can residents copy their own fobs?", "Common low-security fobs can be copied at kiosks. If that matters, choose an encrypted fob type."),
     ("Can we add fobs to our existing intercom?", "Often. A separate reader can release the same door strike."),
     ("How much does a replacement fob cost?", "[PRICE PER FOB]")],
    ["Tap to enter", "Lost fobs switched off <b>at once</b>", "Works with the intercom"])
svc("access-control/electric-strikes-maglocks/", "Strikes and magnetic locks",
    "Electric Strike & Magnetic Lock Installation NYC | Jacob Intercom",
    "Electric strike and magnetic lock installation and repair in New York. Which to choose for your door, how they fail, and what they cost.",
    "Electric strikes and magnetic locks",
    "The part that actually lets people in. Get it wrong and the best intercom in the world buzzes a door that won't open.",
    """
<h2>Two ways to release a door</h2>
<div class="tablebox"><table>
<thead><tr><th scope="col"></th><th scope="col">Electric strike</th><th scope="col">Magnetic lock</th></tr></thead>
<tbody>
<tr><th scope="row">How it works</th><td>Replaces the latch plate in the frame. Releases the latch when powered.</td><td>A magnet on the frame holds a plate on the door. Releases when power is cut.</td></tr>
<tr><th scope="row">In a power cut</th><td>Can be set to stay locked or release</td><td>Releases</td></tr>
<tr><th scope="row">Suits</th><td>Most doors with a latch or lockset</td><td>Glass doors, double doors, doors where the frame can't be cut</td></tr>
<tr><th scope="row">Needs</th><td>A frame that can take the strike</td><td>A request-to-exit button or sensor inside</td></tr>
</tbody></table></div>
<h2>Why strikes fail</h2>
<ul>
<li>The door sags or the frame moves, and the latch binds against the strike.</li>
<li>The strike is held open too long and burns out.</li>
<li>The wrong voltage, or AC on a strike built for DC.</li>
<li>Wear, after hundreds of thousands of releases.</li>
</ul>
<p>See [[intercom-repair/door-release/|door release repair]] for symptoms.</p>
<h2>Getting out safely</h2>
<p>Every locked entrance must open from the inside without a key, code or special knowledge. With magnetic locks that means an exit button, a motion sensor, or both, wired to release the lock. We fit these to the codes that apply.</p>
<h2>What it costs</h2>
<p>[STRIKE AND MAGLOCK INSTALL PRICES]</p>
""",
    [("Which is better, a strike or a magnetic lock?", "For most single wooden or steel doors with a latch, a strike. For glass and double doors, often a magnetic lock."),
     ("Our door doesn't lock again after it's buzzed. Is that the strike?", "Usually, or the door closer. It is a security problem worth fixing promptly."),
     ("Can you fit a strike to an old door?", "Yes, in most cases. Surface-mounted strikes avoid cutting historic frames.")],
    ["Strikes and magnetic locks", "Repair and installation", "Fitted to <b>code</b>"])
svc("security-cameras/", "Security cameras",
    "Security Camera Installation NYC: Buildings, Entrances & Stores | Jacob Intercom",
    "Security camera installation and repair in New York for apartment buildings, entrances, stores and homes. Placement, recording and remote viewing.",
    "Security camera installation",
    "Cameras where they help: the entrance, the mailroom, the hallways and the back door, recorded and viewable on your phone.",
    """
<h2>Where cameras help most</h2>
<ul>
<li><strong>The entrance,</strong> covering everyone who comes and goes.</li>
<li><strong>The mailroom and package area,</strong> where most building thefts happen.</li>
<li><strong>Back doors, alleys and basements.</strong></li>
<li><strong>Hallways and stairwells</strong> in larger buildings.</li>
<li><strong>The sales floor and register</strong> in stores.</li>
</ul>
<h2>What to decide</h2>
<ul>
<li><strong>How many cameras</strong> and where. We walk the building and mark positions with you.</li>
<li><strong>How long to keep recordings,</strong> which sets the size of the recorder.</li>
<li><strong>Who can view,</strong> and from where. Most systems have a phone app.</li>
<li><strong>Night coverage.</strong> Cameras with infrared see in the dark.</li>
</ul>
<h2>Privacy</h2>
<p>Cameras should cover shared and public areas, not into apartments or private spaces. Post a notice where cameras are in use. We place cameras with this in mind.</p>
<h2>Repair</h2>
<p>We repair cameras that have stopped recording, lost their picture or dropped off the app, and recorders that have filled up or failed.</p>
<h2>What it costs</h2>
<p>[CAMERA INSTALL RANGE BY NUMBER OF CAMERAS]. See also [[security-cameras/apartment-buildings/|cameras for apartment buildings]].</p>
""",
    [("Can I view the cameras on my phone?", "Yes, on almost every system we install."),
     ("How long are recordings kept?", "It depends on the recorder's size and the number of cameras, usually from a week to a month or more."),
     ("Which camera brands do you install?", "[CAMERA BRANDS JACOB INSTALLS]")],
    ["Placement, recording, phone viewing", "Buildings, stores and homes", "Repair"])
svc("security-cameras/apartment-buildings/", "Cameras for apartment buildings",
    "Security Cameras for NYC Apartment Buildings | Jacob Intercom",
    "Security cameras for New York apartment buildings: entrances, mailrooms, hallways and package areas. Placement, recording, access for supers and boards.",
    "Security cameras for apartment buildings",
    "Package theft, propped doors and strangers in the stairwell. A few well-placed cameras deal with most of it.",
    """
<h2>A typical layout</h2>
<div class="tablebox"><table>
<thead><tr><th scope="col">Position</th><th scope="col">What it covers</th></tr></thead>
<tbody>
<tr><th scope="row">Outside the front door</th><td>Everyone approaching and leaving</td></tr>
<tr><th scope="row">Inside the vestibule</th><td>Faces at close range, people let in by the intercom</td></tr>
<tr><th scope="row">Mailroom or package shelf</th><td>Package deliveries and pickups</td></tr>
<tr><th scope="row">Back door and basement</th><td>Service entrances, often the least watched</td></tr>
<tr><th scope="row">Elevator lobby or stairwell</th><td>Movement inside the building, in larger buildings</td></tr>
</tbody></table></div>
<h2>Who gets access</h2>
<p>Usually the super and managing agent, sometimes board members. Residents generally don't have live access. We set up separate logins so access can be removed when someone leaves.</p>
<h2>Working with the intercom</h2>
<p>A video intercom and an entrance camera do different jobs: the intercom shows a visitor to one resident, the camera records everyone for the building. Some systems combine both.</p>
<h2>What it costs</h2>
<p>[APARTMENT BUILDING CAMERA RANGE]</p>
<p>[JACOB: A BUILDING CAMERA JOB TO FEATURE]</p>
""",
    [("Can residents see the cameras?", "Usually not live. Footage is reviewed by the super or managing agent when there is an incident."),
     ("Do we need to tell residents about the cameras?", "Yes. Post notices in covered areas, and check any rules in your lease, bylaws or local law.")],
    ["Entrances, mailrooms, hallways", "Access for supers and boards", "Installation and repair"])

# ───────────────────────────── Existing product pages (URLs kept) ─────────────────────────────

PROD_RELATED = [("lee-dan-intercom-systems/2easy/", "Lee-Dan 2Easy"), ("intercom-installation/video/", "Video intercoms"), ("brands/", "Brands we service"), ("contact/", "Contact us")]
PROD_NOTE = '<div class="note"><p><strong>For Jacob to confirm before launch:</strong> whether he still sells and installs this model, and its price fitted. Specifications should be checked against the manufacturer\'s current sheet.</p></div>'


def product(path, nav, title, desc, h1, lead, body, faqs, facts, related=PROD_RELATED):
    page(path=path, nav=nav, title=title, desc=desc, h1=h1, lead=lead, facts=facts,
         aside={"head": "Want this installed?", "text": "Tell us the number of apartments and send a photo of your current panel. We'll tell you if it fits and what it costs."},
         body=PROD_NOTE + body, faqs=faqs, related=related)


product("akuvox-r29/", "Akuvox R29",
        "Akuvox R29 Video Door Phone: Installation in NYC | Jacob Intercom",
        "The Akuvox R29 network video door phone with a 7-inch touchscreen and face recognition, installed in New York apartment buildings and offices.",
        "Akuvox R29 video door phone",
        "A touchscreen door phone for buildings that want a resident directory, video calls to phones and monitors, and keyless entry in one panel.",
        """
<h2>What it is</h2>
<p>The R29 is a network door phone from [[brands/akuvox/|Akuvox]]. A visitor finds a resident on its 7-inch touchscreen directory and calls them. The call reaches an indoor monitor, a phone app, or both, with video from the panel's camera.</p>
<h2>What it does</h2>
<ul>
<li><strong>Resident directory</strong> on the touchscreen, searchable by name.</li>
<li><strong>Video calls</strong> to indoor monitors and to residents' phones.</li>
<li><strong>Face recognition</strong> so residents can enter without a fob or code.</li>
<li><strong>Codes, cards and fobs</strong> for residents, staff and deliveries.</li>
<li><strong>Remote management</strong> of residents and access through Akuvox's cloud service.</li>
</ul>
<h2>Where it fits</h2>
<p>Mid-size and large apartment buildings, condos and offices that want a modern entrance and are ready for a network-based system. It needs a network cable to the door for power and data. See [[intercom-installation/ip-smartphone/|IP and smartphone intercoms]].</p>
<h2>What installation involves</h2>
<ol>
<li>A network cable and switch to power the panel.</li>
<li>Mounting the panel, flush or on the surface, in place of the old one.</li>
<li>Connecting the door strike or lock and the exit button.</li>
<li>Loading the resident directory and setting up the app.</li>
<li>Indoor monitors in apartments that want one.</li>
</ol>
<h2>What it costs</h2>
<p>[R29 SUPPLIED AND FITTED PRICE, PLUS MONITORS AND CLOUD FEES]</p>
""",
        [("Does the R29 need internet?", "It runs on the building's network. Calls to phones need internet; local monitors and door release do not."),
         ("Can face recognition be turned off?", "Yes. Buildings can use codes, cards or fobs instead."),
         ("Can the R29 replace our old intercom panel?", "Yes. We fit it in place of the old panel and run the network cable it needs.")],
        ["7-inch <b>touchscreen</b> directory", "Face recognition and codes", "Calls monitors and phones"],
        related=[("brands/akuvox/", "Akuvox"), ("intercom-installation/ip-smartphone/", "IP and smartphone intercoms"), ("access-control/", "Access control"), ("contact/", "Contact us")])

product("dt-607entry-panels/", "DT-607 entry panels",
        "Lee-Dan 2Easy DT-607 Entry Panel: Installation NYC | Jacob Intercom",
        "The Lee-Dan 2Easy DT-607 video entry panel for brownstones and small buildings, installed on two wires in New York.",
        "DT-607 video entry panel",
        "The door panel of Lee-Dan's 2Easy two-wire video system, sized for houses and small buildings.",
        """
<h2>What it is</h2>
<p>The DT-607 is a video entry panel in Lee-Dan's [[lee-dan-intercom-systems/2easy/|2Easy]] range. It has a camera, a speaker and microphone, and call buttons, and connects to apartment monitors over two wires.</p>
<h2>Where it fits</h2>
<p>Brownstones, two to four family houses and small walk-ups, especially those upgrading from an old audio intercom on the existing wire. See [[brownstone-intercom/|brownstone intercoms]].</p>
<h2>Paired with</h2>
<p>Apartment monitors such as the [[dx-471-monitor/|DX-471]] touchscreen, and the 2Easy power supply.</p>
<h2>What installation involves</h2>
<p>We test the existing wire to each apartment, fit the panel, ideally covering the old panel's opening, connect the monitors and the door release, and test every apartment.</p>
<h2>What it costs</h2>
<p>[DT-607 SYSTEM PRICE BY NUMBER OF APARTMENTS]</p>
""",
        [("Can the DT-607 use our old intercom wiring?", "Often. 2Easy needs two wires per apartment, and older systems usually have more."),
         ("How many apartments can it call?", "[BUTTON COUNTS AVAILABLE]")],
        ["Lee-Dan <b>2Easy</b> range", "Two-wire colour video", "For houses and small buildings"])

product("dvt-104/", "DVT-104 video door phone",
        "Lee-Dan DVT-104 Video Door Phone: Installation NYC | Jacob Intercom",
        "The Lee-Dan DVT-104 video door phone, installed in New York homes and small buildings.",
        "DVT-104 video door phone",
        "A compact video door station for a house or a small building, from Lee-Dan.",
        """
<h2>What it is</h2>
<p>The DVT-104 is a Lee-Dan video door phone: a door station with a camera and call button, used with an indoor monitor so residents can see and talk to visitors and release the door.</p>
<h2>Where it fits</h2>
<p>Single-family houses, townhouses and small buildings that want simple video entry. See [[home-intercom/|home intercoms]] and [[brownstone-intercom/|brownstone intercoms]].</p>
<h2>What installation involves</h2>
<p>Fitting the door station, the indoor monitor and the wiring between them, and connecting the door release. Where an older door station is being replaced, we test whether the existing wire can be reused.</p>
<h2>What it costs</h2>
<p>[DVT-104 SUPPLIED AND FITTED PRICE]</p>
""",
        [("Is the DVT-104 part of the 2Easy range?", "[CONFIRM WITH JACOB]"),
         ("Can it open a gate as well as a door?", "[CONFIRM WITH JACOB]")],
        ["Lee-Dan video door phone", "For houses and small buildings", "Supplied and fitted"])

product("dx-471-monitor/", "DX-471 monitor",
        "Lee-Dan 2Easy DX-471 Touchscreen Monitor: Installation NYC | Jacob Intercom",
        "The Lee-Dan 2Easy DX-471 7-inch colour touchscreen apartment monitor, installed in New York buildings on two-wire systems.",
        "DX-471 touchscreen monitor",
        "The apartment monitor of Lee-Dan's 2Easy system: a 7-inch colour touchscreen that shows the visitor and opens the door.",
        """
<h2>What it is</h2>
<p>The DX-471 is a 7-inch colour touchscreen monitor in Lee-Dan's [[lee-dan-intercom-systems/2easy/|2Easy]] range. When a visitor calls, it shows them from the door panel's camera. The resident talks hands-free and releases the door from the screen.</p>
<h2>Where it fits</h2>
<p>In each apartment of a 2Easy system, with door panels such as the [[dt-607entry-panels/|DT-607]]. It replaces an old audio station on the same wall, often on the same wires.</p>
<h2>Repair and replacement</h2>
<p>A monitor that has stopped showing a picture or ringing is tested at the wall first, because the fault can be in the wiring or the power supply. A failed monitor is replaced like for like.</p>
<h2>What it costs</h2>
<p>[DX-471 SUPPLIED AND FITTED PRICE]</p>
""",
        [("Can one apartment get a DX-471 while others keep old stations?", "Not on an old audio system. The building needs a 2Easy door panel and power supply first."),
         ("Does the DX-471 work with a phone app?", "[CONFIRM WITH JACOB]")],
        ["7-inch <b>colour touchscreen</b>", "Lee-Dan 2Easy range", "Two-wire installation"])

# ───────────────────────────── Guides ─────────────────────────────

G = "guides/"
G_RELATED = [(G, "All guides"), ("intercom-repair/", "Intercom repair"), ("pricing/", "Pricing"), ("contact/", "Contact us")]


def guide(slug, nav, title, desc, h1, lead, body, faqs=None, facts=None):
    page(path=G + slug + "/", nav=nav, title=title, desc=desc, h1=h1, lead=lead,
         facts=facts or ["Written by <b>intercom technicians</b>", "<b>35 years</b> of New York jobs", "Updated November 2026"],
         body=body, faqs=faqs or [], related=G_RELATED)


GUIDES = [
    ("intercom-repair-cost-nyc", "What intercom repair costs in NYC"),
    ("intercom-installation-cost-nyc", "What intercom installation costs in NYC"),
    ("repair-or-replace-intercom", "Repair or replace your intercom?"),
    ("nyc-landlord-intercom-requirements", "NYC intercom law for landlords"),
    ("how-apartment-intercoms-work", "How an apartment intercom works"),
    ("intercom-wiring-explained", "Intercom wiring explained"),
    ("apartment-intercom-troubleshooting", "Apartment intercom troubleshooting"),
    ("renters-broken-buzzer", "Your buzzer is broken: a renter's guide"),
    ("best-intercom-systems-nyc-buildings", "Choosing an intercom for a NYC building"),
    ("wired-vs-wireless-intercom", "Wired or wireless intercom?"),
    ("upgrade-buzzer-to-video", "Upgrading a buzzer system to video"),
    ("co-op-intercom-replacement", "Intercom replacement for co-op boards"),
]

page(path=G, nav="Guides",
     title="Intercom Guides for NYC Buildings, Owners & Renters | Jacob Intercom",
     desc="Plain guides to intercom costs, repairs, wiring, upgrades and NYC intercom law, written by technicians with 35 years of New York jobs.",
     h1="Intercom guides",
     lead="What we explain to customers every week, written down. Costs, how systems work, what to check, and what the law says.",
     facts=["<b>12</b> guides", "Costs, wiring, law, upgrades", "Written by technicians"],
     body="<h2>All guides</h2><ul class=\"linklist\">" + "".join(f"<li>[[{G}{s}/|{t}]]</li>" for s, t in GUIDES) + "</ul>"
          + "<h2>Lee-Dan guides</h2><ul class=\"linklist\"><li>[[lee-dan-intercom-systems/wiring/|Lee-Dan wiring guide]]</li><li>[[lee-dan-intercom-systems/troubleshooting/|Lee-Dan troubleshooting guide]]</li></ul>",
     related=[("intercom-repair/", "Intercom repair"), (INST, "Installation"), ("faq/", "FAQ"), ("contact/", "Contact us")])

guide("intercom-repair-cost-nyc", "Repair costs",
      "Intercom Repair Cost in NYC (2026 Guide) | Jacob Intercom",
      "What intercom repair costs in New York in 2026: price ranges by fault, what pushes the price up, and how to avoid paying for a system you don't need.",
      "What intercom repair costs in NYC",
      "Most intercom repairs in New York cost a few hundred dollars. What decides where yours falls is where the fault is and how easy it is to reach.",
      """
<h2>Typical prices</h2>
<p>Most single-fault repairs we do cost <strong>$100 to $300</strong>. Other New York companies publish similar figures: one lists $150 to $250 flat for common repairs, another a $250 diagnostic visit with parts extra.</p>
<div class="tablebox"><table>
<thead><tr><th scope="col">Repair</th><th scope="col">What it usually costs</th></tr></thead>
<tbody>
<tr><th scope="row">One apartment station replaced</th><td>$100 to $300</td></tr>
<tr><th scope="row">Door strike adjusted or repaired</th><td>$100 to $300</td></tr>
<tr><th scope="row">Panel speaker, microphone or button</th><td>$100 to $300</td></tr>
<tr><th scope="row">Amplifier or power supply</th><td>[AMPLIFIER RANGE]</td></tr>
<tr><th scope="row">Wiring fault inside walls</th><td>[WIRING REPAIR RANGE]</td></tr>
<tr><th scope="row">New entry panel on existing wiring</th><td>[PANEL RANGE]</td></tr>
</tbody></table></div>
<p>See [[pricing/|our full price list]].</p>
<h2>What pushes the price up</h2>
<ul>
<li><strong>Hidden wiring.</strong> A break inside a finished wall takes longer to find and reach than one in a basement.</li>
<li><strong>Discontinued parts.</strong> Parts for systems no longer made can cost more and take time to find.</li>
<li><strong>Building-wide faults.</strong> A problem on a shared wire affects many apartments and takes longer to trace.</li>
<li><strong>After-hours calls.</strong> Evenings and weekends usually cost more.</li>
<li><strong>Repeat visits.</strong> An intermittent fault that isn't happening when the technician arrives can take more than one trip.</li>
</ul>
<h2>How to keep the cost down</h2>
<ul>
<li><strong>Say how many apartments are affected.</strong> It narrows the fault before anyone arrives.</li>
<li><strong>Send photos</strong> of the entry panel, an apartment station and the amplifier.</li>
<li><strong>Ask for the price before work starts.</strong> We give it as standard.</li>
<li><strong>Get a second opinion on a replacement quote</strong> if the system has one fault.</li>
</ul>
<h2>When a repair isn't worth it</h2>
<p>If you've paid for several repairs in a year on different parts, or the parts are no longer made, the money may be better spent on replacement. See [[guides/repair-or-replace-intercom/|repair or replace]].</p>
""",
      [("Is there a charge just to diagnose the problem?", "[DIAGNOSIS FEE, AND WHETHER IT IS CREDITED TO THE REPAIR]"),
       ("Why do quotes vary so much between companies?", "Some price the repair, some price a replacement. Ask each one what they think has failed.")])

guide("intercom-installation-cost-nyc", "Installation costs",
      "Intercom Installation Cost in NYC (2026 Guide) | Jacob Intercom",
      "What a new intercom costs in New York: by building size and system type, what drives the price, and the ongoing fees to compare.",
      "What intercom installation costs in NYC",
      "A new intercom can cost a few hundred dollars for a house or tens of thousands for a large building. Four things decide the price.",
      """
<h2>The four things that set the price</h2>
<ol>
<li><strong>Number of apartments and entrances.</strong> Each apartment needs a station or monitor, each entrance a panel.</li>
<li><strong>Type of system.</strong> Audio is least expensive, then wired video, then network systems with touchscreens.</li>
<li><strong>Whether the existing wire can be reused.</strong> New cable through finished walls is often the largest cost.</li>
<li><strong>The door.</strong> A new strike, closer or magnetic lock is often needed too.</li>
</ol>
<h2>Typical ranges</h2>
<p>ButterflyMX, a smart-intercom maker, puts apartment building installations at about $500 to $5,000 or more for large properties. Our ranges by building size:</p>
<div class="tablebox"><table>
<thead><tr><th scope="col">Building</th><th scope="col">Audio</th><th scope="col">Video</th></tr></thead>
<tbody>
<tr><th scope="row">House or 2 to 4 apartments</th><td>[PRICE]</td><td>[PRICE]</td></tr>
<tr><th scope="row">5 to 12 apartments</th><td>[PRICE]</td><td>[PRICE]</td></tr>
<tr><th scope="row">13 to 30 apartments</th><td>[PRICE]</td><td>[PRICE]</td></tr>
<tr><th scope="row">Over 30 apartments</th><td>Quoted</td><td>Quoted</td></tr>
</tbody></table></div>
<h2>Ongoing costs to compare</h2>
<p>Wired audio and video systems have no monthly fee. Phone-based and cloud systems usually charge a subscription per building or per apartment. Over five or ten years that can exceed the installation price, so compare the total, not just the upfront figure.</p>
<h2>How to get an accurate quote</h2>
<p>A firm price needs a site visit to test the existing wiring. A quote given over the phone without that is an estimate. See [[intercom-installation/|installation]] and [[pricing/|pricing]].</p>
""",
      [("Is video much more expensive than audio?", "Video monitors cost more than audio stations, but on existing wiring the difference is often smaller than people expect."),
       ("Are there grants or tax breaks for intercom upgrades?", "Some building programs can apply. Ask your accountant or managing agent.")])

guide("repair-or-replace-intercom", "Repair or replace",
      "Repair or Replace Your Intercom? A Decision Guide | Jacob Intercom",
      "How to decide whether to repair or replace an apartment intercom: the signs, the costs, and the questions to ask before you sign a quote.",
      "Repair or replace your intercom?",
      "Most intercoms we're called to can be repaired. Here is how to tell when yours is one of the ones that can't.",
      """
<h2>Repair when</h2>
<ul>
<li>One part has failed: a station, the amplifier, the strike, a panel button.</li>
<li>The rest of the system has been reliable.</li>
<li>Parts are available.</li>
<li>The building is happy with what the system does.</li>
</ul>
<h2>Replace when</h2>
<ul>
<li>Different parts keep failing. Three or more repairs on different components in a year is a pattern.</li>
<li>Parts are no longer made and no compatible substitute exists.</li>
<li>The wiring is failing in several places.</li>
<li>The building wants video, phone answering or delivery codes.</li>
</ul>
<h2>A rule of thumb</h2>
<p>Add up what you've spent on repairs in the last two years and what the current repair would cost. If that is approaching half the price of a replacement, get a replacement quote. If it's a small fraction, repair. Connextivity, another New York integrator, uses a similar threshold: repair below about 30% of replacement cost, replace above about 50%.</p>
<h2>Questions to ask a company that recommends replacement</h2>
<ol>
<li>What exactly has failed?</li>
<li>Can that part be replaced on its own? If not, why not?</li>
<li>Can the existing wiring be reused?</li>
<li>What would a repair cost, for comparison?</li>
</ol>
<p>A company that can't answer the first question hasn't diagnosed the system.</p>
<h2>The middle option</h2>
<p>Replacing only the entry panel, or upgrading on the existing wire, often gives most of the benefit of a new system at a fraction of the cost. See [[intercom-replacement/|replacement and upgrades]].</p>
""",
      [("My intercom is 30 years old. Should I replace it?", "Age alone isn't a reason. Many 30-year-old systems still work well with occasional parts. Replace when it keeps failing or can't do what the building needs.")])

guide("nyc-landlord-intercom-requirements", "NYC intercom law",
      "NYC Intercom Law: What Landlords Must Provide (Multiple Dwelling Law 50-a) | Jacob Intercom",
      "What New York law requires of landlords for building intercoms and self-locking entrance doors under Multiple Dwelling Law 50-a, and what tenants can do.",
      "NYC intercom law for landlords",
      "In many New York apartment buildings, a working intercom and a self-locking front door are a legal requirement, not an amenity.",
      """
<div class="note"><p>This is a plain-English summary for general information, not legal advice. Read the law itself or speak to a lawyer about your building. [JACOB OR A LAWYER TO REVIEW BEFORE PUBLISHING]</p></div>
<h2>The law</h2>
<p>New York State's <a href="https://www.nysenate.gov/legislation/laws/MDW/50-A">Multiple Dwelling Law section 50-a</a> sets entrance door and intercom requirements for class A multiple dwellings, which covers most apartment buildings.</p>
<h2>What it requires</h2>
<ul>
<li><strong>Self-closing, self-locking entrance doors.</strong> Street-level entrances must close and lock automatically and stay locked unless an attendant is on duty.</li>
<li><strong>An intercom in buildings with eight or more apartments.</strong> It must be at the self-locking door to the main hall or lobby, let each apartment talk to the visitor outside, and let the occupant release the door lock from the apartment.</li>
<li><strong>Installation and maintenance by the owner.</strong> The owner must install the equipment and keep it working.</li>
</ul>
<h2>Which buildings</h2>
<ul>
<li><strong>Built or converted after January 1, 1968:</strong> the requirements apply directly. The intercom requirement applies to buildings with eight or more apartments.</li>
<li><strong>Built or converted before 1968:</strong> the same doors and intercom are required if tenants in a majority of apartments request them in writing. The owner then has to start work within 90 days and finish within six months.</li>
</ul>
<h2>Penalties</h2>
<p>An owner who fails to install or maintain the required equipment, or anyone who deliberately damages, jams or removes it, commits a misdemeanor under the Multiple Dwelling Law.</p>
<h2>For tenants</h2>
<ul>
<li>Report a broken intercom or door to the landlord or super in writing and keep a copy.</li>
<li>If it isn't fixed, you can report it to the city through 311, which passes housing complaints to HPD.</li>
<li>See [[guides/renters-broken-buzzer/|our renter's guide]].</li>
</ul>
<h2>For owners</h2>
<p>Keeping the intercom and door working is part of keeping the building legal and habitable. A yearly inspection catches most failures before tenants report them. See [[intercom-maintenance-contract/|maintenance contracts]] and [[property-managers/|property managers]].</p>
<h2>Rent-regulated buildings</h2>
<p>The law lets the rent agency set terms for recovering installation costs from tenants in rent-controlled buildings. Ask a lawyer or the agency before passing on any cost.</p>
""",
      [("Does my building have to have an intercom?", "Class A buildings built or converted after 1968 with eight or more apartments must. Older buildings must if a majority of tenants request one in writing."),
       ("Who has to pay to fix a broken intercom?", "The owner is responsible for maintaining it."),
       ("Is a video intercom required?", "No. The law requires voice communication and door release. Video is optional.")],
      facts=["<b>Multiple Dwelling Law 50-a</b>", "Buildings with <b>8 or more</b> apartments", "Owner must <b>maintain</b> it"])

guide("how-apartment-intercoms-work", "How intercoms work",
      "How an Apartment Intercom and Buzzer Works | Jacob Intercom",
      "How an apartment building intercom works, from the button at the door to the buzz that unlocks it. The parts, the wiring and what each does.",
      "How an apartment intercom works",
      "Every apartment intercom, old or new, does the same four things. Knowing how makes faults much easier to describe and to fix.",
      """
<h2>The four parts</h2>
<ol>
<li><strong>The entry panel</strong> at the front door: a button for each apartment, a speaker and a microphone, and on video systems a camera.</li>
<li><strong>The amplifier or controller</strong>, usually in the basement: it powers the system, makes the call tone, carries the voice and switches the door release.</li>
<li><strong>The apartment station</strong> on each apartment wall: a speaker, a microphone, and Talk, Listen and Door buttons, or a video monitor.</li>
<li><strong>The door release</strong>: an electric strike in the frame, or a magnetic lock, that lets the door open when powered.</li>
</ol>
<h2>What happens when a visitor calls</h2>
<ol>
<li>The visitor presses your button. That sends a signal up a wire that runs only to your apartment.</li>
<li>The amplifier sends a tone to your station, and it rings.</li>
<li>You press Talk to speak and Listen to hear. The voice travels on wires shared by every apartment.</li>
<li>You press Door. The amplifier powers the strike for a few seconds, and the visitor pushes the door open.</li>
<li>The door closes and locks itself again.</li>
</ol>
<h2>Shared wires and private wires</h2>
<p>That split explains most faults. A problem on your private call wire affects only you. A problem on a shared wire affects every apartment on it. See the [[guides/intercom-wiring-explained/|wiring guide]].</p>
<h2>How newer systems differ</h2>
<ul>
<li><strong>Two-wire systems</strong> send power, voice, video and calls over just two wires, using digital addressing to reach each apartment.</li>
<li><strong>Network systems</strong> use the building's internet, and can call phones as well as wall monitors.</li>
<li><strong>Telephone entry</strong> dials the resident's own phone instead of a wall station.</li>
</ul>
<p>The door release works the same way in all of them.</p>
""",
      [("Why does my buzzer ring but the door doesn't open?", "The intercom is working. The door strike or its power has failed. See [[intercom-repair/door-release/|door release repair]]."),
       ("Where is the amplifier?", "Usually in the basement near the electric meters, or in a closet near the entrance.")])

guide("intercom-wiring-explained", "Intercom wiring",
      "Intercom Wiring Explained: 2, 3, 4 and 5 Wire Systems | Jacob Intercom",
      "How apartment intercom wiring works: 2-wire, 3-wire, 4-wire and 5-wire systems, common and selective wires, and why the wire count matters.",
      "Intercom wiring explained",
      "The number of wires to each apartment decides which parts fit, which faults are possible, and what you can upgrade to without opening walls.",
      """
<h2>Multi-wire systems: 3, 4 and 5 wires</h2>
<p>Most older New York apartment intercoms use several <strong>common wires</strong>, shared by every apartment, and one <strong>selective wire</strong> per apartment that carries its call.</p>
<div class="tablebox"><table>
<thead><tr><th scope="col">System</th><th scope="col">Common</th><th scope="col">Selective</th><th scope="col">Example station</th></tr></thead>
<tbody>
<tr><th scope="row">3-wire</th><td>2</td><td>1</td><td>[[lee-dan-intercom-systems/ir-203/|Lee-Dan IR-203]]</td></tr>
<tr><th scope="row">4-wire</th><td>3</td><td>1</td><td>[[lee-dan-intercom-systems/ir-204/|Lee-Dan IR-204]]</td></tr>
<tr><th scope="row">5-wire</th><td>4</td><td>1</td><td>[[lee-dan-intercom-systems/ir-205/|Lee-Dan IR-205]]</td></tr>
</tbody></table></div>
<p>The riser cable carries the common wires plus one selective wire for every apartment on that line.</p>
<h2>Two-wire systems</h2>
<p>Newer systems put power, voice, video and calls on two wires. Each apartment unit has an address, so the system reaches it digitally instead of on its own wire. Comelit's Simplebus and Lee-Dan's [[lee-dan-intercom-systems/2easy/|2Easy]] are examples.</p>
<p>This is why older buildings can often get video without rewiring: they already have more than two wires to every apartment.</p>
<h2>Network cable</h2>
<p>IP intercoms use network cable, usually to the door panel at least, and often to each apartment monitor. Where an old riser can't carry network signals, a new cable is run alongside it.</p>
<h2>What wire count tells you about faults</h2>
<ul>
<li>One apartment affected: its selective wire or its station.</li>
<li>A whole line affected: a common wire in that riser.</li>
<li>Two apartments ring together: their selective wires are touching.</li>
</ul>
<h2>Testing old wire</h2>
<p>Before reusing wire we test every conductor for breaks, shorts and leakage between wires. Old cable can look fine and still be corroded inside a wall. See [[intercom-replacement/|replacement and upgrades]].</p>
""",
      [("How do I count the wires in my system?", "Take the apartment station off the wall and count the wires on its terminals, or read the model number."),
       ("Can I mix stations with different wire counts?", "No. Every station on a line must match the system's wire count.")])

guide("apartment-intercom-troubleshooting", "Troubleshooting by symptom",
      "Apartment Intercom Troubleshooting by Symptom | Jacob Intercom",
      "Apartment intercom not working? Match the symptom to the likely cause, see what you can check yourself, and when to call a technician.",
      "Apartment intercom troubleshooting",
      "Find what your intercom is doing in the table, then follow the link for the causes, the checks and the fix.",
      """
<h2>Start here</h2>
<p>Before anything else, find out how many apartments are affected. Ask a neighbour above or below you and one on another line.</p>
<div class="tablebox"><table>
<thead><tr><th scope="col">Symptom</th><th scope="col">Only you</th><th scope="col">Everyone</th></tr></thead>
<tbody>
<tr><th scope="row">No ring</th><td>Your station or call wire</td><td>Power supply or amplifier</td></tr>
<tr><th scope="row">Can't hear the visitor</th><td>Your station's speaker</td><td>Entry panel microphone or amplifier</td></tr>
<tr><th scope="row">Visitor can't hear you</th><td>Your station's microphone or Talk button</td><td>Entry panel speaker or amplifier</td></tr>
<tr><th scope="row">Door won't release</th><td>Your Door button</td><td>Strike, its power, or the release circuit</td></tr>
<tr><th scope="row">Blank video</th><td>Your monitor</td><td>Panel camera or video power</td></tr>
<tr><th scope="row">Static or hum</th><td>Your station or its wiring</td><td>Power supply, amplifier or a shorted shared wire</td></tr>
</tbody></table></div>
<h2>Detailed guides</h2>
<ul>
<li>[[intercom-repair/door-buzzer/|Buzzer doesn't ring]]</li>
<li>[[intercom-repair/door-release/|Door won't unlock]]</li>
<li>[[intercom-repair/no-audio/|No sound, static or one-way audio]]</li>
<li>[[intercom-repair/video/|Video not working]]</li>
<li>[[intercom-repair/entry-panel/|Damaged entry panel]]</li>
<li>[[intercom-repair/not-working/|Nothing works at all]]</li>
<li>[[lee-dan-intercom-systems/troubleshooting/|Lee-Dan systems]]</li>
</ul>
<h2>Safe checks for anyone</h2>
<ul>
<li>Turn up the volume on your station if it has a control.</li>
<li>Make sure the handset is properly on its hook.</li>
<li>Have the super check for a tripped breaker.</li>
<li>Photograph the panel, your station and the amplifier.</li>
</ul>
<h2>Leave to a technician</h2>
<p>Opening the entry panel, the amplifier or the transformer, and swapping wires between terminals.</p>
""")

guide("renters-broken-buzzer", "Renter's guide",
      "Apartment Buzzer Not Working? A Renter's Guide for NYC | Jacob Intercom",
      "Your apartment buzzer or intercom stopped working. What to check, how to report it, what the landlord must do in New York, and how to get by meanwhile.",
      "Your buzzer is broken: a renter's guide",
      "Deliveries are leaving, guests are calling from the sidewalk, and the super says it's on the list. Here's what to do.",
      """
<h2>1. Check it's not something simple</h2>
<ul>
<li>Look for a volume wheel or switch on your station and turn it up.</li>
<li>Check the handset is sitting properly on its hook.</li>
<li>Ask a neighbour whether theirs works. If it's the whole building, tell the super; it's probably the main power or amplifier.</li>
</ul>
<h2>2. Report it in writing</h2>
<p>Text or email your landlord or managing agent, and keep a copy. Say what doesn't work (ring, voice, door, video), since when, and whether neighbours are affected. A written report is your record if it isn't fixed.</p>
<h2>3. Know what the landlord has to do</h2>
<p>In many New York buildings, the owner is legally required to keep the intercom and self-locking front door working. See [[guides/nyc-landlord-intercom-requirements/|NYC intercom law]].</p>
<h2>4. If it isn't fixed</h2>
<p>You can report it to the city through 311, which passes housing complaints to the Department of Housing Preservation and Development. Keep your written report and dates.</p>
<h2>5. Getting by meanwhile</h2>
<ul>
<li>Add your phone number to delivery instructions and ask couriers to call.</li>
<li>Have packages held at a pickup point or locker.</li>
<li>Don't prop the front door open. It makes the building less safe for everyone.</li>
</ul>
<h2>Should I fix it myself?</h2>
<p>The intercom is part of the building, and the owner is responsible for it. Replacing a station yourself can also affect neighbours if it's wired wrongly. Report it instead.</p>
<p class="soon">Landlords, supers and managing agents can call us directly at {{tel}}.</p>
""",
      [("Can I withhold rent over a broken intercom?", "That is a legal question with real risks. Speak to a tenant lawyer or a tenant organisation first."),
       ("Can I hire someone to fix it and deduct the cost?", "Ask a lawyer before doing this. Most renters are better off reporting it and keeping records.")],
      facts=["For <b>renters</b>", "What to check and how to report it", "What the law says"])

guide("best-intercom-systems-nyc-buildings", "Choosing a system",
      "Choosing an Intercom for a NYC Apartment Building (2026) | Jacob Intercom",
      "How to choose an intercom for a New York apartment building: audio, two-wire video, phone-based and IP systems compared on cost, reliability and fees.",
      "Choosing an intercom for a NYC building",
      "There isn't one best intercom. There's a best fit for your building's wiring, residents and budget. Here's how we help buildings choose.",
      """
<h2>The main choices</h2>
<div class="tablebox"><table>
<thead><tr><th scope="col">Type</th><th scope="col">Upfront</th><th scope="col">Monthly fee</th><th scope="col">Needs internet</th><th scope="col">Best for</th></tr></thead>
<tbody>
<tr><th scope="row">Audio</th><td>Lowest</td><td>None</td><td>No</td><td>Small buildings that want simple</td></tr>
<tr><th scope="row">Two-wire video</th><td>Moderate</td><td>None</td><td>No</td><td>Older buildings adding video on existing wire</td></tr>
<tr><th scope="row">Phone-based / cloud</th><td>Moderate to high</td><td>Usually</td><td>Yes</td><td>Buildings with many deliveries and remote residents</td></tr>
<tr><th scope="row">IP with monitors</th><td>Highest</td><td>Sometimes</td><td>Yes, on the building network</td><td>New construction and large buildings</td></tr>
</tbody></table></div>
<h2>Questions to answer first</h2>
<ol>
<li><strong>What wiring do you have?</strong> We test it. It decides what is affordable.</li>
<li><strong>How do residents want to answer?</strong> A wall unit, a phone, or both.</li>
<li><strong>How many deliveries?</strong> Lots of packages favour delivery codes and phone answering.</li>
<li><strong>Who will manage it?</strong> Cloud systems need someone to add and remove residents.</li>
<li><strong>What can you spend each year,</strong> not just upfront?</li>
</ol>
<h2>Systems we install most</h2>
<ul>
<li>[[lee-dan-intercom-systems/2easy/|Lee-Dan 2Easy]] and [[brands/comelit/|Comelit]] two-wire video for older buildings.</li>
<li>[[brands/aiphone/|Aiphone]] wired and network systems for most building sizes.</li>
<li>[[brands/butterflymx/|ButterflyMX]] and [[brands/akuvox/|Akuvox]] for phone answering and keyless entry.</li>
</ul>
<p>[JACOB: WHICH HE RECOMMENDS FOR WHICH BUILDING, AND WHY]</p>
<h2>Our advice</h2>
<p>Don't pay for features residents won't use, and compare the ten-year cost, not just the installation. If the existing wire is good, a wired system on it is usually the best value.</p>
""")

guide("wired-vs-wireless-intercom", "Wired or wireless",
      "Wired vs Wireless Intercom for Apartment Buildings | Jacob Intercom",
      "Wired or wireless intercom for a New York building? Reliability, cost, monthly fees and when each makes sense.",
      "Wired or wireless intercom?",
      "Wireless sounds simpler. Often it is. But in a building that already has wire in the walls, wired usually wins on cost and reliability.",
      """
<h2>Side by side</h2>
<div class="tablebox"><table>
<thead><tr><th scope="col"></th><th scope="col">Wired</th><th scope="col">Wireless</th></tr></thead>
<tbody>
<tr><th scope="row">Depends on internet or cell signal</th><td>No</td><td>Yes</td></tr>
<tr><th scope="row">Monthly fee</th><td>Usually none</td><td>Usually</td></tr>
<tr><th scope="row">Installation in a building with good wiring</th><td>Lower cost</td><td>Similar or higher</td></tr>
<tr><th scope="row">Installation where wiring has failed</th><td>Higher cost, walls may be opened</td><td>Lower cost</td></tr>
<tr><th scope="row">Answer from anywhere</th><td>Only with a network-capable system</td><td>Yes</td></tr>
</tbody></table></div>
<h2>Choose wired when</h2>
<ul><li>The existing wire tests well.</li><li>The building wants no monthly fees.</li><li>Reliability matters more than answering away from home.</li></ul>
<h2>Choose wireless when</h2>
<ul><li>The wiring has failed throughout and walls can't be opened.</li><li>The building never had an intercom.</li><li>Residents mostly want to answer on their phones.</li></ul>
<h2>Mixing both</h2>
<p>A wired system for most apartments with wireless for the few whose lines have failed is often the cheapest fix of all. See [[intercom-installation/wireless/|wireless intercoms]].</p>
""")

guide("upgrade-buzzer-to-video", "Upgrading to video",
      "Upgrading an Old Buzzer System to Video | Jacob Intercom",
      "How to upgrade an old apartment buzzer or audio intercom to video, often on the existing wiring. The options, the steps and the costs.",
      "Upgrading a buzzer system to video",
      "Most buildings with an old audio intercom can get video without opening walls. Here's how it's done.",
      """
<h2>Why it's usually possible</h2>
<p>Older audio systems run three to five wires to each apartment. Two-wire video systems need two. If the old wire is sound, the new system uses it.</p>
<h2>The steps</h2>
<ol>
<li><strong>Test the wire</strong> to every apartment for breaks, shorts and leakage.</li>
<li><strong>Choose the system:</strong> two-wire video with wall monitors, or a phone-based panel.</li>
<li><strong>Fit the new entry panel,</strong> covering the old opening where possible.</li>
<li><strong>Replace each apartment station</strong> with a monitor, usually a short visit per apartment.</li>
<li><strong>Connect the power supply and door release,</strong> and test every apartment.</li>
<li><strong>Show residents</strong> how it works.</li>
</ol>
<h2>What if some lines fail the test?</h2>
<p>Those apartments get new cable, or a wireless link, while the rest use the old wire.</p>
<h2>Options</h2>
<ul>
<li>[[lee-dan-intercom-systems/2easy/|Lee-Dan 2Easy]]: two-wire colour video kits.</li>
<li>[[brands/comelit/|Comelit]] Simplebus: two-wire video for larger buildings.</li>
<li>[[brands/butterflymx/|ButterflyMX]] or [[brands/akuvox/|Akuvox]]: phone answering, no apartment wiring needed.</li>
</ul>
<h2>What it costs</h2>
<p>[VIDEO UPGRADE RANGE BY BUILDING SIZE]. See [[guides/intercom-installation-cost-nyc/|installation costs]].</p>
<p>[JACOB: AN UPGRADE JOB TO FEATURE]</p>
""")

guide("co-op-intercom-replacement", "Co-op replacement",
      "Intercom Replacement for NYC Co-op Boards: A Step-by-Step Guide | Jacob Intercom",
      "A step-by-step guide for New York co-op and condo boards replacing an intercom: inspection, options, board approval, resident notice and changeover.",
      "Intercom replacement for co-op boards",
      "A guide for boards and managing agents taking an intercom replacement from first complaint to finished job.",
      """
<h2>1. Get an inspection and a report</h2>
<p>Ask for the existing wiring to be tested and a written report: what works, what has failed, and what can be reused. Without it, every quote is a guess.</p>
<h2>2. Get two or three options</h2>
<p>A sensible set: renew like for like, upgrade to video on existing wire, and a phone-based system. Each should state the upfront cost, the yearly cost, what residents will use, and what happens to the old equipment.</p>
<h2>3. Compare the ten-year cost</h2>
<p>Include subscriptions, expected repairs and replacement parts. A cheaper installation with a monthly fee can cost more over time.</p>
<h2>4. Check the paperwork</h2>
<p>Licence, insurance certificate naming the corporation and managing agent, warranty terms, and a schedule.</p>
<h2>5. Tell shareholders</h2>
<p>Explain what is changing, when contractors need apartment access, and how residents will answer the door during the changeover.</p>
<h2>6. Plan the changeover</h2>
<p>The old system should work until the new one is ready. Schedule apartment access by floor.</p>
<h2>7. Handover</h2>
<p>Every apartment tested, residents shown the system, a printed guide left in the lobby, and the managing agent given the system details and warranty.</p>
<p>See [[co-op-condo-intercom/|co-op and condo intercoms]] and [[property-managers/|property managers]].</p>
""")

# ───────────────────────────── FAQ, reviews, projects ─────────────────────────────

FAQS = [
    ("How much does intercom repair cost?", "Most single-fault repairs cost $100 to $300. See [[pricing/|pricing]]."),
    ("Do you give the price before starting?", "Yes, always."),
    ("Which areas do you cover?", "Brooklyn, Manhattan, Queens, the Bronx and Staten Island, plus Long Island, Westchester and New Jersey."),
    ("What are your hours?", "Monday to Thursday 9 to 5, Friday 8 to 4. After hours: [AFTER-HOURS LINE]."),
    ("Do you repair Lee-Dan intercoms?", "Yes. See [[lee-dan-intercom-systems/|Lee-Dan repair and service]]."),
    ("Which brands do you service?", "Fifteen, including Aiphone, ButterflyMX, Comelit and Akuvox. See [[brands/|brands]]."),
    ("Can you repair a system another company installed?", "Yes."),
    ("Can you fix just one apartment?", "Yes. It is usually the quickest repair."),
    ("Who is responsible for a building intercom?", "The building owner. Renters should report faults to the landlord or super. See [[guides/renters-broken-buzzer/|renter's guide]]."),
    ("Is an intercom required by law in NYC?", "In many buildings with eight or more apartments, yes. See [[guides/nyc-landlord-intercom-requirements/|NYC intercom law]]."),
    ("Can you add video without rewiring?", "Often. See [[guides/upgrade-buzzer-to-video/|upgrading to video]]."),
    ("Do you install phone-answering intercoms?", "Yes. See [[intercom-installation/ip-smartphone/|IP and smartphone intercoms]]."),
    ("Do you install key fob systems?", "Yes. See [[access-control/key-fob/|key fob systems]]."),
    ("Do you install security cameras?", "Yes. See [[security-cameras/|security cameras]]."),
    ("Can you send a certificate of insurance?", "Yes, before the first visit."),
    ("Do you offer maintenance contracts?", "See [[intercom-maintenance-contract/|maintenance contracts]]."),
    ("Is there a warranty?", "[WARRANTY TERMS]"),
    ("How do I pay?", "[PAYMENT METHODS]"),
    ("Can you tell what's wrong from a photo?", "A photo of the panel and a station usually tells us the make and narrows the fault."),
    ("How long have you been in business?", "35 years."),
]
page(path="faq/", nav="FAQ",
     title="Intercom Repair & Installation FAQ | Jacob Intercom",
     desc="Answers to the questions we're asked most about intercom repair, installation, costs, Lee-Dan systems and NYC intercom law.",
     h1="Frequently asked questions",
     lead="The questions we're asked most, answered briefly, with links to the full detail.",
     facts=["<b>20</b> common questions", "Costs, coverage, law", "Call {{tel}} for anything else"],
     body="<p>Can't find your question? Call {{tel}} or send a photo of your panel.</p>", faqs=FAQS,
     related=[("guides/", "Guides"), ("pricing/", "Pricing"), ("intercom-repair/", "Intercom repair"), ("contact/", "Contact us")])

REAL_REVIEWS = [
    "Highly recommend Jacob Intercom! Their team was professional, knowledgeable, and completed our project on time. We will definitely use them again for future security upgrades.",
    "Excellent service they arrived on time and explained every step of the installation, there technician completed the job exactly as promised. I highly recommend Jacob intercom for anyone looking to upgrade their intercom systems.",
    "I'm very happy with the they handle the problem, fast service very professional from the minet they pick up the phone till the job was completed very much recommended. Thank you for making it easy for me see you next time.",
    "Jacob Intercom helped us modernize our building with a wireless intercom. Residents appreciate the convenience, and we appreciate the increased security.",
    "Great service, quick response, very professional with reasonable prices. It took me a while to find a company that doesn't request a lot of information just to provide an estimate and an appointment. I would recommend to family and friends for sure. Marina is the person to go to!!! Great experience! Thank you!",
]
page(path="reviews/", nav="Reviews",
     title="Jacob Intercom Reviews: 4.7 Stars from 23 Google Reviews",
     desc="Read what customers say about Jacob Intercom: 4.7 stars from 23 Google reviews for intercom repair and installation in New York.",
     h1="Reviews", no_reviews=True,
     lead="4.7 stars from 23 reviews on Google. Here are some of them, as written.",
     facts=["<b>4.7 stars</b>", "<b>23</b> Google reviews", "Reviews shown as written"],
     body="<div class=\"note\"><p>Before launch this page should pull reviews live from Google so the count and rating stay current. [CONNECT GOOGLE BUSINESS PROFILE]</p></div><p><a href=\"https://maps.google.com/?cid=12939931405333589826\" rel=\"noopener\">Read all reviews on Google</a></p><h2>What customers say</h2>"
          + "".join(f"<blockquote class=\"note\" style=\"margin:0 0 16px\"><p>&ldquo;{r}&rdquo;</p><p class=\"soon\" style=\"margin-top:8px\">Google review</p></blockquote>" for r in REAL_REVIEWS)
          + "<h2>Leave a review</h2><p>If we've worked on your intercom, a Google review helps other buildings find us. <a href=\"https://search.google.com/local/writereview?placeid=ChIJF42LFM5EwokRQm_U8A3fk7M\" rel=\"noopener\">Leave a Google review</a></p>",
     related=[("intercom-repair/", "Intercom repair"), ("about/", "About us"), ("contact/", "Contact us")])

page(path="projects/", nav="Projects",
     title="Intercom Projects in New York | Jacob Intercom",
     desc="Intercom repairs, replacements and upgrades Jacob Intercom has carried out in New York buildings, with the problem, the fix and photos.",
     h1="Projects",
     lead="Real jobs, written up: the building, what was wrong, what we did, and what it cost.",
     facts=["Building, problem, fix", "Photos from the job", "Shared with the owner's permission"],
     body="""
<div class="note"><p><strong>Waiting on Jacob.</strong> No competitor publishes case studies, so this page is one of the strongest on the site once it has real jobs. Each needs: building type and neighbourhood, the problem, what was done, the system, roughly what it cost, two or three photos, and permission to publish.</p></div>
<h2>How each project will read</h2>
<p class="sample">Sample layout</p>
<h3>[BUILDING TYPE], [NEIGHBORHOOD]</h3>
<p><strong>The problem:</strong> [WHAT RESIDENTS REPORTED]</p>
<p><strong>What we found:</strong> [THE FAULT]</p>
<p><strong>What we did:</strong> [THE REPAIR OR INSTALLATION]</p>
<p><strong>System:</strong> [MAKE AND MODEL]</p>
<div class="slot">Real photos from the job</div>
<h2>Jobs to come</h2>
<ul><li>A Lee-Dan system repaired instead of replaced</li><li>A buzzer system upgraded to video on existing wire</li><li>A co-op entrance with a new panel and fobs</li><li>A brownstone with a new strike on an original door</li></ul>
""",
     related=[("reviews/", "Reviews"), ("intercom-repair/", "Intercom repair"), (INST, "Installation"), ("contact/", "Contact us")])

# ───────────────────────────── Home intercoms and wider areas ─────────────────────────────

page(path="home-intercom/", nav="Home intercoms",
     title="Home Intercom Repair & Installation NYC and Long Island | Jacob Intercom",
     desc="Home intercom repair and installation: old whole-house intercoms repaired or replaced, and video door stations with phone apps for houses and townhouses.",
     h1="Home intercoms",
     lead="From a 1970s whole-house system in the kitchen to a video door station that rings your phone.",
     facts=["Whole-house intercoms <b>repaired</b>", "Video door stations installed", "Houses and townhouses"],
     aside=INST_ASIDE,
     body="""
<h2>Old whole-house intercoms</h2>
<p>Many houses have a master station in the kitchen and room stations throughout, often [[brands/nutone/|NuTone]] or [[brands/m-and-s/|M&amp;S]]. Most of these are no longer made. We repair them where parts allow, and replace them where they don't.</p>
<h2>Video door stations</h2>
<p>The most common upgrade: a camera door station at the front door, answered on a phone app or an indoor monitor, with the door or gate released remotely. [[brands/doorbird/|DoorBird]] and [[brands/aiphone/|Aiphone]] are typical choices.</p>
<h2>Reusing the old wiring</h2>
<p>The wire to the old front door speaker can often power a new door station. We test it before quoting.</p>
<h2>Two-family houses</h2>
<p>A house with two apartments needs a small two-button system. See [[brownstone-intercom/|two to four family intercoms]].</p>
<h2>What it costs</h2>
<p>[HOME INTERCOM REPAIR AND INSTALL RANGES]</p>
""",
     faqs=[("Can you remove an old intercom and patch the walls?", "We remove the stations and cover the openings with blank plates. Plastering and painting is a separate trade."),
           ("Does a video door station work with Ring or Nest?", "Some do. Tell us what you already use and we'll suggest a compatible option.")],
     related=[("brands/nutone/", "NuTone"), ("brands/doorbird/", "DoorBird"), ("brownstone-intercom/", "Two to four family"), ("contact/", "Contact us")])


def wider(slug, name, places, note):
    page(path=f"service-areas/{slug}/", nav=name,
         title=f"Intercom Repair & Installation {name} | Jacob Intercom",
         desc=f"Intercom repair and installation in {name}: apartment buildings, co-ops, houses and offices. 35 years of experience. Call 718-252-2730.",
         h1=f"Intercom repair and installation in {name}",
         lead=f"We take intercom jobs across {name}, from apartment buildings and co-ops to houses and offices.",
         facts=["<b>35 years</b> of intercom work", "Repair and installation", "Most repairs <b>$100 to $300</b>"],
         body=f"""
<h2>Where we work in {name}</h2>
<p>{places}</p>
{note}
<h2>What we do</h2>
<ul>
<li>[[intercom-repair/|Intercom repair]] for every major brand, including [[lee-dan-intercom-systems/|Lee-Dan]].</li>
<li>[[intercom-installation/|New systems]] and [[intercom-replacement/|replacements]].</li>
<li>[[home-intercom/|Home intercoms]] and video door stations.</li>
<li>[[access-control/|Access control]] and [[security-cameras/|cameras]].</li>
</ul>
<h2>Recent jobs in {name}</h2>
<p>[{name.upper()} JOBS WITH TOWN AND BUILDING TYPE]</p>
<h2>Scheduling</h2>
<p>Jobs outside the five boroughs are scheduled by appointment. [TRAVEL CHARGE, IF ANY]</p>
""",
         faqs=[(f"Do you charge extra to travel to {name}?", "[TRAVEL CHARGE, IF ANY]")],
         related=[("service-areas/", "All service areas"), ("intercom-repair/", "Intercom repair"), (INST, "Installation"), ("contact/", "Contact us")])


wider("long-island", "Long Island", "Nassau County and western Suffolk: [TOWNS JACOB HAS WORKED IN].",
      "<p>Long Island has many garden apartment complexes, co-ops and two-family houses, and a lot of Lee-Dan equipment, which is made on Long Island.</p>")
wider("westchester", "Westchester", "Yonkers, Mount Vernon, New Rochelle, White Plains and nearby: [TOWNS JACOB HAS WORKED IN].",
      "<p>Westchester's apartment buildings and co-ops are concentrated in the southern cities, with houses and townhouses elsewhere.</p>")
wider("new-jersey", "New Jersey", "Jersey City, Hoboken and nearby: [TOWNS JACOB HAS WORKED IN].",
      "<p>[CONFIRM ANY NEW JERSEY LICENSING NEEDED FOR THIS WORK]</p>")

page(path="service-areas/", nav="Service areas",
     title="Intercom Service Areas: NYC, Long Island, Westchester, NJ | Jacob Intercom",
     desc="Jacob Intercom covers all five New York City boroughs, plus Long Island, Westchester and New Jersey. Find your area.",
     h1="Where we work",
     lead="All five boroughs, and jobs further out on Long Island, in Westchester and in New Jersey.",
     facts=["<b>5 boroughs</b>", "Long Island, Westchester, New Jersey", "Based in Brooklyn"],
     body="""
<h2>New York City</h2>
<ul class="linklist">
<li>[[intercom-installation-brooklyn/|Brooklyn]]</li>
<li>[[intercom-installation-manhattan/|Manhattan]]</li>
<li>[[intercom-installation-queens/|Queens]]</li>
<li>[[intercom-installation-bronx/|The Bronx]]</li>
<li>[[intercom-installation-staten-island/|Staten Island]]</li>
</ul>
<h2>Beyond the city</h2>
<ul class="linklist">
<li>[[service-areas/long-island/|Long Island]]</li>
<li>[[service-areas/westchester/|Westchester]]</li>
<li>[[service-areas/new-jersey/|New Jersey]]</li>
</ul>
<h2>Our base</h2>
<p>209 Avenue F, Brooklyn, NY 11218. We reach south and central Brooklyn fastest.</p>
""",
     related=[("intercom-repair/", "Intercom repair"), (INST, "Installation"), ("contact/", "Contact us")])

# ───────────────────────────── Neighbourhoods ─────────────────────────────

HOODS = []


def hood(slug, name, bpath, bname, stock, systems, extra=""):
    HOODS.append((slug, name, bname))
    page(path=f"service-areas/{slug}/", nav=name,
         title=f"Intercom Repair {name}, {bname} | Jacob Intercom",
         desc=f"Intercom repair and installation in {name}, {bname}. Buzzers, door releases, video entry and Lee-Dan systems. Most repairs $100 to $300.",
         h1=f"Intercom repair in {name}",
         lead=f"Intercom repair, replacement and installation for buildings in {name}. Most repairs run $100 to $300, priced before we start.",
         facts=["<b>35 years</b> in New York", "Most repairs <b>$100 to $300</b>", "<b>4.7 stars</b> from 23 Google reviews"],
         body=f"""
<h2>{name}'s buildings</h2>
<p>{stock}</p>
<h2>The intercoms we see here</h2>
<p>{systems}</p>
{extra}
<h2>What we do in {name}</h2>
<ul>
<li>[[intercom-repair/|Intercom repair]]: [[intercom-repair/door-buzzer/|dead buzzers]], [[intercom-repair/door-release/|doors that won't unlock]], [[intercom-repair/no-audio/|static]], [[intercom-repair/video/|blank video]].</li>
<li>[[lee-dan-intercom-systems/|Lee-Dan]] and [[brands/|14 other brands]].</li>
<li>[[intercom-replacement/|Replacements and upgrades]] on existing wiring.</li>
<li>[[access-control/|Fobs]] and [[security-cameras/|cameras]] at the entrance.</li>
</ul>
<h2>A recent job in {name}</h2>
<p class="sample">Sample</p>
<p>[{name.upper()} JOB: BUILDING TYPE, PROBLEM, WHAT WE DID, PHOTO]</p>
<div class="slot">Real job photo from {name}</div>
<h2>Nearby</h2>
<p>We cover all of [[{bpath}|{bname}]]. See [[service-areas/|all service areas]].</p>
""",
         faqs=[(f"How quickly can you get to {name}?", "Call {{tel}} for the next opening. A door that won't lock goes to the front of the schedule."),
               (f"Do you charge extra to come to {name}?", "[TRAVEL CHARGE BY AREA, IF ANY]")],
         related=[(bpath, bname), ("intercom-repair/", "Intercom repair"), ("lee-dan-intercom-systems/", "Lee-Dan systems"), ("contact/", "Contact us")])


BK, MN, QN, BX = "intercom-installation-brooklyn/", "intercom-installation-manhattan/", "intercom-installation-queens/", "intercom-installation-bronx/"

hood("kensington-flatbush", "Kensington and Flatbush", BK, "Brooklyn",
     "Our office is on Avenue F in Kensington, so this is home ground. The area is lined with six-storey pre-war elevator buildings along Ocean Parkway and Coney Island Avenue, Victorian detached houses in Ditmas Park and Prospect Park South, and walk-ups and mid-century apartment houses through Flatbush.",
     "Older Lee-Dan and TekTone audio systems in the walk-ups, two-wire video in buildings that have upgraded, and multi-entrance systems in the larger courtyard buildings. Victorian houses often have a single door station or an old whole-house intercom.",
     "<p>Our Google listing ranks first for intercom repair around our office, and we are usually closest to these jobs.</p>")
hood("park-slope", "Park Slope", BK, "Brooklyn",
     "Brownstone and limestone rowhouses fill the side streets, most divided into two to four apartments, with pre-war apartment buildings on Prospect Park West and the avenues.",
     "Small button panels with two to four apartments, often with an outer stoop door and an inner vestibule door. Owners frequently want video on the existing wire and a panel that suits a landmarked facade. See [[brownstone-intercom/|brownstone intercoms]].")
hood("bay-ridge", "Bay Ridge", BK, "Brooklyn",
     "Pre-war co-ops and elevator buildings line Shore Road and the avenues, with two-family brick houses and limestone rowhouses on the side streets.",
     "Co-op buildings with long riser runs and older audio systems ready for an upgrade, and two-family houses with small two-button systems.")
hood("borough-park", "Borough Park", BK, "Brooklyn",
     "Two and three-family houses, many rebuilt or extended, alongside apartment buildings on the main avenues and new multi-family construction.",
     "Small multi-family systems on the houses, video panels on newer buildings, and frequent requests for door stations that ring several apartments at once.")
hood("sheepshead-bay", "Sheepshead Bay", BK, "Brooklyn",
     "Garden apartment complexes, six-storey co-ops near the bay, and attached and semi-detached houses, with many buildings near the water.",
     "Entry panels exposed to salt air that corrode faster than inland, multi-entrance garden complexes, and older audio systems in the co-ops.")
hood("williamsburg", "Williamsburg", BK, "Brooklyn",
     "Converted warehouses and lofts, new glass towers near the waterfront, and older walk-ups and tenements further inland.",
     "Phone-based and IP systems in the new buildings, which depend on the building's network, and audio systems in the older walk-ups. See [[intercom-installation/ip-smartphone/|IP and smartphone intercoms]].")
hood("bed-stuy", "Bed-Stuy", BK, "Brooklyn",
     "One of the city's largest collections of brownstones and rowhouses, most two to four families, with walk-up apartment buildings and newer infill on the avenues.",
     "Two to four apartment systems on original doors, plenty of old audio stations, and owners adding video and phone answering to houses they've renovated.")
hood("bushwick", "Bushwick", BK, "Brooklyn",
     "Two and three-storey frame and brick rowhouses, walk-up tenements, and a lot of new and converted multi-family buildings.",
     "Small multi-family systems, a mix of very old and very new equipment, and new buildings with cloud-based panels.")
hood("brooklyn-heights", "Brooklyn Heights", BK, "Brooklyn",
     "A landmark district of nineteenth-century rowhouses and townhouses, with pre-war co-ops and a few large apartment buildings near the Promenade.",
     "High-end door stations on townhouses, co-ops weighing upgrades, and street-facing panels that need to suit a landmarked building. See [[co-op-condo-intercom/|co-op intercoms]].")
hood("upper-west-side", "Upper West Side", MN, "Manhattan",
     "Pre-war co-ops on West End Avenue, Riverside Drive and Central Park West, brownstones on the side streets, and walk-ups on the avenues.",
     "Large co-op systems with several entrances, older audio systems in walk-ups, and boards comparing video upgrades with phone-based systems.")
hood("upper-east-side", "Upper East Side", MN, "Manhattan",
     "Doorman buildings on the avenues, townhouses on the side streets from the Sixties to the Nineties, and walk-ups further east in Yorkville.",
     "Townhouse door stations, walk-up audio systems in Yorkville, and service-entrance intercoms in doorman buildings.")
hood("harlem", "Harlem", MN, "Manhattan",
     "Brownstones and rowhouses, many restored, pre-war apartment buildings, and large multi-family buildings, including affordable housing developments.",
     "Older audio systems in the pre-war buildings, two to four family systems on restored brownstones, and larger buildings needing systems that meet the city's intercom requirements. See [[guides/nyc-landlord-intercom-requirements/|NYC intercom law]].")
hood("midtown", "Midtown", MN, "Manhattan",
     "Offices, mixed-use buildings with apartments over stores, and residential towers, with walk-ups in Hell's Kitchen and Murray Hill.",
     "Telephone entry and IP systems in offices, multi-tenant directories in mixed-use buildings, and audio systems in the walk-ups. See [[commercial-intercom/|office intercoms]].")
hood("east-village-les", "East Village and Lower East Side", MN, "Manhattan",
     "Five and six-storey tenements make up most of the housing stock, with some newer buildings and converted lofts.",
     "Tenement walk-ups with long-serving audio systems, often Lee-Dan or TekTone, worn entry panels on busy streets, and a lot of door strike repairs on heavy old doors.")
hood("astoria", "Astoria", QN, "Queens",
     "Two-family brick houses and attached rowhouses on most blocks, with six-storey apartment buildings near Ditmars and the Astoria Boulevard corridor.",
     "Two-button systems on the houses, older audio systems in the apartment buildings, and owners adding video door stations.")
hood("long-island-city", "Long Island City", QN, "Queens",
     "New residential towers along the waterfront and in Court Square, alongside older rowhouses and converted industrial buildings.",
     "Network and phone-based systems in the towers, plus access control and cameras, and smaller systems in the older housing.")
hood("flushing", "Flushing", QN, "Queens",
     "Elevator apartment buildings and co-ops near Main Street, garden complexes, and one and two-family houses further out.",
     "Large co-op systems with directory panels, multi-entrance garden complexes, and home door stations.")
hood("forest-hills", "Forest Hills", QN, "Queens",
     "Six-storey pre-war apartment houses and co-ops along Queens Boulevard and its side streets, and the Tudor houses of Forest Hills Gardens.",
     "Pre-war co-ops with older audio systems and long risers, often good candidates for video on the existing wire, and private houses with door stations.")
hood("jackson-heights", "Jackson Heights", QN, "Queens",
     "A historic district of garden apartment co-ops built around private courtyards, with apartment buildings and attached houses around them.",
     "Courtyard co-ops with several entrances, each needing its own panel calling the same apartments, and street-facing panels in a historic district.")
hood("riverdale", "Riverdale", BX, "the Bronx",
     "High-rise co-ops and apartment buildings along the Henry Hudson Parkway, with large private houses on the hills of Fieldston and Spuyten Duyvil.",
     "Large co-op systems with doormen and service entrances, and home intercoms and gate stations on private houses.")

# Link the neighbourhood pages from the service areas hub
for p in PAGES:
    if p["path"] == "service-areas/":
        groups = {}
        for slug, name, bname in HOODS:
            groups.setdefault(bname, []).append(f"<li>[[service-areas/{slug}/|{name}]]</li>")
        p["body"] += "<h2>Neighborhoods</h2>" + "".join(
            f"<h3>{b[0].upper() + b[1:]}</h3><ul class=\"linklist grid2\">{''.join(items)}</ul>" for b, items in groups.items())

# ───────────────────────────── Visual layer for guides ─────────────────────────────

FLOW_HOW = """
<figure class="diagram" aria-labelledby="flow-how-cap">
<ol class="flow">
<li class="node"><b>Entry panel</b><span>Visitor presses your button</span></li>
<li class="arrow" aria-hidden="true">your call wire</li>
<li class="node"><b>Amplifier</b><span>Usually in the basement. Sends the ring tone.</span></li>
<li class="arrow" aria-hidden="true">shared voice wires</li>
<li class="node"><b>Your station</b><span>You talk, listen, then press Door</span></li>
<li class="arrow" aria-hidden="true">release signal</li>
<li class="node node-brass"><b>Door strike</b><span>Unlocks for a few seconds</span></li>
</ol>
<figcaption id="flow-how-cap">What happens between a visitor pressing your button and the door opening.</figcaption>
</figure>
"""

WIRING_SVG = """
<figure class="diagram" aria-labelledby="wire-cap">
<p class="scroll-hint">Swipe sideways to see the whole diagram.</p>
<div class="scrollbox">
<svg viewBox="0 0 680 330" role="img" aria-labelledby="wire-title" class="svgd">
<title id="wire-title">A four-wire intercom: three common wires reach every apartment, and each apartment has one selective wire of its own from the lobby panel.</title>
<rect x="20" y="100" width="130" height="130" rx="8" class="box"/>
<text x="85" y="128" class="t-b" text-anchor="middle">Lobby panel</text>
<circle cx="55" cy="160" r="9" class="btn"/><text x="72" y="165" class="t-s">1A</text>
<circle cx="55" cy="185" r="9" class="btn"/><text x="72" y="190" class="t-s">2A</text>
<circle cx="55" cy="210" r="9" class="btn"/><text x="72" y="215" class="t-s">3A</text>
<rect x="20" y="262" width="130" height="50" rx="8" class="box"/>
<text x="85" y="292" class="t-b" text-anchor="middle">Amplifier</text>
<rect x="500" y="30" width="160" height="56" rx="8" class="box"/><text x="580" y="64" class="t-b" text-anchor="middle">Apartment 3A</text>
<rect x="500" y="130" width="160" height="56" rx="8" class="box"/><text x="580" y="164" class="t-b" text-anchor="middle">Apartment 2A</text>
<rect x="500" y="230" width="160" height="56" rx="8" class="box"/><text x="580" y="264" class="t-b" text-anchor="middle">Apartment 1A</text>
<path d="M64 210 H300 V258 H500" class="sel"/>
<path d="M64 185 H280 V158 H500" class="sel"/>
<path d="M64 160 H260 V58 H500" class="sel"/>
<path d="M150 280 H420 V48 H500 M420 148 H500 M420 248 H500" class="com"/>
<path d="M150 288 H430 V60 H500 M430 160 H500 M430 260 H500" class="com"/>
<path d="M150 296 H440 V72 H500 M440 172 H500 M440 272 H500" class="com"/>
</svg>
</div>
<div class="legend"><span><i class="k-com"></i>Common wires: shared by every apartment (voice and door release)</span><span><i class="k-sel"></i>Selective wire: one per apartment (its call)</span></div>
<figcaption id="wire-cap">A four-wire system. A three-wire system has two common wires, a five-wire system four. Every apartment still has exactly one selective wire.</figcaption>
</figure>
"""

DECIDE = """
<figure class="diagram" aria-labelledby="decide-cap">
<div class="decide">
<div class="q"><b>1. Is one part failing, and the rest of the system reliable?</b>
<div class="ans"><span class="yes">Yes</span> go to question 2 <span class="no">No</span> go to question 3</div></div>
<div class="q"><b>2. Are parts still made for it?</b>
<div class="ans"><span class="yes">Yes</span> <strong class="out out-repair">Repair it</strong> <span class="no">No</span> <strong class="out out-upgrade">Replace, reusing the wire</strong></div></div>
<div class="q"><b>3. Has it needed three or more repairs in the last year?</b>
<div class="ans"><span class="yes">Yes</span> <strong class="out out-upgrade">Plan a replacement</strong> <span class="no">No</span> <strong class="out out-repair">Repair, and keep a record</strong></div></div>
<div class="q"><b>Either way: does the building want video or phone answering?</b>
<div class="ans"><span class="yes">Yes</span> <strong class="out out-upgrade">Upgrade on the existing wire</strong></div></div>
</div>
<figcaption id="decide-cap">Three questions that settle most repair-or-replace decisions.</figcaption>
</figure>
"""

REPAIR_CALC = """
<div class="calc" data-calc="repair">
<h2>Repair cost estimator</h2>
<label for="rc-problem">What is the intercom doing?
<select id="rc-problem">
<option value="station">One apartment's buzzer doesn't ring</option>
<option value="strike">It buzzes but the door won't open</option>
<option value="audio">No sound, static or one-way audio</option>
<option value="video">The video screen is blank</option>
<option value="panel">The entry panel is damaged</option>
<option value="amp">Nothing works for anyone</option>
<option value="wiring">A whole line of apartments is dead</option>
</select></label>
<div class="calc-out" aria-live="polite"><p class="calc-range" data-out="range"></p><p data-out="note"></p></div>
<p class="calc-fine">Typical prices for common repairs, for planning. You get the actual price before any work starts.</p>
</div>
"""

INSTALL_CALC = """
<div class="calc" data-calc="install">
<h2>Installation cost estimator</h2>
<div class="calc-row">
<label for="ic-size">Building size
<select id="ic-size"><option value="s">House or 2 to 4 apartments</option><option value="m">5 to 12 apartments</option><option value="l">13 to 30 apartments</option><option value="xl">Over 30 apartments</option></select></label>
<label for="ic-type">System
<select id="ic-type"><option value="audio">Audio</option><option value="video">Wired video</option><option value="phone">Phone-based video</option></select></label>
</div>
<div class="calc-out" aria-live="polite"><p class="calc-range" data-out="range"></p><p data-out="note"></p></div>
<p class="calc-fine">Assumes the existing wiring can be reused. A firm quote follows a site visit.</p>
</div>
"""

GUIDE_SHOT = {
    "intercom-repair-cost-nyc": 23, "intercom-installation-cost-nyc": 5, "repair-or-replace-intercom": 20,
    "nyc-landlord-intercom-requirements": 10, "how-apartment-intercoms-work": 2, "intercom-wiring-explained": 4,
    "apartment-intercom-troubleshooting": 6, "renters-broken-buzzer": 21, "best-intercom-systems-nyc-buildings": 3,
    "wired-vs-wireless-intercom": 7, "upgrade-buzzer-to-video": 24, "co-op-intercom-replacement": 22,
}
GUIDE_GROUPS = [
    ("For renters and residents", [
        ("renters-broken-buzzer", "What to check, how to report it, and what the law says your landlord must do."),
        ("apartment-intercom-troubleshooting", "Match what your intercom is doing to the part that has failed."),
        ("how-apartment-intercoms-work", "The four parts of every intercom, and what happens when a visitor calls."),
        ("nyc-landlord-intercom-requirements", "What Multiple Dwelling Law 50-a requires, in plain English."),
    ]),
    ("For owners, supers and managers", [
        ("intercom-repair-cost-nyc", "Typical repair prices, what pushes them up, and an estimator."),
        ("repair-or-replace-intercom", "Three questions that settle most decisions, and what to ask a contractor."),
        ("intercom-wiring-explained", "Common and selective wires, and why the wire count matters."),
        ("wired-vs-wireless-intercom", "When each makes sense, and when to mix them."),
    ]),
    ("Planning a new system", [
        ("intercom-installation-cost-nyc", "What sets the price, typical ranges, and the monthly fees to compare."),
        ("best-intercom-systems-nyc-buildings", "Audio, two-wire video, phone-based and IP systems compared."),
        ("upgrade-buzzer-to-video", "How most buildings get video without opening walls."),
        ("co-op-intercom-replacement", "A step-by-step plan for boards and managing agents."),
    ]),
]

_titles = dict(GUIDES)
_hub = ['<p>Written by intercom technicians with 35 years of New York jobs. Pick the one that matches your situation.</p>']
for head, items in GUIDE_GROUPS:
    cards = "".join(
        f'<a class="card" href="{{{{u:{G}{slug}/}}}}">{{{{img:{GUIDE_SHOT[slug]}}}}}<span class="card-t">{_titles[slug]}</span><span class="card-d">{summary}</span></a>'
        for slug, summary in items)
    _hub.append(f'<h2>{head}</h2><div class="cards">{cards}</div>')
_hub.append('<h2>Lee-Dan guides</h2><ul class="linklist"><li>[[lee-dan-intercom-systems/wiring/|Lee-Dan wiring guide]]</li><li>[[lee-dan-intercom-systems/troubleshooting/|Lee-Dan troubleshooting guide]]</li></ul>')

for p in PAGES:
    path = p["path"]
    if path == G:
        p["body"] = "".join(_hub)
        p["wide"] = True
    elif path.startswith(G):
        slug = path[len(G):].strip("/")
        p["shot"] = GUIDE_SHOT.get(slug)
        if slug == "how-apartment-intercoms-work":
            p["body"] = p["body"].replace("<h2>Shared wires and private wires</h2>", FLOW_HOW + "<h2>Shared wires and private wires</h2>")
        elif slug == "intercom-wiring-explained":
            p["body"] = p["body"].replace("<h2>Two-wire systems</h2>", WIRING_SVG + "<h2>Two-wire systems</h2>")
        elif slug == "repair-or-replace-intercom":
            p["body"] = DECIDE + p["body"]
        elif slug == "intercom-repair-cost-nyc":
            p["body"] = p["body"].replace("<h2>What pushes the price up</h2>", REPAIR_CALC + "<h2>What pushes the price up</h2>")
        elif slug == "intercom-installation-cost-nyc":
            p["body"] = p["body"].replace("<h2>Ongoing costs to compare</h2>", INSTALL_CALC + "<h2>Ongoing costs to compare</h2>")
    elif path == "lee-dan-intercom-systems/wiring/":
        p["body"] = p["body"].replace("<p>[WIRING DIAGRAMS TO BE DRAWN FOR THE SITE AND CHECKED BY JACOB]</p>", WIRING_SVG)
    elif path == "pricing/":
        p["body"] = p["body"].replace("<h2>Installations</h2>", REPAIR_CALC.replace('id="rc-problem"', 'id="rc-problem-p"').replace('for="rc-problem"', 'for="rc-problem-p"') + "<h2>Installations</h2>")


page(path="privacy/", nav="Privacy",
     title="Privacy Policy | Jacob Intercom",
     desc="How Jacob Intercom uses the information you send through this website.",
     h1="Privacy policy", no_reviews=True,
     lead="What we collect when you contact us through this website, and what we do with it.",
     facts=["Used only to <b>answer you</b>", "Never sold", "Delete on request"],
     body="""
<div class="note"><p>A plain starting point, to be checked before launch, especially once the lead form and any analytics are connected. [REVIEW BEFORE LAUNCH]</p></div>
<h2>What we collect</h2>
<p>When you use the contact form we receive your name, phone number, the problem you describe, and any photo you attach. When you call, text or email us, we receive your number or address and what you send.</p>
<h2>How we use it</h2>
<p>Only to answer your request, quote, schedule and carry out the work, and keep a record of the job.</p>
<h2>Who we share it with</h2>
<p>We don't sell or rent your information. We share it only with services that help us run the business, such as our email and scheduling tools, and where the law requires it.</p>
<h2>Website analytics</h2>
<p>[ANALYTICS TOOLS USED AT LAUNCH, E.G. GOOGLE ANALYTICS, AND WHAT THEY COLLECT]</p>
<h2>Your choices</h2>
<p>To see, correct or delete the information we hold about you, email <a href="mailto:jacobintercom@gmail.com">jacobintercom@gmail.com</a> or call {{tel}}.</p>
<p>Last updated: [DATE OF LAUNCH]</p>
""",
     related=[("contact/", "Contact us"), ("about/", "About us")])

page(path="404/", nav="Page not found", noindex=True, no_reviews=True,
     title="Page Not Found | Jacob Intercom",
     desc="This page doesn't exist. Find intercom repair, installation and Lee-Dan service from Jacob Intercom.",
     h1="We couldn't find that page",
     lead="It may have moved when the site was rebuilt. Here are the pages people look for most.",
     facts=["Call {{tel}}"],
     body="""
<ul class="linklist">
<li>[[intercom-repair/|Intercom repair]]</li>
<li>[[intercom-installation/|Intercom installation]]</li>
<li>[[lee-dan-intercom-systems/|Lee-Dan systems]]</li>
<li>[[pricing/|Pricing]]</li>
<li>[[guides/|Guides]]</li>
<li>[[contact/|Contact us]]</li>
</ul>
""")
