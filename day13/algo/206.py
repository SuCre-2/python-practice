#反转链表
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        cur = head
        while cur:
            temp = cur.next  #存住cur的下一个节点
            cur.next = prev  #cur的下一节点指向perv,开始反转了，也就是原本的1->2,变成none-<1
            prev = cur       #然后把prev放在了cur的位置上，cur放在原本的下一步，整体移动方便下一次反转
            cur = temp       #prev->1,cur->2,下一次循环temp->3,cur.next->1,新的链表变成2->1->None,prev->2，cur->3
        return prev          #直到最后一步，prev指向了新链表头节点