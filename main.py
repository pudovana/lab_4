
def calc(loan_amount, interest_rate, loan_term):
    try:
        loan_amount = float(loan_amount)
        interest_rate = float(interest_rate)
        loan_term = float(loan_term)
    except ValueError:
        return 'ValueError: не является числом'
    except TypeError:
        return "TypeError: недопустимое значение"
    if (loan_amount < 0 or interest_rate < 0 or loan_term < 0):
        return "Одно или все значения меньше нуля"
    else:
        return render_template
