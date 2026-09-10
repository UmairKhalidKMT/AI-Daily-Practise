from ai import call_gpt
def main():
    print("Hello! I am your Chess assistant. How can I help you today?")
    grandmaster=input("Enter your favorite chess Grandmaster Name: ")
    level=input("Enter your chess level (beginner, intermediate, advanced): ")
    prompt=call_gpt(f"Please provide a chess tip for a {level} player from the perspective of {grandmaster}.")
    print(prompt)

if __name__=="__main__":
    main()

