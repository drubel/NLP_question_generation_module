import nltk
import function


def init(tag,sen):
        fo=open("OUTPUT.txt","a+")
        fo.write("--------------------------------------------------------\n")
        for j in range(0,len(sen)):
             fo.write(sen[j])
        fo.write("\n")
        fo.close() 
        
        
def whom_1(tag,tok,lis):
    gram=r"""chunk:{<TO>+<DT>?<RB.?>*<JJ.?>*<NN.?|PRP|PRP\$|VBG|DT|POS|CD|VBN>+}"""
    chunkparser=nltk.RegexpParser(gram)
    chunked=chunkparser.parse(tag)
    
    list2=[];list3=[];list4=[];list5=[]
    list2=function.chunked_search(chunked,tok)
    if len(list2)!=0:
        for i in range(0,len(list2)):
            
            check=function.resolve_ambiguity(chunked,list2[i],lis)
            if check==1:
                list5=['To whom']
            elif check==2:
                  list5=['Where']
            else:
                  list5=['To what']
            list3=function.make_list(chunked,tok,0,list2[i])
            chunked1=function.GRAM1(list3)
            list3=function.chunked_search(chunked1,tok)
            if len(list3)!=0:
               list4=function.verb_search(chunked1,list3[len(list3)-1],tok)
               list1=function.make_list(chunked1,tok,0,list3[len(list3)-1])
               for j in range(0,len(list5)):
                   list1.append(list5[j])
               for j in range(0,len(list4)):
                   list1.append(list4[j])
               list3=function.make_list(chunked1,tok,list3[len(list3)-1]+1,len(chunked1))
               for j in range(0,len(list3)):
                   list1.append(list3[j])   
               list3=function.make_list(chunked,tok,list2[i]+1,len(chunked)-1)
               for j in range(0,len(list3)):
                   list1.append(list3[j])
               list1.append('?')
               list1=function.test(list1)
               print list1
            
               fo=open("OUTPUT.txt","a+")
               fo.write("Rule1- ")
               for j in range(0,len(list1)):
                   fo.write(" ")
                   fo.write(list1[j])
               fo.write("\n")
               fo.close()            

               
    
    
def whom_2(tag,tok,lis):
    gram=r"""chunk:{<IN>+<DT>?<RB.?>*<JJ.?>*<NN.?|PRP|PRP\$|POS|VBG|DT|CD|VBN>+}"""
    chunkparser=nltk.RegexpParser(gram)
    chunked=chunkparser.parse(tag)
    
    list2=[];list3=[];list4=[]
    list2=function.chunked_search(chunked,tok) 
    if len(list2)!=0:
        for i in range(0,len(list2)):
            list1=[];list5=[]
            list5.append(chunked[list2[i]][0][0])
            check=function.resolve_ambiguity(chunked,list2[i],lis)
            if check==1:
                list5.append('Whom')
            elif check==2:
                  list5.append('Where')
            else:
                  list5.append('What')
              
            list3=function.make_list(chunked,tok,0,list2[i])
            chunked1=function.GRAM1(list3)
            list3=function.chunked_search(chunked1,tok)
            if len(list3)!=0:
                list4=function.verb_search(chunked1,list3[len(list3)-1],tok)
                list1=function.make_list(chunked1,tok,0,list3[len(list3)-1])
                for j in range(0,len(list5)):
                    list1.append(list5[j])    
                for j in range(0,len(list4)):
                     list1.append(list4[j])
                list3=function.make_list(chunked1,tok,list3[len(list3)-1]+1,len(chunked1))
                for j in range(0,len(list3)):
                    list1.append(list3[j])    
                list3=function.make_list(chunked,tok,list2[i]+1,len(chunked)-1)
                for j in range(0,len(list3)):
                     list1.append(list3[j])
                list1.append('?')
                list1=function.test(list1)
                print list1
            
                fo=open("OUTPUT.txt","a+")
                fo.write("Rule2- ")
                for j in range(0,len(list1)):
                    fo.write(" ")
                    fo.write(list1[j])
                fo.write("\n")
                fo.close()
            
    
def whom_3(tag,tok,lis):
           
    gram=r"""chunk:{<VB.?|MD|RP>+<DT>?<RB.?>*<JJ.?>*<NN.?|PRP|PRP\$|POS|VBG|DT|CD|VBN>+}"""
    chunkparser=nltk.RegexpParser(gram)
    chunked=chunkparser.parse(tag)
    
    list2=[]
    list2=function.chunked_search(chunked,tok)
    
    if len(list2)!=0:
        for i in range(0,len(list2)):
            m=list2[i]
            list3=[];list4=[];list5=[]

            list3=function.make_list(chunked,tok,m,m+1)
            tag1=nltk.pos_tag(list3)
            gram=r"""chunk:{<VB.?|MD>+}"""
            chunkparser=nltk.RegexpParser(gram)
            chunked1=chunkparser.parse(tag1) 
            list3=function.make_list(chunked1,tok,0,1) 


            list4=function.make_list(chunked,tok,0,m)
            list4.extend(list3)     
            tag1=nltk.pos_tag(list4)
            gram=r"""chunk:{<DT>?<RB.?>*<JJ.?>*<NN.?|PRP|PRP\$|POS|VBG|DT|CD|VBN>+<VB.?|MD|RP>+}"""
            chunkparser=nltk.RegexpParser(gram)
            chunked2=chunkparser.parse(tag1)
            list4=function.chunked_search(chunked2,tok)
            n=len(list4)-1
            if n>=0: 
               list4=function.verb_search(chunked2,list4[n],tok)
            
            list1=[]
            list5=function.make_list(chunked,tok,m,m+1)
            tag1=nltk.pos_tag(list5)
            gram=r"""chunk:{<DT>?<RB.?>*<JJ.?>*<NN.?|PRP|PRP\$|POS|VBG|DT|CD|VBN>+}"""
            chunkparser=nltk.RegexpParser(gram)
            chunked3=chunkparser.parse(tag1)
            check=function.resolve_ambiguity_3(chunked3,len(chunked3)-1,lis)
            
            if check==1:
                list1.append('Whom')
            elif check==2:
                  list1.append('What')
            else:
                  list1.append('What')

            list1.extend(list4)
            if len(chunked)>m+1:
               list4=function.make_list(chunked,tok,m+1,len(chunked)-1)
            list1.extend(list4)

            list1.append('?')
            list1=function.test(list1)
            print list1

            fo=open("OUTPUT.txt","a+")
            fo.write("Rule3- ")
            for j in range(0,len(list1)):
                fo.write(" ");fo.write(list1[j])
            fo.write("\n")
            fo.close() 



def whose(tag,tok):
    gram=r"""chunk:{<PRP\$|POS>+<RB.?>*<JJ.?>*<NN.?|VBG|VBN>+<VB.?|MD|RP>+}"""
    chunkparser=nltk.RegexpParser(gram)
    chunked=chunkparser.parse(tag)
    
    list2=[];list3=[]
    list2=function.chunked_search(chunked,tok)
    
    if len(list2)!=0:
        for i in range(0,len(list2)):
            list1=['Whose']
            for j in range(1,len(chunked[list2[i]])):
                list1.append(chunked[list2[i]][j][0])    
            list3=function.make_list(chunked,tok,list2[i]+1,len(chunked)-1)
            list1.extend(list3)
            list1.append('?')
            list1=function.test(list1)
            print list1
            
            fo=open("OUTPUT.txt","a+")
            fo.write("Rule4- ")
            for j in range(0,len(list1)):
                fo.write(" ")
                fo.write(list1[j])
            fo.write("\n")
            fo.close()
            


def what_to_do(tag,tok):
    gram=r"""chunk:{<TO>+<VB|VBP|RP>+<DT>?<RB.?>*<JJ.?>*<NN.?|PRP|PRP\$|POS|VBG|DT>*}"""
    chunkparser=nltk.RegexpParser(gram)
    chunked=chunkparser.parse(tag)
    
    list2=[];
    list2=function.chunked_search(chunked,tok)
    if len(list2)!=0:
       for i in range(0,len(list2)):
           m=list2[i];flag=0;list3=[];list4=[]
           if chunked[m][1][1]=='VB' and len(chunked[m])>2:
              if chunked[m][2][1]=='VBG'or chunked[m][2][1]=='VBN'or chunked[m][2][1]=='VBD' or chunked[m][2][1]=='VBP' or chunked[m][2][1]=='VB':
                 flag=1
                
           list1=['What']
           list3=function.make_list(chunked,tok,0,list2[i])
           chunked1=function.GRAM1(list3)
           list3=function.chunked_search(chunked1,tok)        
           list4=function.verb_search(chunked1,list3[len(list3)-1],tok)
           for j in range(0,len(list4)):
               list1.append(list4[j])  
           list3=function.make_list(chunked1,tok,list3[len(list3)-1]+1,len(chunked1))
           for j in range(0,len(list3)):
               list1.append(list3[j]) 
           if flag==1:
              list1.append('to')
              list1.append(chunked[m][1][0])
           else:
               list1.append('to do')   
           list3=function.make_list(chunked,tok,m+1,len(chunked)-1)
           for j in range(0,len(list3)):
               list1.append(list3[j])
           list1.append('?')
           list1=function.test(list1)
           print list1
           
           fo=open("OUTPUT.txt","a+")
           fo.write("Rule5- ")
           for j in range(0,len(list1)):
               fo.write(" ")
               fo.write(list1[j])
           fo.write("\n")
           fo.close()
           
    


def who(tag,tok,lis):
    gram=r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+<RB.?|VB.?|MD|RP>+}"""
    chunkparser=nltk.RegexpParser(gram)
    chunked=chunkparser.parse(tag)

    list2=[];list3=[]
    list2=function.chunked_search(chunked,tok)
    if len(list2)!=0:
       for i in range(0,len(list2)):
              list4=[];
              check=function.resolve_ambiguity(chunked,list2[i],lis)
              if check==1:
                 list1=['Who']
              elif check==2:
                   list1=['What']
              else:
                   list1=['who']

              m=list2[i]
          
              list4=function.make_list(chunked,tok,m,m+1)
              tag1=nltk.pos_tag(list4)
              gram=r"""chunk:{<RB.?|VB.?|MD|RP>+}"""
              chunkparser=nltk.RegexpParser(gram)
              chunked1=chunkparser.parse(tag1)
              list4=function.make_list(chunked1,tok,len(chunked1)-1,len(chunked1))
              list1.extend(list4)

              list3=function.make_list(chunked,tok,m+1,len(chunked)-1)
              list1.extend(list3)
              list1.append('?')
              list1=function.test(list1)
              print list1
        
              fo=open("OUTPUT.txt","a+")
              fo.write("Rule6- ")
              for j in range(0,len(list1)):
                  fo.write(" ")
                  fo.write(list1[j])
              fo.write("\n")
              fo.close()

        
      

   
