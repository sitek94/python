class Counter:
    count = 0

    def increment(self):
        self.count += 1
        self.log()

    def decrement(self):
        self.count -= 1
        self.log()

    def log(self):
        print(self.count)


my_counter = Counter()

my_counter.increment()
my_counter.increment()
my_counter.increment()

my_counter.decrement()
