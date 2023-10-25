def function(mas: list):
    sr = sum(mas) / len(mas)
    for i in range(len(mas)):
        if mas[i] > sr:
            mas[i] = 0
    return mas

