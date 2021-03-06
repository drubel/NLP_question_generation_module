import nltk
import Identification
import Non_clause


def emotion_1(segment_set,num):
    tok=nltk.word_tokenize(segment_set[num])
    tag=nltk.pos_tag(tok)        
    gram=r"""chunk:{<RB.?>*<JJ.?>*<NN.?|PRP|PRP\$|VBG|DT|POS|CD|VBN>+<IN>+<DT>?<RB.?>*<JJ.?>*<NN.?|PRP|PRP\$|VBG|DT|POS|CD|VBN>+}"""
    chunkparser=nltk.RegexpParser(gram)
    chunked=chunkparser.parse(tag)    

    list1=Identification.chunk_search(segment_set[num],chunked)
    list3=[]

    if len(list1)!=0:
            for j in range(len(list1)):
                m=list1[j];str2=""
                str1=Non_clause.get_chunk(chunked[m])

                tok=nltk.word_tokenize(str1)
                tag=nltk.pos_tag(tok)        
                gram=r"""chunk:{<RB.?>*<JJ.?>*<NN.?|PRP|PRP\$|VBG|DT|POS|CD|VBN>+}"""
                chunkparser=nltk.RegexpParser(gram)
                chunked1=chunkparser.parse(tag)
                
                list2=Identification.chunk_search(str1,chunked1)

                for k in range(1,len(chunked1)):
                    if k in list2:
                         str2+=Non_clause.get_chunk(chunked1[k])
                    else:
                         str2+=chunked1[k][0]
                         str2+=' '

                str3=Non_clause.get_chunk(chunked1[0])

                tokx=nltk.word_tokenize(str3)
                if tokx[0]=='a' or tokx[0]=='the':
                   str3=""
                   for k in range(1,len(tokx)):
                       str3+=(tokx[k]+' ')

                tokx=nltk.word_tokenize(str2)

                if tokx[0]=='for' or tokx[0]=='of' or tokx[0]=='in':
                   st='Is it true that the '+str3+' is '+str2+' ?'
                   st=Identification.postprocess(st)
                   st='Sp.Rule1- Q.'+st
                   list3.append(st)

                if tokx[0]=='for':
                   st='Is it true that the '+str3+' is only '+str2+' ?'
                   st=Identification.postprocess(st)
                   st='Sp.Rule1- Q.'+st
                   list3.append(st)                   


    return list3 


def emotion_2(segment_set,num):
    tok=nltk.word_tokenize(segment_set[num])
    tag=nltk.pos_tag(tok)        
    gram=r"""chunk:{<RB.?>*<JJ.?|VBG|VBN>+<NN.?|PRP|PRP\$|VBG|DT|POS|CD|VBN>+}"""
    chunkparser=nltk.RegexpParser(gram)
    chunked=chunkparser.parse(tag)    

    list1=Identification.chunk_search(segment_set[num],chunked)
    list3=[]

    if len(list1)!=0:
            for j in range(len(list1)):
                m=list1[j];str2=""
                str1=Non_clause.get_chunk(chunked[m])

                tok=nltk.word_tokenize(str1)
                tag=nltk.pos_tag(tok)        
                gram=r"""chunk:{<RB.?>*<JJ.?|VBG|VBN>+}"""
                chunkparser=nltk.RegexpParser(gram)
                chunked1=chunkparser.parse(tag)

                list2=Identification.chunk_search(str1,chunked1)

                for k in range(1,len(chunked1)):
                    if k in list2:
                         str2+=Non_clause.get_chunk(chunked1[k])
                    else:
                         str2+=chunked1[k][0]
                         str2+=' '

                str3=Non_clause.get_chunk(chunked1[0])

                tokx=nltk.word_tokenize(str2)

                st='Is the '+str2+' really '+str3+' ?'
                st=Identification.postprocess(st)
                st='Sp.Rule2- Q.'+st
                list3.append(st)                

    return list3 


def emotion_3(segment_set,num):
    tok=nltk.word_tokenize(segment_set[num])
    tag=nltk.pos_tag(tok)        
    gram=r"""chunk:{<DT|NN.?>*<PRP\$|POS>+<RB.?>*<JJ.?|VBG|VBN>*<NN.?>+}"""
    chunkparser=nltk.RegexpParser(gram)
    chunked=chunkparser.parse(tag)    

    list1=Identification.chunk_search(segment_set[num],chunked)
    list3=[]

    if len(list1)!=0:
            for j in range(len(list1)):
                m=list1[j];str2=""
                str1=Non_clause.get_chunk(chunked[m])

                tok=nltk.word_tokenize(str1)
                tag=nltk.pos_tag(tok)        
                gram=r"""chunk:{<DT|NN.?>*<PRP\$|POS>+}"""
                chunkparser=nltk.RegexpParser(gram)
                chunked1=chunkparser.parse(tag)

                list2=Identification.chunk_search(str1,chunked1)

                for k in range(1,len(chunked1)):
                    if k in list2:
                         str2+=Non_clause.get_chunk(chunked1[k])
                    else:
                         str2+=chunked1[k][0]
                         str2+=' '

                #str3=Non_clause.get_chunk(chunked1[0])

                if len(chunked1[0])==1:
                   if chunked1[0][0][0]=='his' or chunked1[0][0][0]=='His':
                      str3=' really of him ?'
                   if chunked1[0][0][0]=='my' or chunked1[0][0][0]=='My' or chunked1[0][0][0]=='our' or chunked1[0][0][0]=='Our':
                      str3=' really yours ?'   
                   if chunked1[0][0][0]=='their' or chunked1[0][0][0]=='Their':
                      str3=' really of them ?' 
                   if chunked1[0][0][0]=='her' or chunked1[0][0][0]=='Her':
                      str3=' really of her ?'  
                   if chunked1[0][0][0]=='your' or chunked1[0][0][0]=='Your':
                      str3=' really mine ?'
                else:
                     str3="really of "
                     for k in range(0,len(chunked1[0])-1):
                         str3+=(chunked1[0][k][0]+' ')
                     str3+='?'    

                st='Is the '+str2+str3
                st=Identification.postprocess(st)
                st='Sp.Rule3- Q.'+st
                list3.append(st)                

    return list3 


def emotion_4(segment_set,num):
    tok=nltk.word_tokenize(segment_set[num])
    tag=nltk.pos_tag(tok)        
    gram=r"""chunk:{<TO>+<VB|VBP|RP>+<DT>?<RB.?>*<JJ.?>*<NN.?|PRP|PRP\$|POS|VBG|DT>*}""" 
    chunkparser=nltk.RegexpParser(gram)
    chunked=chunkparser.parse(tag)

    list1=Identification.chunk_search(segment_set[num],chunked)
    list3=[]
    
    if len(list1)!=0:
            for j in range(len(chunked)):
                  str1="";str2="";str3=""
                  if j in list1:
                          for k in range(j):
                                if k in list1:
                                        str1+=Non_clause.get_chunk(chunked[k])
                                else:
                                        str1+=(chunked[k][0]+" ")
                          
                          tok=nltk.word_tokenize(str1)
                          tag=nltk.pos_tag(tok)
                          gram=r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+<RB.?>*<VB.?|MD|RP>+}"""
                          chunkparser=nltk.RegexpParser(gram)
                          chunked1=chunkparser.parse(tag)
                          
                          list2=Identification.chunk_search(str1,chunked1)
                          
                          if len(list2)!=0:
                              m=list2[len(list2)-1]
                              
                              str4=Non_clause.get_chunk(chunked1[m])
                              
                              tok=nltk.word_tokenize(str4)
                              tag=nltk.pos_tag(tok)
                              gram=r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+}"""
                              chunkparser=nltk.RegexpParser(gram)
                              chunked2=chunkparser.parse(tag)
                            
                              list6=Identification.chunk_search(str4,chunked2)
                              str2=Non_clause.get_chunk(chunked2[list6[len(list6)-1]])
                              
                              str3=""
                              
                          for yy in range(1,len(chunked[j])):
                              str3+=(chunked[j][yy][0]+" ") 
                          
                          st='How do '+str2+str3+'?'    
                          st=Identification.postprocess(st)
                          st='Sp.Rule4- Q.'+st
                          list3.append(st)                

    return list3 


def emotion_5(segment_set,num):
    tok=nltk.word_tokenize(segment_set[num])
    tag=nltk.pos_tag(tok)        
    gram=r"""chunk:{<DT>?<RB.?>*<JJ.?>*<NN.?|PRP|PRP\$|VBG|DT|POS|CD|VBN>+<VB.?|MD>+<RB.?>*<JJ.?|VBG|VBN>+}""" 
    chunkparser=nltk.RegexpParser(gram)
    chunked=chunkparser.parse(tag)

    list1=Identification.chunk_search(segment_set[num],chunked)
    list3=[]
    
    if len(list1)!=0:
       for j in range(len(list1)):
                m=list1[j];str2=""
                str1=Non_clause.get_chunk(chunked[m])

                tok=nltk.word_tokenize(str1)
                tag=nltk.pos_tag(tok)        
                gram=r"""chunk:{<DT>?<RB.?>*<JJ.?>*<NN.?|PRP|PRP\$|VBG|DT|POS|CD|VBN>+<VB.?|MD>+}"""
                chunkparser=nltk.RegexpParser(gram)
                chunked1=chunkparser.parse(tag)

                list2=Identification.chunk_search(str1,chunked1)

                for k in range(1,len(chunked1)):
                    if k in list2:
                         str2+=Non_clause.get_chunk(chunked1[k])
                    else:
                         str2+=chunked1[k][0]
                         str2+=' '

                str3=Non_clause.get_chunk(chunked1[0])
                str3=Identification.verbphrase_identify(str3)

                st=str3+'really '+str2+' ?'
                st=Identification.postprocess(st)
                st='Sp.Rule5- Q.'+st
                list3.append(st)                

    return list3 


#sen="His work is very good."
#lis=Identification.segment_identify(sen)
#print emotion_5(lis,0)










              
