#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "jutair"
__date__ = "$09/09/2015 21:33:51$"
def number_to_name(number):
  
  if number==0:
      name="Rock"
      return name
  elif number==1:
      name="Spock"
      return name
  elif number==2:
      name="Paper"
      return name
  elif number==3:
      name="Lizard"
      return name
  elif number==4:
      name="Scissors"
      return name
  else:
     return "Error"
 
        
            
  
print number_to_name(0)
print number_to_name(1)
print number_to_name(2)
print number_to_name(3)
print number_to_name(4)
print number_to_name(5)

###################################################
# Output to the console should have the form:
# rock
# Spock
# paper
# lizard
# scissors

