import time
import random

playing_area = 100
dice_face = 6

snake = {32:10, 36:6, 48:26, 62:18, 88:24, 95:56, 98:38 } #take you down

ladder = { 1:38, 4:14, 8:30, 21:41, 50:67, 71:92, 80:81 } #take you up

def get_player_names():    
    player1_name = input("Please enter a valid name for first player: ")       
    time.sleep(0.5)
    
    player2_name = input("Please enter a valid name for second player: ")
    time.sleep(0.5)
    
    print("\n Match will be played between " + player1_name + " and " + player2_name + "\n")
    
    return player1_name, player2_name

def get_dice_value():
    dice_value = random.randint(1, dice_face)
    time.sleep(1)
    print("Its a " + str(dice_value))
    return dice_value

def got_snake_bite(old_value, current_value, player_name):
    print("\n ~~~~~~~~>")
    print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value))
    time.sleep(1)

def got_ladder_jump(old_value, current_value, player_name):
    print("\n  ########")
    print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))
    time.sleep(1)

def snake_ladder(player_name, current_value, dice_value):
    time.sleep(1)
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > playing_area:
        print("You need " + str(playing_area - old_value) + " to win this game. Keep trying.")
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))

    if current_value in snake:
        final_value = snake.get(current_value)
        got_snake_bite(current_value, final_value, player_name)
    elif current_value in ladder:
        final_value = ladder.get(current_value)
        got_ladder_jump(current_value, final_value, player_name)
    else:
        final_value = current_value
    return final_value

def check_win(player_name, position):
    if playing_area == position:
        print("\n\n\nThats it.\n\n" + player_name + " won the game.")
        print("Congratulations " + player_name)
        print("\nThank you for playing the game.\n\n")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        
        exit()  #ends game
        

def start():
    print("~~~~~~~~~~~>:Welcome to SnakeLadder Game:############")
    player1_name, player2_name = get_player_names()
    player1_current_position = 0
    player2_current_position = 0
    
    while True:

        input_1 = input("\n" + player1_name + ": Hit the enter to roll dice: ")
        time.sleep(1)
        print("\nRolling dice...")
        dice_value = get_dice_value()
        print(player1_name + " moving....")
        time.sleep(1)
        player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value)
        check_win(player1_name, player1_current_position)

        input_2 = input("\n" + player2_name + ": Hit the enter to roll dice: ")
        time.sleep(1)
        print("\nRolling dice...")
        dice_value = get_dice_value()
        print(player2_name + " moving....")
        time.sleep(1)
        player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value)
        check_win(player2_name, player2_current_position)

while True:
    start()
