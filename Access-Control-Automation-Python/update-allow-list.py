# Access Control Automation with Python
# This script updates an IP allow list by removing unauthorized addresses.

import_file = "allow_list.txt"

# Open the allow list file and read its contents
with open(import_file, "r") as file:
    ip_addresses = file.read()

# Convert the string of IP addresses into a list
ip_addresses = ip_addresses.split()

# IP addresses that should be removed from the allow list
remove_list = [
    "192.168.97.225",
    "192.168.158.170",
    "192.168.201.40",
    "192.168.58.57"
]

# Remove unauthorized IP addresses from the allow list
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# Convert the updated list back into a string
ip_addresses = "\n".join(ip_addresses)

# Write the updated allow list back to the file
with open(import_file, "w") as file:
    file.write(ip_addresses)
