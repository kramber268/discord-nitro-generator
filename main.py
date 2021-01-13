import random
import time
import datetime
import random

chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'

def localtime():
    time = datetime.datetime.now()
    return f'[{time.strftime("%H:%M:%S")}]'

def generator(number: int):
    num = 0
    for a in range(number):
        num += 1
        CODE = 'https://discord.gift/'
        for a in range(16):
            CODE += random.choice(chars)
        time.sleep(0.4)
        print(f'{localtime()} [{num}] {CODE}')

def main():
    number = int(input('>>> '))
    print('='*53)
    generator(number)
    print('='*53)
    main()

if __name__ == '__main__':
    print('discord-nitro-generator')
    print('How many nitro codes do you need?')
    main()