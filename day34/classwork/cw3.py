sports = ("Football", "Basketball", "Tennis", "Volleyball", "Rugby")

sports_list = list(sports)
sports_list[2] = "Boxing"

sports = tuple(sports_list)

print(sports)