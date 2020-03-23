from LinkedList import LinkedList

sol = "none"
def return_k_last(ll, k):

    def dfs(head):
        if not head:
            return 1

        n = dfs(head.next)
        if n == k:
            print(head.value)

        return n+1

    dfs(ll.head)
    return sol

def return_k_last2(ll, k):
    prev = current = ll.head
    for i in range(k):
        if not prev:
            return None
        prev = prev.next

    while prev:
        prev = prev.next
        current = current.next

    return current




ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
print(return_k_last2(ll, 2))