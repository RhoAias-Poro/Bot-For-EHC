import re

def read_file(num):
    with open("D:\Download\DiscordBot_EHC_Workshop\\text.txt", "r") as f:
        lines = f.readlines()
        global CURRENT_NUMBER_OF_LINES 
        CURRENT_NUMBER_OF_LINES = len(lines) #get current number of lines in the text file
        for str in lines:  # for each lines in the tuple find the matching pattern
            match_object = re.search(pattern=f"^Line {num}.+", string=str)
            if match_object:    
                return match_object.group()[8:]
            else:
                continue


def write_file():
    read_file(-1) # call to get number of lines in the file
    with open("D:\Download\DiscordBot_EHC_Workshop\\text.txt", "a") as f:
        user_input = input("Enter string: ")
        temp = CURRENT_NUMBER_OF_LINES +1
        f.write(f"\nLine {temp}. "+user_input)



if __name__ == '__main__':
    print(read_file(1))
   # write_file()
    
