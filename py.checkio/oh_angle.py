# Решение задачи "Sun Angle" в пайчекио
# Задача: py.checkio.org/ru/mission/sun-angle/
# Автор - M. Batanov, 12.09.19


def sun_angle(time):
    hours, minutes = int(time[0:2]), int(time[3:])
    t = hours + minutes*0.01
    if t > 18 or t < 6:
        return "I don't see the sun!"
    else:
        angle = (hours-6)*15 + minutes*0.25
        return angle
