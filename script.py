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
    zerocount = [0, 0, 0, 0]
    length = len(bits_list)

    if length == 0:
        print 'pybot needs more sample data, nom nom'
        return

    for x in bits_list:
        for idx, val in enumerate(list(x)):
            if val == '0':
                zerocount[idx] += 1

    nextoutput = ''
    for x in zerocount:
        nextoutput += '0' if x / float(length) >= .5 else '1'

    print 'your next output will most likely be', nextoutput

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
