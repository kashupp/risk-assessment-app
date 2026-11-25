
from datetime import datetime

import pandas as pd
import streamlit as st

from app import assess_risk

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Risk Assessment",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ASSESSMENT HISTORY
if "assessment_history" not in st.session_state:
    st.session_state.assessment_history = []

# STYLING
st.markdown(
    """
    <style>
    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .main-header {
        font-size: 2.1rem;
        font-weight: 700;
        color: #183153;
        margin-bottom: 0.2rem;
    }

    .sub-header {
        color: #64748b;
        font-size: 1rem;
        margin-bottom: 1.5rem;
    }

    .section-heading {
        color: #183153;
        font-size: 1.2rem;
        font-weight: 650;
        margin-top: 1rem;
        margin-bottom: 0.8rem;
    }

    .prototype-label {
        background-color: #eaf2ff;
        color: #2457a7;
        padding: 0.4rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
    }

    div[data-testid="stMetric"] {
        background-color: #f5f8fc;
        border: 1px solid #e2e8f0;
        padding: 1rem;
        border-radius: 12px;
    }

    div.stButton > button[kind="primary"] {
        width: 100%;
        border-radius: 9px;
        font-weight: 600;
        min-height: 3rem;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# HEADER
header_col, badge_col = st.columns([5, 1])

with header_col:
    st.markdown(
        '<div class="main-header">Patient Risk Classification Application</div>',
        unsafe_allow_html=True,
    )
    #st.markdown(
    #    '<div class="sub-header">'
    #    'An interactive prototype for demonstrating research risk scoring'
    #    '</div>',
    #    unsafe_allow_html=True,
    #)

with badge_col:
    st.markdown(
        '<div style="text-align:right; padding-top:12px;">'
        '<span class="prototype-label">PATIENT CLASSIFICATION</span>'
        '</div>',
        unsafe_allow_html=True,
    )

st.divider()

# RESAERCH DISCLAIMER
st.info(
    "**This is a protoype application** "
)

# FEATURE INPUT SECTION
st.markdown(
    '<div class="section-heading">Enter the five features required by the model.</div>',
    unsafe_allow_html=True,
)

#st.write(
#    "Enter the five features required by the model. "
#)

# RESEAT BUTTON
if st.button("Reset inputs"):
    for i in range(1, 6):
        st.session_state[f"feature_{i}"] = 10.0

    st.rerun()

with st.form("risk_assessment_form"):

    col1, col2 = st.columns(2)

    features = []

    for i in range(1, 6):
        target_col = col1 if i in (1, 3, 5) else col2

        with target_col:
            value = st.number_input(
                f"Feature {i}",
                min_value=0.0,
                max_value=100.0,
                value=10.0,
                step=1.0,
                key=f"feature_{i}",
                help="Illustrative numerical input.",
            )
            features.append(value)

    st.write("")

    submitted = st.form_submit_button(
        "Calculate risk assessment",
        type="primary",
    )

# ASSESSMENT RESULT
if submitted:
    try:
        result = assess_risk(features)
        total = sum(features)

    except (ValueError, TypeError) as error:
        st.error(f"Invalid assessment: {error}")
        st.stop()

    category = (
        "HIGH RISK"
        if result == "RISK"
        else "LOW RISK"
    )

    record = {
        "Assessment ID": len(st.session_state.assessment_history) + 1,
        "Date and time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Feature 1": features[0],
        "Feature 2": features[1],
        "Feature 3": features[2],
        "Feature 4": features[3],
        "Feature 5": features[4],
        "Total score": total,
        "Category": category,
    }

    st.session_state.assessment_history.append(record)

    st.divider()

    st.markdown(
        '<div class="section-heading">MODEL results</div>',
        unsafe_allow_html=True,
    )

    metric_col1, metric_col2 = st.columns(2)

    with metric_col1:
        st.metric(
            label="Total score",
            value=f"{total:.1f}",
            help="Sum of the five illustrative feature values.",
        )

    with metric_col2:
        if result == "RISK":
            category = "HIGH RISK"
        else:
            category = "LOW RISK"

        st.metric(
            label="MODEL CATEGORY",
            value=category,
        )

    if result == "RISK":
        st.warning(
            "**High risk category**\n\n"
            "The model score is below the demonstration threshold of 50."
        )
    else:
        st.success(
            "**Low risk category**\n\n"
            "The model score is equal to or above the demonstration threshold of 50."
        )

    #st.caption(
    #    "These categories are outputs of an illustrative rule, "
    #    "not estimates of actual patient risk."
    #)

# METHODOLOGY
st.divider()

with st.expander("Scoring methodology"):

    st.markdown("**Scoring method**")

    st.write(
        "The application uses five numerical features "
        "to calculate a total score."
    )

    st.latex(
        r"\text{Total score} = \sum_{i=1}^{5} \text{Feature}_i"
    )

    st.write("The demonstration threshold is 50.")

    st.markdown(
        """
        - Total below 50: HIGH RISK.
        - Total of 50 or above: LOW RISK.
        """
    )


# ASSESSMENT HISTORY DISPLAY
st.divider()

st.markdown(
    '<div class="section-heading">Assessment history</div>',
    unsafe_allow_html=True,
)

history = st.session_state.assessment_history

if history:
    st.write(f"Total assessments: {len(history)}")

    st.table(history)

    confirm_clear = st.checkbox(
        "I confirm that I want to clear the assessment history."
    )

    if st.button(
        "Clear assessment history",
        disabled=not confirm_clear,
    ):
        st.session_state.assessment_history = []
        st.rerun()

    history_df = pd.DataFrame(history)
    csv_data = history_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download assessment history (CSV)",
        data=csv_data,
        file_name="research_assessment_history.csv",
        mime="text/csv",
        use_container_width=True,
    )
else:
    st.info("No assessments recorded yet.")

# FOOTER
st.divider()

st.caption(
    "Patient Risk Assessment | Python · Streamlit | "
    "Prototype"
)
