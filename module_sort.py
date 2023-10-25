def my_sort(mas: list):
    for i in range(len(mas)):
        for t in range(len(mas) - 1):
            if mas[i] > mas[t]:
                mas[i], mas[t] = mas[t], mas[i]
    return mas
