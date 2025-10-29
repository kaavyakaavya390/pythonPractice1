import emoji
def emojize():
    text = input("Input: ")
    emojized = emoji.emojize(text, language="alias" )
    print(f"Output: {emojized}")

def main():
    #-----emojize----
    emojize()
    
main()
