# src/utils.py

import random

def generate_random_sentence(sentences):
    """Return a random sentence from the provided list."""
    return random.choice(sentences)

def format_time(seconds):
    """Format time in seconds into a more readable format (MM:SS)."""
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes:02}:{seconds:02}"

def calculate_wpm(typed_text, elapsed_time):
    """Calculate words per minute (WPM) based on typed text and elapsed time."""
    if elapsed_time > 0:
        words_typed = len(typed_text.split())
        return (words_typed / (elapsed_time / 60))
    return 0

def validate_input(user_input, correct_sentence):
    """Check if user input matches the correct sentence."""
    return user_input.strip() == correct_sentence