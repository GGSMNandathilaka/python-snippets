if __name__ == '__main__':
    magic_num = 9
    limit = 3
    count = 0
    num = -1
    while num != magic_num and count < limit:
        num = int(input('Enter number: '))
        count += 1
        if num == magic_num:
            print('You Won !!!')
            break
    else:
        print('You failed !!!')
