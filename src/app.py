from tkinter import filedialog as fd
from os import execl
from typing import Dict

def getVersion(input_text:str):

    while True:
        i = input(f'\n{input_text}: ')

        try:
            i = float(i)
            return str(i) # This garantees that the version number will be on X.X format
        except:
            print("\nThe value must be numerical! (1, 1.1, 2.0, ...)")

def getType():
    df_types = ['Application', 'Link', 'Directory']

    while True:
        print("\nChoose a type:")

        for index in range(len(df_types)):
            print(f'[{index}] - {df_types[index]}')

        i = input("Option: ")

        if i.isnumeric():
            i = int(i)
            if i >= 0 and i < len(df_types):
                return df_types[i]

        print("\nInvalid input!")
        
def getNotEmptyString(input_text:str):

    while True:
        i = input(f'\n{input_text} (Cannot be empty): ')
        
        if i != '':
            return i

        print("\nThis field cannot be empty!")

def getListOfStrings(input_text:str):
    l = ""

    while True:
        i = input(f'\n{input_text} (Use a empty input to exit): ')
        
        if i == '':
            break

        l += f'{i[0].upper()+i[1:].lower()};'

    return l

def showTerminal():

    while True:
        print("\nShow terminal?")
        print("[Y] - Yes")
        print("[N] - No")

        i = input("Option: ")

        if i.lower() == 'y':
            return "True"
        
        if i.lower() == 'n':
            return "False"
        
        print("\nInvalid input! (Y/N)")

def getFileData():
    data = {}

    data["Version"] = getVersion("Version")
    data["Type"] = getType()
    data["Name"] = getNotEmptyString("Name")
    data["GenericName"] = input("\nGeneric name (Can be empty): ")
    data["Comment"] = input("\nComment (Can be empty): ")
    
    print("\nNow find the icon")
    input("Press ENTER to open the file dialog\n")
    data["Icon"] = fd.askopenfilename(title='Choose the icon', initialdir='~', filetypes=[('Image Files', '.png .jpg .icon')])

    print("\nNow find the executable")
    input("Press ENTER to open the file dialog\n")
    exec_path = fd.askopenfilename(title='Choose the executable', initialdir='~')
    pref = input("\nExecutable prefix (Can be empty): ")

    if pref != '':
        exec_path = pref + " " + exec_path
    
    suf = input("\nExecutable suffix (Can be empty): ")

    if suf != '':
        exec_path = exec_path + " " + suf

    data["Exec"] = exec_path
    
    data["Categories"] = getListOfStrings("Category")
    data["Keywords"] = getListOfStrings("Keyword")
    data["Terminal"] = showTerminal()

    # TODO - Add support user defined options later :P

    return data

def debugPrint(data:Dict):
    for k in data.keys():
        if data[k] != '':
            print(f'[{k}] - {data[k]}')

def writeToFile(data:Dict):
    fd = "[Desktop Entry]"

    for k in data.keys():
        if data[k] != '':
            fd += f'\n{k}={data[k]}' 
    
    with open(f'{data["Name"]}.desktop', "w") as f:
        f.write(fd)
    
    # TODO - Ask if the user wants to save directly into the ~/.local/share/applications/ directory
    print("Finished!")

def main():
    data = getFileData()
    writeToFile(data)
    
if __name__ == "__main__":
    main()