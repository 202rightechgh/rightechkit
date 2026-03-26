from fastapi import FastAPI

app = FastAPI(title="{{ project_name }}")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok", "service": "{{ project_slug }}"}

