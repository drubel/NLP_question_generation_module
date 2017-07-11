import nltk,string
def tolower(word):

    if len(word)==0:
        return word
    else:
        return word[0].lower()+word[1:]    
name=raw_input("\nEnter file name: ")
fout=open("Formated_output.txt","w")
with open(name) as f:
    lines=f.readlines()
for loop in range(len(lines)): 
    ans=[]
    sen=lines[loop]
    if '?' in sen:
        tok=nltk.word_tokenize(sen)
        tag=nltk.pos_tag(tok)
        for i in range(len(tag)):
            word=tag[i][0]
            if i==0:
                word=word.capitalize()
            elif tag[i][1]!='NNP':
                word=tolower(word)    
            ans.append(word)  
        fout.write(' '.join(ans))
        fout.write('\n') 
    else:
        fout.write(sen)
f.close()             
fout.close()            