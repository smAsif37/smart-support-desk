"""Streamlit front-end. Talks to the FastAPI service over HTTP."""
import os

import requests
import streamlit as st

API = os.getenv("API_URL", "http://127.0.0.1:8000")
TIMEOUT = 90

st.set_page_config(page_title="Smart Support Desk Assistant", page_icon="🎧", layout="wide")
st.title("🎧 Smart Support Desk Assistant")
st.caption("Fine-tuned ticket classifier + sentiment + summary + RAG policy chatbot")

SAMPLES = {
    "Angry refund complaint": "I returned my shoes 2 weeks ago and STILL no refund!! This is unacceptable, "
                              "I want my money back today itself. My email is ravi@example.com",
    "Possible fraud (security)": "Someone logged into my account and placed an order I did not make. "
                                 "My account was hacked, please help urgently!",
    "Simple delivery question": "Hi, how long does standard delivery take to Chennai?",
    "Out-of-scope message": "Can you recommend a good biryani place near me?",
    "Messy / typo ticket": "payment faild at checkout agn but money got deducted frm my acct??",
}


def call_api(path, payload):
    try:
        r = requests.post(f"{API}{path}", json=payload, timeout=TIMEOUT)
        if r.status_code != 200:
            detail = r.json().get("detail", r.text) if r.headers.get("content-type", "").startswith("application/json") else r.text
            return None, f"API error {r.status_code}: {detail}"
        return r.json(), None
    except requests.exceptions.ConnectionError:
        return None, "Cannot reach the API service. It may still be starting; try again in a minute."
    except requests.exceptions.Timeout:
        return None, "The request timed out. The models may still be loading or the LLM is slow."
    except Exception as exc:
        return None, f"Unexpected error: {exc}"


def fmt_sources(sources):
    return ", ".join(f"{s['source']} (p.{s['page']})" for s in sources)


with st.sidebar:
    st.subheader("System status")
    try:
        h = requests.get(f"{API}/health", timeout=3).json()
        st.write("API:", "🟢 ready" if h["status"] == "ready" else "🟡 loading models...")
        st.write("LLM key:", "🟢 set" if h["llm_configured"] else "🔴 missing (set GROQ_API_KEY)")
        if h.get("error"):
            st.error(h["error"])
    except Exception:
        st.write("API: 🔴 unreachable")
    st.caption("Do not paste real customer data into the public demo.")

tab1, tab2 = st.tabs(["🎫 Ticket Analyzer", "💬 Policy Chatbot"])

with tab1:
    st.session_state.setdefault("analysis", None)
    choice = st.selectbox("Load a sample ticket (optional)", ["-"] + list(SAMPLES))
    text = st.text_area("Paste a customer message", value=SAMPLES.get(choice, ""), height=140, max_chars=4000)
    if st.button("Analyze", type="primary"):
        if not text.strip():
            st.warning("Please enter a message first.")
        else:
            with st.spinner("Classifying, scoring sentiment, summarising and drafting a reply..."):
                data, err = call_api("/analyze", {"text": text})
            st.session_state.analysis = (data, err)

    if st.session_state.analysis:
        r, err = st.session_state.analysis
        if err:
            st.error(err)
        else:
            c1, c2, c3 = st.columns(3)
            c1.metric("Category", r["category"], f"conf {r['category_confidence']:.2f}")
            c2.metric("Sentiment", r["sentiment"].title(), f"conf {r['sentiment_confidence']:.2f}")
            c3.metric("Priority", r["priority"])
            st.caption("Priority reasons: " + "; ".join(r["priority_reasons"]))
            if r["needs_human_review"]:
                st.warning(f"Route to a human agent: {r['human_review_reason']}")
            st.write(f"**Summary:** {r['summary']}")
            reply = r["suggested_reply"]
            st.markdown("**Suggested reply (draft for agent approval):**")
            st.info(reply["answer"])
            if reply["sources"]:
                st.caption("Sources: " + fmt_sources(reply["sources"]))

with tab2:
    st.session_state.setdefault("msgs", [])
    top = st.columns([6, 1])
    top[0].write("Ask about refunds, shipping, delivery, accounts, invoices, payments...")
    if top[1].button("Clear"):
        st.session_state.msgs = []
        st.rerun()
    for m in st.session_state.msgs:
        st.chat_message(m["role"]).write(m["content"])
    if q := st.chat_input("Ask a policy question"):
        st.chat_message("user").write(q)
        history = [{"role": m["role"], "content": m["raw"]} for m in st.session_state.msgs]
        with st.spinner("Searching policies..."):
            r, err = call_api("/chat", {"text": q, "history": history})
        if err:
            st.chat_message("assistant").error(err)
        else:
            reply = r["answer"] + (f"\n\n*Sources: {fmt_sources(r['sources'])}*" if r["sources"] else "")
            st.chat_message("assistant").write(reply)
            st.session_state.msgs += [{"role": "user", "content": q, "raw": q},
                                      {"role": "assistant", "content": reply, "raw": r["answer"]}]
