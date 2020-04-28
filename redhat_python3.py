import os 
os.system("tput setaf 3")
print("\t\t Welcome to the TUI ")
os.system("tput setaf 7")
print("\t\t----------------------- ")

print("""
    press 1: To create a user
    press 2: To open gedit 
    press 3: To launch firefox
    press 4: To install a package
    press 5: To check IP address
    press 6: To use python3
    press 7: To launch the docker container centos
    press 8: To check the docker images
    press 9: To use nmap
    press 10: To Configure web server
    press 11: To search 
    press 12:
    press 13:
    """)
print("Enter your choice :", end="")
ch = int(input())

if(ch==1):
    print("Enter your username:", end="")
    user_name = input()
    os.system("useradd {}".format(user_name))

elif(ch==2):
    os.system("gedit")

elif(ch==3):
    os.system("firefox &")

elif(ch==4):
    print("Enter you package name: ",end="")
    package_name = input()
    os.system("dnf install {}".format(package_name))

elif(ch==5):
    print("Do you have net-tools ?")
    print("Yes or No:",end="")
    ans = input()
    if(ans == "Yes"):
        os.system("ifconfig")
    else:
        os.system("yum install net-tools")
        os.system("ifconfig")

elif(ch==6):
    os.system("python3")


elif(ch==7):
    print("Please enter the container name:", end="")
    container_name = input()
    os.system("docker container run -it --name {} centos:7".format(container_name))

elif(ch==8):
    os.system("docker images")

elif(ch==9):
    print("Please enter the IP",end="")
    web_address = input()
    os.system("nmap {}".format(web_address))

elif(ch==10):
    os.system("dnf install httpd")
    
elif(ch==11):
    print("Enter your requirement",end="")
    file = input()
    os.system("locate {}".format(file))
    
elif(ch==9):
    pass    
    
elif(ch==9):
    pass
    
elif(ch==9):
    pass

else:
    print("Invalid option")









