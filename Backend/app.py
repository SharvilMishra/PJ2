"""Small read-only API for the daily wellness CSV."""
from __future__ import annotations

import csv
import os
from datetime import date, datetime
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException, Query

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = Path(os.getenv("WELLNESS_CSV", ROOT / "Datasets" / "wellness_daily.csv"))
REQUIRED_COLUMNS = {
    "date", "day_of_week", "steps", "distance_km", "calories_burned",
    "exercise_minutes", "exercise_type", "avg_heart_rate_bpm",
    "resting_heart_rate_bpm", "hrv_ms", "sleep_hours", "deep_sleep_pct",
    "bedtime", "wake_time", "sleep_score", "stress_score", "water_liters",
    "weight_kg", "mood_1to5",
}
NUMERIC_FIELDS = {
    "steps": int, "distance_km": float, "calories_burned": int,
    "exercise_minutes": int, "avg_heart_rate_bpm": int,
    "resting_heart_rate_bpm": int, "hrv_ms": float, "sleep_hours": float,
    "deep_sleep_pct": float, "sleep_score": int, "stress_score": int,
    "water_liters": float, "weight_kg": float, "mood_1to5": int,
}
DAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
EXERCISE_TYPES = {"Weight Training", "Dancing", "Walking", "Running", "Yoga", "None"}
app = FastAPI(title="Zuno Wellness API", version="1.0.0")


def _load_rows() -> list[dict[str, Any]]:
    if not DATA_FILE.is_file():
        raise HTTPException(status_code=503, detail="Wellness dataset is not installed yet.")
    rows: list[dict[str, Any]] = []
    seen: set[date] = set()
    try:
        with DATA_FILE.open(newline="", encoding="utf-8-sig") as source:
            reader = csv.DictReader(source)
            columns = set(reader.fieldnames or ())
            missing = sorted(REQUIRED_COLUMNS - columns)
            if missing:
                raise ValueError(f"Missing required columns: {', '.join(missing)}")
            for line, raw in enumerate(reader, start=2):
                row: dict[str, Any] = dict(raw)
                if any(row.get(key) is None or not str(row[key]).strip() for key in REQUIRED_COLUMNS):
                    raise ValueError(f"Row {line} has a missing required value")
                row_date = date.fromisoformat(row["date"])
                if row_date in seen:
                    raise ValueError(f"Row {line} duplicates date {row_date.isoformat()}")
                seen.add(row_date)
                if row["day_of_week"] not in DAYS or row["day_of_week"] != row_date.strftime("%A"):
                    raise ValueError(f"Row {line} has a day_of_week that does not match its date")
                if row["exercise_type"] not in EXERCISE_TYPES:
                    raise ValueError(f"Row {line} has an unknown exercise_type")
                row["date"] = row_date
                for field in ("bedtime", "wake_time"):
                    datetime.strptime(row[field], "%H:%M")
                for field, converter in NUMERIC_FIELDS.items():
                    row[field] = converter(row[field])
                if not 0 <= row["sleep_score"] <= 100:
                    raise ValueError(f"Row {line}: sleep_score must be between 0 and 100")
                if not 1 <= row["stress_score"] <= 10:
                    raise ValueError(f"Row {line}: stress_score must be between 1 and 10")
                if not 1 <= row["mood_1to5"] <= 5:
                    raise ValueError(f"Row {line}: mood_1to5 must be between 1 and 5")
                if not 0 <= row["deep_sleep_pct"] <= 100:
                    raise ValueError(f"Row {line}: deep_sleep_pct must be between 0 and 100")
                rows.append(row)
    except HTTPException:
        raise
    except (OSError, ValueError, TypeError) as exc:
        raise HTTPException(status_code=422, detail=f"Invalid wellness CSV: {exc}") from exc
    return sorted(rows, key=lambda item: item["date"])


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok", "dataset": "available" if DATA_FILE.is_file() else "not_configured"}


@app.get("/api/daily")
def daily_records(
    start: date | None = Query(default=None, description="First date to include (YYYY-MM-DD)"),
    end: date | None = Query(default=None, description="Last date to include (YYYY-MM-DD)"),
) -> dict[str, Any]:
    if start and end and start > end:
        raise HTTPException(status_code=400, detail="start must be on or before end")
    rows = [r for r in _load_rows() if (start is None or r["date"] >= start) and (end is None or r["date"] <= end)]
    return {"count": len(rows), "records": [{**row, "date": row["date"].isoformat()} for row in rows]}


@app.get("/api/summary")
def summary(
    start: date | None = Query(default=None),
    end: date | None = Query(default=None),
) -> dict[str, Any]:
    if start and end and start > end:
        raise HTTPException(status_code=400, detail="start must be on or before end")
    rows = [r for r in _load_rows() if (start is None or r["date"] >= start) and (end is None or r["date"] <= end)]
    if not rows:
        return {"count": 0, "start": None, "end": None, "averages": {}}
    fields = tuple(NUMERIC_FIELDS)
    averages = {field: round(sum(row[field] for row in rows) / len(rows), 2) for field in fields}
    return {"count": len(rows), "start": rows[0]["date"].isoformat(), "end": rows[-1]["date"].isoformat(), "averages": averages}
