import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

st.set_page_config(
    page_title="Employee Burnout Prediction",
    page_icon="🧠",
    layout="wide"
)
@st.cache_resource
def load_model():
    return joblib.load("employee_burnout_model.pkl")


model = load_model()
st.markdown("""
<style>

.main {
    background-color: black;
}

h1{
    color:#1565C0;
}

div[data-testid="stMetric"]{
    background-color:black;
    border-radius:15px;
    padding:20px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.12);
    text-align:center;
}

.stButton>button{
    background:#1565C0;
    color:white;
    border-radius:12px;
    height:55px;
    font-size:18px;
    font-weight:bold;
    border:none;
}

.stButton>button:hover{
    background:#0D47A1;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

</style>
""", unsafe_allow_html=True)

col1,col2=st.columns([5,1])

with col1:

    st.title("🧠 BurnSafe AI")

    st.caption("Employee Burnout Prediction & Risk Assessment")

with col2:

    st.success("🟢 Online")
st.sidebar.image(
"https://img.icons8.com/color/96/artificial-intelligence.png",
width=80
)

st.sidebar.title("BurnSafe AI")
st.sidebar.caption("AI Powered HR Analytics")
page = st.sidebar.radio(
    "Go to",
    [
        "Prediction",
        "Model Performance",
        "Feature Importance",
        "About"
    ]
)
if page == "Prediction":

    st.header("👤 Employee Information")

    col1, col2 = st.columns(2)

    with col1:

        gender = st.selectbox(
            "Gender",
            ["Female", "Male"]
        )

        company = st.selectbox(
            "Company Type",
            ["Product", "Service"]
        )

        wfh = st.selectbox(
            "WFH Available",
            ["No", "Yes"]
        )

        designation = st.slider(
            "Designation",
            0,
            5,
            2
        )

    with col2:
        resource = st.slider(
            "Resource Allocation",
            1.0,
            10.0,
            5.0
        )

        fatigue = st.slider(
            "Mental Fatigue Score",
            1.0,
            10.0,
            5.0
        )

        month = st.selectbox(
            "Joining Month",
            list(range(1, 13))
        )

    predict = st.button(
        "🔍 Predict Burnout",
        use_container_width=True
    )
    import joblib
    import pandas as pd

    model = joblib.load("employee_burnout_model.pkl")

    if predict:

        quarter = (month - 1) // 3 + 1

        gender_value = 1 if gender == "Male" else 0
        company_value = 1 if company == "Service" else 0
        wfh_value = 1 if wfh == "Yes" else 0

        employee = pd.DataFrame({
            "Gender": [gender_value],
            "Company Type": [company_value],
            "WFH Setup Available": [wfh_value],
            "Designation": [designation],
            "Resource Allocation": [resource],
            "Mental Fatigue Score": [fatigue],
            "Month": [month],
            "Quarter": [quarter]
        })

        prediction = model.predict(employee)[0]

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(
                "Burnout Score",
                f"{prediction:.2f}"
            )
        with col2:
            if prediction < 0.30:
                risk = "🟢 LOW"

            elif prediction < 0.60:
                risk = "🟡 MODERATE"

            else:
                risk = "🔴 HIGH"


            st.metric(
                "Risk Level",
                risk
            )
        with col3:

            st.metric(
                "Model",
                "Gradient Boosting"
            )

if page == "Model Performance":

    st.header("📊 Model Performance")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "🏆 Best Model",
        "Gradient Boosting"
    )

    c2.metric(
        "📈 R² Score",
        "0.905"
    )

    c3.metric(
        "✅ Cross Validation",
        "0.906"
    )

    performance = pd.DataFrame({

        "Model":[
            "Linear Regression",
            "Decision Tree",
            "Random Forest",
            "Gradient Boosting"
        ],

        "R² Score":[
            0.895065,
            0.830056,
            0.888121,
            0.904782
        ],

        "MAE":[
            0.049646,
            0.061107,
            0.050279,
            0.047425
        ],

        "RMSE":[
            0.063220,
            0.080454,
            0.065278,
            0.060222
        ]

    })

    st.subheader("📋 Model Comparison")

    st.dataframe(performance, use_container_width=True)

    fig = px.bar(
        performance,
        x="Model",
        y="R² Score",
        text="R² Score",
        title="Model Comparison (R² Score)"
    )
    fig.update_yaxes(
    range=[0.75, 1]
    )
    fig.update_layout(
        plot_bgcolor="white",
        height=450,
        paper_bgcolor="white",
        font=dict(
            color="black"
        ),
        xaxis=dict(
            tickfont=dict(color="black")
        ),
        yaxis=dict(
            tickfont=dict(color="black")
        )
    )

    fig.update_traces(
        textposition="outside"
    )

    
    st.plotly_chart(fig, use_container_width=True)

if page == "Feature Importance":

    st.header("📈 Feature Importance")

    st.write(
        "The chart below shows how much each feature contributes to predicting employee burnout."
    )

    importance = pd.DataFrame({

        "Feature":[
            "Mental Fatigue Score",
            "Resource Allocation",
            "WFH Setup Available",
            "Designation",
            "Gender",
            "Month",
            "Company Type",
            "Quarter"
        ],

        "Importance":[
            0.901640,
            0.093874,
            0.002689,
            0.001500,
            0.000205,
            0.000067,
            0.000013,
            0.000012
        ]

    })

    fig = px.bar(
        importance,
        x="Importance",
        y="Feature",
        orientation="h",
        color="Importance",
        text="Importance",
        title="Factors Affecting Employee Burnout"
    )

    fig.update_layout(
        plot_bgcolor="white",
        height=500,
        xaxis_title="Importance Score",
        yaxis_title=""
    )

    st.plotly_chart(fig, use_container_width=True)

if page == "About":

    st.header("ℹ️ About BurnSafe AI")

    st.markdown("""
### BurnSafe AI – Employee Burnout Prediction & Risk Assessment

This project uses Machine Learning to predict employee burnout based on workplace and employee-related factors.

### Objective
To help HR departments identify employees who may be at risk of burnout and support proactive interventions.

### Technologies Used
- Python
- Pandas
- Scikit-learn
- Streamlit
- Plotly

### Machine Learning Model
Gradient Boosting Regressor

### Dataset
Employee Burnout Analysis Dataset (Kaggle)

### Developed By
Ranjan A
""")    