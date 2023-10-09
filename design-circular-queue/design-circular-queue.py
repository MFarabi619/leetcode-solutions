class MyCircularQueue:

    def __init__(self, k: int):
        # Initializing the queue with a fixed size 'k' and setting the initial values
        self.queue = [None] * k
        self.head = 0   # Head pointer to the front of the queue
        self.tail = 0   # Tail pointer to the next available position in the queue
        self.size = 0   # Current size of the queue (number of elements present)
        self.capacity = k   # Maximum number of elements the queue can hold

    def enQueue(self, value: int) -> bool:
        # Check if the queue is full
        if self.isFull():
            return False
        # Assign the value to the tail's position
        self.queue[self.tail] = value
        # Move the tail to the next available position, wrap around if needed
        self.tail = (self.tail + 1) % self.capacity
        # Increase the current size of the queue
        self.size += 1
        return True

    def deQueue(self) -> bool:
        # Check if the queue is empty
        if self.isEmpty():
            return False
        # Remove the element from the head's position
        self.queue[self.head] = None
        # Move the head to the next position, wrap around if needed
        self.head = (self.head + 1) % self.capacity
        # Decrease the current size of the queue
        self.size -= 1
        return True

    def Front(self) -> int:
        # If the queue is not empty, return the front element
        return self.queue[self.head] if not self.isEmpty() else -1

    def Rear(self) -> int:
        # If the queue is empty, return -1
        if self.isEmpty():
            return -1
        # Since the tail points to the next free position, get the element before it.
        # We adjust for the wrapping around with the modulo operation
        return self.queue[(self.tail - 1 + self.capacity) % self.capacity]

    def isEmpty(self) -> bool:
        # Check if the queue's current size is 0
        return self.size == 0

    def isFull(self) -> bool:
        # Check if the queue's current size equals its capacity
        return self.size == self.capacity
