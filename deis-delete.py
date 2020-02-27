from subprocess import check_output
import pprint as pp
import simplejson
import sys

def main():
    f = open("./deisoutput.json", "r")
    if f.mode == 'r':
        contents = f.read()
    # print(contents)
    json_input = simplejson.loads(contents)
    # pp.pprint(json_input[0])
    # print(sys.argv[1])
    if sys.argv[1] == 'set':
        set(json_input)
    elif sys.argv[1] == 'unset':
        unset(json_input)
    else:
        print('help message')

    # cmd_result = check_output((["echo","apps:unset","-a",app_name]))
    #
    # print(cmd_result)

def set(input):
    print('do the set thing')
    for app in input:
        app_name = app["name"]
        for cpu_limit in app["cpu"]:
            limit_val = cpu_limit["limit"]
            req_val = cpu_limit["request"]
            process_name = cpu_limit["name"]
            command_result = check_output((["echo","limits:set","-a",app_name,process_name+'='+req_val+"/"+limit_val]))
            print(command_result)

if __name__ == "__main__":
    main()
