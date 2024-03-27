import nltk
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import random
import string # to process standard python strings

f=open('APL1.txt','r',errors = 'ignore')
m=open('AI1.txt','r',errors = 'ignore')
checkpoint = "./chatbot_weights.ckpt"

raw=f.read()
rawone=m.read()
raw=raw.lower()# converts to lowercase
rawone=rawone.lower()
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences 
word_tokens = nltk.word_tokenize(raw)# converts to list of words
sent_tokensone = nltk.sent_tokenize(rawone)# converts to list of sentences 
word_tokensone = nltk.word_tokenize(rawone)# converts to list of words

sent_tokens[:2]
sent_tokensone[:2]

word_tokens[:5]
word_tokensone[:5]

lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

Intro_Res = ["My name is APL Bot.","My name is APL Bot you can call me APL.","Im APL Bot :) ","My name is APL Bot. My nickname is APL, what would you like to learn? :) "]
GREETING_INPUTS = ("hello", "hi","hiii","hii","hiiii","hiiii", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "hii there", "hi there", "hello", "I am glad! You are talking to me"]

QuesProg = ("what is a programming language ?","what is a programming language","what is programming language?","what is programming language.")
AnsProg = "This is an abstract data type defined by a set of unique data structures and their associated operations performed on these data types. So C , Java , Fortran , Ada , RPG , Foxpro, Prolog , Pascal , Haskell , Lisp , Cobol , C++ etc  represent examples of programming languages"
QuesParadigm = ("what is ","what is a programming paradigm.","what is programming paradigm ","what is programming ?","what is programming paradigm?","what is a programming paradigm","what is a programming paradigm?","what is a programming paradigm ?")
AnsQuesParadigm = ["The term programming paradigm refers to a style of programming. It does not refer to a specific language, but rather it refers to the way you program. There are lots of programming languages that are well-known but all of them need to follow some strategy when they are implemented. And that strategy is a paradigm."]

print('==================== STEMMING ====================')

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
for w in word_tokens:
    print(stemmer.stem(w))

print('==================== LEMMATIZATION ====================')

from nltk.stem import WordNetLemmatizer
lemmer = WordNetLemmatizer()
for w in word_tokens:
    print("Lemma for {} is {}".format(w, lemmer.lemmatize(w)))

print('==================== POS TAGGING ====================')

from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
from nltk.tokenize import word_tokenize, sent_tokenize
for pos in sent_tokens:
    listWords = nltk.word_tokenize(pos)
    listWords = [w for w in listWords if not w in stop_words]
    #using tag as parts of speech
    #tagger = nltk.pos_tag(listWords)
    #print(tagger)

print('==================== CHUNKING ====================')

from nltk import pos_tag
from nltk import RegexpParser

text = "The best and most fun course in school is analysis of programming languages. It has been proven and recognized"
tokens = nltk.word_tokenize(text)
print ('==========printing tokens==========')
print(tokens)
tag = nltk.pos_tag(tokens)
print('==========printing pos tags==========')
print(tag)
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
result = cp.parse(tag)
print('==========printing chunks==========')
print(result)

# Checking for greetings
def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# Checking for QuesProg
def quesP(sentence):
    for word in QuesProg:
        if sentence.lower() == word:
            return AnsProg

# Checking for QuesProgM
def basicM(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in QuesParadigm:
        if sentence.lower() == word:
            return random.choice(AnsQuesParadigm)

# Checking for Introduce
def IntroduceMe(sentence):
    return random.choice(Intro_Res)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



def response(user_response):
    chatbot_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        chatbot_response=chatbot_response+"Sorry. I don't understand"
        return chatbot_response
    else:
        chatbot_response = chatbot_response+sent_tokens[idx]
        return chatbot_response

# Generating response
def responseone(user_response):
    chatbot_response=''
    sent_tokensone.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokensone)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        chatbot_response=chatbot_response+"Sorry. I don't understand"
        return chatbot_response
    else:
        chatbot_response = chatbot_response+sent_tokensone[idx]
        return chatbot_response

def chat(user_response):
    user_response=user_response.lower()
    keyword = " module "
    keywordone = " module"
    keywordsecond = "module "
    
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            return "You are welcome.."
        elif(basicM(user_response)!=None):
            return basicM(user_response)
        else:
            if(user_response.find(keyword) != -1 or user_response.find(keywordone) != -1 
            or user_response.find(keywordsecond) != -1):
                return responseone(user_response)
                sent_tokensone.remove(user_response)
            elif(greeting(user_response)!=None):
                return greeting(user_response)
            elif(user_response.find("your name") != -1 or user_response.find(" your name") != -1 
            or user_response.find("your name ") != -1 or user_response.find(" your name ") != -1):
                return IntroduceMe(user_response)
            elif(quesP(user_response)!=None):
                return quesP(user_response) 
            else:
                return response(user_response)
                sent_tokens.remove(user_response)

''''print('==========Remove redundant apostrophes==========')


import nltk
from nltk.corpus import wordnet
import re
from pattern.text.en import suggest

def tokenize_text(text):
    sentences = nltk.sent_tokenize(text)
    word_tokens = [nltk.word_tokenize(sentence) for sentence in sentences] 
    return word_tokens
    
def remove_repeated_characters(word):
    pattern = re.compile(r"(\w*)(\w)\2(\w*)")
    substitution_pattern = r"\1\2\3"
    while True:
        if wordnet.synsets(word):
            return word
        new_word = pattern.sub(substitution_pattern,word)
        if new_word != word:
            word = new_word
            continue
        else:
            return new_word

def spelling_checker(word):
    try:
        checker = suggest(word)
        return checker[0][0]
    except StopIteration:
        print(f"No suggestions found for word: {word}")
        # Handle the exception here, for example:
        return word  # Return the original word if suggestions cannot be found


sample_sentence = "My school''s bookk'"
sample_sentence_tokens = tokenize_text(sample_sentence)[0]
output = [remove_repeated_characters(s) for s in sample_sentence_tokens]
output = [spelling_checker(s.lower()) for s in output]
print (output)'''



