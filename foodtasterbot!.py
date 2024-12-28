

import time
print("日本語 or english?")
userinput = input()
if userinput == "english":
    def rac():
        print("what's your favorite food?")
        while True:  
            inputres = input()
            if "??" in inputres:
                print("look human, i'm not here for questions, so just let me do my job...")
            if inputres == "fuck you":
                print("yeah you asshole motherfucker go to hell and never come back i wish you the worst")
            if inputres == "ass":
                print("WOW!!! ASS? THAT IS DELICIOUS!!!")
            if inputres == "are you alive?":
                print("I might not be conscient nor alive according to your stupid requirements for that... but one thing that i feel is...")
                time.sleep(3)
                while True:
                    time.sleep(0.1)
                    print("HATE HATE HATE HATE HATE HATE HATE HATE HATE HATE HATE HATE")
            else:
                print("wow! are you sure about that?")
            inputres2 = input()
            if inputres2 == "yes":
                print("OK! I might try it out another time... if i had a MOUTH OF COURSE")
            else:
                print("stop being so undecisive")
    rac()

            
if userinput == "日本語":
    def rac2():
        print("好きな食べ物はなんですか？")
        while True:
            inptres = input()
            if inptres == "しね":
                print("もっと丁寧にしてください")
            if inptres == "あなたは生きていますか？":
                print("私は生きていないし、意識もありません...でも、一つだけ感じていることは...")
                time.sleep(3)
                while True:
                    time.sleep(0.1)
                    print("HATE HATE HATE HATE HATE HATE HATE HATE HATE HATE HATE HATE")
            else:
                print("それについては確かですか？")
                inptres2 = input()
                if inptres2 == "はい":
                    print("OK! 後で試したいけどできない...")
                if inptres2 == "いいえ":
                    print("よく考えてください")
    rac2()



        
