print ("enter a starting year")
start=int(input())
print("enter an end year")
end=int(input())
print("list of leap years")
for year in range(start,end):
    if(0==year%4)and(0!=year%100)or(0==year%400):
     print(year)
