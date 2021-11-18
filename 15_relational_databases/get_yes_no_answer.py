def get_yes_no_answer(question, yes, no):
    while True:
        answer = input(question)

        if answer == yes:
            return True
        if answer == no:
            return False
