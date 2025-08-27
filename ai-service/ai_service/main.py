from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/scrape-jobs")
def scrape_jobs_stub():
    return [
        {
            "id": 1,
            "job_role": "Data Scientist",
            "skills_required": ["Python", "SQL"],
            "qualification": "B.Tech",
            "domain": "Data Science"
        },
        {
            "id": 2,
            "job_role": "Frontend Engineer",
            "skills_required": ["React", "TypeScript"],
            "qualification": "B.E.",
            "domain": "Fullstack"
        },
        {
            "id": 3,
            "job_role": "Security Analyst",
            "skills_required": ["Network Security", "Python"],
            "qualification": "B.Tech",
            "domain": "Cybersecurity"
        }
    ]