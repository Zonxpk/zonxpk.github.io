from pathlib import Path

path = Path("index.html")
text = path.read_text(encoding="utf-8")

if 'href="break-even/index.html">Case study</a>' in text:
    print("When? card already present")
    raise SystemExit(0)

empeo = '<span class="period mono">empeo</span>'
anchor = text.find(empeo)
if anchor < 0:
    raise SystemExit("Lab project anchor not found")

article = text.rfind('<article class="proj">', 0, anchor)
if article < 0:
    raise SystemExit("Lab article anchor not found")

line_start = text.rfind("\n", 0, article) + 1
indent = text[line_start:article]
i = indent

card = f'''<article class="proj">
{i}  <div class="proj-meta reveal">
{i}    <span class="period mono" style="color: var(--c-cyan)">2026 · product experiment</span>
{i}    <h3>When? / กี่โมง?</h3>
{i}    <p class="story">
{i}      A parody Thai super app engineered as a real cross-platform product:
{i}      food, dating, merch, vouchers, and partner campaigns share one
{i}      deterministic tracking-and-failure engine.
{i}    </p>
{i}    <dl class="proj-dl">
{i}      <div><dt>Kind</dt><dd>Full-stack product experiment</dd></div>
{i}      <div><dt>Focus</dt><dd>Reusable domain engine · cross-platform UI</dd></div>
{i}      <div><dt>Stack</dt><dd>Expo · React Native · Supabase</dd></div>
{i}    </dl>
{i}    <div class="proj-keys">
{i}      <a class="key" href="break-even/index.html">Case study</a>
{i}      <a class="key" href="https://break-even-beta.vercel.app" target="_blank" rel="noopener">Live app</a>
{i}    </div>
{i}  </div>
{i}  <div class="proj-screens">
{i}    <figure class="screen screen--phone reveal">
{i}      <div class="screen-top">
{i}        <span class="mono">WHEN? · HOME</span><span class="plat">Expo</span><span class="led" aria-hidden="true"></span>
{i}      </div>
{i}      <div class="screen-body screen-body--frame">
{i}        <img src="break-even/home.png" alt="When? Thai super app home screen" style="display:block;width:100%;height:auto" />
{i}      </div>
{i}      <figcaption class="mono">parody super-app home · hand-drawn UI system</figcaption>
{i}    </figure>
{i}    <figure class="screen screen--phone reveal">
{i}      <div class="screen-top">
{i}        <span class="mono">WHEN? · DATING</span><span class="plat">Expo</span><span class="led" aria-hidden="true"></span>
{i}      </div>
{i}      <div class="screen-body screen-body--frame">
{i}        <img src="break-even/dating.png" alt="When? dating simulation screen" style="display:block;width:100%;height:auto" />
{i}      </div>
{i}      <figcaption class="mono">dating domain · same shared failure lifecycle</figcaption>
{i}    </figure>
{i}    <figure class="screen screen--phone reveal">
{i}      <div class="screen-top">
{i}        <span class="mono">WHEN? · MERCH</span><span class="plat">Expo</span><span class="led" aria-hidden="true"></span>
{i}      </div>
{i}      <div class="screen-body screen-body--frame">
{i}        <img src="break-even/merch.png" alt="When? timed merch pop-up screen" style="display:block;width:100%;height:auto" />
{i}      </div>
{i}      <figcaption class="mono">timed merch · voucher and redemption workflow</figcaption>
{i}    </figure>
{i}  </div>
{i}</article>

{i}'''

path.write_text(text[:article] + card + text[article:], encoding="utf-8")
print("Inserted When? Lab card")
