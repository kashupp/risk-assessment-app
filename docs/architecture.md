# Application Architecture

## Overview

The Risk Assessment application consists of three main Python modules. The scoring logic is separated from the user interfaces so that both applications use the same assessment function.

## Architecture

```text
                 User
                  |
          +-------+-------+
          |               |
     Desktop GUI       Web GUI
     (gui.py)     (streamlit_app.py)
          |               |
          +-------+-------+
                  |
             app.py
          assess_risk()
                  |
          Risk Classification
```

## Main Components

### 1. Scoring Engine — `app.py`

Contains the shared `assess_risk()` function.

Responsibilities:

- Accept five numerical feature values.
- Validate the number and type of inputs.
- Reject negative and non-finite values.
- Calculate the total score.
- Return the risk classification using the predefined threshold.

### 2. Desktop Interface — `gui.py`

Built with CustomTkinter.

Responsibilities:

- Collect five feature values from the user.
- Call the shared scoring function.
- Display the total score and classification.
- Maintain a timestamped assessment history.
- Provide controls to clear inputs and assessment history.

### 3. Web Interface — `streamlit_app.py`

Built with Streamlit.

Responsibilities:

- Collect five feature values through a web interface.
- Call the shared scoring function.
- Display the model score and classification.
- Maintain assessment history using Streamlit session state.
- Display scoring methodology.
- Export assessment history as a CSV file.

## Data Flow

1. The user enters five feature values through either interface.
2. The interface collects the input values.
3. The shared `assess_risk()` function in `app.py` validates the inputs.
4. The function calculates the model value and determines the classification.
5. The interface displays the assessment result.
6. The interface records the assessment in its history.

## Design Considerations

- **Code reuse:** Both interfaces share the same scoring function.
- **Separation of concerns:** Scoring logic and user-interface code are maintained in separate modules.
- **Input validation:** Invalid values are rejected before classification.
- **Maintainability:** The scoring engine can be modified independently of the interfaces.

