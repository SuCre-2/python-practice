# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。
# 你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

# 思路：链表是环环相扣的，那就要让第一个节点，指向下下个节点，下个节点指向
# 它的上个节点

# 但是一开始没节点指向1号，所以要创建一个0节点，一开始指向1号
# 0指向2，1指向3，2指向1
# 0 =0->1
# 1 = head
# while 至少有两个节点：
# 定义2是指向1的下一节点
# 定义3指向2的下一节点
# 2 = 1.next
# 3 = 2.next
# 0指向2
# 0.next =2
# 2指向1
# 2.next = 1
# 1指向3
# 1.next = 3
# 变的都是指向，本身不变
# 全程不碰0和1，好让0和1定位住下一轮循环
# 0 =1
# 1 =3
# 此时变成0->2->1->3
# #下一轮
# 2->1->4->3

# 直到循环结束，输出头节点，也就是2,用了虚拟头节点后输出虚拟头节点的下一个节点就是了
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
         # 虚拟节点（哨兵）：不存数据，专门占住链表头前面的位置
        # 这样"头两个节点"也变成普通的一对，不用单独处理边界
        # dummy 永远指向"当前链表真正的头"，所以最后要 return dummy.next
        node0 = dummy = ListNode(next=head)
         # node1 指向当前要交换的"这一对的第一个节点"
        node1 = head

        while node1 and node1.next:
            # 只要还有至少两个节点（node1 和 node1.next 都存在），就继续交换
            #定义2，3节点用来接住
            node2 = node1.next
            node3 = node2.next


            node0.next = node2
            node2.next = node1
            node1.next = node3

            node0 = node1
             # 下一对的"前驱"就是现在的 node1
            node1 = node3
            # 下一对的"第一个"就是现在的 node3
        return dummy.next

# 构造链表 1 -> 2 -> 3 -> 4
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

# 运行函数
new_head = Solution().swapPairs(head)

# 打印结果
while new_head:
    print(new_head.val, end=" -> ")
    new_head = new_head.next
print("None")
