import os
import csv

csvpath=os.path.join('Resources','election_data.csv')

total_count=0
#create the candidates array 
candidates=[]
#create a dictionary to count the votes for each candidate. Basically each candidate is a key, and their vote count is a value
candidates_dictionary={}

with open(csvpath) as csvfile:
  csvreader=csv.reader(csvfile,delimiter=',')
      
  #Skipping the header on the fist row of the csv
  csv_header=next(csvreader)
#Read each row of data after header
  for row in csvreader:
    candidates.append(row[2])
    total_count=total_count+1

#This is to create the dictionary with candidate and its vote count
  for candidate in candidates:
     if candidate in candidates_dictionary:
        candidates_dictionary[candidate]=candidates_dictionary[candidate]+1
     else:
        candidates_dictionary[candidate] = 1 #this is the initial value when the dictionary is empty
#Now, we have the dictionary of each candidate with the total votes as value-key pair
#we print the election results
print(f"Election Results")
print(f"---------------------")
print(f"Total Votes: {total_count}")
print(f"---------------------")

#This in cludes the winning percentage calc of each candidate within the print function
for candidate,vote_count in candidates_dictionary.items():
   print(f"{candidate}: {round(vote_count*100/sum(candidates_dictionary.values()),3)} % ({vote_count})")

print(f"---------------------")
#Find the winner
winner=max(candidates_dictionary,key=candidates_dictionary.get)
print(f"Winner: {winner}")
print(f"---------------------")

#Write the report to txt file at the designated path
designatedpath=os.path.join('analysis','data_analysis.txt')
with open(designatedpath, 'w') as text:
    text.write(f"Election Results"+"\n")
    text.write(f"----------------------------"+"\n")
    text.write(f"Total Votes: {total_count}"+"\n")
    text.write(f"----------------------------"+"\n")
    for candidate,vote_count in candidates_dictionary.items():
     text.write(f"{candidate}: {round(vote_count*100/sum(candidates_dictionary.values()),3)} % ({vote_count})"+"\n")
    text.write(f"----------------------------"+"\n")
    text.write(f"Winner: {winner}"+"\n")
    text.write(f"----------------------------"+"\n")