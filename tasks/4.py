def month_to_season(n):
    if n >= 1 or n <= 3:
        return "Qish"
    elif n >= 4 or n <= 6:
        return "Bahor"
    elif n >= 7 or n <= 9:
        return "Yoz"
    else:
        return "Kuz"

print(month_to_season(7))