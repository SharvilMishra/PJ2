# Zuno Wellness Frontend

Responsive React and Vite interface for the PJ2 wellness dashboard. The current interface uses illustrative sample values; the local API serves the synthetic daily dataset in `Datasets/wellness_daily.csv` for development. The UI is not yet connected to the API.

## Run locally

```powershell
cd Frontend
npm install
npm run dev
```

The app includes a sign-in entry screen, overview dashboard, trends, appearance and notification preferences, and an editable profile. Sign-in and profile/preferences are frontend prototype interactions; they do not authenticate or persist data yet.
