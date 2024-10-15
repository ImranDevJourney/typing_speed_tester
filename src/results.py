# src/results.py

class Results:
    def __init__(self):
        self.results = []

    def add_result(self, wpm):
        """Add a new result to the results list."""
        self.results.append(wpm)

    def get_average_wpm(self):
        """Calculate and return the average WPM from results."""
        if not self.results:
            return 0
        return sum(self.results) / len(self.results)

    def clear_results(self):
        """Clear all stored results."""
        self.results.clear()

    def display_results(self):
        """Format results for display."""
        return "\n".join(f"Test {i + 1}: {wpm:.2f} WPM" for i, wpm in enumerate(self.results))