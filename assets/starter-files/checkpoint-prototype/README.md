# Checkpoint prototype (week 7)

A working three-screen first-box flow for the fictional Kitchen Crate case, built on the starter design system. Use it if you missed week 6, or if you want a known starting point for the refine and alignment-check practice. Open `index.html` in a browser.

**Flow:** Start, Choose your delivery day, Check your first box (then "You are set").

## What is already right
Real headings and labels, keyboard operation, visible focus, a step indicator, an inline error with a live announcement, and content that answers the user-voice findings: the delivery day is shown as changeable until a stated cut-off, and the skip route is shown on the confirm screen.

## Known gaps to refine in week 7 (on purpose)
1. **States:** no loading state, no "no delivery days available" state, no error if the booking fails.
2. **Real content:** the days are placeholders. Dates, cut-off times and delivery windows need real values.
3. **Responsive:** only checked at phone width; check a wide screen.
4. **System check:** ask the AI to audit the screens against `design-system/tokens.css` and `components.css` (raw values? missing classes?). Confirm each finding yourself.
5. **Accessibility check:** focus order, contrast of the badge, the wording of the "I will not be home" option, and what a screen reader hears on the confirm screen.
6. **Alignment check:** write down the design decisions in this prototype (D items) and see which opportunity and hypothesis each one serves.
7. **Principle audit:** where does it pull against a principle? For example, error prevention if the cut-off is not visible on the first screen.
