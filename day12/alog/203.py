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
