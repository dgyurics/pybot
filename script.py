import sys

bits_list = []

def valid_bits(bits):
    ERROR_MESSAGE = 'error: input must consist of four binary digits'
    if len(input) != 4:
        print ERROR_MESSAGE
        return False
    for x in bits:
        if x != '1' and x != '0':
            print ERROR_MESSAGE
            return False
    return True

def analyze():
    # create probability array/list
    print bits_list

banner =  '-------------------------------------------------\n'
banner += '-- Type analyze to predict the next four bits  --\n'
banner += '-- Type exit to exit                           --\n'
banner += '-------------------------------------------------\n'
print banner

while True:
    print 'Enter four bits, or a command:'
    input = raw_input()
    if input == 'analyze':
        analyze()
    elif input == 'exit':
        quit();
    elif valid_bits(input):
        bits_list.append(input)
