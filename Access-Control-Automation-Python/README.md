# Access-Control-Automation-with-Python

## Overview

This project demonstrates a Python-based security automation workflow for maintaining an IP address allow list. The algorithm reviews a list of authorized IP addresses, compares it against a removal list, removes unauthorized entries, and updates the original file.

The scenario represents a healthcare environment where access to restricted systems containing sensitive patient information must be controlled through accurate authorization lists.

## Objective

Automate the process of updating an IP allow list by:

- Reading an existing allow list file
- Parsing IP addresses into a Python list
- Identifying unauthorized addresses
- Removing revoked access entries
- Writing the updated list back to the file

## Implementation

The Python script uses:

- `open()` and `with` statements for secure file handling
- `.read()` to retrieve file contents
- `.split()` to convert string data into a list
- `for` loops for iteration
- Conditional logic to identify matching IP addresses
- `.remove()` to revoke unauthorized entries
- `.join()` and `.write()` to update the file

## Security Relevance

Automating access control maintenance supports least-privilege principles by ensuring that unauthorized systems do not retain access to restricted resources. This project demonstrates how Python can be used to improve security operations efficiency and reduce manual administrative errors.

## Summary

This project demonstrates how Python can automate access control maintenance by updating an IP address allow list. The algorithm reads an existing allow list, converts the file contents into a list structure, and compares entries against a removal list. Unauthorized IP addresses are identified and removed before the updated list is written back to the original file. This workflow demonstrates how Python can support security operations by improving accuracy, reducing manual effort, and reinforcing least-privilege access control practices.

## Project Files

- [update-allow-list.py](https://github.com/cmelias-cyber/cybersecurity-portfolio/blob/main/Access-Control-Automation-with-Python/update-allow-list.py) → Python script implementing access control automation
