vocab={}
def add_word():
    eng=input("enter a english word: ").strip().lower()
    tr=input("enter the turkish version of the word: ").strip().lower()        
    vocab[eng]=tr
    print(f"{eng}={tr} added.")
def translate():
    eng=input("please enter you want for translate of the word: ").strip().lower()
    if(eng in vocab):
        print(f"this word {eng}={vocab[eng]}")
    else:
        print("this word absent ")
def show_list():
    print("\ndictionry:\n")
    if(not vocab):
        print("dictionary absent")
    else:
        for eng,tr in vocab.items():
            print(f"{eng}={tr}")  

while (True):
    print("\n-- choices--")
    print("1. add word")
    print("2.translate")
    print("3.show list")
    print("4. exit")

    your_choice=(input("enter a number (1,2,3,4): ")).strip()
    if(your_choice=="1"):
        add_word()
    elif(your_choice=="2"):
        translate()    
    elif(your_choice=="3"):
        show_list()
    elif(your_choice=="4"):
        print("exiting...")
        break
    else:
        print("violent choice")
        