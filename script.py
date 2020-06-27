import sys

bits_list = []

def valid_bits(bits):
    for x in bits:
        x = int(x)
        if x > 1 or x < 0:
           print 'error: input must consist of 1s and 0s only'
           return False
    return True

def analyze():
    return

# commands
# enter four bits
# enter analyze
# enter exit
while True:
    print 'enter a command'
    input = raw_input()
    if input == 'analyze':
        analyze()
    elif input == 'exit' or len(input) != 4:
        quit();
    elif valid_bits(input):
        bits_list.append(input)
