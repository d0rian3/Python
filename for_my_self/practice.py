def nb_year(p0, percent, aug, p):
    year = 0
    while p0 < p:
        p0 += p0 * percent / 100 + aug
        year += 1
    print(year)
    return year
nb_year(1500, 5, -111, 5000)