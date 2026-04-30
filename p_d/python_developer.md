# 12-Month Roadmap: QA Python Automation → Junior Python Developer

## Overview
Transition from Senior QA Python Automation Engineer to Junior Python Developer. Focus on essentials only: practical coding, one solid project, and fundamentals.

**Time Commitment**: 30 minutes/day (~3.5 hours/week)  
**Target**: Land a Junior Python Developer role (0-2 years experience level)  
**Timeline**: 12 months (realistic with part-time learning)

---

## Phase 1: Foundations (Months 1-3) - 30 mins/day

### What to Learn
- [ ] Python fundamentals deeper (you know this, just refresh)
- [ ] FastAPI basics (3-4 hours from official tutorial)
- [ ] PostgreSQL basics (not deep, just how to use it)
- [ ] Basic pytest (you know testing, adapt it to unit testing)

### What to Build
**Single Project**: Todo API
- Users can create, read, update, delete todos
- Uses FastAPI + PostgreSQL
- No auth, no fancy features
- Just CRUD operations

### Time Breakdown (30 mins/day)
- 15 mins: Watch/read (FastAPI docs, PostgreSQL basics)
- 15 mins: Code (build Todo API incrementally)

### Deliverable
- GitHub repo with Todo API
- Basic README

---

## Phase 2: Deeper Into One Project (Months 4-8) - 30 mins/day

### Focus on Todo API - Make it Production-Ready
- [ ] Add tests (pytest - 50+ simple tests)
- [ ] Add input validation (Pydantic)
- [ ] Add error handling
- [ ] Add proper folder structure
- [ ] Write good README

### Skip (Don't do)
- ❌ Async/await (nice to have for junior)
- ❌ Docker (nice to have for junior)
- ❌ Redis/caching (advanced)
- ❌ CI/CD pipeline (can add later)
- ❌ System design (not needed for junior)

### Time Breakdown (30 mins/day)
- 10 mins: Read tests/examples from other projects
- 20 mins: Code & test Todo API

### Deliverable
- Todo API with >80% test coverage
- Professional README with instructions
- Clean code (follow PEP8)

---

## Phase 3: Second Smaller Project (Months 9-11) - 30 mins/day

### Build: Simple Notes API
- Users can create, read, update, delete notes
- Even simpler than Todo API
- Uses same tech stack: FastAPI + PostgreSQL + pytest
- Just prove you can build more than one project

### Time Breakdown (30 mins/day)
- 5 mins: Plan structure (reuse from Todo API)
- 25 mins: Code

### Deliverable
- GitHub repo with Notes API
- README

---

## Phase 4: Polish & Job Search (Month 12) - 30 mins/day

### Polish
- [ ] Review both projects for code quality
- [ ] Add proper docstrings
- [ ] Ensure both projects have great README files
- [ ] Clean up GitHub profile

### Job Search
- [ ] Update resume: highlight projects, not just QA experience
- [ ] Write LinkedIn summary focused on developer journey
- [ ] Apply to 3-5 junior Python developer roles
- [ ] Prepare 2-3 standard interview answers about projects

---

## What NOT to Do (Stay Focused)

❌ Don't learn Django, Flask, or other frameworks yet  
❌ Don't implement advanced features (caching, queues, etc.)  
❌ Don't worry about Docker, Kubernetes, or DevOps  
❌ Don't study system design or complex architectures  
❌ Don't aim for 100% test coverage (80% is enough)  
❌ Don't watch endless tutorials (12 months = 30 mins, not 8 hours)  
❌ Don't chase async/concurrent programming yet  

---

## Simple Weekly Schedule

Treat it like a habit, not a job:
- **Monday**: Code on project (20 mins) + read docs (10 mins)
- **Tuesday**: Code on project (30 mins)
- **Wednesday**: Code on project (20 mins) + look at test examples (10 mins)
- **Thursday**: Code on project (30 mins)
- **Friday**: Code on project (30 mins)
- **Saturday**: Code on project (20 mins) + review code (10 mins)
- **Sunday**: Off or optional docs reading (10 mins)

**Total**: ~3.5 hours/week

---

## The Absolute Minimum to Learn

### FastAPI (8 hours total)
- Route handlers (GET, POST, PUT, DELETE)
- Path parameters & query parameters
- Request body with Pydantic models
- Response models
- Basic error handling
- That's it. You don't need middleware, dependencies, etc.

### PostgreSQL (4 hours total)
- CREATE TABLE, INSERT, SELECT, UPDATE, DELETE
- Foreign keys (for users-todos relationship)
- Basic indexing
- That's it. You don't need JSON types, advanced queries, etc.

### pytest (3 hours total)
- Write test functions
- Use fixtures
- Mock external calls (if any)
- Test endpoints with TestClient
- That's it. You don't need parametrize or complex patterns.

### Python Best Practices (2 hours total)
- PEP8 formatting
- Type hints (basic)
- Docstrings
- Folder structure

---

## Project Details

### Todo API Structure
```
todo-api/
├── main.py                 # FastAPI app
├── models.py              # Pydantic models
├── database.py            # DB connection
├── routes.py              # API endpoints
├── tests/
│   ├── test_routes.py
│   └── test_models.py
├── requirements.txt
└── README.md
```

### Notes API (Same Structure, Reuse)
```
notes-api/
├── main.py
├── models.py
├── database.py
├── routes.py
├── tests/
│   ├── test_routes.py
│   └── test_models.py
├── requirements.txt
└── README.md
```

---

## Month-by-Month Checklist

### Months 1-3: Foundation ✓
- [ ] FastAPI tutorial completed (4 hours)
- [ ] PostgreSQL basics learned (2 hours)
- [ ] Todo API basic CRUD working
- [ ] Can run locally: `pip install -r requirements.txt && python main.py`

### Months 4-8: Polish ✓
- [ ] 50+ tests written
- [ ] >80% code coverage
- [ ] Input validation added
- [ ] Error handling added
- [ ] Professional README with setup instructions
- [ ] Repo pushed to GitHub with good commit messages

### Months 9-11: Second Project ✓
- [ ] Notes API built (same structure)
- [ ] Tests written (at least 30 tests)
- [ ] GitHub repo created
- [ ] README written

### Month 12: Job Search ✓
- [ ] Code reviewed for quality
- [ ] Resume updated
- [ ] LinkedIn polished
- [ ] Applications sent to 3+ positions

---

## Resources (Only Essential)

### Learn FastAPI
- Official docs: fastapi.tiangolo.com (free, 4 hours max)
- Real Python "FastAPI by Example" (1 article)

### Learn PostgreSQL
- W3Schools PostgreSQL tutorial (basics only)
- Official docs when you get stuck

### Learn pytest
- Real Python pytest tutorial (free)
- pytest docs for reference

### Practice
- Build the projects (this IS the practice)

---

## Realistic Expectations

**This is achievable because:**
- You already know Python (saving 30+ hours)
- You already know testing concepts (saving 20+ hours)
- You already know debugging and problem-solving
- Juniors don't need to know everything—just fundamentals

**Junior role requirements (realistic):**
- Can build basic CRUD API ✓
- Understands FastAPI routing ✓
- Can write unit tests ✓
- Can use PostgreSQL basics ✓
- Can follow code standards (PEP8) ✓
- Has 2 projects on GitHub ✓

**Senior QA advantage:**
- You already test thoroughly—your code will be better
- You know about edge cases
- You're detail-oriented
- You understand logging and debugging

---

## How to Stay Consistent

1. **Make it a daily habit** - Like brushing teeth, do 30 mins every day
2. **Same time daily** - e.g., 6:30 AM before work, or 30 mins at lunch
3. **Track progress** - Check off boxes as you go
4. **Don't skip days** - Even 15 mins beats skipping
5. **Build momentum** - Once you see your Todo API working, it feels rewarding

---

## Red Flags (What Goes Wrong)

🚩 "I'll do 2 hours on weekends instead of daily" → Usually doesn't happen  
🚩 "I'll learn Django too" → Distraction, stick to FastAPI  
🚩 "I need to understand async first" → Not needed for junior role  
🚩 "My project isn't perfect yet" → Perfectionism kills progress, done > perfect  
🚩 "I'll start next week" → Start NOW, today, with 30 mins

---

## After 12 Months

**Best case**: Land a junior role at month 11-12  
**Good case**: Have 2 solid projects, ready to apply aggressively month 12+  
**Realistic case**: Still learning, but comfortable building simple APIs

**After you get the job:**
- You'll learn 10x faster on the job
- Your QA background = advantage with testing
- Pick one specialization: web, data, DevOps, etc.

---

## The Mental Shift

**From QA to Dev thinking:**
- ❓ QA: "What if this breaks?" → Dev: "How do I build this?"
- ❓ QA: "Edge cases first" → Dev: "Happy path first, then edge cases"
- ❓ QA: "Test everything" → Dev: "Test critical logic"
- ❓ QA: "Prevent bugs" → Dev: "Ship features, fix bugs fast"

---

## Success Looks Like (Month 12)

✅ GitHub profile with 2 real projects  
✅ Both projects have working APIs  
✅ >80% test coverage on both  
✅ README files explain how to run them  
✅ Clean, readable code (PEP8)  
✅ Can explain what each project does in a job interview  
✅ Confident enough to apply for junior roles

---

## Final Advice

**Don't try to be perfect.** Your goal is junior, not senior. Build simple, working projects. Good code > complex code.

**30 mins/day is enough.** It compounds. 12 months × 180 hours = a real developer.

**Your QA background is gold.** Own it. You test better than most junior devs. Use that advantage.

**Start building today.** Not tomorrow. Not Monday. Today. 30 minutes. Create the first FastAPI route.

---

**Last Updated**: April 2026  
**Your start date**: [Date you begin]  
**Your target job date**: [12 months from start]
