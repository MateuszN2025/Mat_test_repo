# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Task: Create a function to validate device configurations
def validate_device_config(config):
    required_keys = ['hostname', 'ip_address', 'port']
    return [key in config for key in required_keys]

# Test the function
test_config = {
    'hostname': 'test-device',
    'ip_address': '192.168.1.100',
    'port': 8080
}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    print(validate_device_config(test_config))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
