import streamlit as st
import random

st.title("💔 Emujin's Love Life Analytics™")

st.write("Welcome to the world's most scientifically questionable relationship analysis.")

name = st.text_input("Your name")

crush = st.text_input("Your crush's name")

texting = st.slider(
    "How often do they text you?",
    0, 10, 5
)

first_text = st.selectbox(
    "Who usually texts first?",
    ["Me 😭", "Them 👀", "We both do", "Nobody 💀"]
)

red_flag = st.selectbox(
    "Their biggest red flag:",
    [
        "Leaves me on read",
        "Replies after 7 business days",
        "Says 'I'm bad at texting'",
        "Has too many girl/boy besties",
        "None... suspiciously"
    ]
)

delusion = st.slider(
    "How delusional are you?",
    0, 100, 50
)

if st.button("🔮 ANALYZE MY LOVE LIFE"):

    score = texting * 5

    if first_text == "Them 👀":
        score += 25
    elif first_text == "We both do":
        score += 15
    elif first_text == "Me 😭":
        score -= 10
    else:
        score -= 20

    score += delusion * 0.3

    score = min(100, max(0, int(score)))

    st.divider()

    st.header("📊 Analysis Results")

    st.write("### Love Score:", score, "/100")

    if score >= 80:
        st.success("🚨 THEY MIGHT ACTUALLY LIKE YOU. STOP OVERTHINKING.")
        diagnosis = "Potentially Mutual Delusion"
    elif score >= 60:
        st.info("👀 There is something here... probably.")
        diagnosis = "Situationship Loading..."
    elif score >= 40:
        st.warning("💀 The data is not looking good.")
        diagnosis = "One-Sided Investment"
    else:
        st.error("🏃 RUN. THIS IS NOT A LOVE STORY.")
        diagnosis = "Emotional Damage"

    st.write("### Official diagnosis:")
    st.write("**", diagnosis, "**")

    st.write("### 🚩 Red Flag Detected:")
    st.write(red_flag)

    if delusion >= 80:
        st.write("🧠 Delusion level: **CRITICAL**")
        st.write("You have already planned the wedding.")
    elif delusion >= 50:
        st.write("🧠 Delusion level: **Moderate**")
        st.write("You analyzed their 'haha' for 45 minutes.")
    else:
        st.write("🧠 Delusion level: **Healthy**")
        st.write("Congratulations. You still have a brain.")

    if score >= 70:
        st.balloons()

    st.write("---")
    st.write("⚠️ This analysis is 100% fake and 0% scientifically valid.")
    
    st.header("📱 Decode Their Message")

message = st.text_input(
    "Enter the message they sent you:"
)

if st.button("Decode Message"):
    answers = [
        "They like you. Probably. Maybe. We have no evidence.",
        "They're bored.",
        "They're being polite 😭",
        "You are currently being delusional.",
        "This requires further investigation.",
        "Girl... stand up.",
        "HE WANTS YOU. SOURCE: TRUST ME BRO."
    ]

    st.write(random.choice(answers))