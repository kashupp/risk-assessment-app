# Application Usage Guide

## 1. Installation

Clone the repository:

```bash
git clone https://github.com/kashupp/risk-assessment-app.git
cd risk-assessment-app
```

Create and activate a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 2. Running the Desktop Application

Start the CustomTkinter application:

```bash
python gui.py
```

### Using the Desktop Application

1. Enter a numerical value in each of the five feature fields.
2. Select **CALCULATE RISK**.
3. Review the total model value and classification.
4. View previous assessments in the history log.
5. Select **CLEAR** to reset the input fields.
6. Select **CLEAR LOG** to clear the assessment history.

## 3. Running the Web Application

Start the Streamlit application:

```bash
streamlit run streamlit_app.py
```

Open the local URL displayed in the terminal.

### Using the Web Application

1. Enter values for the five numerical features.
2. Select **Calculate risk assessment**.
3. Review the model score and classification.
4. Expand **Scoring methodology** to view the scoring rule.
5. Review previous assessments in the history section.
6. Select **Download assessment history (CSV)** to export the records.
7. Use **Reset inputs** to reset the feature values.
8. Confirm the clearing action before selecting **Clear assessment history**.

## 4. Input Requirements

The scoring engine requires:

- Exactly five feature values.
- Numerical values only.
- Finite values (no NaN or infinity).
- Non-negative values.

Invalid inputs are rejected by the scoring engine.

## 5. Assessment Classification

The prototype uses a predefined threshold of 50:

| Total score | Classification |
|---|---|
| Below 50 | HIGH RISK |
| 50 or above | LOW RISK |

This scoring rule is illustrative and is not a clinically validated assessment model.

## 6. Assessment History

- The desktop application maintains an assessment log while it is running.
- The web application maintains assessment history using Streamlit session state.
- The web application supports CSV export.
