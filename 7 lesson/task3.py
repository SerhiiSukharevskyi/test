begin = int(input("nachalo"))
end = int(input("konec"))
esey_numbers = []
esey_numbers.append(2)
# if end > begin:
for i in range(2, end):
    pointment1 = True
    num = 0
    while True:
        if i**0.5 < esey_numbers[num]:
            esey_numbers.append(i)
            break
        elif i % esey_numbers[num] == 0:
            pointment1 = False
            break
        else:
            num += 1


    if pointment1 and i>begin:
        print(i)