from PyDictionary import PyDictionary
from random import *

def check_if_word_in_dictionary(word):
    if dictionary.meaning(word,True) is None:
        return False
    else:
        return True
    
def green(guess,target):
    ans=[]
    for i in range(5):
        if guess[i]==target[i]:
            ans.append(i)
    return ans

def yellow(guess,target):
    check=green(guess,target)
    possible=set()
    for i in range(5):
        if i not in check:
            for j in range(5):
                if j not in check and guess[i]==target[j]:
                    possible.add(guess[i])
    return sorted(list(possible))

def test():
    assert check_if_word_in_dictionary("stump")==True
    assert check_if_word_in_dictionary("abcde")==False
    assert green("stump","stamp")==[0,1,3,4]
    assert green("stump","happy")==[]
    assert green("doors","proud")==[2]
    assert yellow("spend","stump")==["p"]
    assert yellow("doors","proud")==["d","r"]

dictionary=PyDictionary()
test()
wordgen=['early', 'heave', 'grout', 'slick', 'flirt', 'stamp', 'cheer', 'crowd', 'growl', 'bling', 'dance', 'thing', 'agent', 'wharf', 'quack', 'moody', 'thorn', 'twerp', 'payee', 'valid', 'aroma', 'crown', 'untie', 'gummy', 'liver', 'aptly', 'crimp', 'hefty', 'nifty', 'pluck', 'steep', 'finch', 'hasty', 'lunar', 'nanny', 'vowel', 'decay', 'clasp', 'amigo', 'derby', 'steed', 'dingy', 'chuck', 'bluff', 'basis', 'front', 'shirt', 'never', 'maker', 'blunt']
print(len(wordgen))
breaker=True
while breaker:
    print("WORDLE")
    print()
    target=wordgen[randint(0,50)]
    attempt=0
    while attempt<6:
        print("Guess No.",attempt+1)
        guess=input("Enter 5 letter word as guess: ")
        if check_if_word_in_dictionary(guess) and len(guess)==5:
            attempt+=1
            ans=green(guess,target)
            if len(ans)==5:
                print("Congrats ! You got the word")
                break
            else:
                if attempt!=6:
                    for i in range(5):
                        if guess[i]==target[i]:
                            print(guess[i],end="")
                        else:
                            print("-",end="")
                    print()
                    print("Other characters present: ",end="")
                    possible=yellow(guess,target)
                    for i in range(len(possible)):
                        if i==len(possible)-1:
                            print(possible[i],end="")
                        else:
                            print(possible[i],end=", ")
                    print()
        else:
            print("Invalid guess")
    else:
        print("You weren't able to get the word")
        print("The word was",target)
    while True:
        choice=input("Would you like to try again ? (Y/N): ")
        if choice in "Nn":
            breaker=False
            print("Thank you for playing!")
            break
        elif choice in "Yy":
            break
        else:
            print("Invalid Response")