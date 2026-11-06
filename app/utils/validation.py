def validate_question(question: str):
    question = question.strip()
    if not question or len(question) > 500:
        raise ValueError('Question must be between 1 and 500 characters')
    return question
