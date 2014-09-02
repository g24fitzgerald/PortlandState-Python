#Exercise
#(c) Gina Fitzgerald 7/7/14
#sum numbers 1 through n

accumulator = 0
n = int(input("summing 1..n: n?"))

for i in range (n + 1):
    accumulator += i
print(accumulator)
