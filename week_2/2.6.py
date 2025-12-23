def all_eq(list):
    high = max(len(strings) for strings in list)
    return [strings + "_" * (high - len(strings)) for strings in list]
nabor = all_eq(["", "", ""])
print(nabor)
