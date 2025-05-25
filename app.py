
import streamlit as st
import re
import random

# List of common weak passwords
blacklist = ["123456", "password", "123456789", "qwerty", "password123"]

# Generate a strong password
def generate_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return ''.join(random.choices(chars, k=12))

# Score the password
def score_password(password):
    score = 0
    suggestions = []

    if password in blacklist:
        return 0, "Weak", ["This is a commonly used password. Please choose something unique."]

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add at least one digit (0–9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("Include at least one special character (!@#$%^&*).")

    # Strength label
    if score <= 2:
        strength = "Weak"
    elif 3 <= score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return score, strength, suggestions

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter")
st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password:", type="password")

if password:
    score, strength, tips = score_password(password)

    st.subheader(f"🔎 Strength: **{strength}**")
    st.progress(score / 5)

    if strength == "Strong":
        st.success("✅ Your password is strong!")
    else:
        st.warning("⚠️ Suggestions to improve your password:")
        for tip in tips:
            st.write("- " + tip)

st.markdown("---")
st.subheader("💡 Need help?")
if st.button("Generate a strong password"):
    st.info(f"Suggested password: `{generate_password()}`")
