# college_name: [NIRF_Ranking, "Branch-Last Rank"]
college = {
    "IIT BOMBAY": [3, "CS - 68", "EC - 464", "BS(Math) - 1191", "Economics - 2282", "Aerospace - 2388", "Chemical - 2500", "Civil - 3900", "Chemistry - 6969"],
    "IIT DELHI" : [2, "CS - 116", "MNC - 329", "EC - 622", "Computional Mech - 1154", "Mechanical - 1774", "Chemical - 2200", "Eng Physics - 2400", "Energy - 2600", "Civil - 3900"],
    "IIT MADRAS": [1, "CS - 149", "AI - 415", "EC - 835", "Computional Mech - 1154",  "Eng Physics - 1775", "Mechanical - 2302", "Aerospace - 2800"],
    "IIT KANPUR": [4, "CS - 248", "MNC - 926", "Statistics Data - 990", "EC - 1260", "Mechanical - 2730",  "Economics - 2990", "Aerospace - 3495"],
    "IIT KHARAGPUR": [5, "CS - 414", "AI - 795", "MNC - 1250", "EC - 1880", "Mechanical - 3300", "Aerospace - 4385"],
    "IIT ROORKEE": [6, "CS - 481", "AI - 677", "EC - 1970", "Mechanical - 3437"],
    "IIT GUWAHATI": [7, "CS - 607", "AI - 970", "MNC - 1000", "Mechanical - 4185"],
    "IIT HYDERABAD": [8, "CS - 649", "AI - 852", "MNC - 951", "Computational Eng - 1771", "EC - 1981", ],
    "IIT BHU": [10, "CS - 1051", "MNC - 2129", "EC - 3441", "Mechanical - 6000"]
}

mnc = [
    "IIT DELHI - 329",
    "IIT KANPUR - 926",
    "IIT HYDERABAD - 951",
    "IIT GUWAHATI - 1000 ",
    "IIT KHARAGPUR - 1250",
    "IIT BHU - 2129"
]

AI = [
    "IIT MADRAS - 415",
    "IIT ROORKEE - 677",
    "IIT KHARAGPUR - 795",
    "IIT HYDERABAD - 852",
    "IIT GUWAHATI - 970"
]

EC = [
    "IIT BOMBAY - 464",
    "IIT DELHI - 622",
    "IIT MADRAS - 835",
    "IIT KANPUR - 1260",
    "IIT KHARAGPUR - 1880",
    "IIT ROORKEE - 1970",
    "IIT HYDERABAD - 1981",
    "IIT BHU - 3441",
]

# userInput = input("Enter the college: ")
# print(college[userInput])

def persCollege(userInput):
    clgValue = college[userInput]
    for index,i in enumerate(clgValue):
       if(index==0):
           print(f"NIRF Ranking - {i}")
       else:
           print(i)
    
# user1 = input("Enter the College: ")
# print("\n")
# persCollege(user1)
# print("\n")

def rankSorter(userInput):
    if(userInput=="CS"):
        for i in college:
            a = college[i]
            print(i + " " +a[1])
    elif(userInput=="EC"):
        for i in EC:
            print(i)
    elif(userInput=="MNC"):
        for i in mnc:
            print(i)
    elif(userInput=="AI"):
        for i in AI:
            print(i)

# Main System
print(" If you want to see all the ranks in colleges. Type 1!\n", "If you want to see ranks of particular branch in different colleges. Type 2!")
userChoice = int(input("Please Enter 1 or 2: "))
if (userChoice==1):
    user1 = input("Enter the College: ")
    print("\n")
    persCollege(user1)
    print("\n")
elif(userChoice==2):
    userBranchChoice = input("Enter the name of branch you wanna check in capital letters: ")
    print("\n")
    rankSorter(userBranchChoice)
    print("\n")
else:
    pass
