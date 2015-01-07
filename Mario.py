from msvcrt import getch

standingMarioRight = dict()
standingMarioRight[1] = "         ▄▄▄▄       "
standingMarioRight[2] = "      ▄▀▀▓▓▓▓█      "
standingMarioRight[3] = "    ▄▀▓▓▄▄██████▄   "
standingMarioRight[4] = "   ▄█▄▄█▀░░▄░█▀▀    "
standingMarioRight[5] = "   █░░██▄░░▀░▀▀▀▄   "
standingMarioRight[6] = "   ▀▄░░▀░▄█▄░░░▄▀   "
standingMarioRight[7] = "    ▄██▄░░░▀▀█▀     "
standingMarioRight[8] = "   ▄▀▓▓▀██▀▀▀▄      "
standingMarioRight[9] = "   █▓▓▓▓█░░░░░█     "
standingMarioRight[10] = "   ██▄▓▓▓█▄▄▄█▀█    "
standingMarioRight[11] = "    ██████▄▄██▄█    "
standingMarioRight[12] = "    ███████████     "
standingMarioRight[13] = "     █▀▀▀▀▀█▀▀      "
standingMarioRight[14] = "     █▄▄▄▄▄▄█       "

crouchingMarioRight = dict()
crouchingMarioRight[1] = "         ▄▄▄▄       "
crouchingMarioRight[2] = "    ▄▀▓▓▄▄██████▄   "
crouchingMarioRight[3] = "   ▄█▄▄█▀░░▄░█▀▀    "
crouchingMarioRight[4] = "   █░░██▄░░▀░▀▀▀▄   "
crouchingMarioRight[5] = "    ▄██▄░░░▀▀█▀     "
crouchingMarioRight[6] = "   ▄▀▓▓▀██▀▀▀▄      "
crouchingMarioRight[7] = "   ██▄▓▓▓█▄▄▄█▀█    "
crouchingMarioRight[8] = "    ███████████     "
crouchingMarioRight[9] = "     █▄▄▄▄▄▄█       "

def standing_mario_right():
	for i in range(1,15):
		print(standingMarioRight[i])

def standing_mario_left():
	for i in range(1,15):
		print(standingMarioRight[i][::-1])
		
def crouching_mario_right():
	for i in range(1,10):
		print(crouchingMarioRight[i])

def crouching_mario_left():
	for i in range(1,10):
		print(crouchingMarioRight[i][::-1])

def spacing():
	print("\n\n\n\n\n\n\n\n\n\n")

direction = "right"
crouching = False
standing_mario_right()

while True:
	key = ord(getch())
	if key == 224: #Special keys (arrows, f keys, ins, del, etc.)
		key = ord(getch())
		# Right Arrow = 77, Left Arrow = 75, Down Arrow = 80, Up Arrow = 72
		if crouching == False:
			if direction == "right":
				if key == 77:
					spacing()
					standing_mario_right()
					direction = "right"
					crouching = False
				if key == 75:
					spacing()
					standing_mario_left()
					direction = "left"
					crouching = False
				if key == 80:
					spacing()
					crouching_mario_right()
					crouching = True
					direction = "right"
				if key == 72:
					spacing()
					standing_mario_right()
					crouching = False
					direction = "right"
			if direction == "left":
				if key == 77:
					spacing()
					standing_mario_right()
					crouching = False
					direction = "right"
				if key == 75:
					spacing()
					standing_mario_left()
					crouching = False
					direction = "left"
				if key == 80:
					spacing()
					crouching_mario_left()
					crouching = True
					direction = "left"
				if key == 72:
					spacing()
					standing_mario_left()
					crouching = False
					direction = "left"
		if crouching == True:
			if direction == "right":
				if key == 77:
					spacing()
					crouching_mario_right()
					direction = "right"
					crouching = True
				if key == 75:
					spacing()
					crouching_mario_left()
					direction = "left"
					crouching = True
				if key == 80:
					spacing()
					crouching_mario_right()
					crouching = True
					direction = "right"
				if key == 72:
					spacing()
					standing_mario_right()
					crouching = False
					direction = "right"
			if direction == "left":
				if key == 77:
					spacing()
					crouching_mario_right()
					crouching = True
					direction = "right"
				if key == 75:
					spacing()
					crouching_mario_left()
					crouching = True
					direction = "left"
				if key == 80:
					spacing()
					crouching_mario_left()
					crouching = True
					direction = "left"
				if key == 72:
					spacing()
					standing_mario_left()
					crouching = False
					direction = "left"