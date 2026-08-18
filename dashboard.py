import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- PAGE SETUP ---
st.set_page_config(
    page_title="AutoKube | K8's Whisperer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ADVANCED MODERN DARK THEME CSS ---
st.markdown("""
    <style>
    /* Global Base */
    .stApp {
        background: radial-gradient(circle at 50% 0%, #0d1527 0%, #020617 70%);
        color: #f8fafc;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* Centered Header Section */
    .header-container {
        text-align: center;
        padding: 10px 0 20px 0;
    }
    .main-title {
        font-size: 2.3rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        background: linear-gradient(135deg, #ffffff 30%, #94a3b8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 4px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
    }
    .subtitle-banner {
        color: #64748b;
        font-size: 0.95rem;
        font-weight: 500;
        letter-spacing: 0.04em;
        text-transform: uppercase;
        margin-bottom: 18px;
    }
    
    /* Top Badges Row */
    .badge-bar {
        display: flex;
        justify-content: center;
        gap: 12px;
        flex-wrap: wrap;
        margin-bottom: 24px;
    }
    .status-pill {
        display: inline-flex;
        align-items: center;
        gap: 7px;
        padding: 6px 14px;
        border-radius: 9999px;
        font-size: 0.78rem;
        font-weight: 500;
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(51, 65, 85, 0.6);
        backdrop-filter: blur(10px);
        color: #cbd5e1;
    }
    .dot-green { width: 7px; height: 7px; background: #10b981; border-radius: 50%; box-shadow: 0 0 8px #10b981; }
    .dot-blue { width: 7px; height: 7px; background: #38bdf8; border-radius: 50%; box-shadow: 0 0 8px #38bdf8; }
    .dot-purple { width: 7px; height: 7px; background: #a855f7; border-radius: 50%; box-shadow: 0 0 8px #a855f7; }

    /* Section Headers */
    .section-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #e2e8f0;
        margin-top: 18px;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 8px;
        letter-spacing: -0.01em;
    }

    /* Cards & Containers */
    .panel-card {
        background: #090e1a;
        border: 1px solid #1e293b;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.4);
    }
    .hitl-alert {
        background: rgba(245, 158, 11, 0.08);
        border: 1px solid rgba(245, 158, 11, 0.3);
        border-left: 4px solid #f59e0b;
        padding: 12px 16px;
        border-radius: 8px;
        margin-bottom: 14px;
        color: #fde68a;
        font-size: 0.88rem;
    }

    /* Buttons override for cleaner sleek look */
    div.stButton > button {
        border-radius: 8px;
        font-weight: 600;
        font-size: 0.82rem;
        border: 1px solid #334155;
        background-color: #0f172a;
        color: #94a3b8;
        transition: all 0.2s ease;
    }
    div.stButton > button:hover {
        border-color: #64748b;
        color: #f8fafc;
        background-color: #1e293b;
    }
    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #059669 0%, #10b981 100%) !important;
        color: #ffffff !important;
        border: none !important;
        box-shadow: 0 0 16px rgba(16, 185, 129, 0.35) !important;
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        border-bottom: 1px solid #1e293b;
        padding-bottom: 4px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border-radius: 6px;
        color: #64748b;
        font-weight: 500;
        font-size: 0.88rem;
        padding: 8px 16px;
    }
    .stTabs [aria-selected="true"] {
        color: #38bdf8 !important;
        background: rgba(56, 189, 248, 0.08) !important;
        border-bottom: 2px solid #38bdf8 !important;
    }

    /* Metrics */
    div[data-testid="metric-container"] {
        background: #090e1a;
        border: 1px solid #1e293b;
        border-radius: 10px;
        padding: 14px 18px;
    }
    [data-testid="stMetricValue"] {
        color: #38bdf8 !important;
        font-family: -apple-system, sans-serif;
        font-weight: 700;
    }
    [data-testid="stMetricLabel"] {
        color: #64748b !important;
        font-size: 0.78rem !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    </style>
""", unsafe_allow_html=True)

# --- CENTERED HEADER & BADGES ---
st.markdown("""
    <div class="header-container">
        <div class="main-title">⚡ AutoKube</div>
        <div class="subtitle-banner">K8's Whisperer : The Air Gapped Autonomous SRE Agent</div>
        <div class="badge-bar">
            <div class="status-pill"><span class="dot-green"></span> 100% Offline (Ollama LLaMA 3.2 3B)</div>
            <div class="status-pill"><span class="dot-blue"></span> Minikube Local (RBAC Enforced)</div>
            <div class="status-pill"><span class="dot-purple"></span> Stellar Testnet Synced</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- TABS ---
tab_ops, tab_audit, tab_health = st.tabs([
    "Operations Dashboard", 
    "Incident Audit Reports", 
    "Cluster Damage & Health"
])

# ==============================================================================
# VIEW 1: OPERATIONS DASHBOARD
# ==============================================================================
with tab_ops:
    st.markdown('<div class="section-title">Autonomous Execution Loop</div>', unsafe_allow_html=True)
    
    stages = ["Observe", "Detect", "Diagnose", "Plan", "Execute", "Explain"]
    stage_cols = st.columns(6)
    for i, stage in enumerate(stages):
        is_active = (stage == "Diagnose")
        stage_cols[i].button(
            f"● {stage}" if is_active else stage,
            key=f"stg_{stage}",
            type="primary" if is_active else "secondary",
            use_container_width=True
        )

    st.write("")

    st.markdown('<div class="section-title">Pending Approvals (Human-in-the-Loop)</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="panel-card">
            <div class="hitl-alert">
                <strong>Action Required:</strong> Resource Limit Patch staged for <code>payment-processor</code> (Namespace: <code>finance</code>)
            </div>
            <div style="font-size: 0.85rem; color: #94a3b8; margin-bottom: 8px;">
                <strong>Diagnosis:</strong> OOMKilled (Exit code 137). Ingestion burst exceeded 1Gi memory ceiling.
            </div>
        </div>
    """, unsafe_allow_html=True)

    with st.expander("Inspect Proposed YAML Patch (limits.yaml)", expanded=True):
        st.code("""spec:
  template:
    spec:
      containers:
      - name: payment-processor
        resources:
          limits:
            memory: 2Gi      # Auto-scaled from 1Gi
            cpu: 1000m
          requests:
            memory: 1Gi      # Auto-scaled from 512Mi
            cpu: 500m""", language="yaml")
        
        btn_col1, btn_col2, _ = st.columns([1.5, 1.2, 5])
        if btn_col1.button("Approve & Execute Patch", type="primary", use_container_width=True):
            st.toast("Patch successfully committed via RBAC!", icon="✅")
        if btn_col2.button("Reject Action", use_container_width=True):
            st.toast("Action rejected by operator.", icon="❌")

    st.write("")

    st.markdown('<div class="section-title">Live Pod & Workload Anomaly Grid</div>', unsafe_allow_html=True)
    
    mock_pods = pd.DataFrame([
        {"Pod Instance": "auth-service-7x89q", "Namespace": "default", "Status": "🔴 CrashLoopBackOff", "Restarts": 14, "CPU": "45m", "Memory": "90Mi"},
        {"Pod Instance": "payment-processor-9k2x", "Namespace": "finance", "Status": "🔴 OOMKilled", "Restarts": 6, "CPU": "920m", "Memory": "2048Mi"},
        {"Pod Instance": "api-gateway-01a", "Namespace": "default", "Status": "🟢 Running", "Restarts": 0, "CPU": "110m", "Memory": "140Mi"},
        {"Pod Instance": "redis-master-0", "Namespace": "cache", "Status": "🟢 Running", "Restarts": 0, "CPU": "310m", "Memory": "256Mi"},
        {"Pod Instance": "ingress-nginx-44a", "Namespace": "kube-system", "Status": "🟢 Running", "Restarts": 1, "CPU": "80m", "Memory": "110Mi"}
    ])
    st.dataframe(mock_pods, use_container_width=True, hide_index=True)

# ==============================================================================
# VIEW 2: INCIDENT AUDIT REPORTS
# ==============================================================================
with tab_audit:
    st.markdown('<div class="section-title">Cryptographic Incident Audit Log</div>', unsafe_allow_html=True)
    
    s1, s2 = st.columns([3, 1])
    with s1:
        st.text_input("Filter logs by keyword or rationale", placeholder="Search pod, error, or hash...", label_visibility="collapsed")
    with s2:
        st.selectbox("Severity", ["All Severities", "Critical", "Warning"], label_visibility="collapsed")

    st.markdown("""
    <div class="panel-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
            <span style="font-family: monospace; font-size: 0.9rem; font-weight: bold; color: #10b981;">INC-1029</span>
            <span style="color: #64748b; font-size: 0.8rem;">2026-08-18 08:02:11 UTC</span>
            <span style="background: rgba(244, 63, 94, 0.15); color: #f43f5e; border: 1px solid rgba(244, 63, 94, 0.3); padding: 2px 8px; border-radius: 4px; font-size: 0.72rem; font-weight: bold;">CRITICAL</span>
        </div>
        <div style="font-size: 0.84rem; margin-bottom: 6px;">
            <strong>Target:</strong> <code>auth-service-7x89q</code> (Namespace: default)
        </div>
        <div style="background: #020617; border: 1px solid #1e293b; padding: 8px 12px; border-radius: 6px; font-family: monospace; color: #f43f5e; font-size: 0.8rem; margin-bottom: 8px;">
            [STDERR]: dial tcp 10.96.12.44:5432: i/o timeout - connection refused
        </div>
        <div style="font-size: 0.84rem; color: #cbd5e1; margin-bottom: 6px;">
            <span style="color: #10b981; font-weight: 600;">LLM Diagnosis:</span> PostgreSQL service endpoint unreachable due to missing NetworkPolicy egress rule. Created autonomous egress allowlist.
        </div>
        <div style="font-family: monospace; font-size: 0.74rem; color: #38bdf8;">
            ⛓️ Stellar TX: a4f8d97e2c056b3e1c5908f51a42bc7190ea4d8c6b73918f673e4a908bcfe912
        </div>
    </div>

    <div class="panel-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
            <span style="font-family: monospace; font-size: 0.9rem; font-weight: bold; color: #10b981;">INC-1028</span>
            <span style="color: #64748b; font-size: 0.8rem;">2026-08-18 07:44:05 UTC</span>
            <span style="background: rgba(244, 63, 94, 0.15); color: #f43f5e; border: 1px solid rgba(244, 63, 94, 0.3); padding: 2px 8px; border-radius: 4px; font-size: 0.72rem; font-weight: bold;">CRITICAL</span>
        </div>
        <div style="font-size: 0.84rem; margin-bottom: 6px;">
            <strong>Target:</strong> <code>payment-processor-9k2x</code> (Namespace: finance)
        </div>
        <div style="background: #020617; border: 1px solid #1e293b; padding: 8px 12px; border-radius: 6px; font-family: monospace; color: #f43f5e; font-size: 0.8rem; margin-bottom: 8px;">
            [STDERR]: fatal error: runtime: out of memory (allocation size 134217728) - Exit Code 137
        </div>
        <div style="font-size: 0.84rem; color: #cbd5e1; margin-bottom: 6px;">
            <span style="color: #10b981; font-weight: 600;">LLM Diagnosis:</span> Batch queue processing spike exceeded allocation limits. Staged YAML memory ceiling expansion.
        </div>
        <div style="font-family: monospace; font-size: 0.74rem; color: #38bdf8;">
            ⛓️ Stellar TX: 7b63f281e01bc4987f1a309ec98f165a2d040854497e289b43c6802319efae61
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# VIEW 3: CLUSTER DAMAGE & HEALTH
# ==============================================================================
with tab_health:
    st.markdown('<div class="section-title">Cluster Health & Velocity KPIs</div>', unsafe_allow_html=True)
    
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Health Score", "87%", delta="Nominal")
    k2.metric("Incidents Prevented", "142", delta="+12 today")
    k3.metric("MTTR", "38s", delta="-18s vs baseline")
    k4.metric("Unresolved Criticals", "1", delta="Awaiting Approval", delta_color="inverse")

    st.write("")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="section-title">Crash Distribution by Namespace</div>', unsafe_allow_html=True)
        fig_bar = go.Figure(go.Bar(
            x=["finance", "default", "monitoring", "kube-system", "cache"],
            y=[14, 8, 2, 1, 0],
            marker_color=["#f43f5e", "#f59e0b", "#10b981", "#10b981", "#10b981"]
        ))
        fig_bar.update_layout(
            paper_bgcolor="#090e1a",
            plot_bgcolor="#090e1a",
            font=dict(color="#94a3b8", size=11),
            height=260,
            margin=dict(l=20, r=20, t=10, b=20),
            yaxis=dict(gridcolor="#1e293b")
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    with c2:
        st.markdown('<div class="section-title">Resource Stress Gauge</div>', unsafe_allow_html=True)
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=78,
            title={'text': "Memory Pressure (%)", 'font': {'color': '#94a3b8', 'size': 13}},
            gauge={
                'axis': {'range': [0, 100], 'tickcolor': "#475569"},
                'bar': {'color': "#f43f5e"},
                'steps': [
                    {'range': [0, 60], 'color': "#0f172a"},
                    {'range': [60, 85], 'color': "#1e293b"}
                ],
                'threshold': {'line': {'color': "#f43f5e", 'width': 3}, 'thickness': 0.75, 'value': 85}
            }
        ))
        fig_gauge.update_layout(
            paper_bgcolor="#090e1a",
            font=dict(color="#f8fafc"),
            height=260,
            margin=dict(l=30, r=30, t=20, b=20)
        )
        st.plotly_chart(fig_gauge, use_container_width=True)