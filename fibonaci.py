# Write a program to generate the Fibonacci sequence up to 100.

prev = 0
curr = 1
print(prev)
print(curr)
for i in range(0, 100):
    next=curr+prev
    print(next)
    prev=curr
    curr=next
    if next > 100:
        break
        
    


