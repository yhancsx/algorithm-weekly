from LinkedList import LinkedList

def partition(ll, value):
    current = ll.tail = ll.head

    while current:
        next = current.next
        current.next = None
        if current.value >= value:
            ll.tail.next = current
            ll.tail = current
        else:
            current.next = ll.head
            ll.head = current

        current = next
    ll.tail.next = None

ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
partition(ll, ll.head.value)
print(ll)