import re

file_path = "C:\\Users\\baseb\\Downloads\\access.log"

with open (file_path , "r") as file:
    log = file.readlines()

    sorted_file = [entry for entry in log if "BoxPoke" not in entry]

    count = len(sorted_file)

    ip = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")

    unique = set(ip.findall("\n".join(sorted_file)))
    count ,unique
print (count, "\n", unique)