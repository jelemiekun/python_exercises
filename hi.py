def isPassedOrFailed(
    grade,
):
    if grade >= 75:
        return "Passed"
    else:
        return "Failed"


print(isPassedOrFailed(75))
