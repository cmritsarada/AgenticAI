def generate_advice(summary):

    advice = ""

    if summary["Expense"] > summary["Income"]*0.8:

        advice += "⚠ High spending detected.\n"

    if summary["Savings"] < 10000:

        advice += "Increase monthly savings.\n"

    advice += "Reduce online food ordering."

    return advice
