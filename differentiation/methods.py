import simpleDeriv
import diff
import helpFunc

def summ(a,b):
    return diff.distr(a) + '+' + diff.distr(b)

def multi(a, b):    #a*b
    c = diff.distr(a)
    d = diff.distr(b)
    print('(' + c + ')' + '*' + '(' + b + ')' + '+' + '(' + a + ')' + '*' + '(' + d + ') -- multy check')
    return '(' + c + ')' + '*' + '(' + b + ')' + '+' + '(' + a + ')' + '*' + '(' + d + ')'

def comp(a, b):     #a(b)
    c = diff.distr(a)
    d = diff.distr(b)
    return c + '(' + b + ')*' + '(' + d + ')'

def div(a, b):      #a/b
    c = diff.distr(a)
    d = diff.distr(b)
    return '(' + '(' + c + ')' + '*' + '(' + b + ')' + '-' + '(' + a + ')' + '*' + '(' + d + ')' + ')/(' + b + ')^2'