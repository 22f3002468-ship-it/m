# api/latency.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.post("/metrics")
async def latency_metrics(req: Request):
    body = await req.json()
    regions = body["regions"]
    threshold = body["threshold_ms"]

    # Load telemetry data
    df = pd.read_json("q-vercel-latency.json")

    # Filter by requested regions
    result = []
    for region in regions:
        sub = df[df["region"] == region]
        avg_latency = sub["latency_ms"].mean()
        p95_latency = sub["latency_ms"].quantile(0.95)
        avg_uptime = sub["uptime_pct"].mean()
        breaches = (sub["latency_ms"] > threshold).sum()

        result.append({
            "region": region,
            "avg_latency": round(avg_latency, 2),
            "p95_latency": round(p95_latency, 2),
            "avg_uptime": round(avg_uptime, 3),
            "breaches": int(breaches)
        })

    return result
