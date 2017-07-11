import nltk
import function

def howMuch(tag,tok,lis):
    #file_write=open('QUESTIONS','w')
    gram=r"""chunk:{<IN>+<\$>?<CD>+}"""                   
    chunkparser=nltk.RegexpParser(gram)
    chunked=chunkparser.parse(tag)
    list2=[]
    list1=[]
    pos=flag=count=0
    ques=""
    for i in range(0,len(chunked)-1):
        if(len(chunked[i])!=2):
            flag=1
            for j in range(0,len(chunked[i])):
                if chunked[i][j][1]=='IN':
                    pos=1
                    list2.append(chunked[i][j][0])        
        else:
             flag2=0
             for j in range(0,len(tok)):
                if chunked[i][0][0]==tok[j] and len(chunked[i][0][0])!=1:
                    flag=flag2=1
                    pos=1
             if flag2==1:
                list2.append(chunked[i][0][0])
             elif pos==1: #words after chunked part
                list2.append(chunked[i][0])
             else: #words before chunked part
                list1.append(chunked[i][0])
    if flag!=0:
        count=count+1
        list2.insert(pos,'how much')
        for i in range(0, len(list1)):
            list2.append(list1[i])
        for i in range(0, len(list2)-1):
            ques=ques+list2[i]+" "
        ques=ques+list2[len(list2)-1]+"?"
        ques=nltk.word_tokenize(ques)
        list2=[]
        for a1 in range(0,len(ques)):
            list2.append(ques[a1])
        list2=function.test(list2)

        fo=open("OUTPUT.txt","a+")
        fo.write("Rule7- ")
        for a1 in range(0,len(list2)):
            fo.write(list2[a1])
            fo.write(" ")
        fo.write('\n')
        fo.close()
        print list2
   
 
def howMuch2(tag,tok,lis):
    #file_write=open('QUESTIONS','w')
    gram=r"""chunk:{<\$>*<CD>+<MD>?<VB|VBD|VBG|VBP|VBN|VBZ|IN>+}"""                   
    chunkparser=nltk.RegexpParser(gram)
    chunked=chunkparser.parse(tag)
    list2=[]
    list1=[]
    pos=flag=count=0
    ques=""
    flag=0 #whether rule is applicable for the sentence
    for i in range(0,len(chunked)-1):
        if(len(chunked[i])!=2):
            flag=1
            for j in range(0,len(chunked[i])):
                if chunked[i][j][1]!='$' and chunked[i][j][1]!='CD':
                    pos=1
                    list1.append(chunked[i][j][0])        
        elif pos==1: #words after chunked part
                list2.append(chunked[i][0])
        else: #words before chunked part
                list1.append(chunked[i][0])
    if flag!=0:
        count=count+1
        list1.insert(0,'how much')
        for i in range(0, len(list2)):
            list1.append(list2[i])
        for i in range(0, len(list1)-1):
            ques=ques+list1[i]+" "
        ques=ques+list1[len(list1)-1]+"?"
        ques=nltk.word_tokenize(ques)
        list2=[]
        for a1 in range(0,len(ques)):
            list2.append(ques[a1])
        list2=function.test(list2)

        fo=open("OUTPUT.txt","a+")
        fo.write("Rule8- ")
        for a1 in range(0,len(list2)):
            fo.write(list2[a1])
            fo.write(" ")
        fo.write('\n')
        fo.close()
        print list2
 
        
def howMuch3(tag,tok,lis):
    #file_write=open('QUESTIONS','w')

    gram=r"""chunk:{<MD>?<VB|VBD|VBG|VBP|VBN|VBZ>+<IN>?<PRP|PRP\$>?<\$>*<CD>+}"""                   
    chunkparser=nltk.RegexpParser(gram)
    chunked=chunkparser.parse(tag)
    list1=[]
    list2=[]
    list3=[]
    pos=flag=count=0
    ques=""
    flag=0 #whether rule is applicable for the sentence
    for i in range(0,len(chunked)-1):
        if(len(chunked[i])!=2):
            flag=1
            for j in range(0,len(chunked[i])):
                if chunked[i][j][1]!='$' and chunked[i][j][1]!='CD':
                    pos=1
                    list1.append(chunked[i][j][0])        
        elif pos==1: #words after chunked part
                list1.append(chunked[i][0])
        else: #words before chunked part
                list2.append(chunked[i][0])
    if flag!=0:
        count=count+1
        for i in range(0, len(list1)):
            list2.append(list1[i])
        list2.insert(0,'How much')
        for i in range(0, len(list2)-1):
            ques=ques+list2[i]+" "
        ques=ques+list2[len(list2)-1]+"?"
        ques=nltk.word_tokenize(ques)
        list2=[]
        for a1 in range(0,len(ques)):
            list2.append(ques[a1])
        list2=function.test(list2)

        fo=open("OUTPUT.txt","a+")
        fo.write("Rule9- ")
        for a1 in range(0,len(list2)):
            fo.write(list2[a1])
            fo.write(" ")
        fo.write('\n')
        fo.close()
        print list2
 
def howMany(tag,tok,lis):
    #file_write=open('QUESTIONS','w')

    gram=r"""chunk:{<DT>?<CD>+<RB>?<JJ|JJR|JJS>?<NN|NNS|NNP|NNPS|VBG>+}"""                   
    chunkparser=nltk.RegexpParser(gram)
    chunked=chunkparser.parse(tag)
    list1=[]
    list2=[]
    list3=[]
    pos=flag=count=0
    ques=""
    flag=0 #whether rule is applicable for the sentence
    for i in range(0,len(chunked)-1):
        if len(chunked[i])!=2:
            flag=1
            for j in range(0,len(chunked[i])):
                if chunked[i][j][1]!='CD' and chunked[i][j][1]!='DT':
                    pos=1
                    list1.append(chunked[i][j][0])
        else:
            flag2=0
            for j in range(0,len(tok)):
                if chunked[i][1][0]==tok[j] and len(chunked[i][1][0])!=1:
                    flag=flag2=1
                    pos=1
            if flag2==1:
                list1.append(chunked[i][1][0])
            elif pos==1: #words after chunked part
                list3.append(chunked[i][0])
            else: #words before chunked part
                list2.append(chunked[i][0])
                        
    if flag!=0:
        count=count+1
        for i in range(0, len(list2)):
             list1.append(list2[i])
        for i in range(0, len(list3)):
             list1.append(list3[i])
        list1.insert(0,'How many')
        for i in range(0, len(list1)-1):
             ques=ques+list1[i]+" "
        ques=ques+list1[len(list1)-1]+"?"
        ques=nltk.word_tokenize(ques)
        list2=[]
        for a1 in range(0,len(ques)):
            list2.append(ques[a1])
        list2=function.test(list2)

        fo=open("OUTPUT.txt","a+")
        fo.write("Rule10- ")
        for a1 in range(0,len(list2)):
            fo.write(list2[a1])
            fo.write(" ")
        fo.write('\n')
        fo.close()
        print list2
    


