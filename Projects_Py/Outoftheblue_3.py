print("O U T   OF   T H E   BLUE\n")
print('''                                                   ___
                                             ___..--'  .`.
                                    ___...--'     -  .` `.`.
                           ___...--' _      -  _   .` -   `.`.
                  ___...--'  -       _   -       .`  `. - _ `.`.
           __..--'_______________ -         _  .`  _   `.   - `.`.
        .`    _ /\    -        .`      _     .`__________`. _  -`.`.
      .` -   _ /  \_     -   .`  _         .` |PENHURST UK|`.   - `.`.
    .`-    _  /   /\   -   .`        _   .`   |___________|  `. _   `.`.
  .`________ /__ /_ \____.`____________.`     ___       ___  - `._____`|
    |   -  __  -|    | - |  ____  |   | | _  |   |  _  |   |  _ |
    | _   |  |  | -  |   | |.--.| |___| |    |___|     |___|    |
    |     |--|  |    | _ | |'--'| |---| |   _|---|     |---|_   |
    |   - |__| _|  - |   | |.--.| |   | |    |   |_  _ |   |    |
 ---``--._      |    |   |=|'--'|=|___|=|====|___|=====|___|====|
 -- . ''  ``--._| _  |  -|_|.--.|_______|_______________________|
`--._           '--- |_  |:|'--'|:::::::|:::::::::::::::::::::::|
_____`--._ ''      . '---'``--._|:::::::|:::::::::::::::::::::::|
----------`--._          ''      ``--.._|:::::::::::::::::::::::|
`--._ _________`--._'        --     .   ''-----..............LGB'
     `--._----------`--._.  _           -- . :''           -    ''
          `--._ _________`--._ :'              -- . :''      -- . ''
 -- . ''       `--._ ---------`--._   -- . :''
          :'        `--._ _________`--._:'  -- . ''      -- . ''
  -- . ''     -- . ''    `--._----------`--._      -- . ''     -- . ''
                              `--._ _________`--._
 -- . ''           :'              `--._ ---------`--._-- . ''    -- . ''
          -- . ''       -- . ''         `--._ _________`--._   -- . ''
:'                 -- . ''          -- . ''  `--._----------`--._''')
print('''\n\nIt is 12.34 am in penhurst town,London,United Kingdom.You are Andrew, you are
returning to your apartment after a hangover with your friends.Suddenly, you hear a gun sound
nearby.\n\nDo you want to "go home" or "investigate" the situation?\n''')
command1=input("\nEnter your response: ")
if command1.lower() == "investigate":
  print('''\nYou see a shadow pass by one of the neighbour window.You go into the house.
  Suddenly, you hear a noise from the other side of the house.\n\nDo you want to "go back home" or in"investigate"?\n''')
  command1=input("\nEnter your response: ")
  if command1.lower() == "investigate":
    print('''\nYou encounter 3 doors, one is green, the other one is blue and the last one is black.\n\nWhat do you choose?\n''')
    command1=input("\nEnter your response: ")
    if command1.lower() == "blue":
      print('''\nAh! you see the killer right in front of you at a distance.suddenly you 
      realize that you have a pistol in your right pocket. You take it out and shoot his leg.
      After 10 mins the cops arrive and you explain the situation.\nThe cops arrest the killer and you return home.''')
      print("\nDo you want to listen to the news which came about the incident?(yes/no):\n")
      command1=input("\nEnter your response: ")
      if command1.lower() == "yes":
        print("\n\n")
        print('''                                                     
8b,dPPYba,   ,adPPYba, 8b      db      d8 ,adPPYba,  
88P'   `"8a a8P_____88 `8b    d88b    d8' I8[    ""  
88       88 8PP"""""""  `8b  d8'`8b  d8'   `"Y8ba,   
88       88 "8b,   ,aa   `8bd8'  `8bd8'   aa    ]8I  
88       88  `"Ybbd8"'     YP      YP     `"YbbdP"'  ''')
        print('''\n\nIt's 1.30 am at penhurst,London. A house in the penhurst town was broken into.A retired
        military officer was shot by a unknown killer whoes main motive was to take revenge on the official for \ndisclosing a confidential information.Soon after 5 mins of the killing, a 24 year old man "Andrew" passes by the house.
        Due to eerie gun shots, he gets lured into this house soon to find that the killer is still in.\nThe brave
        young man soon realizes that he has a pistol.But, instead of shooting the killer on the head,which could lead
        to 5 years in prison,He witfully aimed at the killers legs, hence making the killer limp.Thereby saving his future too.
        \nThat's all folks! Have a great day ahead! over to michael....\n\n''')
        print(''' ********** **      ** ********   ******** ****     ** *******  
/////**/// /**     /**/**/////   /**///// /**/**   /**/**////** 
    /**    /**     /**/**        /**      /**//**  /**/**    /**
    /**    /**********/*******   /******* /** //** /**/**    /**
    /**    /**//////**/**////    /**////  /**  //**/**/**    /**
    /**    /**     /**/**        /**      /**   //****/**    ** 
    /**    /**     /**/********  /********/**    //***/*******  
    //     //      // ////////   //////// //      /// /////// \n\n\n''')
        
      else:
        print(''' ********** **      ** ********   ******** ****     ** *******  
/////**/// /**     /**/**/////   /**///// /**/**   /**/**////** 
    /**    /**     /**/**        /**      /**//**  /**/**    /**
    /**    /**********/*******   /******* /** //** /**/**    /**
    /**    /**//////**/**////    /**////  /**  //**/**/**    /**
    /**    /**     /**/**        /**      /**   //****/**    ** 
    /**    /**     /**/********  /********/**    //***/*******  
    //     //      // ////////   //////// //      /// /////// \n\n\n''')
    elif command1.lower() == "green":
      print("\n\nWelcome to the poison room. Bye Bye!\nGAME OVER, DUDE!")
    else:
      print("\n\nWanna FLOAT? You've just encountered Pennywise!. You're OVER, BRUH!")
      print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠶⣦⣤⡀⠀⢸⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣷⣶⣿⣧⣠⣴⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣤⣶⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣴⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣦⠀⠀
⢸⣿⣿⣿⣦⡀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⡀
⢸⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣿⠿⢻⣿⠟⠻⠿⠻⠋⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠘⢿⡿⠉⢿⣿⣿⣿⣿⣶⣄⣀⠀⠀⠀⠀⣠⣿⣿⣧
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠈⠁⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣿⣿⠿⠋⠀⢿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇
⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠛⠛⠛⠛⠛⠉⠁⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏
⠀⠀⣦⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀
⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣋⠀⠀
⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀
⠀⠀⠀⠀⠀⠛⢿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣇⠹⡄⠀⣀⠤⠤⢄⡀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⢀⠠⠤⣀⠀⠀⣼⢋⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠻⢿⣿⣿⣿⣿⡄⢧⠀⠀⠀⠀⠀⠈⣒⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⠊⠁⠀⠀⠀⠀⢰⡏⣾⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⢿⣷⠸⡄⠀⠀⠀⠰⣿⣅⠣⠽⣢⣀⠀⠀⢠⠀⡎⠀⠀⢀⡠⢞⡩⢉⣶⠄⠀⠀⠀⡾⣸⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⢷⠀⠀⠀⠀⠙⢿⣿⡿⠟⠋⠉⠉⣓⡒⠈⠒⠚⠛⠻⠶⠶⣿⡏⠀⠀⠀⢸⢷⡟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣼⡄⠀⠀⠀⢀⣼⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⠀⠀⠀⣾⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀⣰⡟⠁⠀⠀⠀⣠⣀⣀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠘⢷⡀⠀⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⢿⡇⠀⠀⠀⠀⢿⣿⣿⣻⣿⣿⣿⡿⠇⠀⠀⠀⠀⢀⣼⡗⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠀⠀⠀⠀⠈⠒⢤⣀⠀⠀⠀⠈⠛⠛⠛⠁⠀⠀⢀⣀⡤⠖⠋⠉⠀⢀⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⡀⠀⠀⠀⠀⠙⢿⣿⣶⣶⣦⣤⣶⣶⣾⣿⡟⠁⠀⠀⢀⣠⠴⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠲⢤⡀⠀⠀⠀⢻⣿⣯⣁⣀⣀⣿⣿⠏⠀⠀⣠⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⢫⣽⣻⣿⣿⡿⠃⠀⢠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠣⡀⠀⠈⠉⠉⠉⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠲⠤⣀⣀⣠⠴⠋⠀⠀⠀⠀⠀⠀\n\n\n''')
  elif command1.lower() == "go back home":
    print("\n\nOH BOY! You are so cowardly. You just went home and slept!. Game Over!")
elif command1.lower() == "go home":
  print('''\n\nYou go home. Enjoy some time in television. See documentaries about LEGENDARY rocket scientist
  Akalnutt Kenny Netherson and sleep. What a day!.\nGAME OVER!''')   
