from utilities import *

words = ['the', 'child', 'will', 'the', 'child', 'can', 'the',
         'child','will', 'the', 'child', 'may', 'go', 'home', '.']

def parse_story(file_name):
    '''
    (str)--> list
    return an ordered list of words with bad characters removed from the text in the file given by file_name
    Bad chars are in the utilities
    '''
    myfile = open(file_name, 'r')
    body = (myfile.read()).lower()
    BAD_CHARS = ['"', "(", ")", "{", "}", "[", "]", "_"]
    VALID_PUNCTUATION = ['?', '.' , '!', ',', ':', ';']
    new_list = []
    token = ""
    for char in body:
        if char not in BAD_CHARS:
            if char in VALID_PUNCTUATION:
                if token != "":
                    new_list.append(token)
                new_list.append(char)
                token = ""
            else:
                if char == " ":
                    if token != "":
                        new_list.append(token)
                        token = ""
                else:
                    token += char
                    if "\t" in token:
                        token = token[:len(token)-1]
                        if token != "":
                            new_list.append(token)
                            token = ""
                    if "\n" in token:
                        token = token[:len(token)-1]
                        if token != "":
                            new_list.append(token)
                            token = ""
    if token != "":             
        new_list.append(token)              
    return new_list

def get_prob_from_count(counts):
    '''
    (list)-->list
    Return a list of probabilities derived from counts.
    '''
    total = sum(counts)
    prob = [x/total for x in counts]
    return prob

def build_ngram_counts(words, n):
    '''
    (list, int)--> dictionary
    Return a dictionary of N-grams (where N=n) and the counts of the words that follow the Ngram.
    '''
    dic = {}
    for i in range(len(words)):
        #bound checking
        #keep checking till it reaches the second last element.
        if i + n <= len(words)-1:
            list_ = words[i:i+n]
            value = words[i+n] #string output
            key = tuple(list_) #tuple 
            if key in dic.keys():
                previous = dic.get(key) #values of the dictionary
                if value in previous[0]: #previous[0] is a list
                    ind = previous[0].index(value)
                    previous[1][ind] += 1
                    dic[key] = previous
                else:
                    previous[0].append(value)
                    previous[1].append(1)
                    dic[key] = previous
            else:
                dic[key] = ([value],[1])
        else:
            return dic

counts = {('i', 'love'): [['js', 'py3', 'c', 'no'], [20, 20, 10, 2]],
          ('u','r'): [['cool', 'nice', 'lit', 'kind'], [8, 7, 5, 5]],
          
('toronto', 'is'): [['six', 'drake'], [2, 3]]
}
				
def prune_ngram_counts(counts, prune_len):
#check if the list has prune_len amount of words
#if the list has more than prune_len amount of words-->surgery
    '''
    (dict,int)-->dict
    Return a dictionary of N-grams
    and counts of words with lower frequency words removed.
    '''
    for key in counts.keys():
        value = counts[key] #get the value associated to the key
        numcount = value[1] #from value, get the list of counts
        liststr = value[0]  #from value, get the list of strings
        
#sort the numcount in ascending order manually
#when moving, move the liststr too
#after everything is sorted
#compare
        N = len(numcount)
        for i in range(1,N+1):
            for j in range(1,N):
                if numcount[j-1] < numcount[j]:
                    numcount[j-1], numcount[j] = numcount[j], numcount[j-1]
                    liststr[j-1], liststr[j] = liststr[j], liststr[j-1]
        if prune_len < len(numcount): 
            if numcount[prune_len-1] > numcount[prune_len]:
                del(numcount[prune_len:])
                del(liststr[prune_len:])
            else:
                for n in range(prune_len,len(numcount)):
                    if numcount[prune_len-1] != numcount[n]:
                        del(numcount[n])
                        del(liststr[n])
    
    return counts
        
def probify_ngram_counts(counts):
    '''
    (dictionary) --> (dictionary)
    Take a dictionary of N-grams and counts and convert the counts to probabilities.
    '''
    for key in counts.keys():
        numcount = counts[key][1] #from value, get the list of counts
        numcount = get_prob_from_count(numcount) #reset the value of numcount
        #change each value one by one
        for i in range(len(numcount)):
            counts[key][1][i] = numcount[i]
    return counts


def build_ngram_model(words, n):
    '''
    (list,int)-> dict
    Create and return a dictionary of the format given above in probify_ngram_counts.
    '''
    ngram = build_ngram_counts(words, n)
    nonprop = prune_ngram_counts(ngram, 15)
    return probify_ngram_counts(nonprop)

ngram_model = build_ngram_model(words, 2)
seed = ('the','child')
       
def gen_bot_list(ngram_model, seed, num_tokens=0):
    '''
    ngram_model: given, a input
    gen_seed(ngram_model)
    seed: a tuple of strings representing the first N tokens in the list.
    
num_tokens: a positive int representing the largest number of tokens to be put in the list
    '''
   
    output = []
    n = len(seed)
    
    if len(seed) <= num_tokens:
        ls_seed = list(seed)
        output += ls_seed
    
    
        count = 2 #stop appending when the count == num of token

        while count < num_tokens:
            if seed in list(ngram_model.keys()):
               content = list(ngram_model[seed])
               value = content[0][0]
               output.append(value)

               
               seed = tuple(output[-n:])

               count += 1
               
            else:
                break
        #keep looking and updating for the seed and add to output
    else:
        seed = list(seed)
        output += seed[:num_tokens]
        
    return output
'''
def gen_bot_text(token_list, bad_author):

def write_story(file_name, text, title, student_name, author, year):
'''
    
if __name__=='__main__':
        pass                                           
