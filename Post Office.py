#Project name: GCDS Rust Removal AKA the GCDS Post office algorithm
#Started: 9/18/23
#Ended: 
#Current version: 0.191823

import random

postage = ""

print("Hey there! Welcome to the digital Post office")
postage = input('''
      What're you sending today?
      1) Envelope
      2) Package
      3) Other
      Enter response here: 
      ''').lower
if postage == "envelope" or "1":
    posdim1 = input("")
    posdim2 = input("")
    posdim3 = input("")