from SortiPy import file_sorter
class menu:
    def main():
        print("----------------------------------------")
        print("Welcome To File Sorter")
        while True:
            print("----------------------------------------")
            print("1.Sort\n2.Change Path (Current:",file_sorter.path(),")\n3.Change Folder Properties\n4.Exit")
            print("----------------------------------------")
            ch = int(input("Enter Choice: "))
            print("----------------------------------------")

            if(ch == 4):
                break

            elif(ch == 1):
                file_sorter.sort()

            elif(ch == 2):
                x = input("Enter new Path: ")
                if(file_sorter.path(x) != -1):
                    print("New Path set as ",file_sorter.path())
                else:    
                    print("Path Doesn't Exist")

            elif(ch == 3):
                print("Current Folder & Its Extension:\n")
                transposed = file_sorter.properties(0)
                for e in transposed:
                    print(e)
                print("----------------------------------------")
                ch2 = int(input("\n1.Add Folder & Its Extension\n2.Remove Folder & Its Extensions\nEnter Choice: "))
                print("----------------------------------------")

                if(ch2 == 1):
                    name = input("Enter Folder Name: ")
                    extensions = input("Enter Extensions(seperate with ,): ")
                    file_sorter.properties(1,name,extensions)

                elif(ch2 == 2):
                    name = input("Enter Folder Name: ")
                    file_sorter.properties(2,name)
                    if(name != -1):
                        print(name,"Folder & Its Propertise Are Removed")

                else:
                    print("Invalid Choice")

menu.main()