import nltk
def g(tok,tag):             #function if NER tagger fails

    #w_list=["under","across","around","along","through","over","into","onto"]
    anslist=[]      
    gram=r"""chunk:{<DT>?<JJ|JJR|JJS>?<RB>?<IN|TO|RP>+<DT>*<NN|NNP|NNS|NNPS|PP|PRP|PP\$|VBG|POS|CD|RB|DT>+}"""
    chunkparser=nltk.RegexpParser(gram)
    chunked=chunkparser.parse(tag)
    length=len(chunked)
    #print(chunked)
    for i in range(length):
        t=i
        list1=[]
        whlist=[]
        when_flag=0
        question_flag=1
        if type(chunked[i]) is not tuple:  
            for k in range(len(chunked[i])):
                if (chunked[i][k][0]=='under' or chunked[i][k][0]=='across' or chunked[i][k][0]=='around' or chunked[i][k][0]=='along' or
                    chunked[i][k][0]=='through' or chunked[i][k][0]=='over' or chunked[i][k][0]=='into' or chunked[i][k][0]=='onto'):
                    question_flag=0
                    break;
            if question_flag==0:  
                for k in range(len(chunked[i])):
                    if chunked[i][k][0]=='from' or chunked[i][k][0]=='until' or chunked[i][k][0]=='till':
                        list1.append(chunked[i][k][0])  
                list1.append("where")
                for k in range(len(chunked[i])):
                    if ( chunked[i][k][0]=='tomorrow' or chunked[i][k][0]=='yesterday' or chunked[i][k][0]=='today' or 
                    chunked[i][k][0]=='tonight' or chunked[i][k][0]=='AM' or chunked[i][k][0]=='pm' or chunked[i][k][0]=='PM'): 
                        list1.remove("where")
                        list1.append("when")
                        when_flag=1
                    # print(chunked)        
                for j in range(t):
                
                    if type(chunked[j]) is tuple:
                        whlist.append(chunked[j][0])
                    else:   
                        for k in range(len(chunked[j])):
                            whlist.append(chunked[j][k][0])         
                t+=1    
                #print(whlist)    
                while t<length:
                    #print(whlist)
                    if type(chunked[t]) is tuple:
                        whlist.append(chunked[t][0])
                    else:   
                        for k in range(len(chunked[t])):
                            whlist.append(chunked[t][k][0])
                    t+=1      
                whlist.append("?")                      
                tag1=nltk.pos_tag(whlist)
                if when_flag==0:       
                    for j in range(len(tag1)-1):
                        if tag1[j][1]=="MD":
                            list1.append(whlist.pop(j))    
                #print(whlist)                   
                tag1=nltk.pos_tag(whlist)
                list1.extend(whlist)
                anslist.append(list1)
                fout=open("OUTPUT.txt","a+")
                fout.write("Rule12- ")
                fout.write(' '.join(list1)) 
                fout.write('\n')    
                fout.close()       
    return anslist  

    
def where(tok,tag,i,count,q):     #function if NER tagger works
    
    #check_list1=["DT","RB","RP","JJ","JJR","JJS","IN","TO","CD","NNP"] #for chunking
    #first_word_list=["from","until","till"]
    temp=i
    whlist=[]
    temp_list=[]
    from_flag=0
    word=""
    while (tag[i][1]=='DT' or tag[i][1]=='RB' or tag[i][1]=='RP' or tag[i][1]=='JJ' or tag[i][1]=='JJR' or tag[i][1]=='JJS' or
         tag[i][1]=='IN' or tag[i][1]=='TO' or tag[i][1]=='CD' or tag[i][1]=='NNP'):#removing words if in checklist1    
        if tag[i][0]=='from' or tag[i][0]=='until' or tag[i][0]=='till':
            from_flag=1
            word=tag[i][0]
        i-=1
    if from_flag==1:                #insert from in  the begining
        temp_list.append(word)        
    if q==1:                        #insert 'where' or 'when'
        temp_list.append("where")
    else:
        temp_list.append("when")    #if we find no 'DATE' or 'TIME', then no questions with 'When'
    for j in range(i+1):            
        whlist.append(tok[j])
    for j in range(temp+2+count,len(tok)):
        whlist.append(tok[j])    
    whlist.append("?")
    tag1=nltk.pos_tag(whlist)  
    if q==1:     
        for j in range(len(tag1)-1):
            if tag[j][1]=="MD":
                temp_list.append(whlist.pop(j))            
    temp_list.extend(whlist)
    fout=open("OUTPUT.txt","a+")
    fout.write("Rule11- ")
    fout.write(' '.join(temp_list)) 
    fout.write('\n')    
    fout.close() 
    return temp_list    

def qs(tok,tag,ner_chunked):    #function for finding question pattern/ner working/fails

    #where_list=["ORGANIZATION","LOCATION"]              #NER where list
    #when_list=["DATE","TIME"]                           #NER when list
    #date_list=["tomorrow","yesterday","today","tonight","pm","AM","PM"] #not detected by NER
    list1=[]
    temp=[]
    count=0
    for i in range(len(ner_chunked)):
        count=0
        if ner_chunked[i][1]=='ORGANIZATION' or ner_chunked[i][1]=='LOCATION': #generate question with where/when
            while ner_chunked[i][1]=='ORGANIZATION' or ner_chunked[i][1]=='LOCATION':
                count+=1
                i+=1
                if i>=len(ner_chunked):
                    break
            list1.append(where(tok,tag,i-1,count,1))
    for i in range(len(ner_chunked)):        
        count=0
        if ner_chunked[i][1]=='DATE' or ner_chunked[i][1]=='TIME':
            while ner_chunked[i][1]=='ORGANIZATION' or ner_chunked[i][1]=='LOCATION':
                count+=1
                i+=1
                if i>=len(ner_chunked):
                    break
            list1.append(where(tok,tag,i-1,count,2))
    for i in range(len(tok)):
        if tok[i]=="here" or tok[i]=="there" or tok[i]=="There" or tok[i]=="There":
            list1.append(where(tok,tag,i-1,0,1))
        elif tok[i]=='tomorrow' or tok[i]=='yesterday' or tok[i]=='today' or tok[i]=='tonight' or tok[i]=='pm' or tok[i]=='AM' or tok[i]=='PM': 
            list1.append(where(tok,tag,i-1,0,2))        
    temp=g(tok,tag)
    for i in range(len(temp)):
        if temp[i] not in list1:
            list1.append(temp[i])        
    return list1                    

def question_where_when(tag,tok,total_chunked):
    from nltk.tag.stanford import StanfordNERTagger
    st=StanfordNERTagger('/home/rubel/stanford-ner/classifiers/english.muc.7class.distsim.crf.ser.gz',
    '/home/rubel/stanford-ner/stanford-ner.jar',encoding='utf-8')
    ner_chunked=st.tag(tok)
    anslist=qs(tok,tag,ner_chunked)
    fo=open("OUTPUT.txt","a+")
    for i in range(len(anslist)):
        anslist[i].pop(len(anslist[i])-2)
        for j in range(len(anslist[i])):
            fo.write(anslist[i][j])
            fo.write(" ")
        fo.write("\n")
        print anslist[i]
        print("\n") 
    fo.close()    
