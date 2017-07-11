import nltk
import Identification
import Non_clause


def whom_1(segment_set,num):
    tok=nltk.word_tokenize(segment_set[num])
    tag=nltk.pos_tag(tok)        
    gram=r"""chunk:{<TO>+<DT>?<RB.?>*<JJ.?>*<NN.?|PRP|PRP\$|VBG|DT|POS|CD|VBN>+}"""
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

                          str3=Non_clause.get_chunk(chunked[j])

                          tok=nltk.word_tokenize(str1)
                          tag=nltk.pos_tag(tok)
                          gram=r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+<RB.?>*<VB.?|MD|RP>+}"""
                          chunkparser=nltk.RegexpParser(gram)
                          chunked1=chunkparser.parse(tag)
                          
                          list2=Identification.chunk_search(str1,chunked1)
                          if len(list2)!=0:
                              m=list2[len(list2)-1]
                              
                              str4=Non_clause.get_chunk(chunked1[m])
                              str4=Identification.verbphrase_identify(str4)
                              str5="";str6=""
                              
                              for k in range(m):
                                   if k in list2:
                                         str5+=Non_clause.get_chunk(chunked1[k])
                                   else:
                                         str5+=(chunked1[k][0]+" ")
                                        
                              for k in range(m+1,len(chunked1)):
                                    if k in list2:
                                         str6+=Non_clause.get_chunk(chunked1[k])
                                    else:
                                         str6+=(chunked1[k][0]+" ")

                              st=str5+" why "+str4+str6+str3
                              st+='?'
                              st=Identification.postprocess(st)
                              st='Rule1- Q.'+st
                              list3.append(st)

                              st=str5+" how "+str4+str6+str3
                              st+='?'
                              st=Identification.postprocess(st)
                              st='Rule1- Q.'+st
                              list3.append(st)

                              st=str5+str4+str6+' only '+str3
                              st+='?'
                              st=Identification.postprocess(st)
                              st='Rule1- Q.'+st
                              list3.append(st)

    return list3  


def whom_2(segment_set,num):
    tok=nltk.word_tokenize(segment_set[num])
    tag=nltk.pos_tag(tok)        
    gram=r"""chunk:{<IN>+<DT>?<RB.?>*<JJ.?>*<NN.?|PRP|PRP\$|POS|VBG|DT|CD|VBN>+}""" 
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

                          str3=Non_clause.get_chunk(chunked[j])

                          tok=nltk.word_tokenize(str1)
                          tag=nltk.pos_tag(tok)
                          gram=r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+<RB.?>*<VB.?|MD|RP>+}"""
                          chunkparser=nltk.RegexpParser(gram)
                          chunked1=chunkparser.parse(tag)
                          
                          list2=Identification.chunk_search(str1,chunked1)
                          if len(list2)!=0:
                              m=list2[len(list2)-1]
                              
                              str4=Non_clause.get_chunk(chunked1[m])
                              str4=Identification.verbphrase_identify(str4)
                              str5="";str6=""
                              
                              for k in range(m):
                                   if k in list2:
                                         str5+=Non_clause.get_chunk(chunked1[k])
                                   else:
                                         str5+=(chunked1[k][0]+" ")
                                        
                              for k in range(m+1,len(chunked1)):
                                    if k in list2:
                                         str6+=Non_clause.get_chunk(chunked1[k])
                                    else:
                                         str6+=(chunked1[k][0]+" ")

                              st=str5+" why "+str4+str6+str3
                              st+='?'
                              st=Identification.postprocess(st)
                              st='Rule2- Q.'+st
                              list3.append(st)

                              st=str5+" how "+str4+str6+str3
                              st+='?'
                              st=Identification.postprocess(st)
                              st='Rule2- Q.'+st
                              list3.append(st)

                              st=str5+str4+str6+' only '+str3
                              st+='?'
                              st=Identification.postprocess(st)
                              st='Rule2- Q.'+st
                              list3.append(st)

                              lxx=nltk.word_tokenize(str3)
                              if lxx[0]=='with':
                                 str3=""
                                 for yy in range(1,len(lxx)):
                                     str3+=(lxx[yy]+' ')
                                 str3=' without '+str3+'ever ?'
                                 st=str5+str4+str6+str3
                                 st=Identification.postprocess(st)
                                 st='Rule2- Q.'+st
                                 list3.append(st)                                  

    return list3 


def who(segment_set,num):
    tok=nltk.word_tokenize(segment_set[num])
    tag=nltk.pos_tag(tok)
    gram=r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+<RB.?>*<VB.?|MD|RP>+}"""
    chunkparser=nltk.RegexpParser(gram)
    chunked=chunkparser.parse(tag)

    list1=Identification.chunk_search(segment_set[num],chunked)
    list3=[]
    
    if len(list1)!=0:
            for j in range(len(list1)):
                    m=list1[j];str1=""
                    for k in range(m+1,len(chunked)):
                            if k in list1:
                                    str1+=Non_clause.get_chunk(chunked[k])
                            else:
                                    str1+=(chunked[k][0]+" ")

                    str2=Non_clause.get_chunk(chunked[m])
                    str4=Identification.verbphrase_identify(str2)

                    st=" how "+str4+str1;
                    st+='?'
                    st=Identification.postprocess(st)
                    st='Rule4- Q.'+st
                    list3.append(st)

                    st=str4+str1;
                    st+='?'
                    st=Identification.postprocess(st)

                    tokx=nltk.word_tokenize(st)
                    tokx.insert(1,'only')
                    st=""

                    for l in range(len(tokx)):
                         st+=(tokx[l]+" ")

                    st='Rule4- Q.'+st
                    list3.append(st)

                    st=' why '+str4+str1;
                    st+='?'
                    st=Identification.postprocess(st)

                    tokx=nltk.word_tokenize(st)
                    tokx.insert(2,'only')
                    st=""

                    for l in range(len(tokx)):
                         st+=(tokx[l]+" ")

                    st='Rule4- Q.'+st
                    list3.append(st)
   
    return list3

def whom_3(segment_set,num):
    tok=nltk.word_tokenize(segment_set[num])
    tag=nltk.pos_tag(tok)           
    gram=r"""chunk:{<VB.?|MD|RP>+<DT>?<RB.?>*<JJ.?>*<NN.?|PRP|PRP\$|POS|VBG|DT|CD|VBN>+}"""
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


                          strx=Non_clause.get_chunk(chunked[j])
                          
                          tok=nltk.word_tokenize(strx);
                          tag=nltk.pos_tag(tok)
                          gram=r"""chunk:{<DT>?<RB.?>*<JJ.?>*<NN.?|PRP|PRP\$|POS|VBG|DT|CD|VBN>+}"""
                          chunkparser=nltk.RegexpParser(gram)
                          chunked1=chunkparser.parse(tag)
                           

                          list2=Identification.chunk_search(strx,chunked1)
                          if len(list2)!=0:
                             m=list2[len(list2)-1]
                             str3=Non_clause.get_chunk(chunked1[m])
                          #str3=Non_clause.get_chunk(chunked1[len(chunked1)-1])

                          gram=r"""chunk:{<VB.?|MD>+}"""
                          chunkparser=nltk.RegexpParser(gram)
                          chunked1=chunkparser.parse(tag)
                           

                          strx=Non_clause.get_chunk(chunked1[0])                                                               
                          str1+=strx;

                          tok=nltk.word_tokenize(str1)
                          tag=nltk.pos_tag(tok)
                          gram=r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+<RB.?>*<VB.?|MD|RP>+}"""
                          chunkparser=nltk.RegexpParser(gram)
                          chunked1=chunkparser.parse(tag)
                          
                          list2=Identification.chunk_search(str1,chunked1)
                          
                          if len(list2)!=0:
                              m=list2[len(list2)-1]
                              
                              str4=Non_clause.get_chunk(chunked1[m])
                              str4=Identification.verbphrase_identify(str4)
                              str5="";str6=""
                              
                              for k in range(m):
                                   if k in list2:
                                         str5+=Non_clause.get_chunk(chunked1[k])
                                   else:
                                         str5+=(chunked1[k][0]+" ")
                                        
                              for k in range(m+1,len(chunked1)):
                                    if k in list2:
                                         str6+=Non_clause.get_chunk(chunked1[k])
                                    else:
                                         str6+=(chunked1[k][0]+" ")


                              st=str5+" why "+str4+str6+str3
                              st+='?'
                              st=Identification.postprocess(st)
                              st='Rule3- Q.'+st
                              list3.append(st)

                              st=str5+" how "+str4+str6+str3
                              st+='?'
                              st=Identification.postprocess(st)
                              st='Rule3- Q.'+st
                              list3.append(st)

                              st=str5+str4+str6+str3
                              st+='?'
                              st=Identification.postprocess(st)
                              st='Rule3- Q.'+st
                              list3.append(st)

    return list3


def what_to_do(segment_set,num):
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

                          ls=Non_clause.get_chunk(chunked[j])
                          
                          tok=nltk.word_tokenize(str1)
                          tag=nltk.pos_tag(tok)
                          gram=r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+<RB.?>*<VB.?|MD|RP>+}"""
                          chunkparser=nltk.RegexpParser(gram)
                          chunked1=chunkparser.parse(tag)
                          
                          list2=Identification.chunk_search(str1,chunked1)
                          if len(list2)!=0:
                              m=list2[len(list2)-1]
                              
                              str4=Non_clause.get_chunk(chunked1[m])
                              str4=Identification.verbphrase_identify(str4)
                              str5="";str6=""
                              
                              for k in range(m):
                                   if k in list2:
                                         str5+=Non_clause.get_chunk(chunked1[k])
                                   else:
                                         str5+=(chunked1[k][0]+" ")
                                        
                              for k in range(m+1,len(chunked1)):
                                    if k in list2:
                                         str6+=Non_clause.get_chunk(chunked1[k])
                                    else:
                                         str6+=(chunked1[k][0]+" ")

                              st=str5+" why "+str4+str6+ls
                              st+='?'
                              st=Identification.postprocess(st)
                              st='Rule5- Q.'+st
                              list3.append(st)

                              st=str5+str4+str6+ls+' really '
                              st+='?'
                              st=Identification.postprocess(st)
                              st='Rule5- Q.'+st
                              list3.append(st)

    return list3


def howmuch_3(segment_set,num):
    tok=nltk.word_tokenize(segment_set[num])
    tag=nltk.pos_tag(tok)
    gram=r"""chunk:{<MD>?<VB|VBD|VBG|VBP|VBN|VBZ>+<IN|TO>?<PRP|PRP\$|NN.?|DT>?<\$>*<CD>+}""" 
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


                          strx=Non_clause.get_chunk(chunked[j])
                          tok=nltk.word_tokenize(strx)
                          tag=nltk.pos_tag(tok)
                          gram=r"""chunk:{<MD>?<VB|VBD|VBG|VBP|VBN|VBZ>+<IN|TO>?<PRP|PRP\$|NN.?|DT>?}"""
                          chunkparser=nltk.RegexpParser(gram)
                          chunked1=chunkparser.parse(tag)
 
                          lis=Identification.chunk_search(strx,chunked1)

                                             
                          strx=Non_clause.get_chunk(chunked1[0])
                          str1+=(" "+strx)
                          

                          for k in range(1,len(chunked1)):
                                if k in lis:
                                        str3+=Non_clause.get_chunk(chunked1[k])
                                else:
                                        str3+=(chunked1[k][0]+" ")

                          tok=nltk.word_tokenize(str1)
                          tag=nltk.pos_tag(tok)
                          gram=r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+<RB.?>*<VB.?|MD|RP>+}"""
                          chunkparser=nltk.RegexpParser(gram)
                          chunked1=chunkparser.parse(tag)                              

                          list2=Identification.chunk_search(str1,chunked1)

                          if len(list2)!=0:
                              m=list2[len(list2)-1]
                              
                              str4=Non_clause.get_chunk(chunked1[m])
                              str4=Identification.verbphrase_identify(str4)
                              str5="";str6=""
                              
                              for k in range(m):
                                   if k in list2:
                                         str5+=Non_clause.get_chunk(chunked1[k])
                                   else:
                                         str5+=(chunked1[k][0]+" ")
                                        
                              for k in range(m+1,len(chunked1)):
                                    if k in list2:
                                         str6+=Non_clause.get_chunk(chunked1[k])
                                    else:
                                         str6+=(chunked1[k][0]+" ")

                              st=str5+" why "+str4+str6+'exactly '+str3
                              st+='?'
                              st=Identification.postprocess(st)
                              st='Rule6- Q.'+st
                              list3.append(st)

                              st=str5+str4+str6+str3+' really '
                              st+='?'
                              st=Identification.postprocess(st)
                              st='Rule6- Q.'+st
                              list3.append(st)

                              st=str5+str4+str6+str3+' only '
                              st+='?'
                              st=Identification.postprocess(st)
                              st='Rule6- Q.'+st
                              list3.append(st)                              

    return list3


def howmuch_1(segment_set,num):
    tok=nltk.word_tokenize(segment_set[num])
    tag=nltk.pos_tag(tok)
    gram=r"""chunk:{<IN>+<\$>?<CD>+}""" 
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


                          str2=Non_clause.get_chunk(chunked[j])


                          tok=nltk.word_tokenize(str1)
                          tag=nltk.pos_tag(tok)
                          gram=r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+<RB.?>*<VB.?|MD|RP>+}"""
                          chunkparser=nltk.RegexpParser(gram)
                          chunked1=chunkparser.parse(tag)
                          
                          list2=Identification.chunk_search(str1,chunked1)
                          if len(list2)!=0:
                              m=list2[len(list2)-1]
                              
                              str4=Non_clause.get_chunk(chunked1[m])
                              str4=Identification.verbphrase_identify(str4)
                              str5="";str6=""
                              
                              for k in range(m):
                                   if k in list2:
                                         str5+=Non_clause.get_chunk(chunked1[k])
                                   else:
                                         str5+=(chunked1[k][0]+" ")
                                        
                              for k in range(m+1,len(chunked1)):
                                    if k in list2:
                                         str6+=Non_clause.get_chunk(chunked1[k])
                                    else:
                                         str6+=(chunked1[k][0]+" ")


                              st=str5+str4+str6+chunked[j][0][0]+' exactly '+chunked[j][1][0]+' '+chunked[j][2][0]+'?'
                              st=Identification.postprocess(st)
                              st='Rule7- Q.'+st
                              list3.append(st)

                              st=str5+str4+str6+chunked[j][0][0]+' '+chunked[j][1][0]+' '+chunked[j][2][0]+' only ?'
                              st=Identification.postprocess(st)
                              st='Rule7- Q.'+st
                              list3.append(st)


    return list3


def howmany(segment_set,num):
    tok=nltk.word_tokenize(segment_set[num])
    tag=nltk.pos_tag(tok)
    gram=r"""chunk:{<MD>?<VB.?>+<DT>?<CD>+<RB>?<JJ|JJR|JJS>?<NN.?|VBG|VBN>+}""" 
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


                          strx=Non_clause.get_chunk(chunked[j])
                          tok=nltk.word_tokenize(strx)
                          tag=nltk.pos_tag(tok)
                          gram=r"""chunk:{<MD>?<VB.?>+}"""
                          chunkparser=nltk.RegexpParser(gram)
                          chunked1=chunkparser.parse(tag)
 
                          lis=Identification.chunk_search(strx,chunked1)

                                             
                          strx=Non_clause.get_chunk(chunked1[0])
                          str1+=(" "+strx)
                          

                          for k in range(1,len(chunked1)):
                                if k in lis:
                                        str3+=Non_clause.get_chunk(chunked1[k])
                                else:
                                        str3+=(chunked1[k][0]+" ")

                          tok=nltk.word_tokenize(str1)
                          tag=nltk.pos_tag(tok)
                          gram=r"""chunk:{<EX>?<DT>?<JJ.?>*<NN.?|PRP|PRP\$|POS|IN|DT|CC|VBG|VBN>+<RB.?>*<VB.?|MD|RP>+}"""
                          chunkparser=nltk.RegexpParser(gram)
                          chunked1=chunkparser.parse(tag)                              

                          list2=Identification.chunk_search(str1,chunked1)

                          if len(list2)!=0:
                              m=list2[len(list2)-1]
                              
                              str4=Non_clause.get_chunk(chunked1[m])
                              str4=Identification.verbphrase_identify(str4)
                              str5="";str6=""
                              
                              for k in range(m):
                                   if k in list2:
                                         str5+=Non_clause.get_chunk(chunked1[k])
                                   else:
                                         str5+=(chunked1[k][0]+" ")
                                        
                              for k in range(m+1,len(chunked1)):
                                    if k in list2:
                                         str6+=Non_clause.get_chunk(chunked1[k])
                                    else:
                                         str6+=(chunked1[k][0]+" ")

                              st=str5+str4+str6+str3+'exactly '
                              st+='?'
                              st=Identification.postprocess(st)
                              st='Rule8- Q.'+st
                              list3.append(st)

                              st=str5+str4+str6+str3+' really '
                              st+='?'
                              st=Identification.postprocess(st)
                              st='Rule8- Q.'+st
                              list3.append(st)

                              st=str5+str4+str6+str3+' only '
                              st+='?'
                              st=Identification.postprocess(st)
                              st='Rule8- Q.'+st
                              list3.append(st)                              

    return list3



sen="You will buy the three books."
lis=Identification.segment_identify(sen)
#print whom_1(lis,0)
#print whom_2(lis,0)
#print who(lis,0)
#print whom_3(lis,0)
#print what_to_do(lis,0)
#print howmany(lis,0)
