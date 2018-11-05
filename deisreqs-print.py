from subprocess import check_output
import pprint as pp
import json

results = []
memory_dict = {
    "name": "",
    "request": "",
    "limit": ""
}
cpu_dict = {
    "name": "",
    "request": "",
    "limit": ""
}
# app_result = {
#     "name": "",
#     "memory": [],
#     "cpu": []
# }
apps = []

app_gather = check_output(["deis","apps:list"])
app_gather = app_gather.split("\n")
for app_name in app_gather:
    if app_name != '=== Apps':
        if app_name != '':
            apps.append(app_name)

for app in apps:
    app_result = {
        "name": "",
        "memory": [],
        "cpu": []
    }
    app_string = check_output(["deis","limits:list","-a",app])
    app_split = app_string.split("\n\n")
    #Name Parsing
    name_split = app_split[0].split(" ")
    print(name_split[1])
    #Memory parsing
    mem_split = app_split[1].split("\n")
    print("  -MEMORY-")
    for entry in mem_split:
        entry = ' '.join(entry.split())
        entry = entry.split(' ')
        if entry[0] != "---":
            try:
                print("  "+entry[0])
                print("    "+entry[1])
                # app_result["memory"].append(memory_dict.copy())
            except:
                pass
    #CPU parsing
    cpu_split = app_split[2].split("\n")
    print("  -CPU-")
    for entry in cpu_split:
        entry = ' '.join(entry.split())
        entry = entry.split(' ')
        if entry[0] != "---":
            if entry[0] != "":
                try:
                    print("  "+entry[0])
                    print("    "+entry[1])
                    # print("    Request - "+req_split[0])
                    # print("    Limit - "+req_split[1])
                    # app_result["cpu"].append(cpu_dict.copy())
                except:
                    pass
    # results.append(app_result.copy())

# results=json.dumps(results)
# pp.pprint(results)
