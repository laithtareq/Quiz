def Cahsher():
    Dic = {} # Add Impty dic
    while True:
        Item_Code = input("Insert Item Code: ") # Ask the user for Item Code
        Item_Name = input("Insert Item Name: ") # Ask the user for Item Name

        if Item_Code == "": # Check if stop or not
            break

        Dic[Item_Code] = Item_Name # Add the Item to Dic where key = Item_Code and value = Item_Name
        
    return Dic

print(Cahsher())