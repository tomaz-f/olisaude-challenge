from fastapi import FastAPI
import uvicorn

from app.routers import health_checker_route

app = FastAPI()

app.include_router(health_checker_route.router, tags=["health-checker"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
