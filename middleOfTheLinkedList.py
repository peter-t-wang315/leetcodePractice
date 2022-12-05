# __Big O Time__
# The big O time complexity of this algorithm is O(n). This is because it traverses the entire linked list at least once so that it knows where the middle point is. 

# __Space complexity__
# The space complexity of this algorithm is O(1). This is because there are only 3 things generated regardless of what the inputs are.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    # 2 pointers. One indexing list, one indexing at 1/2 speed.
    fast_index = head
    slow_index = head
    count = 1

    while(fast_index.next != None):
        count+=1
        fast_index = fast_index.next
        if count % 2 == 0:
            slow_index = slow_index.next
    
    return slow_index


if __name__ == "__main__":
    head = ListNode(val=1)
    current = ListNode(val=2)
    head.next = current
    for i in range(3,6):
        current.next = ListNode(val=i)
        current = current.next
    print(middleNode(head).val)