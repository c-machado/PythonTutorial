def calculateIncome(state, income):

    state_tax = {'alabama': 0.02, 'connecticut': 0.0499, 'new york': 0.082, 'texas': 0, 'california': 0.013}
    if state in state_tax:
        finalIncome = income - (income * state_tax[state])
        print("Your final income is going to be " + str(finalIncome))
        return finalIncome
    else:
        print("The entered state is not in the list")
        return None

calculateIncome('new york', 10000)

