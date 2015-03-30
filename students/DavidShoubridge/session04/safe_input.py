def safe_input(user_prompt):
    try:
        raw_input(user_prompt)
    except(KeyboardInterrupt, EOFError):
        return "None"

