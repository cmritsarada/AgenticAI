def analyze_transactions(df):

    income = df[df["Category"]=="Income"]["Credit"].sum()

    expense = df["Debit"].sum()

    savings = income-expense

    category_spending = df.groupby("Category")["Debit"].sum()

    return {

        "Income": income,

        "Expense": expense,

        "Savings": savings,

        "Category Spending": category_spending.to_dict()

    }