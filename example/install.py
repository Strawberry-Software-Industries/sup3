from sup3.installer import create_directory, do_install, extract, wait_after_installation, finish_installation

create_directory("D:\Test")
do_install("https://github.com/Strawberry-Software-Industries/SecureCloud/releases/download/v1.3/SecureCloud-Server_1.3-LTS_Win64-bin.7z", "D:\Test", "SecureCloud-Server_1.3-LTS_Win64-bin.7z")
extract("D:\Test\SecureCloud-Server_1.3-LTS_Win64-bin.7z", "D:\Test")
finish_installation()
wait_after_installation()