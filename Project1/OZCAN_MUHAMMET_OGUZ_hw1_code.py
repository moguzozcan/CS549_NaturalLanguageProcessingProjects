
# coding: utf-8

# In[4]:


# Question 1
import re

def remove_one_token_lines(in_file_tr, in_file_eng):
    """
    This method removes all lines with one token in a given file, and writes the result to another file

    :param in_file_tr: turkish file name from which we will remove the tokens of length one
    :param in_file_eng: english file name from which we will remove the corresponding lines (look at project description)
    :param out_file_name: file where we will write the results of our operation

    :return morph_line_count: number of lines in new files for both tr and eng files
    """

    # Remember to write your results to the files morph.tr and morph.eng
    
    num_lines_in_file_tr = sum(1 for line in open(in_file_tr))
    num_lines_in_file_eng = sum(1 for line in open(in_file_eng))
    
    # Print line numbers in the original files just to check correctness
    print("Number of lines in the original document in TR", num_lines_in_file_tr)
    print("Number of lines in the original document in EN", num_lines_in_file_eng)

    # While reading original.eng utf-8 format gave the following error so I read it with another decoding 'windows-1252'
    # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf6 in position 6091: invalid start byte

    with open(in_file_tr, encoding='utf-8') as in_tr, open(in_file_eng, encoding='iso-8859-1') as in_en, open("morph.tr", "wb") as out_tr, open("morph.eng", "wb") as out_eng:
        morph_line_count_tr = 0
        indexes = []
        for i, line in enumerate(in_tr):
            regex = "^(\S+|)(\s+)(\S+\s*)+" # This regex matches lines with more than one word, ^(\S+)$
            pattern = re.compile(regex)
            
            for match in re.finditer(pattern, line):
                #print ('Found on line %s: %s' % (i+1, match.group()))
                morph_line_count_tr = morph_line_count_tr + 1
                out_tr.write(match.group().encode("utf-8"))
                indexes.append(i)
        print("Total lines after eliminating one word line is: ", morph_line_count_tr)
        print("So there are : ", num_lines_in_file_tr - morph_line_count_tr, " lines with one word")
        
        #Loop through the eng file with the same indexes found in the Turkish file
        indexes_array_count = 0
        for i, line in enumerate(in_en):
            if(i == indexes[indexes_array_count]):
                out_eng.write(line.encode("iso-8859-1", 'ignore'))  # utf-8
                #print(line)
                indexes_array_count = indexes_array_count + 1
        
        morph_line_count_eng = morph_line_count_tr
    return morph_line_count_tr, morph_line_count_eng


# In[5]:


remove_one_token_lines("train.baseline.tr", "train.baseline.eng")  #remove_one_token_lines("original.tr", "original.eng")


# In[6]:


# Question 2a
def get_num_of_tokens(in_file_name):
    """
    Finds the number of tokens in a given file
    :param in_file_name: name of the input file

    :return num_of_tokens: the number of tokens in the given file
    """
    if "eng" not in in_file_name: 
        file=open(in_file_name,"r+", encoding="utf-8")
    else:
        file=open(in_file_name,"r+", encoding="iso-8859-1")
    num_of_tokens=0
    for token in file.read().split():
        num_of_tokens += 1
    print (num_of_tokens)
    file.close();
    return num_of_tokens


# In[16]:


# Question 2b
def get_num_of_unique_tokens(in_file_name):
    """
    Finds the number of times each token appears in a given file
    :param in_file_name: name of the input file

    :return unique_tokens: The number of unique tokens in the given file
    """
    if "eng" not in in_file_name: 
        file=open(in_file_name,"r+", encoding="utf-8")
    else:
        file=open(in_file_name,"r+", encoding="iso-8859-1")
    token_dictionary = {}
    for token in file.read().split():
        if token not in token_dictionary:
            token_dictionary[token.lower()] = 1
        else:
            token_dictionary[token.lower()] += 1
    
    unique_tokens = len(token_dictionary)
    return unique_tokens


# In[23]:


original_token_count = get_num_of_tokens("original.tr")
morph_token_count = get_num_of_tokens("morph.tr")

original_unique_token_count = get_num_of_unique_tokens("original.tr")
morph_unique_token_count = get_num_of_unique_tokens("morph.tr")

print("Number of tokens in original.tr file is :", original_token_count , ". Number of unique tokens is original.tr file is: ", original_unique_token_count
     , ". The difference between two files is ", original_token_count - original_unique_token_count)

print("Number of tokens in morph.tr file is :", morph_token_count , ". Number of unique tokens is morph.tr file is: ", morph_unique_token_count
     , ". The difference between two files is ", morph_token_count - morph_unique_token_count)

original_token_count_eng = get_num_of_tokens("original.eng")
morph_token_count_eng = get_num_of_tokens("morph.eng")

original_unique_token_count_eng = get_num_of_unique_tokens("original.eng")
morph_unique_token_count_eng = get_num_of_unique_tokens("morph.eng")

#print("Number of tokens in original.eng file is :", original_token_count_eng , ". Number of unique tokens is original.eng file is: ", original_unique_token_count_eng
#     , ". The difference between two files is ", original_token_count_eng - original_unique_token_count_eng)

#print("Number of tokens in morph.eng file is :", morph_token_count_eng , ". Number of unique tokens is morph.eng file is: ", morph_unique_token_count_eng
#     , ". The difference between two files is ", morph_token_count_eng - morph_unique_token_count_eng)


print("Number of tokens in original.tr file is :", original_token_count , ". Number of tokens is original.eng file is: ", original_token_count_eng
     , ". The difference between two files is ", original_token_count - original_token_count_eng)

print("Number of unique tokens in original.tr file is :", original_unique_token_count , ". Number of unique tokens is original.eng file is: ", original_unique_token_count_eng
     , ". The difference between two files is ", original_unique_token_count - original_unique_token_count_eng)

print("Number of tokens in morph.tr file is :", morph_token_count , ". Number of tokens is morph.eng file is: ", morph_token_count_eng
     , ". The difference between two files is ", morph_token_count - morph_token_count_eng)

print("Number of unique tokens in morph.tr file is :", morph_unique_token_count , ". Number of unique tokens is morph.eng file is: ", morph_unique_token_count_eng
     , ". The difference between two files is ", morph_unique_token_count - morph_unique_token_count_eng)


print("INTERPRETATION: Although the number of tokens in original.tr file is 279730 less than the original.eng file, the number of unique tokens in original.tr file is 36881 more than original.eng file")
print("This shows that the Turkish language is far more reacher than English language in terms of the variety of the words.")


# In[1]:


# Question 3a
def get_token_freq_distribution(in_file_name):
    """
    Finds the number of times each token appears in a given file
    :param in_file_name:

    :return freq_dist: A list of tuples with the frequency of each token sorted in descending order 
    """
    if "eng" not in in_file_name: 
        file=open(in_file_name,"r+", encoding="utf-8")
    else:
        file=open(in_file_name,"r+", encoding="iso-8859-1")
    token_dictionary = {}  # Firsly let's store them in a dictionary
    for token in file.read().split():
        if token not in token_dictionary:
            token_dictionary[token] = 1
        else:
            token_dictionary[token] += 1
    
    freq_dist = []
    for k,v in token_dictionary.items():
        freq_dist.append((k, v))
        
    freq_dist.sort(key=lambda tup: tup[1], reverse=True) 
            
    return freq_dist


# In[2]:


get_token_freq_distribution("original.tr")


# In[3]:


get_token_freq_distribution("original.eng")


# In[34]:


import matplotlib.pyplot as plt
import math

# Question 3b
def plot_freq_dist(freq_dist):
    """
    Plots the relationship between log of rank and log of frequency
    :param freq_dist: 

    :return: void
    """
    # Plot the freq distribution you found in 3a. Can you observe Zipf's law?
    
    x = []
    y = []
    
    for i in range(1, len(freq_dist) + 1):   #  token, frequency in freq_dist:        
        x.append(math.log10(i))
        y.append(math.log10(freq_dist[i - 1][1]))
    
    plt.plot(x, y, 'ro')
    plt.title('Zipf Law observation for original documents')
    plt.xlabel('log(rank)')
    plt.ylabel('log(frequency)')
    plt.show()


# In[35]:


plot_freq_dist(get_token_freq_distribution("original.tr"))


# In[36]:


plot_freq_dist(get_token_freq_distribution("original.eng"))


# In[ ]:


#After plotting the log(rank) vs. log(frequency) for original.tr and original.eng documents, the zipf law can easily be observed


# In[49]:


import matplotlib.pyplot as plt

# Question 4
def heaps_law_check(in_file_name):
    """
    Plots the relationship between term occurance and vocabulary size in a given file
    :param in_file_name:
    :return void:
    """
    term_occurrence = 0
    vocabulary_size = 0
    term_occurrence_arr = []
    vocabulary_size_arr = []
    
    if "eng" not in in_file_name: 
        file=open(in_file_name,"r+", encoding="utf-8")
    else:
        file=open(in_file_name,"r+", encoding="iso-8859-1")
    token_dictionary = {}  # Firsly let's store them in a dictionary
    for token in file.read().split():
        term_occurrence += 1
        term_occurrence_arr.append(term_occurrence)
        if token not in token_dictionary:    
            token_dictionary[token] = 1
            vocabulary_size += 1        
        else:
            token_dictionary[token] += 1
        vocabulary_size_arr.append(vocabulary_size)
    
    plt.plot(term_occurrence_arr, vocabulary_size_arr, 'ro')
    plt.title('Zipf Law observation for original documents')
    plt.xlabel('term occurrence')
    plt.ylabel('vocabulary size')
    plt.show()
    


# In[50]:


heaps_law_check("original.tr")


# In[51]:


heaps_law_check("original.eng")


# In[ ]:


#Heap's Law states that: The number of new words decreases as the size of the corpus increases. 
#In this example I've observe the same thing, as the term occurence increases, the vocabulary size is also increases but slowly
#The slope of the graph is less than 1, which means vocabulary size increase is less than the term occurrence.
#My findings is very similar to the IMDB corpus which is in page 47 of Statistical Properties of Text slides.


# In[24]:


# Question 5
def get_token_occurrence(in_file_name, n):
    """
    Finds the list of words that occurs n times in the given file

    :param in_file_name:
    :param n:
    :return tok_occurence: Number of terms in input file that are occuring n times
    """
    tok_occurence = []
    if "eng" not in in_file_name: 
        file=open(in_file_name,"r+", encoding="utf-8")
    else:
        file=open(in_file_name,"r+", encoding="iso-8859-1")
    token_dictionary = {}  # Firsly let's store them in a dictionary
    #Create token occurrences dictionary
    for token in file.read().split():
        if token not in token_dictionary:    
            token_dictionary[token] = 1
        else:
            token_dictionary[token] += 1
    
    for key, value in token_dictionary.items():
        if(value == n):
            tok_occurence.append(key)
            
    tok_occurence.sort() 
    
    return tok_occurence


# In[25]:


get_token_occurrence("morph.tr", 200)


# In[26]:


get_token_occurrence("morph.tr", 250)


# In[27]:


get_token_occurrence("morph.eng", 200)


# In[28]:


get_token_occurrence("morph.eng", 250)


# In[29]:


get_token_occurrence("original.tr", 200)


# In[30]:


get_token_occurrence("original.tr", 250)


# In[31]:


get_token_occurrence("original.eng", 200)


# In[32]:


get_token_occurrence("original.eng", 250)


# In[33]:


# Question 6a
def find_lines_in_file(in_file_name, string):
    """
    Prints all the lines in which string occurs in the input file
    :param in_file_name:
    :param string:

    :return count: Number of lines containing the string
    """    
    count = 0
    
    with open(in_file_name) as file:
        for num, line in enumerate(file, 1):
            if string in line:
                print(line)
                count += 1
    return count


# In[34]:


find_lines_in_file("original.eng", "prosecutors on European Union legislation")


# In[44]:


# Question 6b
def find_tokens_in_file(in_file_name, tag):
    """
    Prints all the tokens in the file that are labelled with the tag.
    :param in_file_name:
    :param string:

    :return token_count: Number of tokens with the specified tag
    """
    token_count = 0
    if "eng" not in in_file_name: 
        file=open(in_file_name,"r+", encoding="utf-8")
    else:
        file=open(in_file_name,"r+", encoding="iso-8859-1")
    for token in file.read().split():
        if tag in token:
            token_count += 1
            print(token)    
    
    return token_count


# In[45]:


find_tokens_in_file("morph.tr", "Noun")


# In[46]:


find_tokens_in_file("morph.eng", "NN")


# In[63]:


# Question 7
from collections import OrderedDict

def get_main_part_of_speech_tag(in_file_name):
    """
    Prints all the main part of speech tags of the roots of a given file
    :param in_file_name:

    :return void
    """
    tok_occurence = []
    if "eng" not in in_file_name: 
        file=open(in_file_name,"r+", encoding="utf-8")
    else:
        file=open(in_file_name,"r+", encoding="iso-8859-1")
    main_part_of_speech_dictionary = {}  # Firsly let's store them in a dictionary
    #Create main_part_of_speech occurrences dictionary
    for token in file.read().split():
        start = token.find( "+" )
        if token.find("+", start + 1) == -1:
            #Look for end of the token
            end = len(token)
        else:
            end = token.find("+", start + 1)
        main_part_of_speech = token[start + 1:end]
        if main_part_of_speech not in main_part_of_speech_dictionary:    
            main_part_of_speech_dictionary[main_part_of_speech] = 1
        else:
            main_part_of_speech_dictionary[main_part_of_speech] += 1
    
    d_sorted_by_value = OrderedDict(sorted(main_part_of_speech_dictionary.items(), key=lambda x: x[1], reverse=True))
    
    for k, v in d_sorted_by_value.items():
        print ("%s: %s %", (k, v))


# In[64]:


get_main_part_of_speech_tag("morph.tr")


# In[65]:


get_main_part_of_speech_tag("morph.eng")


# In[ ]:


print("In terms of variety of the main speech tags, English Morph subset data is has more variation. Two of the files have Nouns as the most used main speech tag")
print("Number of used nouns is almost two times in Turkish file than the English file")
print("In Turkish second main speech tag is the Verb whereas in English file it is IN which means <Prepositions and Subordinating Conjunctions>")

