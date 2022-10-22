class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def solve(self, a):
        k = 0
        temp = ListNode(-1)
        ans = temp
        i = 0
        while k != len(a):
            if ans.val == -1 and a[i] != None:
                k = 0
                ans.val = a[i].val
                a[i] = a[i].next
                i += 1
                if i == len(a):
                    i = 0
                continue
            if a[i] == None:
                k += 1
                i += 1
                if i == len(a):
                    i = 0
                continue
            if a[i] != None:
                k == 0
                ans.next = ListNode(a[i].val)
                ans = ans.next
                a[i] = a[i].next
                i += 1
                if i == len(a):
                    i = 0
                continue
        return temp

    a1 = ListNode(1)
    temp = a1
    temp.next = ListNode(2)
    temp = temp.next
    temp.next = ListNode(3)
    temp = temp.next
    temp.next = None
    ar = [a1, a1, a1]
    print(solve(ar))

