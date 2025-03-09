import streamlit as st
import random

# Set page config and title
st.set_page_config(page_title="Number Guessing Game", page_icon="🎲")

# Custom CSS styling
st.markdown("""
    <style>
    @keyframes titleAnimation {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    .animated-title {
        display: inline-block;
        animation: titleAnimation 2s ease-in-out infinite;
        background: linear-gradient(45deg, #FF6B6B, #4a90e2, #4CAF50);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-size: 200% 200%;
        animation: titleAnimation 2s ease-in-out infinite, gradient 3s ease infinite;
    }
    .stButton>button {
        background-color: #FF6B6B;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.5rem 2rem;
        border: 2px solid #FF5252;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.3);
    }
    .number-input {
        background-color: #f0f8ff;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
        border: 2px solid #4a90e2;
    }
    .game-container {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Initialize game state
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# Title and description
st.markdown("<h1 class='animated-title'>🎲 Number Guessing Game</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #4CAF50;'>Apna number darj karo 1 se 100 tak 🤔</h3>", unsafe_allow_html=True)

# Main game container
with st.container():
    st.markdown('<div class="game-container">', unsafe_allow_html=True)
    
    # Game input
    guess = st.number_input("Number darj karo:", min_value=1, max_value=100, key="guess")
    
    # Check guess button
    if st.button("Submit"):
        st.session_state.attempts += 1
        st.balloons()  # Show balloons on every submit
        
        if guess == st.session_state.secret_number:
            for _ in range(5):  # Extra balloons for winning
                st.balloons()
            st.success(f"🎉 Mubarak ho! Apne {st.session_state.attempts} koshishon mein number guess kar liya!")
            st.session_state.game_over = True
        elif guess < st.session_state.secret_number:
            st.warning("Ye number chota hai! Bara number try karo 👆")
        else:
            st.warning("Ye number bara hai! Chota number try karo 👇")
            
    # Display attempts
    st.info(f"Koshishein: {st.session_state.attempts}")
    
    # New game button
    if st.session_state.game_over:
        if st.button("Phir se khelo"):
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.attempts = 0
            st.session_state.game_over = False
            st.experimental_rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Game rules
with st.expander("Khel ke Qawaid 📜"):
    st.markdown("""
    <div style='color: #4a90e2;'>
    1. Computer 1 se 100 tak ka number chunega<br>
    2. Ap us number ko guess karein<br>
    3. Har guess ke bad computer bataega ke number chota hai ya bara<br>
    4. Kam koshishon mein number guess karne ki koshish karein!
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("<hr style='border: 2px solid #4CAF50;'>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; color: #4CAF50;'><small>Created with ❤️ by LuckyDS</small></div>", unsafe_allow_html=True)
