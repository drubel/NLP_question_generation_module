import nltk

def make_list(chunked,tok,i,j):
    list1=[]
    for k in range(i,j):
        if len(chunked[k])!=2:
            for s in range(0,len(chunked[k])):
                list1.append(chunked[k][s][0])
        elif len(chunked[k])==2:
             flag=0
             for s in range(0,len(tok)):
                 if chunked[k][1][0]==tok[s] and tok[s]!='.':
                    flag=1
             if flag==1:
                 list1.append(chunked[k][0][0])
                 list1.append(chunked[k][1][0])
             else:
                 list1.append(chunked[k][0])
    return list1


def verb_search(chunked,i,tok):
    list1=[];list2=[];list3=[]



    for j in range(0,len(chunked[i])):
        list2.append(chunked[i][j][0])

    if len(list2)!=0:
       tag=nltk.pos_tag(list2)
       gram=r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN|RB.?>+}"""
       chunkedparser=nltk.RegexpParser(gram)
       chunked1=chunkedparser.parse(tag)
    
       list1=make_list(chunked1,tok,1,len(chunked1))
       list2=make_list(chunked1,tok,0,1)
    
       if len(list1)==1:
          tag=nltk.pos_tag(list1)
          if tag[0][0]=='is' or tag[0][0]=='are' or tag[0][0]=='am' or tag[0][0]=='were' or tag[0][0]=='was':
             list3.append(tag[0][0])
             list1.pop(0)

          else:
               if tag[0][1]=='VBD':
                   list3.append('did')
               if tag[0][1]=='VBZ':
                     list3.append('does')
               if tag[0][1]=='VB' or tag[0][1]=='VBP':
                  list3.append('do')

               st=nltk.stem.porter.PorterStemmer()
               pt=st.stem(list1[0])
               list1.pop(0)
               list1.append(pt)
           
       else:
           if (len(list1)!=0):
              list3.append(list1[0])
              list1.pop(0)
 
       list3.extend(list2)
       list3.extend(list1)

    return list3





def chunked_search(chunked,tok):
    list1=[]
    for i in range(0,len(chunked)):
        if len(chunked[i])!=2:
            list1.append(i)
        elif len(chunked[i])==2:
             flag=0
             for s in range(0,len(tok)-1):
                 if chunked[i][1][0]==tok[s] and tok[s]!='.':
                    flag=1
             if flag==1:    
                 list1.append(i)
    
    return list1


def GRAM1(list1):
    tag=nltk.pos_tag(list1)
    gram=r"""chunk:{<DT>?<JJ.?>*<NN.?|PRP|PRP\$|IN|DT|CC|VBG|VBN>+<RB.?|VB.?|MD>+}"""                   
    chunkparser=nltk.RegexpParser(gram)
    chunked=chunkparser.parse(tag)
    return chunked


def test(list1):
    for i in range(0,len(list1)):
        if list1[i]=='I' or list1[i]=='we' or list1[i]=='i' or list1[i]=='We':
           list1.pop(i)
           list1.insert(i,'you')
        if list1[i]=='am':
           list1.pop(i)
           list1.insert(i,'is/are')
    return list1


def resolve_ambiguity(chunked,i,lis):
    list1=[]
    if chunked[i][0][1]=='TO' or chunked[i][0][1]=='IN':
        for j in range(1,len(chunked[i])):
            list1.append(chunked[i][j][0])
    else:
        for j in range(0,len(chunked[i])):
            list1.append(chunked[i][j][0])
            
    tag=nltk.pos_tag(list1)
    gram=r"""chunk:{<DT>?<RB.?>*<JJ.?>*<\$|CD>*<NN.?|PRP|PRP\$|IN|DT|CC|VBG|VBD>+}"""
    chunkedparser=nltk.RegexpParser(gram)
    chunked1=chunkedparser.parse(tag)

    count=0;flag=0;fla=0

    for j in range(0,len(chunked1[0])):
         if (chunked1[0][j][1]=='NN' or chunked1[0][j][1]=='NNS' or chunked1[0][j][1]=='NNP' or chunked1[0][j][1]=='NNPS'):
             fla=1
         if (chunked1[0][j][1]=='NNP' or chunked1[0][j][1]=='NNPS') and fla==1:
             fla=2
             chunk=j
         if fla!=0:
            break
         if chunked1[0][0][1]=='PRP':
            flag=1
         
    if fla==2:
        for q in range(0,len(lis)):
             if chunked1[0][j][0]==lis[q][0] and lis[q][1]=='PERSON':
                   flag=1
             if (chunked1[0][0][0]==lis[q][0] and lis[q][1]=='ORGANISATION') or (lis[q][1]=='LOCATION' and chunked1[0][0][0]==lis[q][0]):
                   flag=2
             if flag:
                 break
                           
    else:
        f=0
        for k in range(0,len(chunked1[0])):
            if (chunked1[0][k][1]=='NN' or chunked1[0][k][1]=='NNS')and f==0:
                 flag2=k;f=1 
                 for j in range(0,len(lis)):
                      if chunked1[0][flag2][0]==lis[j][0] and lis[j][1]=='PERSON':
                          flag=1
                      elif chunked1[0][flag2][0]==lis[j][0] and (lis[j][1]=='ORGANISATION' or lis[j][1]=='LOCATION'):
                            flag=2
                      else: 
                          flag=0
                      if flag:
                          break
    
    return flag             


        
def resolve_ambiguity_3(chunked,i,lis):
    list1=[]
    for j in range(0,len(chunked[i])):
        list1.append(chunked[i][j][0])
           
    tag=nltk.pos_tag(list1)
    gram=r"""chunk:{<DT>?<RB.?>*<JJ.?>*<NN.?|PRP|PRP\$|IN|DT|CC|VBG>+}"""
    chunkedparser=nltk.RegexpParser(gram)
    chunked1=chunkedparser.parse(tag)
    
    m=len(chunked1)-1

    count=0;flag=0;fla=0

    if chunked1[m][0][1]=='PRP':
       flag=1
    for j in range(0,len(chunked1[m])):
         if (chunked1[m][j][1]=='NN' or chunked1[m][j][1]=='NNS' or chunked1[m][j][1]=='NNP' or chunked1[m][j][1]=='NNPS'):
             fla=1
         if (chunked1[m][j][1]=='NNP' or chunked1[m][j][1]=='NNPS') and fla==1:
             fla=2
             chunk=j
         if fla!=0:
            break

         
    if fla==2:
        for q in range(0,len(lis)):
             if chunked1[m][j][0]==lis[q][0] and lis[q][1]=='PERSON':
                   flag=1
             if (chunked1[m][0][0]==lis[q][0] and lis[q][1]=='ORGANISATION') or (lis[q][1]=='LOCATION' and chunked1[m][0][0]==lis[q][0]):
                   flag=2
             if flag:
                 break

    else:
        f=0
        for k in range(0,len(chunked1[m])):
            if (chunked1[m][k][1]=='NN' or chunked1[m][k][1]=='NNS')and f==0:
                 flag2=k;f=1 
                 for j in range(0,len(lis)):
                      if chunked1[m][flag2][0]==lis[j][0] and lis[j][1]=='PERSON':
                          flag=1
                      elif chunked1[m][flag2][0]==lis[j][0] and (lis[j][1]=='ORGANISATION' or lis[j][1]=='LOCATION'):
                            flag=2
                      else: 
                          flag=0
                      if flag:
                          break
    
    return flag            
            
