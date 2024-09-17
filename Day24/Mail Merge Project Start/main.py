#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"
with open("/Users/shifa/OneDrive/Documents/100 Days of Code The Complete Python Pro Bootcamp for 2023/Day24/Mail Merge Project Start/Input/Names/invited_names.txt") as Names_file:   
    Name = Names_file.readlines()
    print(Name) 
    
with open("/Users/shifa/OneDrive/Documents/100 Days of Code The Complete Python Pro Bootcamp for 2023/Day24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as Letter_file:
    letter_content = Letter_file.read()  
    for name in Name:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER,stripped_name)
        with open(f"/Users/shifa/OneDrive/Documents/100 Days of Code The Complete Python Pro Bootcamp for 2023/Day24/Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
