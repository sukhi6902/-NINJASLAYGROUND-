## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
n=int(input())
even=0
odd=0
while (n>0):
    r=n%10
    n=n//10
    
    if r%2==0:
        even+=r
    else:
        odd+=r
print(even,odd)

https://www.codingninjas.com/studio/problems/sum-of-even-odd_9065111?challengeSlug=ninja-slayground
