# StudyBuddy — Project Scope

## Problem
Students lose time hunting through course pages, handbooks and announcements for
simple answers: deadlines, grading rules, where a topic is covered, how to submit
work. Lecturers answer the same questions repeatedly.

## Goal
A chat assistant that answers students' course questions **only from the course's
own published material**, and cites where each answer came from.

## Users
- **Primary:** students enrolled in the course.
- **Secondary:** lecturers and TAs, who maintain the source material.

## In scope (v1)
1. **Scrape** — collect text from a fixed list of course web pages into `data/`.
2. **Knowledge base** — index the scraped text and retrieve relevant passages.
3. **Bot** — answer questions in plain English using retrieved passages, with sources.
4. **Refusal** — say "I don't know" (and point to the lecturer) when the answer is not in the material.
5. **Evaluation** — score the bot against the golden conversations in `docs/golden_conversations/`.

## Out of scope (v1)
- Doing students' assignments or writing graded work for them.
- Answering questions unrelated to the course.
- Personal records (grades, attendance, fees) — no access to student data.
- Logins, user accounts, or a mobile app.

## Requirements
| ID | Requirement | Type |
|----|-------------|------|
| R1 | Answers come only from scraped course material | Functional |
| R2 | Every answer lists its source document(s) | Functional |
| R3 | Unknown questions get an honest "not in the material" reply | Functional |
| R4 | Declines requests to complete graded work | Functional |
| R5 | Responds in under 5 seconds | Non-functional |
| R6 | API keys live in `.env` and are never committed | Non-functional |
| R7 | Runs in Docker with one command | Non-functional |

## Success criteria
- At least 8 of 10 golden conversations pass in `eval/`.
- Zero answers that invent facts not in the source material.

## Tech stack
Python 3.12 · requests + BeautifulSoup (scraping) · LLM API (answering) · Docker.

## Risks
- Course pages change → re-scrape on a schedule.
- LLM hallucination → answer only from retrieved text; refuse otherwise.
- Students may try to get assignment answers → explicit refusal rule (R4).
