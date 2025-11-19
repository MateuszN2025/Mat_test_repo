import module3_main

# When You run it nothing will happen because in imported module we have:
# if __name__ == "__main__":
#     print(__name__)
# It means that this condition protect from running program from different file
# if __name__ == "__main__" makes code run only when you run the file yourself, not when someone imports it.

module3_main.anyfunc()