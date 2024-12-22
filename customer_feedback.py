def calculate_positive_feedback(rating):
    if not rating:
        return "No ratings available."
    positive_count = sum(1 for rating in rating if rating >= 4)
    percentage = (positive_count / len(rating)) * 100
    return f"Positive Feedback: {percentage:.2f}%"


ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print(calculate_positive_feedback(ratings))