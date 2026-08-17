# Module 3 — Research: Anomaly/Fault Detection AND Recommendation

Before writing any code against the real log, understand *why* this field exists and where it's actually used. This module is research, not coding — no `pandas` yet.

## The task

Real products don't stop at "something's different." There are two halves to research, and both matter:

1. **Detection** — how the system decides something is actually a fault or anomaly in the first place (what pattern in the data triggers it, out of all the normal noise).
2. **Recommendation** — how that detection turns into something a customer actually sees and can act on, e.g. *"Your fridge is using more power than usual"* or *"You haven't been this inactive in 3 weeks."*

Research **both halves** — detection and recommendation — for three domains:

1. **Smart home** (the domain of this course's dataset)
2. **Energy efficiency**
3. **Health & safety**

For each domain, you're looking for the full pipeline: what pattern gets detected → how the system decides it's real and worth telling someone → what the actual recommendation to the customer looks like.

## How to research

- Search the web, read articles, look at real products (thermostats, wearables, energy monitors, industrial sensors) and how they describe both their detection methods and their alerts/insights/recommendations to users.
- **You can use Claude Code to help** — ask it to explain a term you don't understand, give you a concrete example, or point you toward real products. Good prompts to try:
  - "What techniques do smart home products use to detect a device is behaving abnormally?"
  - "Give me a real example of a smart home product that turns unusual sensor patterns into a recommendation for the homeowner."
  - "How do energy monitoring apps detect wasteful usage, and how do they decide when to tell a customer about it?"
  - "What patterns do wearables detect before recommending someone see a doctor?"
- **Ground rule: you will be quizzed on this module**, without your notes or Claude open. So take notes *in your own words* as you go — don't paste an answer you can't explain yourself. If you can't say it out loud without looking, you haven't actually learned it yet.

## Guiding questions

Work through these for each of the three domains. You don't need to answer every single one in writing — they're there to point your research somewhere useful.

### Smart home
- **Detection:** What kinds of things go wrong with smart devices (thermostats, plugs, sensors, switches)? What pattern in the data signals it — a value out of range, a device going silent, a change from its usual schedule?
- **Recommendation:** What real products turn that detection into a message the homeowner sees, and what does the message actually say / ask them to do?

### Energy efficiency
- **Detection:** What patterns (constant high draw, spikes at odd hours, gradual drift upward over months) usually point to a fault or wasted energy? What's the difference between a device that's *broken* and one that's just *inefficient* — does a detector need to know?
- **Recommendation:** What real products or utility programs turn a wasteful pattern into a recommendation (e.g. a savings estimate, a comparison to similar homes)? How do they get a customer to actually act on it?

### Health & safety
- **Detection:** Where is anomaly/fault detection used to catch health or safety problems (wearables, fall detection, industrial safety sensors, elderly monitoring)? What pattern triggers it — a sudden change, a gradual trend, or the absence of expected activity?
- **Recommendation:** What does the resulting recommendation or alert look like, and why might it be phrased more cautiously or urgently than a smart home or energy one? Why might catching it *quickly* matter more than catching it *accurately* here, or vice versa?

## Deliverable

Write up in this module's `answers.md`:

1. In your own words: what does "anomaly detection" mean, and how does it differ from "fault detection"? Then: how does a system get from "raw sensor data" to "a recommendation a customer reads"? Name the steps.
2. One real example per domain (3 total) — for each: the product, the pattern it *detects*, and the *recommendation* it gives the customer as a result.
3. Thoughts, questions, and what you actually did to research this (per the format in the main [README](../../README.md#instructions)).

Be ready to explain all of it without your notes.
