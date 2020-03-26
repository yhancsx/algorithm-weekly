from LinkedList import LinkedList, LinkedListNode


def sum_lists(ll_a, ll_b):
    ll = LinkedList()
    a = ll_a.head
    b = ll_b.head

    o = 0
    while a and b:
        v = (a.value + b.value + o) % 10

        ll.add(v)
        o = (a.value + b.value + o) // 10
        a = a.next
        b = b.next

    while a:
        v = (a.value + o) % 10
        ll.add(v)
        o = (a.value + o) // 10
        a = a.next

    while b:
        v = (b.value + o) % 10
        ll.add(v)
        o = (b.value + o) // 10
        b = b.next

    if o:
        ll.add(o)
    return ll


def sum_lists_followup(ll_a, ll_b):
    la = len(ll_a)
    lb = len(ll_b)
    if la > lb:
        for i in range(la - lb):
            ll_b.add_to_beginning(0)

    elif lb > la:
        for i in range(lb - la):
            ll_a.add_to_beginning(0)

    # return carry
    def dfs(ll_a, ll_b, ll_n):
        if not ll_a or not ll_b:
            return 0

        c = dfs(ll_a.next, ll_b.next, ll_n)
        v = (c + ll_a.value + ll_b.value) % 10
        c = (c + ll_a.value + ll_b.value) // 10
        n = LinkedListNode(v)
        if ll_n.head is None:
            ll_n.head = ll_n.tail = n
        else:
            n.next = ll_n.head
            ll_n.head = n
        return c

    ll = LinkedList()
    c = dfs(ll_a.head, ll_b.head, ll)
    if c:
        n = LinkedListNode(c)
        n.next = ll.head
        ll.head = n
    return ll


ll_a = LinkedList()
ll_a.generate(4, 0, 9)
ll_b = LinkedList()
ll_b.generate(3, 0, 9)
print(ll_a)
print(ll_b)
print(sum_lists(ll_a, ll_b))
print(sum_lists_followup(ll_a, ll_b))
