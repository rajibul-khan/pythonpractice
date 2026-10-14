import csv
class solution:
    def memberAnalyser(filename):
        try:
            with open("filename","r") as file:
                member =[]
                reader = csv.Dictreader(file)
                
            
        except:
            print("Error occurred while reading the file.")
        