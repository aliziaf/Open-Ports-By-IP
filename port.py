# import socket , subprocess ,sys
# from colorama import Fore,init
# init()


# ports ={'x':20 , 'y':21 , 'http':80 , 'https': 443 , 'w':444 , 'NetBios': 445 , 'q' : 446 , 'k':447}
# #ports = [20,21,79,80,443,444,445,446,447]
# subprocess.call('cls', shell=True)
# for port in ports:
#     #print(res[port]) 
#     port = int(port)
#     #ip = "192.168.0.100"
#     ip = "127.0.0.1"
#     location = (ip,port)
#     a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     result_of_check = a_socket.connect_ex(location)


#     if result_of_check == 0:

#         print(f"{Fore.GREEN}Port {port} is open{Fore.RESET}")
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#     else:

#         print(f"{Fore.RED}Port {port} is not open {Fore.RESET}")


#     a_socket.close()

import socket , subprocess ,sys
from colorama import Fore,init
init()


ports ={'x':20 , 'y':21 , 'http':80 , 'https': 443 , 'w':444 , 'NetBios': 445 , 'q' : 446 , 'k':447}
#ports = [20,21,79,80,443,444,445,446,447]
subprocess.call('cls', shell=True)
ip = str(input("Enter Ip :"))
print("SERVICE | Port num | STATE")
for port , nums in ports.items():
    #print(res[port]) 
    nums = int(nums)
    #ip = "192.168.0.100"
    #ip = "127.0.0.1"
    location = (ip,nums)
    a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result_of_check = a_socket.connect_ex(location)


    if result_of_check == 0:
        
        print(f"{Fore.GREEN}{port}|{nums}|open{Fore.RESET}")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    else:

        print(f"{Fore.RED}{port}|{nums}|CLOSED{Fore.RESET}")


    a_socket.close()























