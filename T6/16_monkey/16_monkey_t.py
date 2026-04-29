import subprocess

class Greeter:
	def say_hello(self):
		return "Hello from the original method"


def louder_hello(self):
	return "HELLO FROM THE PATCHED METHOD"


def main():
    subprocess.run(args="clear")
    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
    print("Monkey patching basics")
    print("- changing code behavior at runtime")
    print("- useful in tests, experiments, and temporary overrides")
    print("- risky when overused because it changes normal behavior")
    print()

    person = Greeter()
    print("1. Before patch:")
    print(person.say_hello())
    print()

    original_method = Greeter.say_hello
    Greeter.say_hello = louder_hello

    print("2. After class patch:")
    print(person.say_hello())
    print(Greeter().say_hello())
    print()

    another_person = Greeter()
    another_person.say_hello = lambda: "Hello only from this one instance"

    print("3. Instance-level patch:")
    print(another_person.say_hello())
    print(person.say_hello())
    print()

    Greeter.say_hello = original_method

    print("4. After restore:")
    print(Greeter().say_hello())
    print()

    print("Rule of thumb: patch small, patch locally, and restore after use.")

    print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")  # noqa: E303
    
if __name__ == "__main__":
	main()
