import streamlit as st
import random

# Function to start a new game
def start_game():
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.guess_count = 0
    st.session_state.game_over = False

# Function to check the user's guess
def check_guess():
    if st.session_state.user_guess is None:
        st.warning("Please enter a number.")
        return

    st.session_state.guess_count += 1
    guess = st.session_state.user_guess

    if guess < st.session_state.number_to_guess:
        st.success("Higher! Try again.")
    elif guess > st.session_state.number_to_guess:
        st.success("Lower! Try again.")
    else:
        st.success(f"Congratulations! You've guessed the number {st.session_state.number_to_guess} in {st.session_state.guess_count} attempts.")
        st.session_state.game_over = True

# Streamlit UI
st.title("Number Guessing Game")

# Initialize game state
if 'number_to_guess' not in st.session_state:
    start_game()

# Input for user's guess
if not st.session_state.game_over:
    st.session_state.user_guess = st.number_input("Enter your guess (1-100):", min_value=1, max_value=100, step=1)
    if st.button("Submit Guess"):
        check_guess()
else:
    if st.button("Play Again"):
        start_game()
