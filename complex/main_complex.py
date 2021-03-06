import nltk
import question
import howMuch_howMany
import clause
import where

f1=open("/home/rubel/pyt/project_resource/complex/test_complex.txt","r+")
str1=','
for i in range(0,10):
    sen=f1.next()
    from nltk.tag.stanford import StanfordNERTagger
    st=StanfordNERTagger('/home/rubel/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz','/home/rubel/stanford-ner/stanford-ner.jar',encoding='utf-8')
    lis=st.tag(sen.split())

    tok=nltk.word_tokenize(sen)
    tag=nltk.pos_tag(tok)

    question.init(tag,sen)
       
    if str1 not in sen:

       question.whom_1(tag,tok,lis)
       question.whom_2(tag,tok,lis)
       question.whom_3(tag,tok,lis)
       question.who(tag,tok,lis)
       howMuch_howMany.howMuch(tag,tok,lis)
       howMuch_howMany.howMuch2(tag,tok,lis)
       howMuch_howMany.howMuch3(tag,tok,lis)
       howMuch_howMany.howMany(tag,tok,lis)
       question.what_to_do(tag,tok)
       question.whose(tag,tok)
       clause.because_that(tok)
       where.question_where_when(tag,tok,lis)
       
    else:        
        clause.clause_ques(tok,lis,sen)
        
    
f1.close()





