# Print all the possible combinations when we press 3 keys on the phone keypad.

keypad = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

def printcombination(combination, curr, output, n):
    if(curr == n):
        print(*output,sep=",")
        return
    #curr: tells us which digit we are processing.
    # print all the possible combination by iterating first 1 to 3 for number an finding that index in keypad.
    for i in range(len(keypad[combination[curr]])):

        output.append(keypad[combination[curr]][i])
        print(output)

        printcombination(combination,curr + 1, output, n)
        output.pop()


combination = [4,3,4]
n = len(combination)
printcombination(combination, 0, [], n)