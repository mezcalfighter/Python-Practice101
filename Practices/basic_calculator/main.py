import sum

if __name__ == '__main__':
    answer_input = '_'
    while(answer_input != "*"):
        try:
            input1 = int(input('Enter a number: '))
            input2 = int(input('Enter a second number: '))
            result = sum.Sum(input1,input2)
            print("Total is: {}".format(result.get_sum_result()))

        except:
            if NameError:
                print('Must enter a number not a different character')

        finally:
            answer_input = input('Enter "*" if you wish to stop: ')
            if answer_input == '*':
                print('Thanks for using my program')