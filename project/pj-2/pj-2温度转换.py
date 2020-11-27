def c2f_temperature(celsius):
    fahrenheit = (9 / 5) * celsius + 32
    return fahrenheit

if __name__=='__main__':
    celsius_degrees = list(["celsius"])+list(range(-20, 41, 5))
    fahrenheit_degrees = list(["fahrenheit"])
    for i in range(0, len(celsius_degrees)):
        if i: fahrenheit_degrees.append(c2f_temperature(celsius_degrees[i]))        
        print("{0:>10}\t{1:>10}".format(celsius_degrees[i], fahrenheit_degrees[i]))