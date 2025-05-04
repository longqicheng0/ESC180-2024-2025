'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 20, 2023.
'''

import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as 
    described in the handout for Project 3.
    '''
    
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    numer = 0.0
    for key in vec1:
        if key in vec2:
            numer += vec1[key] * vec2[key]
    
    return numer / (norm(vec1) * norm(vec2))


def build_semantic_descriptors(sentences):
    semantic_descripter = {}

    for i in range(len(sentences)):
        checked = []

        for word in sentences[i]: #checks the whole sentence
            indv_dic = {}

            if word not in checked:
                checked.append(word)
                curword = word.lower()

                if curword not in semantic_descripter:
                    for j in range(len(sentences[i])): #check all otehr words in the sentence
                        otherwords = sentences[i][j].lower()
                        
                        #and is to make sure if its the first occurance
                        if otherwords != curword and sentences[i].index(otherwords) == j:
                            #update individual dic
                            if otherwords in indv_dic:
                                indv_dic[otherwords] += 1
                            else:
                                indv_dic[otherwords] = 1
                    #update main descriptor idx = curword
                    semantic_descripter[curword] = indv_dic

                else:
                    for j in range(len(sentences[i])): #check all otehr words in the sentence
                        otherwords = sentences[i][j].lower()
                        if otherwords != curword and sentences[i].index(otherwords) == j:
                            if otherwords in semantic_descripter[curword]:
                                semantic_descripter[curword][otherwords] += 1
                            else:
                                semantic_descripter[curword][otherwords] = 1

    return semantic_descripter


def build_semantic_descriptors_from_files(filenames):
    sentences = []
    for i in range(len(filenames)):
        txt = open(filenames[i], "r", encoding="latin1").read()
        txt = txt.lower()

        #end of sentence
        txt = txt.replace("!",".").replace("?",".")
        #punctuations -- [",", "-", "--", ":", ";"]
        txt = txt.replace(",","").replace("-"," ").replace("--"," ").replace(":","").replace(";","")
        txt = txt.split(".")

        for sentence in txt:
            sentences.append(sentence.split())

    return build_semantic_descriptors(sentences)


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    word = word.lower()
    maxSIM = -1
    maxWORD = choices[0]

    for i in range(len(choices)):
        curChoice = choices[i].lower()
        if word in semantic_descriptors and curChoice in semantic_descriptors:
            curSIM = similarity_fn(semantic_descriptors[word],semantic_descriptors[curChoice])
            if curSIM > maxSIM:
                maxSIM = curSIM
                maxWORD = curChoice
            else:
                curSIM = -1
    return maxWORD


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    correctness = 0.0
    txt = open(filename, "r", encoding="latin1").read()
    txt = txt.split("\n")

    for i in range(len(txt)):
        line = txt[i].split(" ")
        choices = []
        for j in range (2, len(line)):
            choices.append(line[j])
        answer = most_similar_word(line[0],choices, semantic_descriptors,similarity_fn)

        if answer == line[1]:
            correctness += 1.0
    return (correctness/float(len(txt)))*100