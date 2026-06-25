"""
Page 2 — Beat The Model
The core interactive challenge: user vs XGBoost, 10 rounds.
"""

import streamlit as st
import pandas as pd
import numpy as np
import random
import os

st.set_page_config(
    page_title="Beat The Model | Challenge",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Shared CSS ────────────────────────────────────────────────────────────────
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

/* ── Progress bar override ── */
.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #0099CC, #00D4FF) !important;
}
.stProgress > div > div { background: #1A2235 !important; }

/* ── Scoreboard header ── */
.score-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #0D1117;
    border: 1px solid #1E2A3A;
    border-radius: 14px;
    padding: 20px 28px;
    margin-bottom: 28px;
}
.score-side { text-align: center; flex: 1; }
.score-vs {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px; color: #3A4A5A;
    font-weight: 600; padding: 0 24px;
}
.score-label {
    font-size: 11px; color: #7C8FA6;
    text-transform: uppercase; letter-spacing: 1.5px;
    margin-bottom: 6px; font-weight: 600;
}
.score-val {
    font-family: 'JetBrains Mono', monospace;
    font-size: 36px; font-weight: 600;
    line-height: 1;
}
.score-val.user  { color: #00D4FF; }
.score-val.model { color: #7C8FA6; }
.score-sub {
    font-size: 12px; color: #3A4A5A; margin-top: 4px;
}

/* ── Article card ── */
.article-card {
    background: #0D1117;
    border: 1px solid #1E2A3A;
    border-radius: 16px;
    padding: 32px 36px;
    margin-bottom: 24px;
}
.round-badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px; letter-spacing: 2px;
    text-transform: uppercase; color: #00D4FF;
    margin-bottom: 16px;
}
.article-title {
    font-size: clamp(20px, 3vw, 28px);
    font-weight: 700; color: #F0F4FF;
    line-height: 1.3; margin-bottom: 16px;
    letter-spacing: -0.5px;
}
.article-meta {
    display: flex; gap: 20px; flex-wrap: wrap;
    margin-bottom: 20px;
}
.meta-item {
    font-size: 12px; color: #4A5A6A;
    background: #141C28;
    padding: 4px 12px; border-radius: 6px;
}
.article-url-wrap {
    background: #141C28;
    border: 1px solid #1E2A3A;
    border-radius: 10px;
    padding: 12px 16px;
    margin-bottom: 8px;
}
.article-url-label {
    font-size: 11px; color: #3A4A5A;
    text-transform: uppercase; letter-spacing: 1px;
    margin-bottom: 4px;
}
.article-url-link {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px; color: #00D4FF;
    word-break: break-all;
    text-decoration: none;
}
.article-url-link:hover { text-decoration: underline; }

/* ── Question ── */
.question-text {
    font-size: 20px; font-weight: 600;
    color: #E8EFF8; text-align: center;
    margin: 28px 0 20px;
}

/* ── Vote buttons ── */
div[data-testid="column"] .stButton > button {
    width: 100%;
    padding: 18px 20px !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    border-radius: 12px !important;
    border: 2px solid transparent !important;
    transition: all 0.15s ease !important;
}
.btn-popular .stButton > button {
    background: rgba(0, 212, 255, 0.12) !important;
    border-color: rgba(0, 212, 255, 0.4) !important;
    color: #00D4FF !important;
}
.btn-popular .stButton > button:hover {
    background: rgba(0, 212, 255, 0.22) !important;
    border-color: #00D4FF !important;
}
.btn-notpopular .stButton > button {
    background: rgba(255, 255, 255, 0.04) !important;
    border-color: #2A3A4A !important;
    color: #7C8FA6 !important;
}
.btn-notpopular .stButton > button:hover {
    background: rgba(255, 255, 255, 0.08) !important;
    border-color: #4A5A6A !important;
    color: #C8D8E8 !important;
}

/* ── Reveal battle card ── */
.battle-card {
    background: #0D1117;
    border: 1px solid #1E2A3A;
    border-radius: 16px;
    padding: 28px;
    margin-bottom: 20px;
}
.battle-title {
    font-size: 12px; color: #7C8FA6;
    text-transform: uppercase; letter-spacing: 1.5px;
    margin-bottom: 20px; font-weight: 600;
}
.battle-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    text-align: center;
}
.battle-col-head {
    font-size: 11px; color: #4A5A6A;
    text-transform: uppercase; letter-spacing: 1px;
    margin-bottom: 8px; font-weight: 600;
}
.battle-answer {
    font-size: 22px; font-weight: 700;
    padding: 14px 8px;
    border-radius: 10px;
    line-height: 1;
}
.answer-popular   { background: rgba(0,212,255,0.1); color:#00D4FF; border:1px solid rgba(0,212,255,0.3); }
.answer-notpop    { background: rgba(255,255,255,0.04); color:#7C8FA6; border:1px solid #1E2A3A; }
.answer-correct   { background: rgba(50,205,50,0.12); color:#50E070; border:1px solid rgba(50,205,50,0.3); }
.answer-wrong     { background: rgba(255,80,80,0.1); color:#FF6060; border:1px solid rgba(255,80,80,0.25); }

/* ── Share count reveal ── */
.share-reveal {
    text-align: center;
    padding: 16px;
    background: #141C28;
    border-radius: 10px;
    margin-bottom: 16px;
}
.share-reveal-label {
    font-size: 12px; color: #4A5A6A;
    text-transform: uppercase; letter-spacing: 1px; margin-bottom: 6px;
}
.share-reveal-val {
    font-family: 'JetBrains Mono', monospace;
    font-size: 28px; font-weight: 600;
    color: #00D4FF;
}
.share-threshold {
    font-size: 12px; color: #4A5A6A; margin-top: 4px;
}

/* ── Round outcome banner ── */
.outcome-banner {
    text-align: center; padding: 14px 20px;
    border-radius: 10px; margin-bottom: 20px;
    font-weight: 700; font-size: 16px;
}
.outcome-win  { background: rgba(50,205,50,0.12); color:#50E070; border:1px solid rgba(50,205,50,0.25); }
.outcome-lose { background: rgba(255,80,80,0.1);  color:#FF6060; border:1px solid rgba(255,80,80,0.2); }
.outcome-tie  { background: rgba(255,180,0,0.1);  color:#FFB800; border:1px solid rgba(255,180,0,0.2); }

/* ── Next / continue button ── */
.stButton > button {
    background: #00D4FF !important;
    color: #0A0E1A !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    padding: 13px 32px !important;
    border-radius: 10px !important;
    border: none !important;
}
.stButton > button:hover { opacity: 0.88 !important; }

/* ── Final results ── */
.final-hero {
    text-align: center; padding: 40px 20px;
}
.final-trophy { font-size: 64px; margin-bottom: 16px; }
.final-headline {
    font-size: 36px; font-weight: 700;
    color: #F0F4FF; letter-spacing: -1px;
    margin-bottom: 8px;
}
.final-sub { font-size: 16px; color: #7C8FA6; }
.final-score-big {
    font-family: 'JetBrains Mono', monospace;
    font-size: 72px; font-weight: 600;
    color: #00D4FF; line-height: 1;
}
.result-row {
    display: flex; justify-content: space-between;
    align-items: center;
    padding: 10px 0;
    border-bottom: 1px solid #141C28;
    font-size: 14px; color: #C8D8E8;
}
.result-row:last-child { border-bottom: none; }
.result-icon { font-size: 16px; }
</style>
""", unsafe_allow_html=True)

# ── Helpers ───────────────────────────────────────────────────────────────────

ROUNDS_PER_GAME = 10
POPULARITY_THRESHOLD = 1400  # Matches UCI dataset split

def load_articles() -> pd.DataFrame:
    """Load demo articles CSV. Falls back to synthetic data if file not found."""
    csv_path = os.path.join(os.path.dirname(__file__), "..", "demo_articles.csv")
    csv_path = os.path.normpath(csv_path)
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
    else:
        # ── Synthetic fallback for demo purposes ──────────────────────────────
        # Replace with your actual demo_articles.csv for real predictions
        np.random.seed(42)
        rng = np.random.default_rng(99)
        titles = [
            "10 Productivity Hacks That Will Change How You Work Forever",
            "Scientists Discover New Species in Amazon Rainforest",
            "The Ultimate Guide to Home Brewing Your Own Beer",
            "Why Remote Work Is Here to Stay (And What That Means for Cities)",
            "5 Reasons Your Morning Routine Is Sabotaging Your Success",
            "Breakthrough in Battery Technology Could Power Electric Cars for 500 Miles",
            "How to Train Your Brain to Be More Creative",
            "The Dark Side of Social Media Algorithms Nobody Talks About",
            "25 Places You Must Visit Before You Die",
            "Why Most Diets Fail — And What Actually Works",
            "New Study Links Sleep Deprivation to Long-Term Memory Loss",
            "The Rise of AI in Healthcare: Promise and Peril",
            "How One Man Turned a $500 Investment Into $1 Million",
            "The Countries With the Happiest Workers in the World",
            "Inside the Secret World of Professional Gaming",
            "A Beginner's Guide to Investing in Index Funds",
            "Why Your Password Is Probably Already Compromised",
            "The Future of Food: Lab-Grown Meat Is Almost Here",
            "How Meditation Changed My Life (And the Science Behind It)",
            "The Most Common Mistakes First-Time Homebuyers Make",
        ]
        urls = [
            f"http://mashable.com/2013/{'01' if i<10 else '02'}/{'0'+str(i+1) if i<9 else str(i+1)}/article-{i+1}/"
            for i in range(len(titles))
        ]
        shares = np.abs(rng.lognormal(mean=6.5, sigma=1.5, size=len(titles))).astype(int) + 50
        channels = rng.choice(
            ["Tech", "Lifestyle", "Business", "Entertainment", "Health", "World"],
            size=len(titles)
        )
        model_preds = (rng.random(len(titles)) > 0.45).astype(int)
        df = pd.DataFrame({
            "title": titles,
            "url": urls,
            "shares": shares,
            "channel": channels,
            "model_prediction": model_preds,   # 1 = Popular, 0 = Not Popular
            "word_count": rng.integers(200, 2000, size=len(titles)),
            "num_images": rng.integers(0, 12, size=len(titles)),
        })

    # Ensure required columns exist with sensible defaults
    if "model_prediction" not in df.columns:
        # Derive from shares if no pre-computed prediction
        df["model_prediction"] = (df["shares"] >= POPULARITY_THRESHOLD).astype(int)
    if "title" not in df.columns:
        df["title"] = df.get("url", pd.Series(["Article"] * len(df))).str[-40:]

    df["actual"] = (df["shares"] >= POPULARITY_THRESHOLD).astype(int)
    return df


def init_session():
    """Initialise or reset all session state variables."""
    all_articles = load_articles()
    sampled = all_articles.sample(n=min(ROUNDS_PER_GAME, len(all_articles)),
                                  random_state=random.randint(0, 9999)).reset_index(drop=True)
    st.session_state.articles      = sampled
    st.session_state.round_index   = 0
    st.session_state.user_score    = 0
    st.session_state.model_score   = 0
    st.session_state.history       = []          # list of round result dicts
    st.session_state.phase         = "question"  # "question" | "reveal" | "final"
    st.session_state.user_answer   = None


def get_result_label(correct: bool) -> str:
    return "✅ Correct" if correct else "❌ Wrong"


# ── Initialise session on first load ─────────────────────────────────────────
if "round_index" not in st.session_state:
    init_session()

# ── Derived state ─────────────────────────────────────────────────────────────
total_rounds  = len(st.session_state.articles)
current_round = st.session_state.round_index  # 0-indexed
phase         = st.session_state.phase

# ── Scoreboard header (always visible) ───────────────────────────────────────
u_score = st.session_state.user_score
m_score = st.session_state.model_score
rounds_done = len(st.session_state.history)

st.markdown(f"""
<div class="score-header">
  <div class="score-side">
    <div class="score-label">You</div>
    <div class="score-val user">{u_score}</div>
    <div class="score-sub">{rounds_done} rounds played</div>
  </div>
  <div class="score-vs">VS</div>
  <div class="score-side">
    <div class="score-label">XGBoost Model</div>
    <div class="score-val model">{m_score}</div>
    <div class="score-sub">67.32% overall accuracy</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Progress bar ──────────────────────────────────────────────────────────────
if phase != "final":
    progress_val = rounds_done / total_rounds
    st.progress(progress_val)
    st.markdown(
        f"<div style='font-family:JetBrains Mono,monospace;font-size:12px;color:#4A5A6A;"
        f"text-align:right;margin-top:4px;margin-bottom:20px'>"
        f"Round {min(rounds_done + 1, total_rounds)} / {total_rounds}</div>",
        unsafe_allow_html=True
    )

# ══════════════════════════════════════════════════════════════════════════════
# PHASE: QUESTION
# ══════════════════════════════════════════════════════════════════════════════
if phase == "question" and current_round < total_rounds:
    article = st.session_state.articles.iloc[current_round]

    # Meta tags
    channel_tag = article.get("channel", "Article")
    word_count  = article.get("word_count", "—")
    images      = article.get("num_images", "—")

    st.markdown(f"""
    <div class="article-card">
      <div class="round-badge">🎮 Round {current_round + 1} of {total_rounds}</div>
      <div class="article-title">{article['title']}</div>
      <div class="article-meta">
        <span class="meta-item">📂 {channel_tag}</span>
        <span class="meta-item">📝 {word_count} words</span>
        <span class="meta-item">🖼️ {images} images</span>
      </div>
      <div class="article-url-wrap">
        <div class="article-url-label">Article URL</div>
        <a class="article-url-link" href="{article['url']}" target="_blank">{article['url']}</a>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="question-text">
        Did this article become popular? <span style="color:#4A5A6A;font-size:15px">(≥1,400 shares)</span>
    </div>
    """, unsafe_allow_html=True)

    col_l, spacer, col_r = st.columns([5, 1, 5])

    with col_l:
        st.markdown('<div class="btn-popular">', unsafe_allow_html=True)
        if st.button("🔥  Popular", key="btn_pop", use_container_width=True):
            st.session_state.user_answer = 1
            st.session_state.phase = "reveal"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with col_r:
        st.markdown('<div class="btn-notpopular">', unsafe_allow_html=True)
        if st.button("💤  Not Popular", key="btn_not", use_container_width=True):
            st.session_state.user_answer = 0
            st.session_state.phase = "reveal"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PHASE: REVEAL
# ══════════════════════════════════════════════════════════════════════════════
elif phase == "reveal" and current_round < total_rounds:
    article        = st.session_state.articles.iloc[current_round]
    user_pred      = st.session_state.user_answer
    model_pred     = int(article["model_prediction"])
    actual         = int(article["actual"])
    shares         = int(article["shares"])

    user_correct   = (user_pred  == actual)
    model_correct  = (model_pred == actual)

    # Update scores (only if not already recorded)
    if len(st.session_state.history) == current_round:
        if user_correct:
            st.session_state.user_score  += 1
        if model_correct:
            st.session_state.model_score += 1
        st.session_state.history.append({
            "round":         current_round + 1,
            "title":         article["title"],
            "user_pred":     user_pred,
            "model_pred":    model_pred,
            "actual":        actual,
            "shares":        shares,
            "user_correct":  user_correct,
            "model_correct": model_correct,
        })

    # ── Outcome banner ────────────────────────────────────────────────────────
    if user_correct and not model_correct:
        banner_cls, banner_txt = "outcome-win", "🏆 You beat the model this round!"
    elif model_correct and not user_correct:
        banner_cls, banner_txt = "outcome-lose", "🤖 Model wins this round."
    elif user_correct and model_correct:
        banner_cls, banner_txt = "outcome-tie", "🤝 Both correct — tie round."
    else:
        banner_cls, banner_txt = "outcome-lose", "😬 Both wrong this round."

    st.markdown(f'<div class="outcome-banner {banner_cls}">{banner_txt}</div>',
                unsafe_allow_html=True)

    # ── Share count ───────────────────────────────────────────────────────────
    pop_label = "🔥 Popular" if actual == 1 else "💤 Not Popular"
    pop_color = "#00D4FF" if actual == 1 else "#7C8FA6"
    st.markdown(f"""
    <div class="share-reveal">
      <div class="share-reveal-label">Actual Shares</div>
      <div class="share-reveal-val">{shares:,}</div>
      <div class="share-threshold" style="color:{pop_color}; font-weight:600;">{pop_label}</div>
      <div class="share-threshold">Threshold: 1,400 shares</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Battle card ───────────────────────────────────────────────────────────
    def pred_label(val): return "🔥 Popular" if val == 1 else "💤 Not Popular"
    def pred_css(val, correct):
        if correct: return "answer-correct"
        return "answer-wrong"

    user_css  = pred_css(user_pred, user_correct)
    model_css = pred_css(model_pred, model_correct)
    actual_css = "answer-popular" if actual == 1 else "answer-notpop"

    st.markdown(f"""
    <div class="battle-card">
      <div class="battle-title">Round Results</div>
      <div class="battle-grid">
        <div>
          <div class="battle-col-head">You</div>
          <div class="battle-answer {user_css}">{pred_label(user_pred)}</div>
        </div>
        <div>
          <div class="battle-col-head">Actual</div>
          <div class="battle-answer {actual_css}">{pred_label(actual)}</div>
        </div>
        <div>
          <div class="battle-col-head">XGBoost</div>
          <div class="battle-answer {model_css}">{pred_label(model_pred)}</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Article link again ────────────────────────────────────────────────────
    st.markdown(f"""
    <div style="text-align:center; margin-bottom:24px;">
      <a href="{article['url']}" target="_blank"
         style="font-family:'JetBrains Mono',monospace; font-size:12px; color:#4A5A6A;
                text-decoration:none;">
        🔗 Read the full article
      </a>
    </div>
    """, unsafe_allow_html=True)

    # ── Next button ───────────────────────────────────────────────────────────
    col_l, col_c, col_r = st.columns([2, 2, 2])
    with col_c:
        next_label = "Next Round →" if current_round < total_rounds - 1 else "See Final Results →"
        if st.button(next_label, use_container_width=True):
            st.session_state.round_index += 1
            st.session_state.phase = "question"
            st.session_state.user_answer = None
            if st.session_state.round_index >= total_rounds:
                st.session_state.phase = "final"
            st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
# PHASE: FINAL RESULTS
# ══════════════════════════════════════════════════════════════════════════════
elif phase == "final" or (phase == "question" and current_round >= total_rounds):
    st.session_state.phase = "final"

    u_final = st.session_state.user_score
    m_final = st.session_state.model_score

    # ── Trophy / headline ─────────────────────────────────────────────────────
    if u_final > m_final:
        trophy, headline = "🏆", "You Beat The Model!"
        sub = f"You scored {u_final}/{total_rounds} — the model only got {m_final}/{total_rounds}."
    elif u_final == m_final:
        trophy, headline = "🤝", "It's a Tie!"
        sub = f"Both you and the model scored {u_final}/{total_rounds}. Impressive."
    else:
        trophy, headline = "🤖", "Model Wins This Time"
        sub = f"You scored {u_final}/{total_rounds} — the model got {m_final}/{total_rounds}."

    user_pct  = round(u_final / total_rounds * 100, 1)
    model_pct = round(m_final / total_rounds * 100, 1)

    st.markdown(f"""
    <div class="final-hero">
      <div class="final-trophy">{trophy}</div>
      <div class="final-headline">{headline}</div>
      <div class="final-sub">{sub}</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Score comparison ──────────────────────────────────────────────────────
    col_l, col_r = st.columns(2)
    with col_l:
        st.markdown(f"""
        <div style="background:#0D1117;border:1px solid #1E2A3A;border-radius:14px;
                    padding:28px;text-align:center;">
          <div style="font-size:12px;color:#7C8FA6;text-transform:uppercase;
                      letter-spacing:1.5px;margin-bottom:10px;">Your Score</div>
          <div class="final-score-big" style="color:#00D4FF">{u_final}/{total_rounds}</div>
          <div style="font-family:'JetBrains Mono',monospace;font-size:22px;
                      color:#00D4FF;margin-top:8px;">{user_pct}%</div>
        </div>
        """, unsafe_allow_html=True)

    with col_r:
        st.markdown(f"""
        <div style="background:#0D1117;border:1px solid #1E2A3A;border-radius:14px;
                    padding:28px;text-align:center;">
          <div style="font-size:12px;color:#7C8FA6;text-transform:uppercase;
                      letter-spacing:1.5px;margin-bottom:10px;">Model Score</div>
          <div class="final-score-big" style="color:#7C8FA6">{m_final}/{total_rounds}</div>
          <div style="font-family:'JetBrains Mono',monospace;font-size:22px;
                      color:#7C8FA6;margin-top:8px;">{model_pct}%</div>
        </div>
        """, unsafe_allow_html=True)

    # ── Round-by-round breakdown ──────────────────────────────────────────────
    st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size:13px;color:#7C8FA6;text-transform:uppercase;
                letter-spacing:1.5px;margin-bottom:12px;font-weight:600;">
        Round Breakdown
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="background:#0D1117;border:1px solid #1E2A3A;border-radius:14px;padding:20px 24px;">',
                unsafe_allow_html=True)
    for r in st.session_state.history:
        u_icon = "✅" if r["user_correct"]  else "❌"
        m_icon = "✅" if r["model_correct"] else "❌"
        st.markdown(f"""
        <div class="result-row">
          <span style="color:#4A5A6A;font-family:'JetBrains Mono',monospace;font-size:12px">
            #{r['round']:02d}
          </span>
          <span style="flex:1;margin:0 12px;font-size:13px;color:#C8D8E8;
                       white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">
            {r['title'][:55]}{'…' if len(r['title'])>55 else ''}
          </span>
          <span style="color:#4A5A6A;font-size:12px;margin-right:12px">
            {r['shares']:,} shares
          </span>
          <span style="margin-right:8px;">{u_icon} You</span>
          <span>{m_icon} Model</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Play again ────────────────────────────────────────────────────────────
    st.markdown("<div style='height:28px'></div>", unsafe_allow_html=True)
    col_l, col_c, col_r = st.columns([2, 1.5, 2])
    with col_c:
        if st.button("🔄  Play Again", use_container_width=True):
            init_session()
            st.rerun()