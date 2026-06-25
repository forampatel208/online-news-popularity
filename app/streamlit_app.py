"""
Beat The Model — Main Entry Point
Landing page / hero for the ML portfolio project.
"""

import streamlit as st

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Beat The Model | ML Portfolio",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap');

/* ── Reset & base ── */
html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
}

/* ── Hide default Streamlit chrome ── */
#MainMenu { visibility: hidden; }
footer    { visibility: hidden; }
header    { visibility: hidden; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #0D1117;
    border-right: 1px solid #1E2A3A;
}
[data-testid="stSidebar"] .css-pkbazv { color: #7C8FA6 !important; }

/* ── Page background ── */
.stApp { background: #0A0E1A; }

/* ── Hero wrapper ── */
.hero {
    padding: 60px 20px 40px;
    text-align: center;
}

/* ── Badge ── */
.badge {
    display: inline-block;
    background: rgba(0, 212, 255, 0.12);
    border: 1px solid rgba(0, 212, 255, 0.35);
    color: #00D4FF;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 6px 16px;
    border-radius: 20px;
    margin-bottom: 28px;
}

/* ── Hero headline ── */
.hero-title {
    font-size: clamp(42px, 7vw, 88px);
    font-weight: 700;
    line-height: 1.05;
    color: #F0F4FF;
    letter-spacing: -2px;
    margin-bottom: 8px;
}
.hero-title .accent {
    color: #00D4FF;
}
.hero-subtitle {
    font-size: clamp(15px, 2vw, 19px);
    color: #7C8FA6;
    font-weight: 400;
    max-width: 560px;
    margin: 0 auto 40px;
    line-height: 1.6;
}

/* ── Stat cards ── */
.stat-row {
    display: flex;
    justify-content: center;
    gap: 16px;
    flex-wrap: wrap;
    margin-bottom: 48px;
}
.stat-card {
    background: #0D1117;
    border: 1px solid #1E2A3A;
    border-radius: 14px;
    padding: 22px 32px;
    min-width: 160px;
    text-align: center;
    transition: border-color 0.2s;
}
.stat-card:hover { border-color: rgba(0, 212, 255, 0.4); }
.stat-number {
    font-family: 'JetBrains Mono', monospace;
    font-size: 32px;
    font-weight: 600;
    color: #00D4FF;
    line-height: 1;
    margin-bottom: 6px;
}
.stat-label {
    font-size: 12px;
    color: #7C8FA6;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: 500;
}

/* ── VS benchmark bar ── */
.benchmark-wrap {
    max-width: 540px;
    margin: 0 auto 48px;
    background: #0D1117;
    border: 1px solid #1E2A3A;
    border-radius: 16px;
    padding: 24px 28px;
}
.benchmark-title {
    font-size: 12px;
    color: #7C8FA6;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 16px;
    font-weight: 600;
}
.bar-track {
    background: #1A2235;
    border-radius: 6px;
    height: 10px;
    position: relative;
    margin-bottom: 10px;
}
.bar-fill-bench {
    position: absolute; left: 0; top: 0;
    height: 10px; border-radius: 6px;
    background: #2A3A5A;
    width: 67%;
}
.bar-fill-model {
    position: absolute; left: 0; top: 0;
    height: 10px; border-radius: 6px;
    background: linear-gradient(90deg, #0099CC, #00D4FF);
    width: 67.32%;
    transition: width 1s ease;
}
.bar-labels {
    display: flex; justify-content: space-between;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px; color: #7C8FA6;
}
.bar-labels .model-score { color: #00D4FF; font-weight: 600; }

/* ── CTA button ── */
.cta-wrapper { margin-bottom: 60px; }
.stButton > button {
    background: #00D4FF !important;
    color: #0A0E1A !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 700 !important;
    font-size: 16px !important;
    padding: 14px 40px !important;
    border-radius: 10px !important;
    border: none !important;
    cursor: pointer;
    transition: opacity 0.2s, transform 0.1s !important;
    letter-spacing: 0.3px;
}
.stButton > button:hover {
    opacity: 0.88 !important;
    transform: translateY(-1px) !important;
}

/* ── Feature cards ── */
.features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
    gap: 16px;
    max-width: 900px;
    margin: 0 auto 60px;
}
.feature-card {
    background: #0D1117;
    border: 1px solid #1E2A3A;
    border-radius: 14px;
    padding: 24px;
    text-align: left;
    cursor: pointer;
    transition: all 0.2s;
}
.feature-card:hover {
    border-color: rgba(0, 212, 255, 0.4);
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0, 212, 255, 0.1);
}
.feature-icon {
    font-size: 28px; margin-bottom: 12px;
}
.feature-heading {
    color: #E8EFF8;
    font-size: 15px;
    font-weight: 600;
    margin-bottom: 6px;
}
.feature-desc {
    color: #7C8FA6;
    font-size: 13px;
    line-height: 1.55;
}

/* ── Divider ── */
.divider {
    border: none;
    border-top: 1px solid #1E2A3A;
    margin: 0 auto 40px;
    max-width: 800px;
}

/* ── Footer note ── */
.footer-note {
    text-align: center;
    color: #3A4A5A;
    font-size: 12px;
    padding-bottom: 40px;
}
.footer-note a { color: #00D4FF; text-decoration: none; }

/* ── Hide extra buttons in card columns ── */
.feature-card-button { display: none; }
</style>

<script>
// Make feature cards clickable
document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.feature-card');
    cards.forEach((card, index) => {
        card.addEventListener('click', function() {
            const buttons = document.querySelectorAll('button[data-testid="stButton"]');
            if (buttons[index]) {
                buttons[index].click();
            }
        });
    });
});
</script>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="badge">🎯 ML Portfolio Project</div>
  <div class="hero-title">Beat The<br><span class="accent">Model.</span></div>
  <div class="hero-subtitle">
    Can you out-predict a trained XGBoost model? 
    Read real news articles and guess if they went viral — 
    then see how your intuition stacks up against machine learning.
  </div>
</div>
""", unsafe_allow_html=True)

# ── Stats row ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="stat-row">
  <div class="stat-card">
    <div class="stat-number">39,797</div>
    <div class="stat-label">Articles</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">67.32%</div>
    <div class="stat-label">Model Accuracy</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">61</div>
    <div class="stat-label">Features Used</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">10</div>
    <div class="stat-label">Rounds / Game</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Benchmark comparison ──────────────────────────────────────────────────────
st.markdown("""
<div class="benchmark-wrap">
  <div class="benchmark-title">Model vs Benchmark Accuracy</div>
  <div style="margin-bottom:14px;">
    <div style="font-size:12px; color:#7C8FA6; margin-bottom:6px;">Benchmark (majority class)</div>
    <div class="bar-track"><div class="bar-fill-bench"></div></div>
    <div class="bar-labels"><span>0%</span><span>67.00%</span></div>
  </div>
  <div>
    <div style="font-size:12px; color:#00D4FF; font-weight:600; margin-bottom:6px;">XGBoost Model</div>
    <div class="bar-track"><div class="bar-fill-model"></div></div>
    <div class="bar-labels"><span>0%</span><span class="model-score">67.32% ▲ +0.32pp</span></div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── CTA ───────────────────────────────────────────────────────────────────────
col_l, col_c, col_r = st.columns([2, 1, 2])
with col_c:
    if st.button("🎮  Start Challenge", use_container_width=True):
        st.switch_page("pages/2_Beat_The_Model.py")

st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

# ── Clickable Feature cards ───────────────────────────────────────────────────
st.markdown("<div class='features'>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4, gap="small")

with col1:
    st.markdown("""
    <div class="feature-card" style="display: block; padding: 24px; height: 100%; box-sizing: border-box;">
      <div class="feature-icon">📰</div>
      <div class="feature-heading">Project Overview</div>
      <div class="feature-desc">Explore the dataset, model, and project architecture. Understand how the model works.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("View", key="btn_overview", use_container_width=True):
        st.switch_page("pages/1_Project_Overview.py")

with col2:
    st.markdown("""
    <div class="feature-card" style="display: block; padding: 24px; height: 100%; box-sizing: border-box;">
      <div class="feature-icon">🎮</div>
      <div class="feature-heading">Play Game</div>
      <div class="feature-desc">Test your intuition! Read articles and predict if they went viral. Beat the model!</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Play", key="btn_play", use_container_width=True):
        st.switch_page("pages/2_Beat_The_Model.py")

with col3:
    st.markdown("""
    <div class="feature-card" style="display: block; padding: 24px; height: 100%; box-sizing: border-box;">
      <div class="feature-icon">🔍</div>
      <div class="feature-heading">Model Insights</div>
      <div class="feature-desc">Dive deep into feature importance, confusion matrix, and model performance metrics.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Explore", key="btn_insights", use_container_width=True):
        st.switch_page("pages/3_Model_Insights.py")

with col4:
    st.markdown("""
    <div class="feature-card" style="display: block; padding: 24px; height: 100%; box-sizing: border-box;">
      <div class="feature-icon">📊</div>
      <div class="feature-heading">Dataset Explorer</div>
      <div class="feature-desc">Analyze the raw data. Explore distributions, correlations, and news channel insights.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Analyze", key="btn_dataset", use_container_width=True):
        st.switch_page("pages/1_Project_Overview.py")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Tech stack note ───────────────────────────────────────────────────────────
st.markdown("""
<div class="footer-note">
  Built with Python · XGBoost · Streamlit · Plotly &nbsp;|&nbsp; 
  Dataset: <a href="https://archive.ics.uci.edu/ml/datasets/online+news+popularity" target="_blank">
  UCI Online News Popularity</a>
</div>
""", unsafe_allow_html=True)