# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

#思路拆解：
# 获取整个链表，找到第n个节点，删除
# 删除就是把n-1的节点指向n+1
# 怎么找n呢
# 从头结点开始，走n-1步，因为第一个节点开始，走一步就是第二个了，走n步就是n-1个
# cur =head
# count = 1
# while cur !=null and count< 0 :
#     cur = cur .next
#     count +1
# return cur
# 或者双指针，快指针走n步，然后快慢指针一起走直到快指针走到尾，此时慢指针就到第n个节点的前一个也就是n -1
# 正好让n -1 指向n+1就行了。slow.next= slow.next.next
# 加个虚拟头节点处理删除头部节点的情况就行了
def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next
