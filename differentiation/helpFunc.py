def founder(string, part):             #founds part in string and returns it indexes
    places = []
    for i in range(len(string)):
        if string[i] == part[0] and i+len(part) <= len(string):
            if string[i:i + len(part)] == part:
                places.append(i)
    return places

def replacer(string, part1, part2, exceptions):     #part1 - what to replace, part2 - what to replace with
    places = founder(string, part1)
    if len(exceptions) != 0:
        for index in exceptions:
            if index in places:
                places.remove(index)
    i = 0
    k = 0
    while i < len(places):
        k = places[i]
        string = string[:k] + part2 + string[k+len(part1):]   
        for j in range(len(places)):
            places[j] -= len(part1) - len(part2)
        i += 1
    return string

def goUntil(equation, a, way, stop):       #records part of equation from index 'a' until reaching one of symbols in 'stop' (or until end or start if stop == ['#']) in 'way' (can be 1 or -1), (a - includes, stop - not)
    part = ''
    i = a
    flag = False
    if way == 1:
        while True:
            for symbol in stop:
                if equation[i] == symbol:
                    flag = True
            if flag:
                break
            part = part + equation[i]
            i += way
            if i == len(equation):
                break
    else:
        while True:
            for symbol in stop:
                if equation[i] == symbol:
                    flag = True
            if flag:
                break
            part = equation[i] + part
            i += way
            if i == -1:
                break
    return part

def bracketFounder(equation, a, way):           #find bracket that close (or open) brakcet on 'a' place
    if way == 1:
        if equation[a] != '(':
            print('exception: equation[a] != "("')
            return
        else:
            openBracket = 1
            closeBracket = 0
            i = a
            while openBracket != closeBracket:
                i += 1
                if i == len(equation):
                    print('exception: wrong brackets places and/or count')
                    break
                if equation[i] == '(':
                    openBracket += 1
                elif equation[i] == ')':
                    closeBracket += 1
        return i

    elif way == -1:
        if equation[a] != ')':
            print('exception: equation[a] != ")"')
            return
        else:
            openBracket = 0
            closeBracket = 1
            i = a
            while openBracket != closeBracket:
                i -= 1
                if i == -1:
                    print('exception: wrong brackets places and/or count')
                    break
                if equation[i] == '(':
                    openBracket += 1
                elif equation[i] == ')':
                    closeBracket += 1
        return i


def isNumber(equation):
    if equation.isdigit():          #12345
        return True
    dots = founder(equation, '.')
    if len(dots) == 0:              #-12345
        if equation[0] == '-' and equation[1:].isdigit():   
            return True
    elif len(dots) == 1:            #12.345 and -12.345
        if equation[0] == '-' and equation[1:dots[0]].isdigit() and equation[dots[0]+1:].isdigit() or equation[:dots[0]].isdigit() and equation[dots[0]+1:].isdigit():
            return True
    else:
        return False


def returnTo(equation):             #returns power(a,b) to a^b, sin to sin(x) and so on...
    commas = founder(equation, ',')
    for i in range(len(equation)):
        print(equation[i])
        if equation[i] == 'p':
            for index in commas:
                if index > i:
                    index1 = index
                    break
            closeBracket = bracketFounder(equation, i+5, 1)
            part1 = equation[i+6:index1]
            part2 = equation[index1 + 1:closeBracket]
            equation = replacer(equation, 'power(' + part1 + ',' + part2 + ')', '(' + part1 + ')^(' + part2 + ')', [])

        #if (equation[i] == 's' or equation[i] == 'c') and equation[i+3] != '(':
        #    equation = equation[:i+3] + '(x)' + equation[i+3:]
        #elif equation[i] == 't' and equation[i+3] != '(':
        #    equation = equation[:i+2] + '(x)' + equation[i+2:]
        #elif equation[i] == 'a':
        #    if equation[i+3] == 's' or equation[i+3] == 'c' and equation[i+6] != '(':
        #        equation = equation = equation[:i+6] + '(x)' + equation[i+6:]
        #    elif equation[i+3] == 't' and equation[i+6] != '(':
        #        equation = equation[:i+5] + '(x)' + equation[i+5:]

    return equation