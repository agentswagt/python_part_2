import os
import datetime
import webbrowser as wb
time = datetime.datetime.today()
programs_list = os.listdir()

programs_list.remove("programs.html")
print(programs_list)

with open("programs.html", "w") as programs_webpage:
    for i in programs_list:
        programs_webpage.write(f"""<a href="{i}">{i}</a>""" "| time: " + str(time) + "<br>")

    programs_webpage.close()

