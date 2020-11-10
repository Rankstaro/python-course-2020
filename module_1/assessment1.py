# This program is a madlib joke maker
# prompt_list is a list which defines the words that the user must input
prompt_list = ["(plural) a group of people e.g. boys, farm workers", 
              "a snobbish sounding first name", 
              "a common first name", 
              "a goofy sounding first name", 
              "a mysterious location or place",
              "an object which can contain things", 
              "an unusual exclamation",
              "a tool used for cleaning",
              "a magic creature", 
              "a very attractive celebrity",
              "an attractive attribute",
              "(verb present tense) an action that one can perform with their arms e.g. clap, wave",
              "a very rich person",
              "a very profitable business",
              "(verb present tense) an action that one can perform with their legs e.g. wiggle, kick",
              "a positive emotion",
              "a crisis that is facing humanity",
              "(verb present tense) an action that one can perform with their head e.g. nod, roll",
              "a magical exclamation",
              "an exclamation when you have made a terrible mistake"
             ]
# Input_list is a list which stores the input of the user from the prompts.
input_list = list(range(0, len(prompt_list)))

# get_input give the user a prompt and recieves the input for the defined index
def get_input(itr):
    input_list[itr] = input(f"{itr}/{len(prompt_list)} - Please input a name, word or phrase for {prompt_list[itr]}: ")
# Title
print("JOKE MADLIB")
print("="*11)
print("Avoid using 'a', 'an' or 'the' in your responses, e.g. instead of 'a house', just input 'house'.\n")

# Iterate through the prompts in prompt_list and have the user populate data into input_list.
for itr in range(0, len(prompt_list)):
    get_input(itr)

print("\nHere is your result:\n")
    
print(f"""One day, a group of three {input_list[0]}, named {input_list[1]}, {input_list[2]} and {input_list[3]} were walking in a {input_list[4]}, when they spotted a {input_list[5]}.
"{input_list[6]}!", cried {input_list[3]}, "I've found this wonderous {input_list[5]}!".
"It looks filthy!", {input_list[1]} said, turning up their nose.
"Give it here.", {input_list[2]} snatched the {input_list[5]} and began cleaning the object with the {input_list[7]} that they always kept in their pocket.
Suddenly, a {input_list[8]} burst from the {input_list[5]}!

"{input_list[0]}! You have freed me from my prison. To express my gratitude I shall grant you each three wishes to come true upon my departure! What is your first wish?"
{input_list[1]}: "I wish I was happily married to {input_list[9]}".
"YOUR WISH SHALL BE GRANTED!"
{input_list[2]}: "I wish to have {input_list[10]}, so that I can attract any person I want".
"YOUR WISH SHALL BE GRANTED!"
{input_list[3]}: "I wish for my arms to constantly and uncontrollably {input_list[11]}".
"YOUR WISH SHALL BE UHH... GRANTED!"

"Now, what is your second wish?"
{input_list[1]}: "I wish that I had as much money as {input_list[12]}".
"YOUR WISH SHALL BE GRANTED!"
{input_list[2]}: "I wish that I owned {input_list[13]}, so I could make as much money as I could ever need".
"YOUR WISH SHALL BE GRANTED!"
{input_list[3]}: "I wish for my legs to constantly and uncontrollably {input_list[14]}".
"YOUR WISH SHALL BE ERM... GRANTED!"

"You must now tell me your final wish before I depart!"
{input_list[1]}: "I wish that I always felt {input_list[15]}".
"YOUR WISH SHALL BE GRANTED!"
{input_list[2]}: "I wish that {input_list[16]} was solved!".
"YOUR WISH SHALL BE GRANTED!"
{input_list[3]}: "I wish for my head to constantly and uncontrollably {input_list[17]}".
"YOUR WISH SHALL BE UMM... GRANTED!"

"{input_list[18]}!!!"

And with that, the {input_list[8]} disappeared. The three {input_list[0]} looked at eachother and sure enough their wishes had been granted.
{input_list[1]} was overcome with {input_list[15]}, their pockets full of {input_list[12]}'s money and {input_list[9]} clinging to their arm and looking at them adoringly.
{input_list[2]} had irresistible {input_list[10]}, full ownership of {input_list[13]} and worldwide recognition for finally ending {input_list[16]}.
They turned to {input_list[3]} and watched their arms {input_list[11]}, legs {input_list[14]} and head {input_list[17]}.

"I think I messed up guys...", said {input_list[3]}, "{input_list[19]}!"
""")

input("Press Enter to quit...")