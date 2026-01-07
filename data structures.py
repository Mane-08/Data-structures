import heapq
from queue import Queue, LifoQueue

class CustomQueue:
    def __init__(self, queue_type):
        self.queue_type = queue_type
        if queue_type == "FIFO":
            self.queue = Queue()
        elif queue_type == "LIFO":
            self.queue = LifoQueue()
        elif queue_type == "Priority":
            self.queue = []
        else:
            raise ValueError("Invalid queue type")

    def push(self, value):
        if self.queue_type == "FIFO" or self.queue_type == "LIFO":
            self.queue.put(value)
        elif self.queue_type == "Priority":
            heapq.heappush(self.queue, value)
        print(f"Pushed '{value}' into {self.queue_type} queue.")

    def pop(self):
        if self.is_empty():
            print(f"{self.queue_type} queue is empty.")
            return None

        if self.queue_type == "FIFO" or self.queue_type == "LIFO":
            value = self.queue.get()
        elif self.queue_type == "Priority":
            value = heapq.heappop(self.queue)

        print(f"Popped '{value}' from {self.queue_type} queue.")
        return value

    def is_empty(self):
        if self.queue_type == "FIFO" or self.queue_type == "LIFO":
            return self.queue.empty()
        elif self.queue_type == "Priority":
            return len(self.queue) == 0

    def get_top(self):
        if self.is_empty():
            print(f"{self.queue_type} queue is empty.")
            return None

        if self.queue_type == "FIFO" or self.queue_type == "LIFO":
            return self.queue.queue[0]  # Get front element
        elif self.queue_type == "Priority":
            return self.queue[0]  # Get smallest element in priority queue

    def display(self):
        if self.queue_type == "FIFO" or self.queue_type == "LIFO":
            print(f"{self.queue_type} Queue State: {list(self.queue.queue)}")
        elif self.queue_type == "Priority":
            print(f"{self.queue_type} Queue State: {self.queue}")

# Interactive user input
def interactive_demo():
    fifo_queue = CustomQueue("FIFO")
    lifo_queue = CustomQueue("LIFO")
    priority_queue = CustomQueue("Priority")

    while True:
        print("\nChoose an option:")
        print("1. Push a value")
        print("2. Pop a value")
        print("3. Get top value")
        print("4. Display queue state")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            value = input("Enter a value to push (number or name): ")
            try:
                value = int(value)  # Convert to int if possible
            except ValueError:
                pass  # Keep as string if conversion fails

            fifo_queue.push(value)
            lifo_queue.push(value)
            priority_queue.push(value)

        elif choice == "2":
            fifo_queue.pop()
            lifo_queue.pop()
            priority_queue.pop()

        elif choice == "3":
            print(f"FIFO Queue Top: {fifo_queue.get_top()}")
            print(f"LIFO Queue Top: {lifo_queue.get_top()}")
            print(f"Priority Queue Top: {priority_queue.get_top()}")

        elif choice == "4":
            fifo_queue.display()
            lifo_queue.display()
            priority_queue.display()

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

# Run the interactive demo
interactive_demo()
