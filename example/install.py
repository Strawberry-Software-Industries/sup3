from sup3.installer import create_directory, do_install

create_directory("C:\Test")
do_install("https://github.com/Strawberry-Software-Industries/SecureCloud/releases/download/v1.3/SecureCloud-Server_1.3-LTS_Win64-bin.7z", "C:\Test", "SecureCloud-Server_1.3-LTS_Win64-bin.7z")
