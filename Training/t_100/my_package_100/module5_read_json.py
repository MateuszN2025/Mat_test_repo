import json

with open("config.json", 'r') as f:
    f1 = f.read()

print(type(f1))

f1_dict = json.loads(f1)
print(f1_dict)
print(type(f1_dict))

for k,v in f1_dict.items():
    print(f"k:{k}, v:{v}")

print("=====================")

import json

# Open and read the JSON config file
with open("config.json", "r") as file:
    config = json.load(file)

# Print the configuration
print("Configuration loaded:")
print(config)

print(type(config))

# Access individual values
print("Username:", config["username"])
print("Timeout:", config["timeout"])
print("Debug mode:", config["debug"])
