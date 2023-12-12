""" def interpret(command):
    command = command.replace("()", "o")
    command = command.replace("(", "")
    command = command.replace(")", "")

    return command  """


def interpret(command):
    # return len(command)
    command = [x for x in command]
    i, j = 0, 1

    while j < len(command):
        print(i, j)
        print(command[i],command[j])
        if command[i] + command[j] == "()":
            command[i:j+1] = "o"
          
        i, j = i + 2, j + 2
    

    return "".join([x for x in command if x.isalpha()]) 



print(interpret("GG()"))
# print(interpret("G()()()()(al)"))