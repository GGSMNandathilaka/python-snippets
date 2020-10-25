def execute_car_game():
    is_car_started = False
    while True:
        cmd = input('> ').upper()
        if cmd == 'HELP':
            print("start - to start the car\nstop - to stop the car\nquit - to exit\n")
        elif cmd == 'START':
            if is_car_started:
                print('Hey.. car is already started...')
            else:
                is_car_started = True
                print('Car started... Ready to go!')
        elif cmd == 'STOP':
            if not is_car_started:
                print('Hey.. car is already stopped...')
            else:
                is_car_started = False
                print('Car stopped')
        elif cmd == 'QUIT':
            break
        else:
            print('I don''t understand that')


if __name__ == '__main__':
    execute_car_game()
