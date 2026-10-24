# PJ2 Wellness Dashboard

Zuno is a responsive wellness dashboard for exploring daily activity, sleep, recovery, stress, hydration, weight, and mood. It uses a calm, light healthcare palette with vivid lime accents and subtle tactile surfaces, guided by the supplied Zuno logo.

## Project structure

- `About/` — project brief and scope
- `Backend/` — API and data loading/analysis services
- `Datasets/` — data dictionary and synthetic demonstration data
- `docs/` — architecture, dataset notes, and decisions
- `Frontend/` — React/Vite interface

## Frontend

The frontend includes a sign-in entry screen, wellness overview, trends, responsive navigation, settings, profile, and a light/dim appearance control. See [Frontend/README.md](Frontend/README.md) for setup instructions.

`Datasets/wellness_daily.csv` contains generated demonstration values for the fictional profile, not measured wellness data. The backend serves those records when run locally. Authentication and persistent profile/preferences are not connected yet.

## Deploy to Vercel as one project

The root `vercel.json` defines separate frontend and backend services on one deployment. Requests to `/api` and `/api/*` route to the FastAPI service; all other paths route to the Vite frontend. The root `app.py` is the FastAPI deployment entrypoint and imports `Backend.app` so the API can read the shared dataset.

When importing the repository, set the Vercel project root to `./` and the project framework to **Services**. Vercel Services may require beta access for the account. For local combined development, install the Vercel CLI and run `vercel dev -L` from the repository root. The standard local commands are documented in [Backend/README.md](Backend/README.md) and [Frontend/README.md](Frontend/README.md).
