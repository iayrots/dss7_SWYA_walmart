def check_digit(x):
    try:
        odd = map(int, ','.join(x[-1::-2]).split(','))
        even = map(int, ','.join(x[-2::-2]).split(','))
        sum_odd3 = sum(odd) * 3
        total = sum_odd3 + sum(even)
        rem = total % 10
        if rem == 0:
            return rem
        return 10 - rem
    except:
        return -9999

train["check"] = train.Upc.apply(check_digit)

def full_upc(x):
    try:
        if len(x) < 12:
            missing = 11 - len(x)
            zeros = ["0"] * missing
            xx = zeros + ','.join(x).split(',') + [str(check_digit(x))]
            xx = ''.join(xx)
            return xx
    except:
        return -9999

train["full_upc"] = train.Upc.apply(full_upc)

train = train.drop("Upc", axis=1)

def company(x):
    try:
        p = x[:6]
        if p == "000000":
            return x[-5]
        return p
    except:
        return -9999
