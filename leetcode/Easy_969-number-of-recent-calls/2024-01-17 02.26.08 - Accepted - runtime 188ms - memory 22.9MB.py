class RecentCounter:

    def __init__(self):
        self.queue = deque()
        self.count = 0

    def ping(self, t: int) -> int:
        #First add the request to the queue and increment the counter
        self.queue.append(t)
        self.count += 1

        # Return the number of request in the Range
        while self.queue[0] < t - 3000:
            self.queue.popleft()
            self.count -= 1

        return self.count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)