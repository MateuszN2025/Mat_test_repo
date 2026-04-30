def wraping(func):
    def wraping_():
        import subprocess
        subprocess.run(args="clear")
        print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
        func()
        print("\n➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")  # noqa: E303
    return wraping_