import { getApp, getApps, initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

// Firebase web configuration identifies the client project; access is controlled by Firebase Auth and Security Rules.
const firebaseConfig = {
  apiKey: "AIzaSyAiDpUtr6HyE_7J-sj22jmFcB3u6bQ3bxI",
  authDomain: "ignite-1df6e.firebaseapp.com",
  projectId: "ignite-1df6e",
  storageBucket: "ignite-1df6e.firebasestorage.app",
  messagingSenderId: "233569488556",
  appId: "1:233569488556:web:3f53a6dff408fe05559909",
};

export const firebaseApp = getApps().length ? getApp() : initializeApp(firebaseConfig);
export const auth = getAuth(firebaseApp);
