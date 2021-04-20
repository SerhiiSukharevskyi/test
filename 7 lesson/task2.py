#mathematical desigion
def chislo_fibonachi(n):
    fibonachki = []
    fibonachki.append(1)
    fibonachki.append(1)
    for i in range(2, n+1):
        fibonachki.append(fibonachki[-1] + fibonachki[-2])
    return fibonachki[n]



n = int(input("how mutch steirs are "))

print("there is a ", chislo_fibonachi(n), "variant how to get to ",n ," steirs")