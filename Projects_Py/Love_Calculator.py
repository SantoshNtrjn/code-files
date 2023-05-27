print('''                     ..    d$P              $$      `$b
                    z$"   $$F               4$$      $$L
                    $$   4$$                 $$.     4$$    ,z$P
                    $$   $$'                 $$F      $$   $$$P
                   $$$   $$                  $$f      $$   ""`
                  $'$$; 4$F      .,_         $$'      $$
                .$' ?$L 4$'   .d$" `?    zee $$   ,ec $F  d$F z$$   ,ce,.
              .d$ee. $$ 4$'  d$"   z$  $$"  .$f.d$"  4$  4$$ 4$$P z$P?$$$
             d$" "?$$d$,`$  $$F   z$f,$$    $$.$$    $P  $$% $$$4$"   4$$
.$"%.     ,p$"        $$ $ J$$  z$$$ $$"  .$$ $$"  .$$C 4$P  $$$"     $$f
`$.     ,d$b****q,     $.$ $$$$$P $$.$$b.$P4$ $$L.$P4$F $P  4$P     .$$"
 `?$$g$P"        "     `b' `??"   "?"^?F"   $$`?PF"  $$ "   P'     eF
                    
                    |   P   R   E   S   E   N   T   S   |
                    
                    ''')

 #for ascii art go to asciiart.com

print("\nTHE L  O  V  E  CALCULATOR")
print("\nWelcome!\n")
my_name =input("What is your name?\n").lower()
crush_name =input("\nWhat is their name?\n").lower()

joint = f'{my_name}{crush_name}'
t = joint.count("t")
r = joint.count("r")
u = joint.count("u")
e = joint.count("e")

l = joint.count("l")
o = joint.count("o")
v = joint.count("v")
e = joint.count("e")

true = t+r+u+e
love = l+o+v+e
love_score =int( f'{true}{love}')

if love_score < 10 or love_score > 90:
  print(f'Your score is {love_score}, you go together like coke and mentos.')
elif love_score>=40 and love_score<=50:
  print(f'Your score is {love_score}, you are alright together.')
else:
  print(f'your score is {love_score}.')
