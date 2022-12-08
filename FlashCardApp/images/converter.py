def conversion_to_csv(filename):
    with open(filename) as f:
        raw_data = f.readlines()
    list_data = [line.strip().split() for line in raw_data]
    for line in list_data:
        for i in range(len(line)):
            if "," in line[i]:
                line[i] = line[i].replace(",", " ")
        if len(line) == 3:
            line[0] = "," + line[0]
        else:
            line[0] = line[0].rstrip(".")
    with open("{}.csv".format(filename.rstrip(".txt")), "a") as csvfile:
        for line in list_data:
            csvfile.write("{}\n".format(",".join(line)))