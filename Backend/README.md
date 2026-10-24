# Backend

Read-only FastAPI service for the synthetic daily demonstration dataset in `Datasets/wellness_daily.csv`. It validates required columns, dates, categories, and the ranges explicitly defined in the data dictionary before returning records or averages.

## Configure the dataset

The generated demonstration CSV is included at `Datasets/wellness_daily.csv`. To point the API at another compatible CSV, set `WELLNESS_CSV` to its path. The included values are synthetic and must not be represented as measured health data.

## Run locally

From the repository root:

```powershell
python -m pip install -r requirements.txt
python -m uvicorn Backend.app:app --reload
```

- `GET /api/health`
- `GET /api/daily?start=2025-01-01&end=2025-01-31`
- `GET /api/summary?start=2025-01-01&end=2025-01-31`

Date parameters are inclusive. Invalid CSV content returns HTTP 422 with the row and validation issue.
