# Data schema (example)

- patient_id: string
- admission_id: string
- admission_ts: timestamp
- discharge_ts: timestamp
- age: int
- sex: categorical
- primary_diagnosis: ICD code
- secondary_diagnoses: list
- labs_*: numeric (lab values)
- vitals_*: numeric
- medications: list
- prior_admissions_6mo: int
- readmitted_30d: binary (label)
