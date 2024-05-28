# Import Modules
import tkinter as tk
import random

#--------------------------------------------#
# ----------------- VARIABLES -------------- #
#--------------------------------------------#
dark_color = "#5e7b5f"
light_color = "#E0FBE2"
userNo = 0
pcNo = 0


#--------------------------------------------#
# --------------- GAME WINDOW -------------- #
#--------------------------------------------#
# Make The Game Window
window = tk.Tk()
window.title("Tic Tac Toe - nHaji")
window.minsize(850, 650)
window["bg"] = light_color


#--------------------------------------------#
# -------- MAIN FUNCTION FOR START --------- #
#--------------------------------------------#
def start_playing():

    if pc_first_check.get() == 1:
        first_player = "pc"
    else:
        first_player = "user"
    if heigh_pc_level_check.get() == 1:
        pc_level = "heigh"
    else:
        pc_level = "low"


    # Remove First Player Section Elements
    forForget = [start_btn, user_first_que, user_first_btn, pc_first_btn, pc_level_que, low_pc_level, heigh_pc_level ]
    for element in forForget:
        element.grid_forget()

    window.rowconfigure(0, weight=0)
    window.rowconfigure(3, weight=1)
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=0)

    # Function To Disable Buttons
    def disable_btn(btn):
        btn["disabledforeground"] = dark_color
        btn["state"] = "disabled"

    def pc_choicing_algorithm():
        for choice in winner_choices:
            if(choice[0]["text"] == choice[1]["text"] == "O" and choice[2] in btns):
                btn = choice[2]
                break
            elif(choice[0]["text"] == choice[2]["text"] == "O" and choice[1] in btns):
                btn = choice[1]
                break
            elif(choice[1]["text"] == choice[2]["text"] == "O" and choice[0] in btns):
                btn = choice[0]
                break
            elif(choice == winner_choices[len(winner_choices) - 1]):
                for choice in winner_choices:
                    if(choice[0]["text"] == choice[1]["text"] == "X" and choice[2] in btns):
                        btn = choice[2]
                        break
                    elif(choice[0]["text"] == choice[2]["text"] == "X" and choice[1] in btns):
                        btn = choice[1]
                        break
                    elif(choice[1]["text"] == choice[2]["text"] == "X" and choice[0] in btns):
                        btn = choice[0]
                        break
                    elif(choice == winner_choices[len(winner_choices) - 1]):
                        for choice in winner_choices:
                            if(choice[0]["text"] == "O" and choice[1] in btns and choice[2] in btns):
                                btn = random.choice([choice[1],choice[2]])
                                break
                            elif(choice[1]["text"] == "O" and choice[0] in btns and choice[2] in btns):
                                btn = random.choice([choice[0],choice[2]])
                                break
                            elif(choice[2]["text"] == "O" and choice[0] in btns and choice[1] in btns):
                                btn = random.choice([choice[0],choice[1]])
                                break
                            else:
                                btn = random.choice(btns)
        return btn

    # Function For PC Choice
    def pc_touch():
        if len(btns) > 0:
            if pc_level == "heigh":
                btn = pc_choicing_algorithm()
            else:
                btn = random.choice(btns)
            btn["text"] = "O"
            btns.remove(btn)
            disable_btn(btn)
            if check_choices("O"):
                return
        else:
            result_label["text"] = "Tie, No Winner!"
            result_label["bg"] = "#7e0000"
            result_label["fg"] = "white"

    # Function For User Choice
    def user_touch(btn):
        btn["text"] = "X"
        btns.remove(btn)
        disable_btn(btn)
        if check_choices("X"):
            return
        pc_touch()

    # Function For Check If There Is Winner
    def check_choices(option):
        for choice in winner_choices:
            if(choice[0]["text"] == choice[1]["text"] == choice[2]["text"] == option):
                global userNo, pcNo
                for btn in choice:
                    btn["bg"] = dark_color
                    btn["disabledforeground"] = "white"
                if(option == "X"):
                    userNo += 1
                else:
                    pcNo += 1
                result_label["text"] = f"{option} Win!!!"
                result_label["bg"] = dark_color
                result_label["fg"] = "white"
                score_label["text"] = f"You= {userNo}     Computer= {pcNo}"
                for btn in btns:
                    disable_btn(btn)
                return True
            elif len(btns) == 0 and first_player == "pc":
                result_label["text"] = "Tie, No Winner!"
                result_label["bg"] = "#7e0000"
                result_label["fg"] = "white"
    # Function For Restart The Game
    def restart_game():
        result_label["text"] = ""
        result_label["bg"] = light_color
        add_buttons()
        if first_player == "pc":
            pc_touch()
    
    # Score Label
    score_label = tk.Label(text=f"You= {userNo}     Computer= {pcNo}", master=window, font=("Times", 20, "bold"), fg=dark_color, bg=light_color)
    score_label.grid(row=0)


    # Result Label
    result_label = tk.Label(master=window, font=("Times", 30), bg=light_color)
    result_label.grid(row=1, pady=10)

    # Restart Button
    restart_btn = tk.Button(text="Play Again", master=window, command=restart_game,height=1,font=("Times",25, "bold"), bg=dark_color, fg="white", border=0, cursor="circle",activebackground="white", activeforeground=dark_color)
    restart_btn.grid(row=2)


    #--------------------------------------------#
    # ----------- BUTTONS ---------------------- #
    #--------------------------------------------#

    # Playing Buttons Frame
    playing_space_frame = tk.Frame(master=window, bg=dark_color, padx=3,pady=3)
    playing_space_frame.grid(row=3)

    playing_space_frame.columnconfigure([0,1,2], weight=1)

    # Function For Add Buttons To The Game
    def add_buttons():
        global btns
        btns = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(master= playing_space_frame, width=3, height=1, font=("", 50), bg="white", borderwidth=0, cursor="tcross")
                button["command"] = lambda btn=button : user_touch(btn)
                btns.append(button)
                button.grid(row=i, column=j, padx=2, pady=2)
        global winner_choices
        winner_choices = [
            [btns[0], btns[1], btns[2]], 
            [btns[3], btns[4], btns[5]], 
            [btns[6], btns[7], btns[8]],
            [btns[0], btns[3], btns[6]],
            [btns[1], btns[4], btns[7]],
            [btns[2], btns[5], btns[8]],
            [btns[0], btns[4], btns[8]],
            [btns[2], btns[4], btns[6]]
        ]
    
    # Add Buttons When Start The Game
    add_buttons()
    #--------------------------------------------#
    #--------------------------------------------#

    if first_player == "pc":
        pc_touch()


window.rowconfigure([0,6], weight=1)
window.columnconfigure([0,1], weight=1)

#--------------------------------------------#
# ---------- DISABLE OTHER CHOICE ---------- #
#--------------------------------------------#
def disable_other(otherChoice):
    if otherChoice["state"] == "normal":
        otherChoice["state"] = "disabled"
    else:
        otherChoice["state"] = "normal"
#--------------------------------------------#
#--------------------------------------------#

#--------------------------------------------#
# ---------- FIRST PLAYER ELEMENTS --------- #
#--------------------------------------------#
# Question For First Player
user_first_que = tk.Label(
    text="Who will play first?", 
    master=window, font=("Times", 20, "bold"), 
    fg=dark_color, 
    bg=light_color
    )
user_first_que.grid(row=1, column=0, columnspan=2, pady=10)

# User First Play Button
user_first_check = tk.IntVar()
user_first_btn = tk.Checkbutton(
    text="You", 
    master=window, 
    width=10,
    height=1,
    font=("Times",25, "bold"), 
    bg=dark_color, 
    fg="white", 
    border=0, 
    cursor="circle", 
    activebackground="white", 
    activeforeground=dark_color,selectcolor="red", 
    variable=user_first_check, 
    command=lambda :disable_other(pc_first_btn)
    )
user_first_btn.grid(row=2, column=0, pady=10)

# PC First Play Button
pc_first_check = tk.IntVar()
pc_first_btn = tk.Checkbutton(
    text="Computer", 
    master=window, 
    width=10,
    height=1,
    font=("Times",25, "bold"),
    bg=dark_color, 
    fg="white", 
    border=0, 
    cursor="circle", 
    activebackground="white", 
    activeforeground=dark_color, 
    selectcolor="red", 
    variable=pc_first_check, 
    command=lambda :disable_other(user_first_btn)
    )
pc_first_btn.grid(row=2, column=1, pady=10)
#--------------------------------------------#
#--------------------------------------------#

#--------------------------------------------#
# ------------ PC LEVEL ELEMENTS ----------- #
#--------------------------------------------#
# Question For Level Of Pc
pc_level_que = tk.Label(
    text="Computer intelligence level?", 
    master=window, 
    font=("Times", 20, "bold"), 
    fg=dark_color, 
    bg=light_color
    )
pc_level_que.grid(row=3, column=0, columnspan=2, pady=10)

# Low Level For PC Btn
low_pc_level_check = tk.IntVar()
low_pc_level = tk.Checkbutton(
    text="Low", 
    master=window, 
    width=10,
    height=1,
    font=("Times",25, "bold"), 
    bg=dark_color, 
    fg="white", 
    border=0, 
    cursor="circle", 
    activebackground="white", 
    activeforeground=dark_color, 
    selectcolor="red", 
    variable =low_pc_level_check, 
    command=lambda :disable_other(heigh_pc_level)
    )
low_pc_level.grid(row=4, column=0, pady=10)

# PC First Play Button
heigh_pc_level_check = tk.IntVar()
heigh_pc_level = tk.Checkbutton(
    text="Heigh", 
    master=window, 
    width=10,
    height=1,
    font=("Times",25, "bold"), 
    bg=dark_color, 
    fg="white", 
    border=0, 
    cursor="circle", 
    activebackground="white", 
    activeforeground=dark_color,
    selectcolor="red", 
    variable=heigh_pc_level_check, 
    command=lambda :disable_other(low_pc_level)
    )
heigh_pc_level.grid(row=4, column=1, pady=10)
#--------------------------------------------#
#--------------------------------------------#

#--------------------------------------------#
# ------------ START BTN ELEMENTS ---------- #
#--------------------------------------------#
start_btn = tk.Button(
    text="Start Playing", 
    master=window, 
    command=start_playing, 
    width=15,
    height=3,
    font=("Times",25, "bold"), 
    bg=dark_color, 
    fg="white", 
    border=0, 
    cursor="circle", 
    activebackground="white", 
    activeforeground=dark_color
    )
start_btn.grid(row=5, column=0, columnspan=2)
#--------------------------------------------#
#--------------------------------------------#

# Run The Game
window.mainloop()