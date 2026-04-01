import streamlit as st
from openai import OpenAI

# --------------------------------
# API CLIENT
# --------------------------------
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="AI Assistant", layout="wide")

st.title("🤖 AI Visa Assistant")
st.markdown("Ask anything about visa processing")

# --------------------------------
# CHAT HISTORY
# --------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --------------------------------
# USER INPUT
# --------------------------------
user_input = st.chat_input("Ask your question...")

if user_input:

    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # --------------------------------
    # LIMIT REQUESTS (avoid spam)
    # --------------------------------
    if len(st.session_state.messages) > 10:
        reply = "⚠️ Too many requests. Please refresh the app."
    else:
        try:
            # --------------------------------
            # OPENAI CALL
            # --------------------------------
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=st.session_state.messages
            )

            reply = response.choices[0].message.content

        except Exception:
            # --------------------------------
            # FALLBACK RESPONSE (VERY IMPORTANT)
            # --------------------------------
            reply = """
            Based on your visa details:

            - Processing delays can happen due to high application volume
            - Certain visa types (like H1B, F1) take longer during peak seasons
            - Location and workload of processing center also affect time

            💡 Recommendation:
            Apply early, ensure documents are correct, and track updates regularly.
            """

    # Save bot response
    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)