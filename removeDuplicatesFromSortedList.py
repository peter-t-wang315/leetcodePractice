# __Big O time__
# The big O time complexity for this algorithm is O(n) where n is the length of the size of the list. For this problem this is the fastest runtime because one must go through the entire list to know
# if there are duplicates to get rid of. Therefore you would have to iterate through the entire list at least once. Therefore my solution is the most optimal. It is also without reducing already
# O(n) time which makes it the most optimal time complexity as I only run through the entire linked list once to remove the dups.

# __Space complexity__
# The space complexity for this algorithm is O(1). This is because no matter the inputs, there are only 2 variables created to track the already existent nodes. This is the most optimal as it
# doesn't get better than constant space.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    if head == None:
        return head
    
    current = head
    check = head

    while check.next != None:
        check = check.next
        if current.val != check.val:
            current.next = check
            current = check
    current.next = None
    return head

if __name__ == "__main__":
    head = ListNode(val=1)
    current = ListNode(val=1)
    head.next = current
    for i in range(1,6):
        current.next = ListNode(val=i)
        current = current.next
    print(deleteDuplicates(head))