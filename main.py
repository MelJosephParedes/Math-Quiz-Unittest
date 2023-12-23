import random as rd

level = 1 #default level
operator = '+' #default op
num_items = 5 #default number of items
max_diff = 5 #default max difference

def generate_numbers(level):
    if level == 1:
        return rd.randint(1, 10), rd.randint(1, 10)
    if level == 2:
        return rd.randint(11, 100), rd.randint(11, 100)
    if level == 3:
        cLevelFrom = int(input("Custom level from: "))
        cLevelTo = int(input("Custom level to: "))
        return rd.randint(cLevelFrom, cLevelTo), rd.randint(cLevelFrom, cLevelTo)

def select_operator():
    print("[+] Addition \n[-] Subtraction \n[*] Multiplication")
    return input("Select Operator: ")
def number_of_items():
    return int(input("Number of Items: "))
def max_difference():
    return int(input("Max difference of choices from the correct answer: "))

def settings():
    global level, operator, num_items, max_diff
    level = int(input("Select Level (1,2, or 3): "))
    operator = select_operator()
    num_items = number_of_items()
    max_diff = max_difference()
def math_quiz():

    correct = 0
    wrong = 0

    for _ in range(num_items):
        num1, num2 = generate_numbers(level)
        correct_answer = None
        if operator == '+':
            correct_answer = num1 + num2
        elif operator == '-':
            correct_answer = num1 - num2
        elif operator == '*':
            correct_answer = num1 * num2
        
        choices = [correct_answer + rd.randint(-max_diff, max_diff) for _ in range(3)]
        choices.append(correct_answer)
        rd.shuffle(choices)

        print(f"{num1} {operator} {num2}")
        print(f"Choices {choices}")

        try:
            ui_answer = int(input("Select the correct answer: "))
        except EOFError:
            print("EOFError occurred using default answer")
            ui_answer = 0
        if ui_answer == correct_answer:
            print("Correct\n")
            correct += 1
        else:
            print(f"Wrong, the correct answer is {correct_answer}\n")
            wrong += 1
    
    print(f"Correct Answer: {correct}\nWrong answers: {wrong}\nRemarks: ")

if __name__ == "__main__":
    print("Simple Mathematics")
    quiz = True
    while quiz:
        print("[1] Start Quiz \n[2] Close \n[3] Settings")
        select = int(input("Select number: "))

        if select == 1:
            math_quiz()
    
        elif select == 2:
            print("Close")
            quiz = False
        elif select == 3:
            settings()   