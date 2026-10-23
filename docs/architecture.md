# Proposed architecture

```text
Browser dashboard (Frontend)
          | JSON
          v
Data API (Backend) ---- reads ----> Datasets/*.csv
```

Keep dataset loading and validation in the backend. The frontend should request summarized, date-filterable data rather than parsing the source file itself. Start without a database; reconsider persistence only if user accounts, saved settings, or uploads become part of scope.