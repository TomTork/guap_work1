def my_sort(mas: list):
    # Сложность O(len(...)*(len(...)-1))
    for i in range(len(mas)):
        for t in range(len(mas) - 1):
            if mas[i] > mas[t]:
                mas[i], mas[t] = mas[t], mas[i]
    return mas
