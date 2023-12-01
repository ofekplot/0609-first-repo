# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    x="yo"
    print("yolo" + {x})

def print_person_details(age, last_name):
    exchange_rate = 3.45
    print(age)
    print(last_name[0])
    print("Current USD/ILS rate: ", exchange_rate)
    addition = age + exchange_rate
    print("Age + exchange rate = ", addition)

def is_palindrome(text):
    textSize = len(text)
    i=0
    halfWay = int(textSize/2)
    is_pelindrome = True
    while (i < halfWay):
        if text[i] !=  text[textSize-1-i]:
            is_pelindrome = False
            break
        i+=1
    print(is_pelindrome)

def count_file_stats(file):
    lines = 0
    words = 0
    chars = 0
    with open(file) as f:
        for line in f:
            print(line)
            lines +=1
            words_in_line = line.split(" ")
            words+= len(words_in_line)
            for word in words_in_line:
                word.replace("\\\n", "")
                chars+= len(word)
            #Remove end of line char from chars count
            chars -=1
        #Compensate for removal of last char that doesn't happen at last line
        chars+=1

    return lines,words,chars

def is_valid_password(password):
    is_containing_letters = False
    is_containing_numbers = False
    is_long_enough = len(password) > 5
    if (not(is_long_enough)):
        return False
    x=0
    # while(x< len(password)):

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('World')
    # print(is_palindrome("racjcar"))
    filename = "sample.txt"  # Replace with the path to your text file
    line_count, word_count, char_count = count_file_stats(
        filename)  # count_file_stats is the function name. line_count, word_count, char_count are vars that configured inside
    # print(f"Lines: {line_count}, Words: {word_count}, Characters: {char_count}")

    # password = "P@ssw0rd123"
    # print(f"Is Valid: {is_valid_password(password)}")
    # print(f"Strength Score: {password_strength_score(password)}")
    # i = 0
    # while(i<7):
    #     stars = ""
    #     j=0
    #     while(j<7):
    #         if (i==j or 7-j==i+1):
    #             stars = stars + "*"
    #         else:
    #             stars = stars + " "
    #         j+=1
    #     print (stars)
    #     i= i+1

    # last_name = input("What is your last name?")
    # age = float(input("What is your age?"))
    # # age_float = float(age)
    # print_person_details(age, last_name)
    # numbers = [408, 68, 651, 984, 237, 343, 999, 44]
    # for number in numbers:
    #     if number == 237:
    #         break
    #     if number % 2 == 0:
    #         print(number)
    # first = 75
    # second = "44"
    # result = first + second
    # print("Result is:" , first, second)
    # result = first * second
    # print(result)
    # result = second / first
    # print(result)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
