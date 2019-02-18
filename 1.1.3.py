#!/usr/bin/env python3

def is_palindrome(mot):
   inverse = '';
   for i in reversed(range(0,len(mot))):
      if (mot[i] != " "):
         inverse = inverse + mot[i]
   saisie_sans_espace = mot.replace(" ", "")
   if (inverse == saisie_sans_espace):
      return True
   else:
      return False 

saisie = input("Saisissez un mot ou une phrase, le programme va vérifier si c'est un palindrome : ")
if (is_palindrome(saisie)):
    print ("Le mot ou phrase saisi est un palindrome")
else:
    print ("Le mot ou phrase saisi n'est pas un palindrome")
