# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
   print(a)
   a, b = b, a+b
   
 
# [DG]
   # Fibonacci series: the sum of two elements defines the next

Fib_Seq = [0,1]

while len(Fib_Seq) < 10:
    Fib_Seq.append( Fib_Seq[-1] + Fib_Seq[-2] )   
    # Appends sum of last 2 to the list

print(Fib_Seq)
