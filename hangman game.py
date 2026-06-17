import random
word_list=["rabbit","camel","lion","tiger"]
lives = 6
chosen_word= random.choice(word_list)
#print(chosen_word)


# CREATE A PLACEHOLDER AS SAME NUMBER  OF CHOSEN_WORD
placeholder=""
word_Lenght=len(chosen_word)
for position in range(word_Lenght):
      placeholder+="_"  
      print(placeholder)
      
game_over= False 
correct_letter=[]
 
while not game_over:  
    print(f"lives left{lives}")   
    guess=input("guess a letter\n").lower()
    if guess in correct_letter:
        print(f"you have gussed it already,{guess}")
    display=""
    for letter in chosen_word:
      if letter==guess:
         display+=letter
         correct_letter.append(letter)
      elif letter in correct_letter: 
          display+=letter
      else:
         display+="_"
        
    print(display)
    
    if guess not in chosen_word:
        lives-=1
        print(f"you gussed{guess},not in word")
        if lives==0:
             game_over=True
             print(f"the word was {chosen_word}")
             print("game over")
             
    if"_" not in display:
        game_over=True
        print("your win")