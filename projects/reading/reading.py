import marimo

__generated_with = "0.18.1"
app = marimo.App(width="full")

@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
<style>
html, body {
  background-color: #0f1111 !important;
}
:root {
  --ink: #111;
  --muted: #666;
  --line: #e5e5e5;
  --surface: #fafafa;
  --accent:#5b4b8a;
}


.week4 {
  max-width: 920px;
  margin: auto;
  padding: 4rem 1.5rem 5rem;
  background: #fff;
  font-family: -apple-system, BlinkMacSystemFont, "Inter", "Segoe UI", system-ui, sans-serif;
  color: var(--ink);
}

.week4 header {
  margin-bottom: 3.5rem;
}

.week4 .label {
  font-size: 0.8rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 0.6rem;
}

.week4 h1 {
  font-size: 2.8rem;
  line-height: 1.1;
  margin: 0;
}

.week4 .subtitle {
  margin-top: 0.8rem;
  font-size: 1.1rem;
  color: var(--muted);
  max-width: 620px;
}

.week4 section {
  margin-bottom: 2.4rem;
}

.week4 p {
  font-size: 1.05rem;
  line-height: 1.75;
  margin-bottom: 1.4rem;
}

.week4 .divider {
  margin: 3.5rem 0;
  border-top: 1px solid var(--line);
}

.pull {
  margin: 3rem 0;
  padding: 2rem 2.2rem;
  background: var(--surface);
  border-left: 5px solid var(--accent);
  font-size: 1.15rem;
  line-height: 1.6;
}

.meta {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  margin: 3rem 0;
  padding-top: 1.5rem;
  border-top: 1px solid var(--line);
}

.meta div {
  font-size: 0.95rem;
  color: var(--muted);
}

@media (max-width: 720px) {
  .week4 h1 {
    font-size: 2.2rem;
  }
  .meta {
    grid-template-columns: 1fr;
  }
}
</style>

<div class="week4">

<header>
  <div class="label">Week 4 · Reading Reflection</div>
  <h1>Taking Responsibility</h1>
  <p class="subtitle">
    How responsibility shifts, dissolves, and reappears inside the computer-based network.
  </p>
</header>

<section>
<p>
The “Taking Responsibility” reading presents the computer-based network as an active force rather than a neutral tool. It reorganises how political authority, economic value, and personal agency function, producing realities that no longer align with frameworks built for physical space, monetary exchange, and slow institutional change.
</p>

<p>
A recurring theme is the displacement of responsibility. Large technology platforms frequently describe themselves as passive intermediaries responding to user demand and legal constraints. However, the reading demonstrates that these systems actively shape behaviour through design choices, algorithms, and interface logic. Responsibility is not removed from the system, but redirected away from those with the greatest structural influence.
</p>
</section>

<div class="pull">
Responsibility does not disappear in digital systems — it becomes embedded in architecture.
</div>

<section>
<p>
This dynamic becomes especially visible in the discussion of taxation and digital “nexus.” Traditional taxation relies on physical presence and financial transactions. Yet much of the contemporary information economy operates through exchanges of data, attention, and behavioural insight rather than money. Enormous value is generated while remaining invisible to institutions designed to track monetary flows.
</p>

<p>
The reading frames this not as regulatory failure, but as conceptual lag. Political tools such as taxation, sovereignty, and accountability are themselves technologies, designed for an earlier operating environment. When value is extracted without physical presence or direct payment, responsibility becomes difficult to assign using outdated measurement systems.
</p>
</section>

<section>
<p>
Crucially, the text resists blaming individuals. The issue is not ignorance but complexity. Systems driven by algorithms and machine learning evolve faster than public understanding can realistically keep pace. When responsibility is shifted onto users or voters who cannot fully comprehend how these systems function, accountability becomes symbolic rather than practical.
</p>

<p>
What emerges is a call to treat responsibility as a design problem. Writing code, building platforms, and structuring data flows are political acts, whether acknowledged or not. If institutions are not redesigned alongside technical systems, power will default to those best positioned to navigate opacity.
</p>

<p>
The reading ultimately insists that responsibility cannot be deferred. The computer-based network is already producing new political and economic realities. The question is not whether responsibility exists, but where it has been built into the system — and where it has been strategically excluded.
</p>
</section>

<div class="meta">
  <div>
    <strong>Key themes</strong><br>
    Responsibility · Platforms · Nexus · Data · Governance
  </div>
  <div>
    <strong>Format</strong><br>
    Designed reading reflection · Portfolio entry
  </div>
</div>

</div>
"""
    )
    return


if __name__ == "__main__":
    app.run()
