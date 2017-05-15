'''
Please write a function that take an array of x+1 integers between 1 and x as argument and the array has at least one duplicate integer.
1.    Please print all the integers that are duplicate. Please give as many solutions as possible. 
2.    For these methods, which is better and why?


For ex, if x = 2, the array maybe [1,2,2]
output: 2
if x = 4, the array maybe [1,2,2,2,1]
output: 1, 2
'''
#space complexity:  O(n); time complexity: O(n)
def printDup(lst):
    dct = {}
    for i in lst:
        if i in dct:
            if dct[i] == 1:
                print i
            dct[i] += 1
        else:
            dct[i] = 1

#space complexity: O(n); time complexity: O(n); no hash
def printDup2(lst):
    b=[False]*len(lst)
    counter = [0]*len(lst)
    for i in lst:
        if b[i] == True:
            if counter[i] == 0:
                print i
            counter[i] += 1
        b[i] = True

# time complexity: O(n^2), O(1) space
def printDup3(lst):
    for i in xrange(len(lst)):
        for j in xrange(i+1,len(lst)):
            if lst[i] == lst[j]:
                print lst[j]
                break


#Well, I could sort the numbers and compare adjacent pairs. That would take O(n*log n) time and O(1) space if I use an in-place sort like mergesort
def printDup4(lst):
    lst.sort()
    counter = 0
    for i in xrange(len(lst)-1):
        if lst[i] == lst[i+1]:
            if counter == 0:
                print lst[i]
                counter += 1
        else:
            counter = 0

#I think I can binary search for a duplicated number. For example, I go through the list and count the number of integers between 1 and N/2. If the count is greater than the number of possible integers in that range, then I know there's a duplicate in that range. Otherwise, a duplicate must exist in the range of N/2+1 to N. Once I know which half of the range the duplicate is in, I can recurse and binary search in that half, then keep repeating the process until I've found a duplicated number. The time complexity is O(n*log n) and the space complexity is O(1).


#recursive solution
def printDup5(lst):
    
        
#printDup([1,2,2,2,1])
#printDup2([1,2,2,2,1,5,5])
#printDup4([1,2,2,2,1,5,5])
printDup3([1,2,2,2,1,5,5])
