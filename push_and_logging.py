import datetime
import os
import random
x = datetime.datetime.now()
x = str(x)
print("Webpage Updating")
os.system("python I:\\Github\\python_part_2\\program\\webpage_updater.py")
print("Webpage Updated")
os.system("git add .")
os.system(f"git commit -m \"{x}\"")
os.system("git push -u origin master")
#logging
list_dir = os.listdir()

random_number = random.randint(1, 1000000000)
random_number = str(random_number)
log_file_name = f"{random_number}_log_{x}"
log_file_name = log_file_name.replace(":", "_")
log_file_name = log_file_name.replace(".", "_")
log_file_name = log_file_name.replace(" ", "_")
log_file_name = log_file_name + ".txt"
#WebPage Loging Section Shagato
print("Webpage Updating")
os.system("python I:\\Github\\python_part_2\\program\\webpage_updater.py")
print("Webpage Updated")

print("Creatinh Log")
with open(log_file_name, "w") as log_writer:
    log_writer.write(str(list_dir))
    log_writer.close()
moving_command = f"mv {log_file_name} I:\\Github\\python_part_2\\logging\\" #moving command for log text fole
opening_command = f"notepad I:\\Github\\python_part_2\\logging\\{log_file_name}"

os.system(moving_command)
os.system(opening_command)
os.system("git add .")
os.system(f"git commit -m \"{x}\"")
os.system("git push -u origin master")
print("logged perfectly")


