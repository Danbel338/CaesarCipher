import sys
import cipher
from enum import Enum


# python3 main.py (-i file | data_string) [seed_int] [mode] [output]
# mode: [-e | -d]
# output: [-o outpufile]

class Mode(Enum):
    ENCRYPT = 1
    DECRYPT = 2


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


def is_input(option):
    if option[0][0] == '-':
        if option[0] == '-i':
            match len(option):
                case 2:
                    return True
                case 3:
                    try:
                        int(option[2])
                        return True
                    except:
                        return False
                case _:
                    return False
        else:
            return False
    match len(option):
        case 1:
            return True
        case 2:
            try:
                int(option[1])
                return True
            except:
                return False
        case _:
            return False


def get_input(options):
    data : str = ""
    seed : int = 1
    option = options[0]
    try:
        if not is_input(option):
            raise Exception("ERROR: not input provided")
            sys.exit()
        if option[0][0] == '-':
            if len(option) > 3:
                raise Exception("ERROR: too many arguments")
            if option[0] == '-i' and len(option) >= 2:
                with open(option[1]) as f:
                    data = f.read()
                if len(option) == 3:
                    seed = int(option[2])
            else:
                raise Exception("ERROR: invalid input option")
        else:
            if len(option) > 2:
                raise Exception("ERROR: too many arguments")
            data = option[0]
            if len(option) == 2:
                seed = int(option[1])
    except Exception as e:
        print(e)
        sys.exit()
    return (data, seed)

def get_mode(options):
    if len(options) < 2:
       return Mode.ENCRYPT
    option = options[1]
    match option[0]:
        case '-e':
            return Mode.ENCRYPT
        case '-d':
            return Mode.DECRYPT
        case _:
            return Mode.ENCRYPT

def get_output_file(options):
    option = options[len(options)-1]
    if not (option[0] == '-o' and  len(option) == 2):
        return ''
    return option[1]

def save_to_file(data, file_name):
    with open(file_name, 'x') as f:
        f.write(data)

def ciph(data_options, mode):
    data : str = data_options[0]
    seed : int = data_options[1]
    output_string = ''
    match mode:
        case Mode.ENCRYPT:
            print("ENCRIPTAR")
            output_string: str = cipher.encrypt(data, seed)
        case Mode.DECRYPT:
            print("DESENCRIPTAR")
            output_string: str = cipher.decrypt(data, seed)
        case _:
            print("Modo desconocido")
    return output_string


def main(args):
    options = get_options(args)
    data_input = get_input(options)
    mode = get_mode(options)
    output_file = get_output_file(options)
    output_string = ciph(data_input, mode)
    if output_file == '':
        print(output_string)
    else:
        save_to_file(output_string, output_file)
    return 0




if __name__ == '__main__':
    sys.exit(main(sys.argv))
