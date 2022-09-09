from colorama import Fore, Style

def print_colored(color):
    def new_print(*args, **kwargs):
        args = [str(arg) for arg in args]
        if len(args) == 0:
            return print(*args, **kwargs)
        if len(args) == 1:
            [arg] = args
            return print(color + arg + Style.RESET_ALL, **kwargs)
        first, *middle, rest = args
        return print(color + first, *middle, rest + Style.RESET_ALL, **kwargs)
    return new_print

print_error = print_colored(Fore.RED)
print_warning = print_colored(Fore.YELLOW)
print_success = print_colored(Fore.GREEN)
