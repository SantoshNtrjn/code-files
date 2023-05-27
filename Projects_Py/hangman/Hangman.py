import random
import Hangman_art
import Hangman_words
print(Hangman_art.logo)
word_list = Hangman_words.word_list
chosen_word = random.choice(word_list)
chosen = list(chosen_word)

game_list = []

for _ in range(len(chosen_word)):
    game_list.append("_")

lives = 6
not_endgame = True 
while not_endgame:
   user_guess = input("\nEnter your guess: ").lower()

   if user_guess in game_list:
      print(f'\nYou\'ve already guessed {user_guess}\n')

   for word in range(len(chosen)):
      if user_guess == chosen[word]:
         game_list[word] = chosen[word]
   

   if user_guess not in chosen:
      print(f'\nYou guessed {user_guess}, that\'s not in the word. You lose a life.\n')
      lives -= 1
      if lives == 0:
         print("===============================================================")
         print("\nYou Lose!\n")
         print(f'The word is {chosen_word}. Better luck next time :)\n')
         not_endgame = False
   print(" ".join(game_list))
   print(f'\n{Hangman_art.life[lives]}')
   print(f'\n{Hangman_art.stages[lives]}')

   if '_' not in game_list:
      print("You Won!")
      not_endgame = False

