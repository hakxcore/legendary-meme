#!/bin/python
from __future__ import print_function
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
from terminaltables import SingleTable
print(Fore.BLUE+Back.YELLOW+"Hi My name is Mukesh Kumar "+ Fore.YELLOW+ Back.BLUE+"Get this tool from https://github.com/hakxcore/legendary-meme            ") 
table_instance = SingleTable([["""                                                                     
                         .-==++*++*+*+=:                    
                     -+*%@@@@@@@@@@@@@@@@%*:                
                   =%@@@@@@@@@@@@@@@@@@@@@@@%+.             
                  +@@@@@@@@@@@@@@@@@@@@@@@@@@@@=            
                 #@@@@@@@@@@@@@@#*%@@@@@@@@@@@@@%=          
                *@@@@@@@@@@@@*=.    :::=*@@@@@@@@@%         
               .@@@@@@@@@@@@@:            ::-=*@@@@         
               +@@@@@@@@@@@@*.         .:      -@%:         
               *=-=%@@@@@@+.         .---=:..:. #+          
              +-  .:+%@@@+     .+#%%%@%**+.:#*-.==          
              =:  -.  *@@     :-*:::-:    .:.+@%*           
              -%.  -   ..     .-+:-=*#  : -..:=#@=          
              -...-:              ::..    *+=+= *:          
               -  .                       *=..+*.           
                %-:.             ::.-.    :.-  -            
                ++.:        :  ::   :.::.  +.=  :           
                -%-:       - -- :-=:...   ::.: :.           
                 #-        - -=%%+==+=-=+=-. -::            
                 -:         -: +*%#%%*+=+@#-::.             
                 -:.        .-  ::-:--+*++-::               
                .-  :.       --.   .....:=-.                
                =    :.                 .=                  
              :=               :         :                  
             .--                ::..  :-:                   
         .::. +                    .-:=-.                   
         :    :                      -  ::                  
                       =                                         
                                          Author: Hakxcore                            
                                          Email:  anonymous_mails_box@protonmail.ch       
                                          Github: https://github.com/hakxcore             
"""]], '(hakxcore)')#banner
print(Fore.BLACK+Back.WHITE+(table_instance.table))
print()

