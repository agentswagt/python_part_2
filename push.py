import datetime
import os
import random
x = datetime.datetime.now()
x = str(x)

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
log_file_name = log_file_name + ".txt"
with open(log_file_name, "w") as log_writer:
    log_writer.write(str(list_dir))
    log_writer.close()
moving_command = f"mv {log_file_name} I:\\Github\\python_part_2\\logging\\" #moving command for log text fole
opening_command = f"notepad I:\\Github\\python_part_2\\logging\\{log_file_name}"

os.system(moving_command)
os.system(opening_command)