
def f_from_p():

    i, n, p = (input('请依次输入每期利率,期数,现值：').split())
    i = float(i)
    n = int(n)
    p = float(p)
    f =  p*(1+i)**n
    print('终值是'+str(f))
    return f

def p_from_f():
    i, n, f = (input('请依次输入每期利率,期数,终值：').split())
    i = float(i)
    n = int(n)
    f = float(f)
    p = f/((1+i)**n)
    print('现值是' + str(p))
    return p

def f_from_a():

    i, n, a = (input('请依次输入每期利率,期数,年值：').split())
    i = float(i)
    n = int(n)
    a = float(a)
    f =  a*((1+i)**n-1)/i
    print('终值是'+str(f))
    return f

def a_from_f():
    i, n, f = (input('请依次输入每期利率,期数,终值：').split())
    i = float(i)
    n = int(n)
    f = float(f)
    a = f *i / ((1 + i) ** n - 1)
    print('年值是' + str(a))
    return f

def a_from_p():
    i, n, p = (input('请依次输入每期利率,期数,现值：').split())
    i = float(i)
    n = int(n)
    p = float(p)
    f = p*(1+i)**n
    a = f *i / ((1 + i) ** n - 1)
    print('年值是' + str(a))
    return f

def p_from_a():
    i, n, a = (input('请依次输入每期利率,期数,年值：').split())
    i = float(i)
    n = int(n)
    a = float(a)
    f = a * ((1 + i) ** n - 1) / i
    p = f/(1+i)**n
    print('现值是' + str(p))
    return p

operations = {
    '1':f_from_p,
    '2':p_from_f,
    '3':f_from_a,
    '4':a_from_f,
    '5':a_from_p,
    '6':p_from_a,
}

if __name__ == '__main__':
    func_num = input('请选择函数\n'
                     '1) F/P\n'
                     '2) P/F\n'
                     '3) F/A\n'
                     '4) A/F\n'
                     '5) A/P\n'
                     '6) P/A\n'
                     )
    operations[func_num]()

