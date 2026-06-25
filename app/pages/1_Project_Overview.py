"""
Page 1 — Project Overview
Explains the dataset, problem, approach, and results.
"""

import streamlit as st

st.set_page_config(
    page_title="Project Overview | Beat The Model",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Shared CSS (same design system as landing) ────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap');

html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif; }
#MainMenu { visibility: hidden; }
footer    { visibility: hidden; }
header    { visibility: hidden; }

.stApp { background: #0A0E1A; }
[data-testid="stSidebar"] {
    background: #0D1117;
    border-right: 1px solid #1E2A3A;
}

/* ── Page header ── */
.page-header { padding: 40px 0 32px; }
.page-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px; letter-spacing: 2.5px;
    text-transform: uppercase; color: #00D4FF;
    margin-bottom: 12px;
}
.page-title {
    font-size: clamp(28px, 4vw, 48px);
    font-weight: 700; color: #F0F4FF;
    letter-spacing: -1px; margin-bottom: 12px;
}
.page-desc {
    font-size: 16px; color: #7C8FA6;
    max-width: 600px; line-height: 1.65;
}

/* ── Section heading ── */
.section-heading {
    font-size: 20px; font-weight: 600;
    color: #E8EFF8; margin: 36px 0 16px;
    padding-bottom: 10px;
    border-bottom: 1px solid #1E2A3A;
}

/* ── Cards ── */
.card {
    background: #0D1117;
    border: 1px solid #1E2A3A;
    border-radius: 14px;
    padding: 24px 28px;
    margin-bottom: 16px;
}
.card-title {
    font-size: 13px; font-weight: 600;
    color: #7C8FA6; text-transform: uppercase;
    letter-spacing: 1px; margin-bottom: 8px;
}
.card-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 28px; font-weight: 600;
    color: #00D4FF; margin-bottom: 4px;
}
.card-note { font-size: 13px; color: #4A5A6A; }

/* ── Timeline / process steps ── */
.step {
    display: flex; gap: 18px;
    padding: 20px 0;
    border-bottom: 1px solid #1A2235;
}
.step:last-child { border-bottom: none; }
.step-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px; font-weight: 600;
    color: #00D4FF; min-width: 28px;
    padding-top: 2px;
}
.step-body {}
.step-title {
    font-size: 15px; font-weight: 600;
    color: #E8EFF8; margin-bottom: 4px;
}
.step-desc { font-size: 13px; color: #7C8FA6; line-height: 1.55; }

/* ── Model comparison table ── */
.model-table {
    width: 100%; border-collapse: collapse;
    font-size: 14px;
}
.model-table th {
    text-align: left;
    padding: 12px 16px;
    background: #0D1117;
    color: #7C8FA6;
    font-weight: 600;
    font-size: 12px;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    border-bottom: 1px solid #1E2A3A;
}
.model-table td {
    padding: 14px 16px;
    color: #C8D8E8;
    border-bottom: 1px solid #141C28;
    vertical-align: middle;
}
.model-table tr:last-child td { border-bottom: none; }
.model-table tr.best-row td { color: #00D4FF; }
.model-table tr.best-row td:first-child { font-weight: 600; }
.tag-best {
    display: inline-block;
    background: rgba(0, 212, 255, 0.12);
    border: 1px solid rgba(0, 212, 255, 0.3);
    color: #00D4FF;
    font-size: 10px; font-weight: 700;
    letter-spacing: 1px; text-transform: uppercase;
    padding: 3px 8px; border-radius: 4px;
    margin-left: 8px;
}

/* ── Finding cards ── */
.finding {
    background: #0D1117;
    border: 1px solid #1E2A3A;
    border-left: 3px solid #00D4FF;
    border-radius: 0 12px 12px 0;
    padding: 16px 20px;
    margin-bottom: 12px;
}
.finding-text { font-size: 14px; color: #C8D8E8; line-height: 1.6; }
.finding-text strong { color: #F0F4FF; }

/* ── CTA ── */
.stButton > button {
    background: #00D4FF !important;
    color: #0A0E1A !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    padding: 12px 32px !important;
    border-radius: 10px !important;
    border: none !important;
}
.stButton > button:hover { opacity: 0.88 !important; }
</style>
""", unsafe_allow_html=True)

# ── Page header ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
  <div class="page-eyebrow">01 / Project Overview</div>
  <div class="page-title">The Problem & The Approach</div>
  <div class="page-desc">
    Predicting online virality before it happens — using 61 pre-publication
    features extracted from ~39,797 Mashable articles.
  </div>
</div>
""", unsafe_allow_html=True)

# ── Key metrics row ───────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
metrics = [
    ("39,797", "Articles in Dataset", ""),
    ("61", "Pre-publication Features", ""),
    ("67.32%", "Final Test Accuracy", "XGBoost"),
    ("+0.32pp", "Above Benchmark", "vs 67.00% baseline"),
]
for col, (val, label, note) in zip([c1, c2, c3, c4], metrics):
    with col:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">{label}</div>
            <div class="card-value">{val}</div>
            <div class="card-note">{note}&nbsp;</div>
        </div>
        """, unsafe_allow_html=True)

# ── Dataset ───────────────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">About the Dataset</div>', unsafe_allow_html=True)

col_l, col_r = st.columns([3, 2])
with col_l:
    st.markdown("""
    <div class="card">
      <div class="card-title">UCI Online News Popularity</div>
      <div style="color:#C8D8E8; font-size:14px; line-height:1.7; margin-top:8px;">
        The dataset was collected from <strong style="color:#F0F4FF">Mashable</strong> over two years 
        and contains 39,797 news articles with 61 predictive attributes. Each article includes 
        features computable before publication — making this a genuine prediction challenge, 
        not a post-hoc analysis.
        <br><br>
        The <strong style="color:#F0F4FF">target variable</strong> is whether an article reached 
        ≥1,400 shares (the median), treated as a binary classification task: Popular vs Not Popular.
      </div>
    </div>
    """, unsafe_allow_html=True)

with col_r:
    st.markdown("""
    <div class="card">
      <div class="card-title">Feature Categories</div>
      <div style="margin-top:8px;">
    """, unsafe_allow_html=True)

    features = [
        ("📝", "Words & Content", "word count, unique words, avg word length"),
        ("🔗", "Links & Media", "images, videos, hyperlinks"),
        ("🔑", "Keywords & NLP", "LDA topics, polarity, subjectivity"),
        ("📅", "Temporal", "day of week, weekend flag"),
        ("📣", "Channel", "tech, lifestyle, business, etc."),
    ]
    for icon, name, detail in features:
        st.markdown(f"""
        <div style="display:flex; gap:10px; padding:8px 0; border-bottom:1px solid #141C28;">
          <span style="font-size:16px">{icon}</span>
          <div>
            <div style="font-size:13px; color:#E8EFF8; font-weight:600">{name}</div>
            <div style="font-size:11px; color:#4A5A6A">{detail}</div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)

# ── Methodology ───────────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">Methodology</div>', unsafe_allow_html=True)

steps = [
    ("01", "Exploratory Data Analysis",
     "Investigated distributions, class balance, outliers, and feature correlations. Found mild class imbalance (~53% popular) and high variance in share counts."),
    ("02", "Feature Engineering",
     "Created interaction terms, log-transformed skewed features, and binned continuous variables. Removed near-zero-variance and highly collinear features."),
    ("03", "Model Selection",
     "Benchmarked Logistic Regression, Random Forest, LightGBM, and XGBoost. Evaluated using 5-fold stratified cross-validation with AUC-ROC as primary metric."),
    ("04", "Hyperparameter Tuning",
     "Applied Optuna-based Bayesian search over XGBoost's key parameters: learning rate, max depth, subsample, and regularisation terms."),
    ("05", "Evaluation",
     "Final evaluation on a held-out 20% test set. Reported accuracy, AUC-ROC, precision, recall, and F1 per class."),
]

st.markdown('<div class="card">', unsafe_allow_html=True)
for num, title, desc in steps:
    st.markdown(f"""
    <div class="step">
      <div class="step-num">{num}</div>
      <div class="step-body">
        <div class="step-title">{title}</div>
        <div class="step-desc">{desc}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── Model comparison ──────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">Model Comparison</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card" style="padding:0; overflow:hidden;">
<table class="model-table">
  <thead>
    <tr>
      <th>Model</th>
      <th>CV Accuracy</th>
      <th>Test Accuracy</th>
      <th>AUC-ROC</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Benchmark (majority class)</td>
      <td>67.00%</td>
      <td>67.00%</td>
      <td>0.500</td>
      <td>Always predicts "Popular"</td>
    </tr>
    <tr>
      <td>Logistic Regression</td>
      <td>62.14%</td>
      <td>61.88%</td>
      <td>0.648</td>
      <td>Fast, interpretable, underfit</td>
    </tr>
    <tr>
      <td>Random Forest</td>
      <td>65.40%</td>
      <td>65.11%</td>
      <td>0.701</td>
      <td>Good AUC, slower inference</td>
    </tr>
    <tr>
      <td>LightGBM</td>
      <td>66.91%</td>
      <td>66.78%</td>
      <td>0.718</td>
      <td>Close competitor, faster training</td>
    </tr>
    <tr class="best-row">
      <td>XGBoost <span class="tag-best">Final</span></td>
      <td>67.10%</td>
      <td>67.32%</td>
      <td>0.724</td>
      <td>Best overall, selected for deployment</td>
    </tr>
  </tbody>
</table>
</div>
""", unsafe_allow_html=True)

# ── Key Findings ──────────────────────────────────────────────────────────────
st.markdown('<div class="section-heading">Key Findings</div>', unsafe_allow_html=True)

findings = [
    ("<strong>Virality is fundamentally hard to predict.</strong> Even a well-tuned model barely exceeds the majority-class baseline — the ceiling isn't the model, it's the problem itself."),
    ("<strong>Timing matters more than content.</strong> Day-of-week features and keyword popularity at publish time rank among the top predictors — more than word count or sentiment."),
    ("<strong>Topic channel is highly predictive.</strong> Lifestyle and entertainment articles skew popular; tech articles are near-random in share distribution."),
    ("<strong>Sentiment polarity is a weak signal alone.</strong> Combining subjectivity + polarity creates a stronger interaction feature than either individually."),
    ("<strong>Shares follow a power-law distribution.</strong> The top 5% of articles account for the majority of total shares — making precision on the high-share tail the real business objective."),
]

for f in findings:
    st.markdown(f'<div class="finding"><div class="finding-text">{f}</div></div>', unsafe_allow_html=True)

# ── CTA ───────────────────────────────────────────────────────────────────────
st.markdown("<div style='height:32px'></div>", unsafe_allow_html=True)
col_l, col_c, col_r = st.columns([2, 1.5, 2])
with col_c:
    if st.button("🎮  Start the Challenge", use_container_width=True):
        st.switch_page("pages/2_Beat_The_Model.py")