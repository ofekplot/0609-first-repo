import Pillow

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filename = "sample.txt"  # Replace with the path to your text file
    my_file = open(filename, 'r+')
    print(my_file.read())
    my_file.write("Phenomenal")
    my_file.write("פנומנל")
    print(my_file.read())
     # count_file_stats is the function name. line_count, word_count, char_count are vars that configured inside
    # print(f"Lines: {line_count}, Words: {word_count}, Characters: {char_count}")
    #
    # try:
    #     f = 10/0
    #     print("Trying")
    #
    # # except BaseException as e:
    # #     print("In Except")
    #
    # finally:
    #     print("after except")
    # print ("After block")

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
