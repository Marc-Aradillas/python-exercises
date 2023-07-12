#!/usr/bin/env python
# coding: utf-8

# # **Exercises**
# 
# ## Create a file named function_exercises.py for this exercise. After creating each function specified below, write the necessary code in order to test your function. 
# 
#  ✔️
# 

# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[1]:


# defined is_two function with input_value parameter.
def is_two(input_value):
    # used a return statement to used the str(input_value) to convert to s string literal to check if input_value is equal to the string '2'.
    return str(input_value) == '2'

# print statement used to call the functions to test with inputs.
print(is_two(2))
print(is_two('2'))
print(is_two(5))
print(is_two('hello'))


# ### INSTRUCTOR/STUDENT EXAMPLE:

# In[2]:


def is_two(input):
    
    if input == 2 or input == '2':

        return True
        
    else:

        return False


# In[3]:


print(is_two(2))
print(is_two('2'))
print(is_two(5))
print(is_two('hello'))


# In[4]:


def is_two(input):
    
    return input == 2 or input == '2'


# In[5]:


print(is_two(2))
print(is_two('2'))
print(is_two(5))
print(is_two('hello'))


# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[6]:


# definition for function name is_vowel. used input_vowel as parameter.
def is_vowel(input_vowel):
    # if-in statement used to check input_vowel in vowels list which holds vowels in lowercase .
    if input_vowel in (['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']):
        # returns true if input_vowel is equal to strings in list.
        return True
    # otherwise.
    else:
        # return false if letter is a consonant.
        return False
        
# Print statments calling function to check is_vowel function with inputs.
print(is_vowel('a'))
print(is_vowel('s'))


# ### INSTRUCTOR/STUDENT EXAMPLE:

# In[7]:


def is_vowel(input):
    if input in ('aeiou'):
        
        return True
        
    else:

        return False


# In[8]:


print(is_vowel('i'))
print(is_vowel('b'))


# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[9]:


# definition for function name is_consonant. used input_consonant as parameter.
def is_consonant(input_consonant):
    # if-not in statement used to check input_consonant in vowels list which holds vowels in lowercase .
    if input_consonant not in (['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']):
        # returns true if input_consonant is not equal to strings in list.
        return True
    # otherwise.
    else:
        # return false if letter is a vowel.
        return False
# Print statments calling function to check is_vowel function with inputs.
print(is_consonant('a'))
print(is_consonant('s'))
print(is_consonant('A'))
print(is_consonant('S'))


# ### INSTRUCTOR/STUDENT EXAMPLE:

# In[10]:


def is_consonant(input):
    if is_vowel(input):
        return False
    else:
        return True


# In[11]:


is_consonant('a')


# In[12]:


is_consonant('b')


# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[13]:


# defined the function (the_string) with parameter word.
def the_string(word):
    # assigned consonant to a string that holds all consonants in lower case and upper case.
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    # if-an statement used to check the parameter word and the first string at index 0 in word parameter with string assigned to consonants.
    if word and word[0] in consonants:
        # return the word with first letter capitalized.
        return word.capitalize()
    # otherwise.
    else:
        # return word input with no changes if it begins with vowels.
        return word
# Print statements used to call function to test string inputs.
print(the_string('word'))
print(the_string('address'))
print(the_string('dolly'))
print(the_string('echo'))
print(the_string('koolaid'))


# ### INSTRUCTOR/STUDENT EXAMPLE:

# In[14]:


def cap_first(input):
    count = 0
    new_string = ''
    for letter in input:
        if count == 0 and is_consonant(letter):
            new_string += letter.upper()
            count += 1
        else:
            new_string += letter
            count += 1
    return new_string


# In[15]:


cap_first('edwgige')


# In[16]:


cap_first('apple')


# In[17]:


cap_first('marc')


# In[18]:


def cap_first(input):
    if input[0] not in ('aeiou'):
        return input.capitalize()
    else:
        return input


# In[19]:


cap_first('marc')


# In[20]:


def cap_first(input):
    if is_consonant(input[0]):
        return input.capitalize()
    else:
        return input


# In[21]:


cap_first('marc')


# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[22]:


'''
First attempt:


# defined function name calculate_tip and used input as parameter
def calculate_tip(input):
    # assigned bill_total variable to input
    bill_total = input
    # assigned tip_rate variable to 0.15 float value to account for a 15% tip rate.
    tip_rate = 0.15
    # set tip_total equal to the multiplication between bill total and tip rate
    tip_total = bill_total * tip_rate
    # set bill_total equal to the sum of bill_total and the tip_amount
    bill_total = bill_total + tip_total
    # returns tip_total and bill total after calculations
    return tip_total, bill_total


# assigned a random amount to call the defined function and test the implementation to calculate the tip total
bill_total = 50.0 
# referenced input and fixed tip rate in function and assigned to defined fucntion and referenced parameter
tip_total, bill_total = calculate_tip(bill_total)
# prints tip_total
print("Tip total:", tip_total)
# prints bill total
print("Bill total:", bill_total)
'''

# defined function calculate_tip and assigned parameters tip_percentage and bill total
def calculate_tip(tip_percentage, bill_total):
    #if-and statements used to set tip_percentage thresholds between 0 and 1
    if tip_percentage >= 0 and tip_percentage <= 1:
        # tip_amount set equal to bill_totL multiplied by tip_percentage
        tip_amount = bill_total * tip_percentage
        # return the tip_amount
        return tip_amount
    # Otherwise
    else:
        # return invalid message
        return "Invalid tip percentage. Please provide a value between 0 and 1."

# example use
tip_percentage = 0.15
bill_total = 50.0
tip_amount = calculate_tip(tip_percentage, bill_total)
print("Tip Amount:", tip_amount)


# ### INSTRUCTOR/STUDENT EXAMPLE:

# In[23]:


def calculate_tip(bill, percentage):
    return bill * percentage


# In[24]:


calculate_tip(20, .25)


# 6. Define a function named apply_discount. It should accept an original price, and a discount percentage, and return the price after the discount is applied.

# In[25]:


# defined function to apply a discount to a price using paramaters original_price and discount_percentage.
def apply_discount(original_price, discount_percentage):
    # variable name discount_price set equal to orignial price multiplied by a percent value.
    discounted_price = original_price * discount_percentage
    # return new price after discount is applied.
    return discounted_price
    
# example use.
original_price = 20.0
discount_percentage = 0.25
disc_price = apply_discount(original_price, discount_percentage)
print("Price after discount: ", disc_price)

    
    


# ### INSTRUCTOR/STUDENT EXAMPLE:

# In[26]:


def apply_discount(price, discount):
    return price - (price * discount)


# In[27]:


apply_discount(100, .25)


# In[28]:


apply_discount(75, .50)


# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[29]:


# defined a function handle_commas with parameter input
def handle_commas(input):
    # remove commas from the input string
    result = input.replace(',', '')
    # return result
    return result


# In[30]:


handle_commas('4,567,909')


# In[31]:


# defined a function handle_commas with parameter input.
def handle_commas(input):
    # Convert input to a string, remove commas.
    result = str(input).replace(',', '')
    # Convert the modified string back to an integer and return it.
    return int(result)


# In[32]:


handle_commas('4,567,909')


# ### INSTRUCTOR/STUDENT EXAMPLE:

# In[33]:


def handle_commas(input):
    new_number = ''
    for number in input:
        if number != ',':
            new_number += number
    return new_number
    


# In[34]:


handle_commas('3,500,750,000')


# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[35]:


def get_letter_grade(input):

    if input >= 90:

        return 'A'
        
    elif input >= 80:

        return 'B'

    elif input >= 70:

        return 'C'

    elif input >= 60:

        return 'D'

    else:

        return 'F'
    


# In[36]:


get_letter_grade(90)


# In[37]:


get_letter_grade(78)


# In[38]:


get_letter_grade(59)


# In[39]:


get_letter_grade(67.50)


# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[40]:


def remove_vowels(input):

    new_string = ''

    for letter in input:

        if letter not in ('aeiou'):

            new_string += letter
            
    return new_string


# In[41]:


remove_vowels('superfragilisticexpialidocious')


# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# - anything that is not a valid python identifier should be removed
# - leading and trailing whitespace should be removed
# - everything should be lowercase
# - spaces should be replaced with underscores
# - for example:
# - Name will become name
# - First Name will become first_name
# - % Completed will become completed
# 

# In[42]:


def normalize_name(input):
    new_string = ''
    prev_letter = ''
    # remove leading and ending with whitespace
    input.strip()
    for letter in input:
        # if letter is true for letter and number
        if letter.isalnum() == True:
            new_string += letter.lower()
        elif letter == ' ' and prev_letter.isalnum() == True:
            new_string += '_'      
        else:
            new_string += ''
            prev_letter = letter
    if new_string[len(new_string)-1] == '_':
        new_string = new_string[:1]
    return new_string


# In[43]:


normalize_name('Name')


# In[44]:


normalize_name('First Name')


# In[45]:


normalize_name('% Completed')


# In[46]:


normalize_name("% Completed %")


# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
# 

# In[47]:


def cumulative_sum(input):

    new_list = []

    count = 1

    for num in input:

        list_sum = sum(input[:count])

        new_list.append(list_sum)
        
        count += 1
        
    return new_list

        


# In[48]:


cumulative_sum([1, 1,1])


# # **Additional Exercise**
# 
# - **Once you've completed the above exercises, follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment your code to explain your code.**

# # **Bonus**

# 
# 1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.
# 

# In[ ]:





# 2. Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27

# In[ ]:




