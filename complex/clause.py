import nltk
import function
import question
import howMuch_howMany
import where

def because_that(tok):
    list1=[]
    for i in range(0,len(tok)):
        if tok[i]=='because':
           list1.append(i)

    if len(list1)!=0:
       for i in range(0,len(list1)):
           m=list1[i]
           list2=[]
           for j in range(0,m):
               list2.append(tok[j])

           chunked=function.GRAM1(list2)
           list3=[]
           list3=function.chunked_search(chunked,list2)
           if len(list3)!=0:
              list4=[]
              list4=function.verb_search(chunked,list3[len(list3)-1],list2)
              list5=[]
              list5=function.make_list(chunked,list2,0,list3[len(list3)-1])
              list5.extend(list4)
              list4=function.make_list(chunked,list2,list3[len(list3)-1]+1,len(chunked))
              list5.extend(list4)
              list5.insert(0,'Why')
              list5=function.test(list5)
              list5.append('?')

              fo=open("OUTPUT.txt","a+")
              for a1 in range(0,len(list5)):
                  fo.write(list5[a1])
                  fo.write(" ")
              fo.write('\n')
              fo.close()
              print list5


    list1=[]
    for i in range(0,len(tok)):
        if tok[i]=='that':
           list1.append(i)

    if len(list1)!=0:
       for i in range(0,len(list1)):
           m=list1[i]
           list2=[]
           for j in range(0,m):
               list2.append(tok[j])

           chunked=function.GRAM1(list2)
           list3=[]
           list3=function.chunked_search(chunked,list2)
           if len(list3)!=0:
              list4=[]
              list4=function.verb_search(chunked,list3[len(list3)-1],list2)
              list5=[]
              list5=function.make_list(chunked,list2,0,list3[len(list3)-1])
              list5.extend(list4)
              list4=function.make_list(chunked,list2,list3[len(list3)-1]+1,len(chunked))
              list5.extend(list4)
              list5.insert(0,'What')
              list5=function.test(list5)
              list5.append('?')

              fo=open("OUTPUT.txt","a+")
              for a1 in range(0,len(list5)):
                  fo.write(list5[a1])
                  fo.write(" ")
              fo.write('\n')
              fo.close()
              print list5



def clause_ques(tok,lis,sen):
   
    list1=[]
    for i in range(0,len(tok)):
        if tok[i]==',' or tok[i]=='.':
           list1.append(i)
     
    if len(list1)!=0 :
       n=0
       for i in range(0,len(list1)):
           m=list1[i] 
  
           list2=[]
           for j in range(n,m):
               list2.append(tok[j])
           
           for j in range(0,len(list2)):
               if list2[j]=='which' or list2[j]=='what' or list2[j]=='who' or list2[j]=='where' or list2[j]=='whose' or list2[j]=='whom' or list2[j]=='when':
                  li=[]
                  for f in range(j,len(list2)):
                      li.append(list2[f])
                  li.append('?')
                  li=function.test(li)

                  fo=open("OUTPUT.txt","a+")
                  for a1 in range(0,len(li)):
                      fo.write(li[a1])
                      fo.write(" ")
                  fo.write('\n')
                  fo.close()
                  print li

           if (list2[0]=='which' or list2[0]=='what' or list2[0]=='who' or list2[0]=='where' or list2[0]=='whose' or list2[0]=='whom') and len(list2)!=0:
              list2.pop(0)
           #if (list2[1]=='which' or list2[1]=='what' or list2[1]=='who' or list2[1]=='where' or list2[1]=='whose' or list2[1]=='whom'):
              #list2.pop(1)
     
           chunked=function.GRAM1(list2)
           list3=[]
           list3=function.chunked_search(chunked,list2)
           
           if len(list3)==0:
              tag=nltk.pos_tag(list2)
              gram=r"""chunk:{<RB.?>*<VB.?|MD>+}"""
              chunkparser=nltk.RegexpParser(gram)
              chunked=chunkparser.parse(tag)
              list4=[]
              list4=function.chunked_search(chunked,list2)
              
              if len(list4)==0:

                 gram=r"""chunk:{<TO>+<DT>?<RB.?>*<JJ.?>*<NN.?|PRP|PRP\$|VBG|DT|POS|CD|VBN>+}"""
                 chunkparser=nltk.RegexpParser(gram)
                 chunked=chunkparser.parse(tag)
                 
                 list5=[]
                 for y in range(0,len(chunked)):
                     if len(chunked[y])!=2:
                        list5.append(y)
                     elif len(chunked[y])==2:
                          flag=0
                          for s in range(0,len(list2)):
                              if chunked[y][1][0]==list2[s] and list2[s]!='.':
                                 flag=1
                          if flag==1:    
                             list5.append(y)
                 
                 if len(list5)!=0:
                    for p in range(0,len(list5)):
                        list7=[]
                        list6=[]
                        list6=function.make_list(chunked,list2,0,list5[p])
                        list7.extend(list6)
                        check=function.resolve_ambiguity(chunked,list5[p],lis)
                        if check==1:
                           list7.append('to whom')
                        elif check==2:
                             list7.append('where')
                        else:
                             list7.append('to what')

                        list6=[]
                        list6=function.make_list(chunked,list2,list5[p]+1,len(chunked))
                        list7.extend(list6)
                        list7.append(",")

                    for l in range(0,len(tok)-1):
                        if (l<n) or (l>=m):
                           list7.append(tok[l])
                    list7.append('?')

                    for l in range(1,len(list7)):
                        if list7[l-1]==',' and list7[l]==',':
                           list7.pop(l-1)
                    list7=function.test(list7)

                    fo=open("OUTPUT.txt","a+")
                    fo.write("Rule1- ")
                    for a1 in range(0,len(list7)):
                        fo.write(list7[a1])
                        fo.write(" ")
                    fo.write('\n')
                    fo.close()
                    print list7

                 gram=r"""chunk:{<IN>+<DT>?<RB.?>*<JJ.?>*<NN.?|PRP|PRP\$|POS|VBG|DT|CD|VBN>+}"""
                 chunkparser=nltk.RegexpParser(gram)
                 chunked=chunkparser.parse(tag)
                 
                 list5=[]
                 for y in range(0,len(chunked)):
                     if len(chunked[y])!=2:
                        list5.append(y)
                     elif len(chunked[y])==2:
                          flag=0
                          for s in range(0,len(list2)):
                              if chunked[y][1][0]==list2[s] and list2[s]!='.':
                                 flag=1
                          if flag==1:    
                             list5.append(y)
                 
                 if len(list5)!=0:
                    for p in range(0,len(list5)):
                        list7=[]
                        list6=[]
                        list6=function.make_list(chunked,list2,0,list5[p])
                        list7.extend(list6)
                        list7.append(chunked[list5[p]][0][0]) #
                        check=function.resolve_ambiguity(chunked,list5[p],lis)
                        if check==1:
                           list7.append('whom')
                        elif check==2:
                             list7.append('where')
                        else:
                             list7.append('what')

                        list6=[]
                        list6=function.make_list(chunked,list2,list5[p]+1,len(chunked))
                        list7.extend(list6)
                        list7.append(",")

                    for l in range(0,len(tok)-1):
                        if (l<n) or (l>=m):
                           list7.append(tok[l])
                    list7.append('?')

                    for l in range(1,len(list7)):
                        if list7[l-1]==',' and list7[l]==',':
                           list7.pop(l-1)
                    list7=function.test(list7)

                    fo=open("OUTPUT.txt","a+")
                    fo.write("Rule2- ")
                    for a1 in range(0,len(list7)):
                        fo.write(list7[a1])
                        fo.write(" ")
                    fo.write('\n')
                    fo.close()
                    print list7


                 gram=r"""chunk:{<PRP\$|POS>+<RB.?>*<JJ.?>*<NN.?|VBG|VBN>+}"""
                 chunkparser=nltk.RegexpParser(gram)
                 chunked=chunkparser.parse(tag)
                 
                 list5=[]
                 for y in range(0,len(chunked)):
                     if len(chunked[y])!=2:
                        list5.append(y)
                     elif len(chunked[y])==2:
                          flag=0
                          for s in range(0,len(list2)):
                              if chunked[y][1][0]==list2[s] and list2[s]!='.':
                                 flag=1
                          if flag==1:    
                             list5.append(y)

                 if len(list5)!=0:
                    for p in range(0,len(list5)):
                        list7=[]
                        list6=[]
                        list6=function.make_list(chunked,list2,0,list5[p])
                        list7.extend(list6)
                        list7.append('whose')
 
                        for f in range(1,len(chunked[list5[p]])):
                            list7.append(chunked[list5[p]][f][0])

                        list6=[]
                        list6=function.make_list(chunked,list2,list5[p]+1,len(chunked))
                        list7.extend(list6)
                        list7.append(",")

                    for l in range(0,len(tok)-1):
                        if (l<n) or (l>=m):
                           list7.append(tok[l])
                    list7.append('?')

                    for l in range(1,len(list7)):
                        if list7[l-1]==',' and list7[l]==',':
                           list7.pop(l-1)
                    list7=function.test(list7)

                    fo=open("OUTPUT.txt","a+")
                    fo.write("Rule4- ")
                    for a1 in range(0,len(list7)):
                        fo.write(list7[a1])
                        fo.write(" ")
                    fo.write('\n')
                    fo.close()
                    print list7


                 gram=r"""chunk:{<\$>?<CD>+<NN.?>+}""" 
                 chunkparser=nltk.RegexpParser(gram)
                 chunked=chunkparser.parse(tag)
                 
                 list5=[]
                 for y in range(0,len(chunked)):
                     if len(chunked[y])!=2:
                        list5.append(y)
                     elif len(chunked[y])==2:
                          flag=0
                          for s in range(0,len(list2)):
                              if chunked[y][1][0]==list2[s] and list2[s]!='.':
                                 flag=1
                          if flag==1:    
                             list5.append(y)

                 if len(list5)!=0:
                    for p in range(0,len(list5)):
                        list7=[]
                        list6=[]
                        list6=function.make_list(chunked,list2,0,list5[p])
                        list7.extend(list6)
                        list7.append('how many')
 
                        for f in range(1,len(chunked[list5[p]])):
                            list7.append(chunked[list5[p]][f][0])

                        list6=[]
                        list6=function.make_list(chunked,list2,list5[p]+1,len(chunked))
                        list7.extend(list6)
                        list7.append(",")

                    for l in range(0,len(tok)-1):
                        if (l<n) or (l>=m):
                           list7.append(tok[l])
                    list7.append('?')

                    for l in range(1,len(list7)):
                        if list7[l-1]==',' and list7[l]==',':
                           list7.pop(l-1)
                    list7=function.test(list7)

                    fo=open("OUTPUT.txt","a+")
                    fo.write("Rule10- ")
                    for a1 in range(0,len(list7)):
                        fo.write(list7[a1])
                        fo.write(" ")
                    fo.write('\n')
                    fo.close()
                    print list7



              else:                                      #verb phrase
                     list5=[]
                     for x in range(0,n):
                         list5.append(tok[x])

                     tag=nltk.pos_tag(list5)
                     gram=r"""chunk:{<DT>?<JJ.?>*<NN.?|PRP|PRP\$|IN|DT|CC|VBG|VBN>+}"""                   
                     chunkparser=nltk.RegexpParser(gram)
                     chunked1=chunkparser.parse(tag)
                     list6=[]
                     list6=function.chunked_search(chunked1,list5) 
                     list7=[]
                     if len(list6)!=0:
                        z=len(list6)-1
                        list7=function.make_list(chunked1,list5,list6[z],list6[z]+1)
                        list7.extend(list2)
                     else:
                          list7.append('you')

                     list7.append('.')
                     
                     tag=nltk.pos_tag(list7)
                     
                     question.whom_1(tag,list7,lis)
                     question.whom_2(tag,list7,lis)
                     question.whom_3(tag,list7,lis)
                     question.who(tag,list7,lis)
                     howMuch_howMany.howMuch(tag,list7,lis)
                     howMuch_howMany.howMuch2(tag,list7,lis)
                     howMuch_howMany.howMuch3(tag,list7,lis)
                     howMuch_howMany.howMany(tag,list7,lis)
                     question.what_to_do(tag,list7)
                     question.whose(tag,list7)
                     where.question_where_when(tag,list7,lis)

           else:                                           #gram1 phrase search
                     list2.append('.')
                     tag=nltk.pos_tag(list2)
                     question.whom_1(tag,list2,lis)
                     question.whom_2(tag,list2,lis)
                     question.whom_3(tag,list2,lis)
                     question.who(tag,list2,lis)
                     howMuch_howMany.howMuch(tag,list2,lis)
                     howMuch_howMany.howMuch2(tag,list2,lis)
                     howMuch_howMany.howMuch3(tag,list2,lis)
                     howMuch_howMany.howMany(tag,list2,lis)
                     question.what_to_do(tag,list2)
                     question.whose(tag,list2)
                     where.question_where_when(tag,list2,lis)
           n=m+1

