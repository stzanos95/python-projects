def get_template_letter(path):
    with open(path, "r") as f:
        lines = f.readlines()
    return lines


def get_names(path):
    with open(path, "r")  as f:
        names = f.readlines()
    return [name.rstrip("\n") for name in names]


def replace_name(lines_list, name):
    ready_letter = []
    for line in lines_list:
        if "[name]" in line:
            ready_letter.append(line.replace("[name]", name))
        else:
            ready_letter.append(line)
    return ready_letter


def produce_letter(letter_lines, name, path):
    with open("{}{}".format(path, name), "w") as f:
        for line in letter_lines:
            f.write(line)


if __name__ == "__main__":
    template_letter = get_template_letter("./Input/Letters/starting_letter.txt")
    invited_names = get_names("./Input/Names/invited_names.txt")
    for invited_name in invited_names:
        named_letter = replace_name(template_letter, invited_name)
        produce_letter(named_letter, invited_name, "./Output/ReadyToSend/")
