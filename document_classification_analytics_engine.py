folder = "/Users/Jill/Downloads/Assignment 9 Supporting Files/problem1_supporting_files/" # locate folder

# counters
confidential = 0
secret = 0
top_secret = 0
top_secret_sci = 0

year_counts = {} # create dict.
topic_count = {}
author_count = {}

# enter for loop from 1 to 10000
for i in range(1, 10001):

    # build the number string so we can loop through each one
    if i < 10:
        num = "0000" + str(i) #ex: 00003
    elif i < 100:
        num = "000" + str(i) # ex: 0003
    elif i < 1000:
        num = "00" + str(i) # ex: 003
    elif i < 10000:
        num = "0" + str(i) # ex: 03
    else:
        num = str(i) #otherwise 3

    filename = "norida_files_" + num + ".txt" # create the string with the nums above
    path = folder + filename # create path to open

    # open file
    f = open(path, "r")
    text = f.read()
    f.close() # close

   
    
    first_line = text.split("\n")[0] # go into file and extract first line
    classification = first_line.split(":")[1].strip() # extract classification  from first line
    second_line = text.split('\n')[1] # extract second line 
    year = second_line.split(':')[1].strip() # extract yr from second line 
    third_line = text.split('\n')[2] # extract third line 
    authors_line = third_line.split(':')[1].strip() # extract author
    authors_list = authors_line.split(',') # create list of authors 
    fourth_line = text.split('\n')[3] # extract fourth line 
    topic = fourth_line.split(':')[1].strip() # extract topic from fourth line 

    cleaned_authors = [] # create empty list for individ. authors

    for author in authors_list: # for each authors in the list, append it to the empty list we just created
        cleaned_authors.append(author.strip())
    

    if year not in year_counts: # if year isnt in the dicitionary
        year_counts[year] = 1 # its value is one 

    else: # otherwise, increment its value by one 
        year_counts[year] += 1

    if topic not in topic_count: # same for topics
        topic_count[topic] =1
    else:
        topic_count[topic] += 1
        
    for author in cleaned_authors: # loop through the list of authors
        if author not in author_count: # if author isnt in the author dict.
            author_count[author] = 1 # its value is one 
        else:
            author_count[author] += 1 # otherwise increment
        

    # count each classification
    if classification == "CONFIDENTIAL":
        confidential += 1
    elif classification == "SECRET":
        secret += 1
    elif classification == "TOP SECRET":
        top_secret += 1
    elif classification == "TOP SECRET - SCI":
        top_secret_sci += 1

    # create a list of the keys in year dict.
    sorted_year =list(year_counts.keys())
    sorted_year.sort() # sort them from lowest to highest
    sorted_years = sorted_year[::-1] # reverse them 

# write the results
out = open("norida_files_report.txt", "w")

out.write("================================\n")
out.write("DOCUMENT CLASSIFICATION SUMMARY\n")
out.write("================================\n")

out.write(f"{'Classification Level':<25}{'Number of Documents':>20}\n")

out.write(f"{'CONFIDENTIAL':<25}{confidential:>6}\n")
out.write(f"{'SECRET':<25}{secret:>6}\n")
out.write(f"{'TOP SECRET':<25}{top_secret:>6}\n")
out.write(f"{'TOP SECRET - SCI':<25}{top_secret_sci:>6}\n\n")

out.write("==============================\n")
out.write("DOCUMENT PUBLICATION SUMMARY\n")
out.write("==============================\n")
out.write(f"{'Year (BBY)':<15}{'Number of Documents':>10}\n")

for y in sorted_years: # go through the years
    out.write(f"{y:<15}{year_counts[y]:>10}\n") # print year and it's value

out.write("\n======================\n")
out.write("DOCUMENT TOPIC SUMMARY\n")
out.write("======================\n")
out.write(f'{"Topic":<25}{"Number of Documents":>10}\n')

for topic in topic_count: # same for topics
    out.write(f'{topic:<25}{topic_count[topic]:>10}\n')

out.write("\n==============\n")
out.write("AUTHOR SUMMARY\n")
out.write("==============\n")
out.write(f'{"Author":<25}{"Number of Documents":>10}\n')

for name in author_count: # same for authors
    out.write(f'{name:<25}{author_count[name]:>10}\n')

out.close() # close


