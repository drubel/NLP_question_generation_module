# -*- coding: utf-8 -*-
import Clause
import Non_clause
import Identification
import nltk
from nltk.tag.stanford import StanfordNERTagger

def function(sen):
    list1=sen.split(".")
    str1=[]
    if len(list1)!=0:
        for i in range(len(list1)):
            list2=list1[i].split(",")
            str1.append((list1[i]+'.'))
            m11=nltk.word_tokenize(list1[i])
            st=StanfordNERTagger("/home/rubel/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz","/home/rubel/stanford-ner/stanford-ner.jar")
            ner=st.tag(m11)
            
            if(len(list2))!=0:
                for j in range(len(list2)):
                    try:
                        str1+=Clause.howmuch_2(list2,j,ner)
                    except Exception:
                            pass
                        
                
                    if Identification.clause_identify(list2[j])==1:                       
                           
                           try:
                               str1+=Clause.whom_1(list2,j,ner)
                           except Exception:
                               pass
                           try:
                               str1+=Clause.whom_2(list2,j,ner)
                           except Exception:
                               pass
                           try:
                               str1+=Clause.whom_3(list2,j,ner)
                           except Exception:
                               pass
                           try:
                               str1+=Clause.whose(list2,j,ner)
                           except Exception:
                               pass
                           try:
                               str1+=Clause.what_to_do(list2,j,ner)
                           except Exception:
                               pass
                           try:
                               str1+=Clause.who(list2,j,ner)
                           except Exception:
                               pass
                           try:
                               str1+=Clause.howmuch_1(list2,j,ner)
                           except Exception:
                               pass
                           try:
                               str1+=Clause.howmuch_3(list2,j,ner)
                           except Exception:
                               pass
                            
                    else:
                        try:
                            s=Identification.subjectphrase_search(list2,j)
                        except Exception:
                            pass
                        
                        if len(s)!=0:
                           list2[j]=s+list2[j]
                           try:
                               str1+=Clause.whom_1(list2,j,ner)
                           except Exception:
                               pass
                           try:
                               str1+=Clause.whom_2(list2,j,ner)
                           except Exception:
                               pass
                           try:
                               str1+=Clause.whom_3(list2,j,ner)
                           except Exception:
                               pass
                           try:
                               str1+=Clause.whose(list2,j,ner)
                           except Exception:
                               pass
                           try:
                               str1+=Clause.what_to_do(list2,j,ner)
                           except Exception:
                               pass
                           try:
                               str1+=Clause.who(list2,j,ner)
                           except Exception:
                               pass
                            
                            
                        else:
                            try:
                                str1+=Non_clause.what_whom1(list2,j,ner)
                            except Exception:
                                pass
                            try:
                                str1+=Non_clause.what_whom2(list2,j,ner)
                            except Exception:
                                pass
                            try:
                                str1+=Non_clause.whose(list2,j,ner)
                            except Exception:
                                pass                            
                            try:
                                str1+=Non_clause.howmany(list2,j,ner)
                            except Exception:
                                pass                            
                            try:
                                str1+=Non_clause.howmuch_1(list2,j,ner)
                            except Exception:
                                pass
            str1.append('\n')

    return str1


sen='In Scotland,two battlefields, Culloden and Bannockburn ,stand out as iconic spaces, recognised not only by Scots but also by visitors.'

