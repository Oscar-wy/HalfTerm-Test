amtDigits = int(input("How many digits: "))
Digits = {}
highest = None
for i in range(amtDigits):
    num = int(input("Enter a number: "))
    if num in Digits:
        Digits[num] += 1
    else:
        Digits[num] = 1
for key in Digits.keys():
    if highest == None:
        highest = key
    elif Digits[key] > Digits[highest]:
        highest = key
for key in Digits.keys():
    if Digits[key] == Digits[highest] and highest != key:
        highest = "multi"
        break

if highest == "multi":
    print("Data was multimodal")
else:
    print(f"The highest was {highest} at a frequency of {Digits[highest]}")