
word_stats={}
with open("poem.txt","r") as f:
    for line in f:
        words= line.split(' ') #Splits the line into words based on space
        for word in words:
            word= word.lower()
            if word in word_stats:
                word_stats[word] += 1
            else:
                word_stats[word] = 1
print("Word Statistics:")

word_occurances =list(word_stats.values())  #Extracts only the values (counts) from dictionary  
#                                           {'hello':2, 'world':1}
#                                           → [2, 1]
max_count = max(word_occurances)#Finds the highest occurrence
# [2, 1] → max = 2
print(f"Most common word occurs {max_count} times.") #Find words with max occurrence
print("Words with max occurrence:")
for word, count in word_stats.items():
    if count == max_count:
        print(word)
        
        
 #