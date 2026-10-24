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
