# sup3
Setup Utility for Python 3 - Create Installers easily for you Open Source Project!

# What is sup3?
sup3 is a Python 3 framework to easily create an installer for your open source project!

# How to install sup3?
As always, just run `pip install sup3`

# How can I create an Installer?
We have programmed a simple example. This will download SecureCloud from GitHub releases, and extract them. 
```python
from sup3.installer import create_directory, do_install, extract, wait_after_installation, finish_installation

create_directory("C:\SecureCloud")
do_install("https://github.com/Strawberry-Software-Industries/SecureCloud/releases/download/v1.3/SecureCloud-Server_1.3-LTS_Win64-bin.7z", "C:\SecureCloud", "SecureCloud-Server_1.3-LTS_Win64-bin.7z")
extract("C:\SecureCloud\SecureCloud-Server_1.3-LTS_Win64-bin.7z", "C:\SecureCloud")
finish_installation()
wait_after_installation()
```
