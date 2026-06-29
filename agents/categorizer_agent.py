def categorize_transactions(df):

    categories = []

    for desc in df["Description"]:

        desc = desc.lower()

        if "swiggy" in desc or "zomato" in desc:
            categories.append("Food")

        elif "uber" in desc:
            categories.append("Transport")

        elif "amazon" in desc:
            categories.append("Shopping")

        elif "salary" in desc:
            categories.append("Income")

        elif "rent" in desc:
            categories.append("Housing")

        else:
            categories.append("Others")

    df["Category"] = categories

    return df