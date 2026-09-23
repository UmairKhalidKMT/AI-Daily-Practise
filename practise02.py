def kbc():
    crorePati=[["Which Python module is used for regular expressions?","re","regex","pyregex","re"],
               ["Which of the following is not a keyword in Python?","try","pass","raise","val"],
               ["What is the output of print(0.1 + 0.2 == 0.3)?","True","None","Error","False"],
               ["Which of the following is used to define a block of code in Python?","space","Brackets","Parentheses","Indentation "],
               ["What is the output of print(type([]))?","<class 'set'>","<class 'tuple'>","<class 'dict'>","<class 'List'>"]]
    money=0
    level=[1000,2000,5000,10000,20000]

    for i in range(len(crorePati)):
        print(crorePati[i][0], level[i])
        c=crorePati[i]
        print("1.",c[1]," 2.",c[2]," 3.",c[3]," 4.",c[4])

        ans=int(input("Enter your answer (1-4) or 0 to quit: "))
        if ans==0:
            break
        else:
            if c[ans]==c[4]:
                print("Correct Answer! You won Rs.", level[i], "\n")
                money=level[i]
            else:
                print("Wrong Answer! Game Over.")
                break
kbc()
        

