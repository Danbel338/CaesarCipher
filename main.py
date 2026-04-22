import sys
import cipher

# options
# seed
    # if numero (despues de input)
# standard input
    # if '""'
# input file
    # if '-i'
# standard output
    # if ''
# file output
    # if '-o'

def get_options(args):
    options = []
    args.pop(0)
    for arg in args:
        if arg[0] == '-':
            options.append([arg])
        elif len(options) > 0:
            options[len(options) - 1].append(arg)
        else:
            options.append([arg])
    return options

def get_input(option):
    data : str = ""
    seed : int = 1
    if option[0][0] == '-':
        if len(option) > 3:
            print("ERROR: too many arguments")
        if option[0] == '-i' and len(option) >= 2:
            with open(option[1]) as f:
                data = f.read()
            if len(option) == 3:
                seed = int(option[2])
        else:
            print("ERROR: invalid input option")
    else:
        if len(option) > 2:
            print("ERROR: too many arguments")
        data = option[0]
        if len(option) == 2:
            seed = int(option[1])
    return (data, seed)



def main(args):
    options = get_options(args)
    data_input = get_input(options[0])
    print(data_input)
    data : str = data_input[0]
    seed : int = data_input[1]

    
    encrypted_string: str = cipher.encrypt(data, seed)
    print(encrypted_string)
    print("\n\n\n")
    decrypted_string: str = cipher.decrypt(encrypted_string, seed)
    print(decrypted_string)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
