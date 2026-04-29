from collections import Counter, defaultdict, deque


# Counter: counts how many times each value appears.
def counter_example():
	print("1) Counter - counting values")

	numbers = [1, 2, 1, 3, 2, 1]
	counts = Counter(numbers)

	print("Input:", numbers)
	print("Count result:", counts)
	print("How many times is 1?", counts[1])
	print()


# defaultdict: automatically creates a default value if key does not exist.
def defaultdict_example():
	print("2) defaultdict - grouping values")

	words = ["cat", "car", "dog", "door"]
	grouped = defaultdict(list)  # default is empty list

	for word in words:
		first_letter = word[0]
		grouped[first_letter].append(word)

	print("Input:", words)
	print(f"grouped: {grouped}")
	print("Grouped by first letter:", dict(grouped))
	print()


# deque: fast queue from both left and right side.
def deque_example():
	print("3) deque - queue basics")

	q = deque()
	q.append("A")          # add on the right
	q.append("B")
	q.appendleft("START")  # add on the left

	print("Queue now:", q)
	items = list(q)
	print(items)  # ['START', 'A', 'B']

	print("Remove left:", q.popleft())
	print("Remove right:", q.pop())
	print("Queue at end:", q)
	print()


def main():
	print("Easy Python collections examples")
	print()

	counter_example()
	defaultdict_example()
	deque_example()

	print("Start with these 3. Add more later when this feels easy.")


if __name__ == "__main__":
	main()
