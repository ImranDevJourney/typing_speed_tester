import random
import time
import string


class TypingTest:
    def __init__(self):
        self.sentences = self.load_sentences()  # Load sentences from file
        self.current_sentence = ""
        self.start_time = 0

    def load_sentences(self):
        """Load sentences from a text file."""
        with open('src/sentences.txt', 'r') as file:
            return [line.strip() for line in file.readlines()]

    def start_test(self):
        """Randomly select a sentence for the typing test."""
        self.current_sentence = random.choice(self.sentences)
        self.start_time = time.time()  # Start the timer

    def check_typing(self, user_input):
        """Check the user's input against the current sentence and calculate WPM."""
        # Define punctuation to remove
        punctuation_to_remove = string.punctuation  # This includes ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~

        # Create translation table to remove specified punctuation
        translator = str.maketrans('', '', punctuation_to_remove)

        # Clean user input and current sentence
        cleaned_user_input = user_input.translate(translator).strip().lower()
        cleaned_current_sentence = self.current_sentence.translate(translator).strip().lower()

        elapsed_time = time.time() - self.start_time
        if cleaned_user_input == cleaned_current_sentence:
            # Calculate words per minute (WPM)
            words_typed = len(cleaned_user_input.split())
            wpm = (words_typed / (elapsed_time / 60)) if elapsed_time > 0 else 0
            return wpm, None  # Return WPM and no error message
        else:
            # Provide detailed feedback
            correct_words = cleaned_current_sentence.split()
            typed_words = cleaned_user_input.split()

            # Compare words and find mismatches
            feedback = []
            for i, word in enumerate(typed_words):
                if i < len(correct_words):
                    if word != correct_words[i]:
                        feedback.append(f"'{word}' (should be '{correct_words[i]}')")
                else:
                    feedback.append(f"'{word}' (extra word)")

            # Check for missing words
            if len(typed_words) < len(correct_words):
                for i in range(len(typed_words), len(correct_words)):
                    feedback.append(f"Missing word: '{correct_words[i]}'")

            error_message = " ".join(feedback)
            return None, error_message  # Return None for WPM and the error message