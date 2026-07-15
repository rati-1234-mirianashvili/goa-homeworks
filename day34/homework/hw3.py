# Tuple-ის პირდაპირ შეცვლა არ შეიძლება,
# ამიტომ გადავიყვანოთ list-ში

sports_list = list("sports")

sports_list[0] = "Volleyball"

sports = tuple(sports_list)

print(sports)