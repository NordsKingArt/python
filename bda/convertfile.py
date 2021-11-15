
converted = ""
with open("bda/dataset.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        splitted_line = line.split(" ");
        converted+= splitted_line[0]+","+splitted_line[1]

    file = open("bda/data.csv","w")
    file.write(converted)