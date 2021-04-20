#mathematical desigion
def chislo_fibonachi(n):
    s1 = 0
    s2 = 1
    for i in range(n):
        s3 = s1 + s2
        s1 = s2
        s2 = s3

    return s2

n = int(input("how mutch steirs are"))

print("there is a ",chislo_fibonachi(n),"variant how to get to ", n," steirs")