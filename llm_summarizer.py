# llm_summarizer.py

def generate_summary(similarity_score):
    if similarity_score > 0.75:
        reason = f"This project is an excellent match with a similarity score of {similarity_score:.2f}."
    elif similarity_score > 0.5:
        reason = f"This project is a decent match (similarity score: {similarity_score:.2f})."
    else:
        reason = f"This project has a lower similarity score ({similarity_score:.2f}), but was the best available."

    return reason