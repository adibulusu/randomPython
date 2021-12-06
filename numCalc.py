records = []
just_times = []
p1 = []
p2 = []
p3 = []

if __name__ == '__main__':
    for _ in range(int(input("Enter number of drivers, then driver name, then driver lap time, entering after each "
                             "entry. Enter a minimum of 4 drivers: \n"))):
        name = input()
        lap_times = float(input())
        records.append([name, lap_times])
        if lap_times not in just_times:
            just_times.append(lap_times)

    # calculates top three times
    fastest = sorted(just_times)[0]
    second_fastest = sorted(just_times)[1]
    third_fastest = sorted(just_times)[2]

    for name, lap_times in records:
        if lap_times == fastest:
            p1.append(name)
        elif lap_times == second_fastest:
            p2.append(name)
        elif lap_times == third_fastest:
            p3.append(name)

    print(f"P1: {p1[0]}")
    print(f"P2: {p2[0]}")
    print(f"P3: {p3[0]}")




