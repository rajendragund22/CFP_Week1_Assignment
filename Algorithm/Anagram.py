class Anagram:
    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2

    def anagramoOrNot(self):
        if len(string1) == len(string2):
            sorted_String1 = sorted(string1)
            sorted_String2 = sorted(string2)
            if (sorted_String1 == sorted_String2):
                print(string1 + " and " + string2 + " are anagram")
            else:
                print(string1 + " and " + string2 + " are no anagram")
        else:
            print(string1 + " and " + string2 + " are no anagram")

string1=input("Enter the first string : ")
string2=input("Enter the second string : ")
obj = Anagram(string1,string2)
obj.anagramoOrNot()