import json

data = open("data.txt", "r")
data = data.read()

speed_list = data.split("---------------------------------------------------------------------")


speed_dict = {}

for block in speed_list:
    speeds = []
    timestamp = ""
    lines = block.split("\n")
    
    if(len(lines) > 7):
        for line in lines:
            if("Upload" in line):
                speeds.append(line)
            if("Download" in line):
                speeds.append(line)

            if("2019" in line):
                timestamp = line
        
        speed_dict[timestamp] = speeds

    else:
        speeds.append("Download: 0.00 Mbits/s")
        speeds.append("Upload: 0.00 Mbits/s")
        
        for line in lines:
            if("2019" in line):
                timestamp = line
                break
        
        speed_dict[timestamp] = speeds


print(json.dumps(speed_dict))