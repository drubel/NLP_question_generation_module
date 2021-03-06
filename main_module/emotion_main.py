import Identification
import emotion
import emotion_special
import nltk


f1=open("cnv.txt","r+")
fo=open("out_dialouge.txt","a+")

l=f1.readlines()

for i in range(0,len(l)):
    sen=l[i]
    
    if sen.startswith('//')==True:

       fo.write("\n\n")
       fo.write(sen)


    else:

       ll=sen.split(":")
       for i1 in range(1,len(ll)):

           se=ll[i1].split('.')
           for i2 in range(0,len(se)):

               see=se[i2].split('?')
               for i3 in range(0,len(see)):

                    xx1='';xx2=''
                    xx=nltk.word_tokenize(see[i3])
                    if len(xx)!=0:
                       xx1=xx[len(xx)-1]+'?'
                       xx2=xx[len(xx)-1]+' ?'
                    
                    if xx1 in se[i2]:
                        
                        if len(see[i3])!=2:
                           fo.write('\n-----------------------------------------------------\n')
                           fo.write(see[i3]+' ?')
                           fo.write('\n')

                           fo.write('Sp.Rule6- Q. Why '+see[i3]+'?\n')
                           fo.write('Sp.Rule7- Q. How '+see[i3]+'?\n')                           
                           
                        lis1=emotion_special.emotion_5(see,i3)
                        for k in range(0,len(lis1)):
                            if len(lis1[k])!=0:
                               fo.write(lis1[k])
                               fo.write("\n")
                   
                        lis1=emotion_special.emotion_1(see,i3)
                        for k in range(0,len(lis1)):
                            if len(lis1[k])!=0:
                               fo.write(lis1[k])
                               fo.write("\n")

                    else:

                         lis=Identification.segment_identify(see[i3])

                         for j in range(0,len(lis)):

                             fo.write('\n------------------------------------------------\n')
                             fo.write(lis[j]+'.')
                             fo.write("\n")

                             if Identification.clause_identify(lis[j])==1:

                                lis1=emotion.whom_1(lis,j)
                                for k in range(0,len(lis1)):
                                   if len(lis1[k])!=0:
                                      fo.write(lis1[k])
                                      fo.write("\n")
                   
                                lis1=emotion.whom_2(lis,j)
                                for k in range(0,len(lis1)):
                                   if len(lis1[k])!=0:
                                      fo.write(lis1[k])
                                      fo.write("\n")
                   
                                lis1=emotion.whom_3(lis,j)
                                for k in range(0,len(lis1)):
                                   if len(lis1[k])!=0:
                                      fo.write(lis1[k])
                                      fo.write("\n")
                   
                                lis1=emotion.who(lis,j)
                                for k in range(0,len(lis1)):
                                   if len(lis1[k])!=0:
                                      fo.write(lis1[k])
                                      fo.write("\n")
                   
                                lis1=emotion.what_to_do(lis,j)
                                for k in range(0,len(lis1)):
                                   if len(lis1[k])!=0:
                                      fo.write(lis1[k])
                                      fo.write("\n")

                                lis1=emotion_special.emotion_5(lis,j)
                                for k in range(0,len(lis1)):
                                    if len(lis1[k])!=0:
                                       fo.write(lis1[k])
                                       fo.write("\n")
                   
                             lis1=emotion_special.emotion_2(lis,j)
                             for k in range(0,len(lis1)):
                                 if len(lis1[k])!=0:
                                    fo.write(lis1[k])
                                    fo.write("\n")
                   
                             lis1=emotion_special.emotion_3(lis,j)
                             for k in range(0,len(lis1)):
                                 if len(lis1[k])!=0:
                                    fo.write(lis1[k])
                                    fo.write("\n")
                   
                             lis1=emotion_special.emotion_4(lis,j)
                             for k in range(0,len(lis1)):
                                 if len(lis1[k])!=0:
                                    fo.write(lis1[k])
                                    fo.write("\n")
        

f1.close()
fo.close()
