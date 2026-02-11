import streamlit as st
import pandas as pd
import pickle
import time
import plotly.graph_objects as go

# =========================
# 1. PAGE CONFIGURATION
# =========================
st.set_page_config(
    page_title="Predictr AI | Customer Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# 2. LOAD MODELS (Wrapped for Safety)
# =========================
try:
    reg_model = pickle.load(open("reg_model.pkl", "rb"))
    clf_model = pickle.load(open("clf_model.pkl", "rb"))
    encoder_priority = pickle.load(open("encoder_priority.pkl", "rb"))
    encoder_channel = pickle.load(open("encoder_channel.pkl", "rb"))
    models_loaded = True
except FileNotFoundError:
    models_loaded = False

# =========================
# 3. FINAL POLISHED CSS
# =========================
st.markdown("""
<style>
    /* Import Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

    /* --- GLOBAL TEXT --- */
    html, body, [class*="css"], .stMarkdown, .stText, p, h1, h2, h3, h4, li, span {
        font-family: 'Inter', sans-serif;
        color: #e2e8f0 !important;
    }

    /* --- BACKGROUNDS --- */
    .stApp {
        background-color: #0f172a; /* Navy Blue */
        background-image: radial-gradient(at 0% 0%, rgba(56, 189, 248, 0.1) 0px, transparent 50%),
                          radial-gradient(at 100% 100%, rgba(139, 92, 246, 0.1) 0px, transparent 50%);
    }
    
    /* --- FIX: TOP HEADER BAR --- */
    header[data-testid="stHeader"] {
        background-color: transparent !important;
    }

    /* --- SIDEBAR --- */
    section[data-testid="stSidebar"] {
        background-color: #1e293b;
        border-right: 1px solid rgba(255,255,255,0.1);
    }
    
    /* --- FIX: DROPDOWN MENUS (The Invisible Text Fix) --- */
    /* This targets the container of the dropdown options */
    div[data-baseweb="popover"] {
        background-color: #1e293b !important;
        border: 1px solid #475569;
    }
    /* This targets the options themselves */
    div[data-baseweb="popover"] li {
        background-color: #1e293b !important;
    }
    /* Hover state for dropdown options */
    div[data-baseweb="popover"] li:hover {
        background-color: #334155 !important;
    }
    /* Selectbox box itself */
    div[data-baseweb="select"] > div {
        background-color: #0f172a !important;
        border-color: #475569 !important;
        color: white !important;
    }

    /* --- WIDGET LABELS --- */
    .stSelectbox label, .stSlider label, .stNumberInput label, .stTextInput label {
        color: white !important;
        font-weight: 600;
        font-size: 1rem;
    }
    
    /* --- CARDS --- */
    .metric-card {
        background: #1e293b;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
    }
    .metric-label {
        font-size: 0.9rem;
        color: #94a3b8 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: white !important;
    }

    /* --- SUMMARY BOX --- */
    .model-inputs-box {
        background: #1e293b;
        padding: 20px; 
        border-radius: 10px; 
        border: 1px solid #334155;
    }
    .model-inputs-box p {
        margin: 8px 0;
        color: #cbd5e1 !important;
    }
    .model-inputs-box strong {
        color: #60a5fa !important;
    }

    /* --- BUTTONS --- */
    .stButton > button {
        background: linear-gradient(to right, #3b82f6, #8b5cf6);
        color: white !important;
        border: none;
        padding: 0.6rem 1rem;
        border-radius: 8px;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        opacity: 0.9;
        box-shadow: 0 4px 12px rgba(139, 92, 246, 0.4);
    }

    /* --- TEXT COLORS --- */
    .text-success { color: #4ade80 !important; }
    .text-danger { color: #f87171 !important; }
    
    /* --- GRADIENT TEXT --- */
    .gradient-text {
        background: linear-gradient(45deg, #3b82f6, #8b5cf6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }
</style>
""", unsafe_allow_html=True)

# =========================
# 4. SIDEBAR INPUTS
# =========================
with st.sidebar:
    st.title("🎛️ Case Parameters")
    st.markdown("Configure the customer support ticket details below.")
    st.divider()

    # Dropdowns (Handle Demo Mode)
    priority_options = encoder_priority.classes_ if models_loaded else ["Low", "Medium", "High", "Critical"]
    channel_options = encoder_channel.classes_ if models_loaded else ["Email", "Phone", "Chat", "Social Media"]

    ticket_priority = st.selectbox("Ticket Priority", priority_options)
    ticket_channel = st.selectbox("Ticket Channel", channel_options)
    
    st.divider()
    
    customer_age = st.slider("Customer Age", 18, 80, 30)
    first_response_time = st.number_input("First Response Time (mins)", min_value=0, value=25)
    
    st.write("")
    run_btn = st.button("✨ Generate Prediction")
    
    st.markdown("---")
    if not models_loaded:
        st.warning("⚠️ DEMO MODE: Models not found.")

# =========================
# 5. MAIN DASHBOARD
# =========================

# Hero Section
col_logo, col_header = st.columns([1, 6])
with col_header:
    st.markdown("<h1 class='gradient-text'>AI Customer Intelligence</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:1.1rem; color:#94a3b8 !important;'>Real-time prediction of resolution timeline and customer churn risk.</p>", unsafe_allow_html=True)

st.write("")
st.write("")

if run_btn:
    
    with st.spinner("Analyzing historical ticket patterns..."):
        time.sleep(0.6) 

    # --- MODEL INFERENCE ---
    if models_loaded:
        priority_encoded = encoder_priority.transform([ticket_priority])[0]
        channel_encoded = encoder_channel.transform([ticket_channel])[0]

        user_input = pd.DataFrame(
            [[customer_age, priority_encoded, channel_encoded, first_response_time]],
            columns=["customer_age", "ticket_priority", "ticket_channel", "first_response_time"]
        )

        resolution_time = reg_model.predict(user_input)[0]
        abandon_prob = clf_model.predict_proba(user_input)[0][1]
    else:
        # Dummy Logic
        resolution_time = 45.2 + (first_response_time * 0.5)
        abandon_prob = 0.72 if first_response_time > 60 else 0.25

    # --- LAYOUT RESULTS ---
    col1, col2, col3 = st.columns([1, 1, 1.5])
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Est. Resolution Time</div>
            <div class="metric-value">{round(float(resolution_time), 1)} <span style="font-size:1rem; color:#94a3b8 !important;">min</span></div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        risk_label = "High Risk" if abandon_prob > 0.5 else "Safe"
        risk_color = "text-danger" if abandon_prob > 0.5 else "text-success"
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Risk Category</div>
            <div class="metric-value {risk_color}">{risk_label}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        if abandon_prob > 0.5:
            st.error("⚠️ **Action Required:** This customer shows signs of high frustration. Recommend immediate escalation.")
        else:
            st.success("✅ **Stable:** Customer behavior aligns with standard resolution flows. No escalation needed.")

    st.write("")
    
    # --- CHARTS & SUMMARY ---
    viz_col1, viz_col2 = st.columns([2, 1])
    
    with viz_col1:
        st.markdown("### Abandonment Probability Gauge")
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = abandon_prob * 100,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Churn Probability (%)", 'font': {'size': 18, 'color': "white"}},
            gauge = {
                'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "white"},
                'bar': {'color': "#1f2937"},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "#374151",
                'steps': [
                    {'range': [0, 30], 'color': "#4ade80"},
                    {'range': [30, 70], 'color': "#fbbf24"},
                    {'range': [70, 100], 'color': "#f87171"}
                ],
                'threshold': {
                    'line': {'color': "white", 'width': 4},
                    'thickness': 0.75,
                    'value': abandon_prob * 100
                }
            }
        ))
        
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)', 
            plot_bgcolor='rgba(0,0,0,0)',
            font={'color': "white"},
            height=300,
            margin=dict(l=20, r=20, t=50, b=20)
        )
        st.plotly_chart(fig, use_container_width=True)

    with viz_col2:
        st.markdown("### 📝 Model Inputs")
        st.markdown(f"""
        <div class="model-inputs-box">
            <p><strong>Channel:</strong> {ticket_channel}</p>
            <p><strong>Priority:</strong> {ticket_priority}</p>
            <p><strong>Age:</strong> {customer_age}</p>
            <p><strong>Initial Wait:</strong> {first_response_time} min</p>
        </div>
        """, unsafe_allow_html=True)

else:
    st.info("👈 Please configure the ticket parameters in the sidebar and click 'Generate Prediction'.")