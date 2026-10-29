# 链表删除其实是让前驱节点不再指向它

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)      # 哨兵：val 随便填，next 指向真正的头
        prev, cur = dummy, head

        while cur:
            if cur.val == val:
                prev.next = cur.next   # 跳过 cur，prev 不动
            else:
                prev = cur             # cur 保留，prev 跟上来
            cur = cur.next             # cur 始终前进

        return dummy.next             # 不能 return head

class Solution:
    def r2(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 第一段：把开头连续等于 val 的节点剥掉，head 直接后移
        while head and head.val == val:
            head = head.next

        # 第二段：此时 head 要么是 None，要么是第一个确定保留的节点
        cur = head
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next     # 跳过下一个，cur 自己不动
            else:
                cur = cur.next
        return head
