my_dict = {
    "egg" :"tokhme morgh",
    "milk":"shir",
    "fruits":"mive",
    "meat":"goosht"
}
my_word = input("Enter an English word:")
if my_word in my_dict:
    print(my_dict.get(my_word))
else:
    print("Your word is not existed in my dictionary!!")
