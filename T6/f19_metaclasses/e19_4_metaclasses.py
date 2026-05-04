import w_r
class SimpleMeta(type):
	def __new__(mcls, name, bases, namespace):
        # adds a key to the class body dictionary before the class is created.
		namespace["created_by_meta"] = True
		# Return the class object after adjusting the class body dictionary.
        # class Cat:
        #   created_by_meta = True
		return super().__new__(mcls, name, bases, namespace)



class Cat(metaclass=SimpleMeta):
	pass

@w_r
def main():
	print(Cat.created_by_meta)
	print(type(Cat))


if __name__ == "__main__":
	main()
