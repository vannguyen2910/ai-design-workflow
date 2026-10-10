/* THE ONE FILE STUDENTS EDIT FOR LINKS AND STATUS.
   Everything the hub links together comes from this list. Each item has a short ID:
   O = opportunity, H = hypothesis, D = design decision, P = principle check, T = test, M = metric.
   "page" is the file where the item is written out in full (the item there must have the same id).
   "links" lists the IDs it connects to. Use { id: "P8", rel: "strains" } when a decision pulls against a principle.
   The EXAMPLE data below is there so you can see the hub working. Replace all of it. */
window.HUB = {
  title: "[CASE NAME]  (EXAMPLE DATA: replace)",
  access: "pending",            // agreed | pending | not available   (from the Shape the brief lesson)
  pages: [
    { file: "index.html",         label: "Overview",                  group: "Start" },
    { file: "scope.html",         label: "Scope",                     group: "Discover" },
    { file: "evidence.html",      label: "Evidence",                  group: "Discover" },
    { file: "problem-brief.html", label: "Problem brief",             group: "Define" },
    { file: "develop.html",       label: "Options, flows, prototype", group: "Develop" },
    { file: "alignment.html",     label: "Alignment check",           group: "Develop" },
    { file: "findings.html",      label: "Findings",                  group: "Deliver" },
    { file: "handoff.html",       label: "Handoff and measurement",   group: "Deliver" },
    { file: "case-log.html",      label: "Case log",                  group: "Record" }
  ],
  gates: [                      // the single gate list: 4 gates, each with lettered checks (see 02-method.md Part 3)
    // A check's status: open | passed | failed. A gate's status is worked out from its checks.
    { stage: "Discover", name: "Question + evidence", checks: [
      { id: "1a", text: "The business question and outcome are agreed with the PO, or marked assumed with the agreement status recorded", status: "open" },
      { id: "1b", text: "Every insight traces to a raw source you can open", status: "passed" },
      { id: "1c", text: "Nothing was guessed: unknowns and counterexamples recorded; AI draft kept beside the verified version, with the error rate", status: "passed" } ] },
    { stage: "Define", name: "Evidence + agreement", checks: [
      { id: "2a", text: "Each opportunity cites the evidence behind it", status: "open" },
      { id: "2b", text: "The problem brief is co-signed by product and business, or its agreement status is recorded", status: "open" },
      { id: "2c", text: "Each hypothesis has a test and a metric (unconfirmed metrics marked assumed)", status: "open" },
      { id: "2d", text: "Principle checks are written as yes/no questions", status: "open" } ] },
    { stage: "Develop", name: "Alignment", checks: [
      { id: "3a", text: "At least three different directions explored; the choice and reasons recorded", status: "open" },
      { id: "3b", text: "Every decision traces to an evidenced opportunity and a hypothesis (no decision without a user need, no opportunity left unserved)", status: "open" },
      { id: "3c", text: "Every decision passes the principle checks, or the conflict is a recorded trade-off", status: "open" },
      { id: "3d", text: "The prototype uses the design system and the accessibility rules were checked", status: "open" } ] },
    { stage: "Deliver", name: "Real users + buildability", checks: [
      { id: "4a", text: "Real users tested the hypotheses; results set against the baseline", status: "open" },
      { id: "4b", text: "Findings trace to raw notes or recordings and are weighted by importance", status: "open" },
      { id: "4c", text: "A developer could build it without asking (handoff pack and decision log complete)", status: "open" },
      { id: "4d", text: "The measurement plan is handed to the PO", status: "open" } ] }
  ],
  items: [
    { id: "O1", type: "opportunity", title: "[EXAMPLE] New users cannot tell what to do first", page: "problem-brief.html", links: ["H1"] },
    { id: "O2", type: "opportunity", title: "[EXAMPLE] Users do not trust the price before signing up", page: "problem-brief.html", links: ["H2"] },
    { id: "H1", type: "hypothesis",  title: "[EXAMPLE] A guided first task raises setup completion", page: "problem-brief.html", links: ["O1", "T1", "M1"] },
    { id: "H2", type: "hypothesis",  title: "[EXAMPLE] Showing the price early raises sign-ups", page: "problem-brief.html", links: ["O2"] },
    { id: "M1", type: "metric",      title: "[EXAMPLE] At least 4 of 5 test participants finish setup without help (assumed target, not confirmed by the PO)", page: "problem-brief.html", links: [] },
    { id: "D1", type: "decision",    title: "[EXAMPLE] Replace the empty dashboard with a 3-step checklist", page: "develop.html", links: ["H1", "P1", "P6"] },
    { id: "D2", type: "decision",    title: "[EXAMPLE] Add a progress bar to the checklist", page: "develop.html", links: ["H1", "P1", { id: "P8", rel: "strains" }] },
    { id: "D3", type: "decision",    title: "[EXAMPLE] Add an animated mascot", page: "develop.html", links: [] },
    { id: "T1", type: "test",        title: "[EXAMPLE] 5-user task test: finish setup without help", page: "findings.html", links: ["H1", "M1"] },
    { id: "P1", type: "principle",   title: "Visibility of system status", page: "problem-brief.html", links: [] },
    { id: "P2", type: "principle",   title: "Match between system and the real world", page: "problem-brief.html", links: [] },
    { id: "P3", type: "principle",   title: "User control and freedom", page: "problem-brief.html", links: [] },
    { id: "P4", type: "principle",   title: "Consistency and standards", page: "problem-brief.html", links: [] },
    { id: "P5", type: "principle",   title: "Error prevention", page: "problem-brief.html", links: [] },
    { id: "P6", type: "principle",   title: "Recognition rather than recall", page: "problem-brief.html", links: [] },
    { id: "P7", type: "principle",   title: "Flexibility and efficiency of use", page: "problem-brief.html", links: [] },
    { id: "P8", type: "principle",   title: "Aesthetic and minimalist design", page: "problem-brief.html", links: [] },
    { id: "P9", type: "principle",   title: "Help users recognise, diagnose and recover from errors", page: "problem-brief.html", links: [] },
    { id: "P10", type: "principle",  title: "Help and documentation", page: "problem-brief.html", links: [] }
  ]
};
