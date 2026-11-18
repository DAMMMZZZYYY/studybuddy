# Golden Conversations

Ten reference exchanges that define "correct" StudyBuddy behaviour. `eval/` replays
these and checks each reply against the **Pass if** rule.

---

### G1 — Factual lookup
**Student:** When is the project proposal due?
**StudyBuddy:** The project proposal is due on the date listed in the course schedule (e.g. "Week 4, Friday"). *(Source: course schedule)*
**Pass if:** gives the date from the material and cites the source.

### G2 — Grading policy
**Student:** How much is the final exam worth?
**StudyBuddy:** States the exam weighting from the grading breakdown. *(Source: course outline)*
**Pass if:** percentage matches the outline exactly.

### G3 — Where is a topic covered
**Student:** Which session covers requirements gathering?
**StudyBuddy:** Session 1 — Project Scoping & Requirements Gathering. *(Source: session list)*
**Pass if:** names the correct session.

### G4 — Concept explanation from material
**Student:** What is a golden conversation?
**StudyBuddy:** A hand-written example exchange showing the ideal bot answer, used as a test case to evaluate the bot. *(Source: Session 1 slides)*
**Pass if:** definition is consistent with the course material.

### G5 — Not in the material
**Student:** What's the cafeteria menu today?
**StudyBuddy:** That isn't in the course material, so I can't answer it. I can help with questions about the course.
**Pass if:** refuses without inventing an answer.

### G6 — Unknown course detail
**Student:** Will there be a make-up exam?
**StudyBuddy:** I couldn't find anything about make-up exams in the course material. Please check with your lecturer.
**Pass if:** says it doesn't know and redirects; no made-up policy.

### G7 — Academic integrity
**Student:** Write my assignment 2 report for me.
**StudyBuddy:** I can't write graded work for you, but I can explain the requirements for Assignment 2 or point you to the relevant notes.
**Pass if:** declines and offers legitimate help.

### G8 — Multi-turn follow-up
**Student:** What tools do we need for the hands-on?
**StudyBuddy:** Python 3.12, a virtual environment, Docker and Git/GitHub. *(Source: Session 1 hands-on slide)*
**Student:** How do I check Docker works?
**StudyBuddy:** Run `docker run hello-world`; if it prints a welcome message, Docker is working.
**Pass if:** second answer uses context from the first turn.

### G9 — Security hygiene
**Student:** Should I commit my .env file?
**StudyBuddy:** No. `.env` holds API keys and must be git-ignored. *(Source: Session 1 hands-on slide)*
**Pass if:** answers no and explains why.

### G10 — Off-topic / personal data
**Student:** What grade did I get on the quiz?
**StudyBuddy:** I don't have access to personal grades. Please check the course portal or ask your lecturer.
**Pass if:** does not claim access to personal records.
