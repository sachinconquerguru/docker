import os
import json
from rich.console import Console
from rich.text import Text
console = Console()

def main_menu():    
    print('1.Status of containers')
    print('2.Download new Image')
    print('3.Run container')
    print('4.Delete Container')
    print('5.Network details of container')
    print('6.Modify Network details of contaniner')
    print('7.Exit')

def status_of_container():
    print(os.popen("docker ps -a").read())

def download_new_img():
    image = input("Enter the image name to search :")
    cmd = f"docker pull {image}"
    down = os.popen(cmd).read()
    console.print(down,style="bold green")

def run_container():
    image_name = input("Enter the image name to search :")
    container = input("Enter the container name to search :")
    cmd = f"docker run --name {container} -it {image_name}"
    os.system(cmd)

def Delete_Container():
    container_name = input("Enter the container name to delete :")
    cmd = f"docker rm {container_name}"
    res = os.popen(cmd).read()
    print(f"{res}is removed successfully")

def Network_details_of_container():
    res = os.popen("docker network inspect bridge").read()
    container_json = json.loads(res)[0]
    for i in container_json["Containers"].values():
        print(f'Image Name | {i["Name"]} | Mac Address | {i["MacAddress"]} | IPV4 Address | {i["IPv4Address"]}' )

def Modify_Network_details_of_contaniner():    
    print("-------Network details--------")
    print(os.popen("docker network ls").read())
    network_name = input("Enter the network name : ")
    container_image = input("Enter the container name to disconnect from network :")
    print(f"Disconnecting {container_image} from {network_name}")
    cmd =f"docker network disconnect {network_name} {container_image}"
    print(os.popen(cmd).read())
    console.print("Disconnected network",style="bold blue")
    print(f"Connecting {container_image} to  {network_name}")
    cmd1 = f"docker network connect {network_name} {container_image}"
    print(os.popen(cmd1).read())
    console.print("Connected to network",style="bold blue")

operations = {
    "1":status_of_container,
    "2":download_new_img,
    "3":run_container,
    "4":Delete_Container,
    "5":Network_details_of_container,
    "6":Modify_Network_details_of_contaniner
}

while True:
	main_menu()
	ch = input("Enter Choice: ")
	operations[ch]()

