tests=[]
index=1
num_tests = input()
for i in range(int(num_tests)):
    n = input()
    tests.append(int(n))

for num in tests:
    remainder = num%5
    if remainder != 0:
        output = int(num/5)+1
        print(f"Case #{index}: {output}")
    else:
        output = int(num/5)
        print(f"Case #{index}: {output}")
    index+=1
