class DListNode:
    def __init__(self, val=0):
        self.val = val
        self.key = None
        self.prev = None
        self.next = None

class LRUCache:

    # Heper 1: remove a node from DLL
    def _remove(self, node):
        node.prev.next= node.next
        node.next.prev= node.prev
    
    # Helper 2: insert right after head
    def _insert_front(self, node):
        node.next=self.head.next
        node.prev= self.head
        self.head.next.prev=node
        self.head.next=node

    def __init__(self, capacity: int):
        self.cap= capacity
        self.map={}
        # create head and tail and point them to each other
        self.head= DListNode()
        self.tail= DListNode()
        self.head.next=self.tail
        self.tail.prev= self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self._remove(self.map[key])
        self._insert_front(self.map[key])
        return self.map[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._remove(self.map[key])
        node= DListNode(value) #create a node and pass in the value
        node.key= key #store the key on the node
        self.map[key]=node #map/dict sssignment key->node object address

        self._insert_front(node)
        if len(self.map)>self.cap:
            lru=self.tail.prev
            self._remove(lru)
            del self.map[lru.key]