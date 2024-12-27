#chess
import colorama as clr
import time
R=clr.Fore.RED
B=clr.Fore.BLUE
G=clr.Fore.GREEN
Y=clr.Fore.YELLOW
clr.init(autoreset=True)
Reset=clr.Fore.RESET
k=8
product={}
a=['a','b','c','d','e','f','g','h']
for i in range(8):
    printer=''
    for j in range(8):
        position=f"{a[j]}{k}"
        if i+1==2: 
            value="BP "
        elif i+1==1 and (j+1==1 or j+1==8): 
            value="BR "
        elif i+1==1 and (j+1==2 or j+1==7):
            value="BH "
        elif i+1==1 and (j+1==3 or j+1==6):
            value="BB "
        elif i+1==1 and j+1==4:
            value="BQ "
        elif i+1==1 and j+1==5:
            value="BK "
        elif i+1==7:
            value="WP "
        elif i+1==8 and (j+1==1 or j+1==8):
            value="WR "
        elif i+1==8 and (j+1==2 or j+1==7):
            value="WH "
        elif i+1==8 and (j+1==3 or j+1==6):
            value="WB "
        elif i+1==8 and j+1==4:
            value="WQ "
        elif i+1==8 and j+1==5:
            value="WK "
        else:
            value="OO "
        product[position]=value
    k-=1
def banner():
    banner = [
    f"{clr.Fore.BLUE}██      ███████ ██    ██ ██ ████████ ██   ██  █████  ███    ██",
    f"{clr.Fore.BLUE}██      ██       ██  ██  ██    ██    ██   ██ ██   ██ ████   ██",
    f"{clr.Fore.LIGHTBLUE_EX}██      █████    ██  ██  ██    ██    ███████ ███████ ██ ██  ██",
    f"{clr.Fore.RED}██      ██        ████   ██    ██    ██   ██ ██   ██ ██  ██ ██",
    f"{clr.Fore.LIGHTRED_EX}███████ ███████    ██    ██    ██    ██   ██ ██   ██ ██   ████",
    f"="*85,
    f"{clr.Fore.GREEN}██████   ███████  ████████   █████████  ████████  ███       ██ ███████████ █████████",
    f"{clr.Fore.GREEN}██   ██  ██   ██  ██         ██         ██        ██ ██     ██     ██      ██",
    f"{clr.Fore.LIGHTGREEN_EX}██████   ███████  ████████   █████████  ████████  ██   ██   ██     ██      █████████",
    f"{clr.Fore.LIGHTRED_EX}██       ██ ██    ██                ██  ██        ██     ██ ██     ██             ██",
    f"{clr.Fore.LIGHTRED_EX}██       ██  ███  ████████   █████████  ████████  ██       ███     ██      █████████",
    f"="*85,
    f" ♟️♟️♟️♟️♟️",
    f"♟️♟️   ♟️♟️",
    f"♟️♟️   ♟️♟️",
    f" ♟️♟️♟️♟️♟️",
    f"   ♟️♟️",
    f"   ♟️♟️",
    f"   ♟️♟️", 
    f"♟️♟️♟️♟️♟️♟️♟️♟️",
    f"="*10,
    f"CCCC  H   H  EEEE  SSSS  SSSS",
    f"C     H   H  E     S     S",
    f"C     HHHHH  EEEE  SSSS  SSSS",
    f"C     H   H  E         S     S",
    f"CCCC  H   H  EEEE  SSSS  SSSS",
    f"{Y}="*85,
    f"{G}*"*85,
    f"{Y}="*85,
    f" "*85,
    ]
    for line in banner:
        print(line)
        time.sleep(0.2)


def convertor(position):
    alphabets=['a','b','c','d','e','f','g','h']
    string=position[0]
    positionj=int(position[1])
    if string in alphabets:
        positioni=alphabets.index(string)+1
    else:
        print("Invalid position")
    return positioni,positionj
def compiler(i,j):
        alphabets=['a','b','c','d','e','f','g','h']
        string=alphabets[i-1]
        final=string+str(j)
        return final
def checker(position):
    piece=product[position]
    if piece[0]=="W":
        return True
    if piece[0]=="B":
        return False

def rule(position,target):
    piece=product[position]
    positioni,positionj=convertor(position)
    targeti,targetj=convertor(target)
    if checker(position)==True:
        defender="B"
    elif checker(position)==False:
        defender="W"
    match piece.strip():
        case "BP": 
            #normal case
            if targetj==positionj-1 and targeti==positioni and product[target] == "OO ":
                print("Case 1 true")
                return True
            #special case
            elif (targeti==positioni-1 or targeti == positioni+1) and targetj==positionj-1 and product[target] != "OO " and product[target][0]=="W":
                print("Case 2 true")
                return True
            #first move case
            elif targetj==positionj-2 and positionj==7 and targeti==positioni and product[target]=="OO ":
                print("Case 3 true")
                return True

        case "WP":
            #normalcase
            if targetj==positionj+1 and targeti == positioni and product[target] == "OO ":
                print("Case 4 true")
                return True
           # special case
            if (targeti == positioni + 1 or targeti == positioni-1) and targetj == positionj + 1 and product[target] != "OO " and product[target][0] == "B":
                print("Case 5 true")
                return True
            #first move case
            if targetj==positionj+2 and positionj==2 and targeti==positioni and product[target]=="OO ":
                print("Case 6 true")
                return True

        case "BR" | "WR":
            lfanito=False
            pieceintarget=product[target]
            if target!= position:
                #check movement in x axis
                if targetj==positionj:
                    if targeti<positioni:
                        l=-1
                    else:
                        l=1
                    while positioni!=targeti:
                        positioni=positioni+l
                        move=compiler(positioni,positionj)
                        pieceinposition=product[move]
                        if move == target and pieceinposition==pieceintarget and pieceintarget[0] in (defender, "O"):
                            print("Target found!")
                            lfanito= True
                        elif pieceinposition == "OO ":
                            continue
                        elif pieceinposition != "OO ":
                            print(f"There is {pieceinposition} in position {move}")
                            break
                        if lfanito==True:
                            break
                    return(lfanito)
                #check movement in y axis
                elif positioni==targeti:
                    if targetj<positionj:
                        l=-1
                    else:
                        l=1
                    while positionj!=targetj:
                        positionj=positionj+l
                        move=compiler(positioni,positionj)
                        pieceinposition=product[move]
                        if move == target and pieceinposition==pieceintarget and pieceintarget[0] in (defender, "O"):
                            print("Target found!")
                            lfanito= True
                        elif pieceinposition == "OO ":
                            continue
                        elif pieceinposition != "OO ":
                            print(f"There is {pieceinposition} in position {move}")
                            break
                        if lfanito==True:
                            break
                    return(lfanito)
                else:
                    print("Rook can only move straight!")
        case "WB"|"BB":
            positionic=positioni
            positionjc=positionj
            hmm=True
            if (abs(targeti-targetj)==abs(positioni-positionj) or targeti+targetj==positioni+positionj) and position!=target:
                if targeti > positioni and targetj>positionj:
                    direction=1
                elif targeti<positioni and targetj<positionj:
                    direction=-1
                elif targeti<positioni and targetj>positionj:
                    direction=-2
                elif targeti>positioni and targetj<positionj:
                    direction=2
                while (positionic!=targeti) and (positionjc!=targetj):
                    positionic+=(1 if direction in [1,2] else -1)
                    positionjc+=(1 if direction in [1,-2] else -1)
                    testpost = compiler(positionic, positionjc)
                    obstacle = product[testpost]
                    starget=product[target]
                    if testpost == target and starget[0]==defender:
                        print("Target found!")
                        return True
                    if obstacle != "OO ":
                        hmm=False
                        break
                    elif obstacle == "OO ":
                        hmm=True
                        continue
                if hmm == True:
                    print("Hmm came true!")
                    return True
                else:
                    print(f"Obstacle at {testpost}, {obstacle}!")
                    return False
            else:
                print("Bishop can only move diagonally!")
                return False
        case "BH"|"WH":
            pieceintarget=product[target]
            if (abs(targeti-positioni)==1 and abs(targetj-positionj)==2) or (abs(targeti-positioni)==2 and abs(targetj-positionj)==1):
                if pieceintarget[0] in (defender, "O"):    
                    return True
                else:
                    print(f"Blocked by {pieceintarget}")
            else:
                print("Horse move in the direction!")
        case "WQ"|"BQ":
            #Queen moveset
            if ((abs(targeti-targetj)==abs(positioni-positionj) or targeti+targetj==positioni+positionj) and position!=target) or ((target!= position)and(targetj==positionj or targeti==positioni)):
                lfanito=False
                positionic=positioni
                positionjc=positionj
                hmm=True
                pieceintarget=product[target]
                if target!= position:
                    #check movement in x axis
                    if targetj==positionj:
                        if targeti<positioni:
                            l=-1
                        else:
                            l=1
                        while positioni!=targeti:
                            positioni=positioni+l
                            move=compiler(positioni,positionj)
                            pieceinposition=product[move]
                            if move == target and pieceinposition==pieceintarget:
                                if pieceintarget[0] in (defender, "O"):
                                    print("Target found!")
                                    lfanito= True
                                else:
                                    print(f"Blocked by {pieceintarget}!")
                            elif pieceinposition == "OO ":
                                continue
                            elif pieceinposition != "OO ":
                                print(f"There is {pieceinposition} in position {move}")
                                break
                            if lfanito==True:
                                break
                        return(lfanito)
                    #check movement in y axis
                    elif positioni==targeti:
                        if targetj<positionj:
                            l=-1
                        else:
                            l=1
                        while positionj!=targetj:
                            positionj=positionj+l
                            move=compiler(positioni,positionj)
                            pieceinposition=product[move]
                            if move == target and pieceinposition==pieceintarget:
                                if pieceintarget[0] in (defender, "O"):
                                    print("Target found!")
                                    lfanito= True
                                else:
                                    print(f"Blocked by {pieceintarget}")
                            elif pieceinposition == "OO ":
                                continue
                            elif pieceinposition != "OO ":
                                print(f"There is {pieceinposition} in position {move}")
                                break
                            if lfanito==True:
                                break
                        return(lfanito)
                    elif targeti > positioni and targetj>positionj:
                        direction=1
                    elif targeti<positioni and targetj<positionj:
                        direction=-1
                    elif targeti<positioni and targetj>positionj:
                        direction=-2
                    elif targeti>positioni and targetj<positionj:
                        direction=2
                    while (positionic!=targeti) and (positionjc!=targetj):
                        positionic+=(1 if direction in [1,2] else -1)
                        positionjc+=(1 if direction in [1,-2] else -1)
                        testpost = compiler(positionic, positionjc)
                        obstacle = product[testpost]
                        pieceintarget=product[target]
                        if testpost == target:
                            if pieceintarget[0]==defender:
                                print("Target found!")
                                return True
                            else:
                                print(f"Blocked by {pieceintarget}!")
                        if obstacle != "OO ":
                            hmm=False
                            print(f"Obstacle at {testpost}, {obstacle}")
                            break
                        elif obstacle == "OO ":
                            hmm=True
                            continue
                    if hmm == True:
                        return True
                    else:
                        print(f"Obstacle at {testpost}, {obstacle}!")
                        return False
                else:
                    print("Queen = Rook+Bishop so please check its movement!")
        case "WK"|"BK":
            pieceintarget=product[target]
            if (abs(positioni-targeti)==1 or abs(positionj-targetj)==1) and position!=target:
                if pieceintarget[0] in (defender, "O"):
                    return True
                else:
                    print(f"Blocked by {pieceintarget}")
            else:
                print("King can only move in 1x1 box shape!")
        case _:
            print("None of case matched")
            return False
def board():
    winw = 0
    winb = 0
    for i in range(8, 0, -1):
        row = ""
        for j in range(8):
            dm = compiler(j + 1, i)
            piece = product[dm]
            if piece=="WK ":
                winw=1
            if piece=="BK ":
                winb=1
            if piece.startswith("B"):
                piece = f"{B}{piece}{Reset}"
            elif piece.startswith("W"):
                piece = f"{G}{piece}{Reset}"
            row += piece
        print(row)
    if winw==0 and winb==1:
        return -1
    elif winb==0 and winw==1:
        return 1
    elif winw==1 and winb==1:
        return 0

banner()
def main():
    ill=0 
    while True:
        vau=board()
        if vau==0:
            try:
                print(f"{Y}="*24)
                if ill%2==0:
                    trun=f"White's"
                elif ill%2==1:
                    trun=f"Black's"
                while True:
                    print(f"{trun} Trun!")
                    position=input("Select the peice position: ")
                    target=input("Please enter you target position: ")
                    targeti,targetj=convertor(target)
                    print("Targetj=",targetj)
                    positionpeice=product[position]
                    if positionpeice[0]==trun[0]:
                        if rule(position,target)==True:
                            if positionpeice in ["BP ", "WP "] and targetj in [8,1]:
                                if positionpeice=="BP " and targetj==1:
                                    while True:
                                        promo=input(f"{Y}Promote to (queen/horse/rook): ")
                                        if promo.lower()=="queen":
                                            product[target]="BQ "
                                            break
                                        elif promo.lower()=="horse":
                                            product[target]="BH "
                                            break
                                        elif promo.lower()=="rook":
                                            product[target]="BR "
                                            break
                                        else:
                                            print(f"No such option as {promo}!")
                                            continue
                                elif positionpeice=="WP " and targetj==8:
                                    while True:
                                        promo=input(f"{Y}Promote to (queen/horse/rook): ")
                                        if promo.lower()=="queen":
                                            product[target]="WQ "
                                            break
                                        elif promo.lower()=="horse":
                                            product[target]="WH "
                                            break
                                        elif promo.lower()=="rook":
                                            product[target]="WR "
                                            break
                                        else:
                                            print(f"No such option as {promo}!")
                                            continue
                            else:
                                product[target]=product[position]
                            product[position]="OO "
                            ill+=1
                            break
                        else:
                            continue
                    else:
                        print(f"{R}Please play your trun its {trun}'s trun!{Reset}")
                        break
            except Exception as e:
                print(f"{R}Error occured {e}!{Reset}")
            continue
        if vau==1:
            print(Y+"Game over! White won!")
            break
        if vau==-1:
            print(Y+"Gameover! Black won!")
            break
main()