/* One entry per student hub. Add a line when you publish a new hub.
   slug  = the folder name inside hubs/ (lowercase, no spaces; use a pseudonym if the student prefers)
   name  = the name to show (the student's choice)
   title = the case title
   cohort= e.g. "2026 autumn"
   consent = true only after the student agreed to a public link
   url   = the student's own live link (if they publish in their own GitHub repository). Leave it out if you host the hub yourself in hubs/<slug>/
   Without url, the hub lives at hubs/<slug>/index.html */
window.HUBS = [
  // Student-hosted:  { slug: "example-student", name: "Example Student", title: "Onboarding redesign", cohort: "2026 autumn", consent: true, url: "https://example-student.github.io/my-case-hub/" }
  // Hosted by you:   { slug: "example-two", name: "Example Two", title: "Checkout flow", cohort: "2026 autumn", consent: true }
];
