# Zuno Wellness Frontend

Responsive React and Vite interface for the PJ2 wellness dashboard. The current interface uses illustrative sample values; the local API serves the synthetic daily dataset in `Datasets/wellness_daily.csv` for development. The UI is not yet connected to the API.

## Firebase Authentication setup

The app uses Firebase Authentication with email and password. Before signing in or creating accounts:

1. In Firebase Console, open **Authentication → Sign-in method** and enable **Email/Password**.
2. Under **Authentication → Settings → Authorized domains**, add `localhost` for local development and your deployed Vercel domain for production.
3. The supplied Firebase web app configuration is initialized in `src/firebase.ts`. Firebase web config is public client configuration; protect data with Firebase Security Rules and Auth settings.

The login screen supports account creation, sign-in, password reset email, and sign-out. The “Keep me signed in” option selects persistent or browser-session auth state.

## Run locally

```powershell
cd Frontend
npm install
npm run dev
```

The app includes a wellness overview, trends, appearance and notification preferences, and an editable profile. Profile/preferences are currently frontend prototype interactions and do not persist to a database.
