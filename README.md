

# IP Address Classifier 📍

## Overview

This Python project is designed to retrieve an IP address and classify it according to its type. It provides detailed information about the IP address, including its class and relevant characteristics.

## Features ✨

- **Retrieve IP Address**: Automatically obtain the IP address.
- **Classify IP Address**: Determine the class (A, B, C, D, E) of the IP address.
- **Detailed Information**: Display information about the IP address class.

## Requirements 🛠️

- Python 3.x
- import re,sys,os,platform
- `requests` library (for network requests)

You can install the required libraries using pip:

```bash
pip install requests
```

## Installation 📥

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Aouane-S/ip-address-classifier.git
   cd ip-address-classifier
   ```

2. **Install Dependencies**

- Since the project only uses standard libraries, no additional installations are necessary.

## Usage 🚀

1. **Run the Script**

   ```bash
   python ip_classifier.py
   ```

2. **Output**

   The script will output the IP address and its classification, including details about the class it belongs to.

## How It Works 🔍

- **IP Retrieval**: Uses network requests to fetch the IP address.
- **Classification Logic**: Analyzes the IP address and classifies it based on standard IP address ranges.

## Example 📊

```bash
$ python ip_classifier.py
IP Address: 192.168.1.1
Class: C
Information: Class C IP addresses are used for smaller networks, with a range of 192.0.0.0 to 223.255.255.255.
```

## Contributing 🤝

Feel free to fork the repository, create a branch, and submit a pull request. For any issues or feature requests, please open an issue in the GitHub repository.

