# CSCI 2270 – Data Structures - Final Project 

Start by carefully reading the write-up contained in `CSCI2270_Spring22_Project.pdf`.

Please include a thorough description of your program's functionality. Imagine that you are publishing this for users who know nothing about this project. Also, include the names of the team-members/authors.

Catherine Xie

This program transfers cryptocurrency units from person to person, called "BTC". A user will 
start with a wallet with however much BTC, and can transfer payments to other users. Other
users may also transfer money to a user, but if there is insufficient BTC in one's wallet --
meaning one does not have enough funds -- then an error message will be displayed and the 
payment will not go through. 
Each payments has the information of previous senders tied with it, to assure that there can be no counterfeiting. A single payment is called a "block" and the line of previous payments before it is called the "blockchain". A user may also view the information of each payment he or she receives or sends.
