q = 0
'''a = [
     [q,q,q, q,q,q, q,q,q],
     [q,q,q, q,q,q, q,q,q],
     [q,q,q, q,q,q, q,q,q],
     
     [q,q,q, q,q,q, q,q,q],
     [q,q,q, q,q,q, q,q,q],
     [q,q,q, q,q,q, q,q,q],
     
     [q,q,q, q,q,q, q,q,q],
     [q,q,q, q,q,q, q,q,q],
     [q,q,q, q,q,q, q,q,q]
     ]'''

a = [
     [4,q,6, q,q,7, q,q,2],
     [q,q,8, q,9,q, q,4,q],
     [q,q,q, 2,8,q, 1,9,q],
     
     [5,3,q, 6,q,2, 9,q,q],
     [q,q,q, q,q,q, 6,q,3],
     [q,q,q, q,q,q, q,q,q],
     
     [1,q,q, q,q,q, q,2,q],
     [q,q,2, q,1,q, q,q,q],
     [q,7,4, 9,q,q, q,q,q]
     ]

def rcch(i,j,nums):
    nums2 = nums.copy()
    for h in nums:
        w = i
        for e in range(9):
            if (not a[w][e] in [1,2,3,4,5,6,7,8,9]) and not (w == i and e == j):
               if h in b[w][e]:           
                   nums2.remove(h)
                   break
    if len(nums2) == 1:
        print("Row Column Method")
        return nums2
    else:
        return nums

def rccv(i,j,nums):
    nums2 = nums.copy()
    for h in nums:
        e = j
        for w in range(9):
            if (not a[w][e] in [1,2,3,4,5,6,7,8,9]) and not (w == i and e == j):
               if h in b[w][e]:           
                   nums2.remove(h)
                   break
    if len(nums2) == 1:
        print("Row Column Method")
        return nums2
    else:
        return nums
    
def opc(i,j,nums):
    global a
    global b
    global q
    if i in [0,1,2]:
        y = [0,1,2]
    elif i in [3,4,5]:
        y = [3,4,5]
    elif i in [6,7,8]:
        y = [6,7,8]
    if j in [0,1,2]:
        u = [0,1,2]
    elif j in [3,4,5]:
        u = [3,4,5]
    elif j in [6,7,8]:
        u = [6,7,8]
    nums2 = nums.copy()
    for h in nums:
        for w in y:
            for e in u:
                if (not a[w][e] in [1,2,3,4,5,6,7,8,9]) and not (w == i and e == j):
                   if h in b[w][e]:
                       nums2.remove(h)
                       break
            else:
                continue
            break
    
    if len(nums2) == 1:
        return nums2
    else:
        return nums
def cube(i,j,nums):
    global a
    global b
    global q
    if i in [0,1,2]:
        y = [0,1,2]
    elif i in [3,4,5]:
        y = [3,4,5]
    elif i in [6,7,8]:
        y = [6,7,8]
    if j in [0,1,2]:
        u = [0,1,2]
    elif j in [3,4,5]:
        u = [3,4,5]
    elif j in [6,7,8]:
        u = [6,7,8]
    for w in y:
        for e in u:
            if a[w][e] in nums:
                nums.remove(a[w][e])
    return nums
for l in range(100):
    for i in range(9):
        for j in range(9):
            if a[i][j] == q:
                nums = [1,2,3,4,5,6,7,8,9]
                for x in range(9):
                    if a[i][x] in nums:
                        nums.remove(a[i][x])
                    if a[x][j] in nums:
                        nums.remove(a[x][j])
                nums = cube(i,j,nums)
                b[i][j]= nums
                if l > 0 and len(nums) != 1:
                    nums = opc(i,j,nums)
                    if len(nums) != 1:
                        nums = rcch(i,j,nums)
                        nums = rccv(i,j,nums)
                        
                if len(nums) == 1:
                    b[i][j] = nums[0]
                    a[i][j] = nums[0]

for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                print(a[i*3 + j][k * 3 + l] , "|", end = "")
            print(" | " , end = "")
        print()
    print("----------------------------")