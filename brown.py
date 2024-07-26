#  Write a Python program to test whether a passed letter is a vowel or not.
def letter_cheaker():
  while True:
       vowel=str(input('Enter a vowel or a consonant: ' ))      
       if ( vowel == 'a' or vowel == 'e' or
        vowel == 'i' or vowel == 'o' or vowel == 'u'): 
        print("Vowel")
       else: 
        print("Consonant")
letter_cheaker()