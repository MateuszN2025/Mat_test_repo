import subprocess
subprocess.run(args="clear")
print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")


"""
Very simple introduction to metaclasses.

Key idea:
- A class creates objects.
- A metaclass creates classes.

In Python, the default metaclass is `type`.
"""


# 1) Normal class: class -> object
class Dog:
	def bark(self):
		return "woof"





# 2) Metaclass: metaclass -> class
# If you need to manage class creation behavior across
# many classes, consider metaclasses.
# SimpleMeta is the metaclass.
class SimpleMeta(type):
	def __new__(mcls, name, bases, attrs):
		# `__new__` in a metaclass is called when Python builds a NEW CLASS.
		# Compare:
		# - normal class __new__/__init__ -> creates OBJECT instances
		# - metaclass __new__/__init__ -> creates CLASS objects
		#
		# Parameters:
		# - mcls: the metaclass itself (here: SimpleMeta)
		# - name: class name as a string (for example: "Cat")
		# - bases: tuple of base classes the new class inherits from
		# - attrs: dictionary with class body attributes/methods
		#          before the class object is finalized
		print(f"Creating class: {name}")

		# We can modify `attrs` to inject behavior into EVERY class
		# that uses this metaclass.
		# This creates a class attribute, not an instance attribute.
		attrs["created_by_meta"] = True
		attrs["meta_creator"] = mcls.__name__
		attrs["class_label"] = name.upper()
		attrs["base_count"] = len(bases)

		# Delegate real class creation to `type.__new__`.
		# Return value must be the created class object.
		return super().__new__(mcls, name, bases, attrs)

# Cat is a normal class created by that metaclass.
class Cat(metaclass=SimpleMeta):
	# At this point, class body is almost empty (`pass`),
	# but during class creation SimpleMeta.__new__ runs,
	# and injects `created_by_meta = True` into this class.
	pass


# Tiger is also a normal class created by SimpleMeta.
# It gets the same injected attribute automatically.
class Tiger(metaclass=SimpleMeta):
	pass

d = Dog()
print("Dog object says:", d.bark())
print("------------------------------------------")
print("Cat.created_by_meta:", Cat.created_by_meta)
print("Cat.meta_creator:", Cat.meta_creator)
print("Cat.class_label:", Cat.class_label)
print("Cat.base_count:", Cat.base_count)
c1 = Cat()
print("c1.created_by_meta:", c1.created_by_meta)
print("------------------------------------------")
print("Tiger.created_by_meta:", Tiger.created_by_meta)
print("Tiger.meta_creator:", Tiger.meta_creator)
print("Tiger.class_label:", Tiger.class_label)
print("Tiger.base_count:", Tiger.base_count)
t1 = Tiger()
print("t1.created_by_meta:", t1.created_by_meta)

print("------------------------------------------")
print("PRACTICAL EXAMPLE")


# Standard class/object approach:
# We can use a normal base class, but each child must remember
# to register itself manually.
MANUAL_PLUGINS = []


class ManualPluginBase:
	@classmethod
	def register(cls):
		MANUAL_PLUGINS.append(cls)


class CsvManualPlugin(ManualPluginBase):
	pass


class JsonManualPlugin(ManualPluginBase):
	pass


# Each class must do this explicitly.
CsvManualPlugin.register()
JsonManualPlugin.register()

print("Manual registry:", [plugin.__name__ for plugin in MANUAL_PLUGINS])


# Metaclass approach:
# Classes are registered automatically when Python creates them.
AUTO_PLUGINS = []


class PluginMeta(type):
	def __new__(mcls, name, bases, attrs):
		new_class = super().__new__(mcls, name, bases, attrs)

		# Skip the abstract root class itself.
		if name != "AutoPluginBase":
			AUTO_PLUGINS.append(new_class)
		# AUTO_PLUGINS.append(new_class)

		return new_class


class AutoPluginBase(metaclass=PluginMeta):
	pass


class CsvAutoPlugin(AutoPluginBase):
	pass


class JsonAutoPlugin(AutoPluginBase):
	pass


print("Auto registry:", [plugin.__name__ for plugin in AUTO_PLUGINS])


print("Benefits of metaclass in this example:")
print("1. No class can forget registration code.")
print("2. Registration happens once, centrally, in one place.")
print("3. Every new plugin gets the same setup automatically.")


# Quick recap:
# - Dog is a normal class used to create `d`.
# - SimpleMeta is a metaclass used to create `Cat`.

print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")  # noqa: E303
