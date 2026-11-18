# StudyBuddy

A course Q&A assistant: scrape course pages → build a knowledge base → answer questions with sources.

See [docs/SCOPE.md](docs/SCOPE.md) for scope and requirements, and
[docs/golden_conversations/golden.md](docs/golden_conversations/golden.md) for the test cases.

## Setup (Windows)
```powershell
py -3.12 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env   # then add your API key
```

macOS/Linux: `python3.12 -m venv .venv && source .venv/bin/activate`

## Run
```powershell
python -m studybuddy.bot
```

## Docker
```powershell
docker build -t studybuddy .
docker run -it studybuddy
```
