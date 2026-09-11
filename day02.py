def main():
    a='2'
    b='3'
    print(int(a)+int(b))  #type casting
    c="hiiiiiiiiiiiiiiiiiiiiiii,!!!!!!!!!!!"
    d="umair"
    print(c.rstrip("!"))
    print(d.replace("umair","khalid"))

    f=input("Enter any Prime Number: ")
    f=int(f)
    if(f<2):
        print("Not a Prime Number")

    else:
        if(f % 2 == 0):
            print("Not a Prime Number")
        else:
            print("Prime Number")


if __name__ == "__main__":
    main()