class Counter:
    count = 0

    def __init__(self, initial_count):
        print('🔨🔨🔨 Counter constructed 🔨🔨🔨')
        self.count = initial_count

    def increment(self):
        self.count += 1
        self.log()

    def decrement(self):
        self.count -= 1
        self.log()

    def log(self):
        print(self.count)

    def __del__(self):
        print('💣💣💣 Counter destroyed 💣💣💣')


my_counter = Counter(initial_count=10)

my_counter.increment()
my_counter.increment()
my_counter.increment()

my_counter.decrement()

# Remove reference to Counter instance, effectively destroying the object.
my_counter = 100
