# Dataset notes

## Coverage and grain

The dictionary describes 365 rows, one per day, for 1 January through 31 December 2025. The subject, Emily Park (35), is explicitly fictional.

## Fields

- Calendar: `date`, `day_of_week`
- Activity: `steps`, `distance_km`, `calories_burned`, `exercise_minutes`, `exercise_type`
- Cardiovascular and recovery: `avg_heart_rate_bpm`, `resting_heart_rate_bpm`, `hrv_ms`
- Sleep: `sleep_hours`, `deep_sleep_pct`, `bedtime`, `wake_time`, `sleep_score`
- Other wellness: `stress_score`, `water_liters`, `weight_kg`, `mood_1to5`

## Interpretation

Stress ranges from 1 to 10, with higher values indicating more stress. Mood ranges from 1 (low) to 5 (high). Deep sleep is a percentage of total sleep. The dictionary notes that higher HRV usually indicates better recovery and lower resting heart rate is generally associated with fitness; these are contextual signals, not diagnoses.

Validate date continuity, categorical values, numeric ranges, missing values, and sleep time handling when the dataset is added. Preserve the original input.