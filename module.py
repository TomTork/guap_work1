def function(mas: list, tf=True):
    sr = sum(mas) / len(mas)
    for i in range(len(mas)):
        if mas[i] > sr and tf:
            mas[i] = 0
        elif mas[i] < sr and not tf:
            mas[i] = 0
    return mas

