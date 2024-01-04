import pandas as pd

def keep_first_two_words(sentence):
    words = sentence.split()
    return ' '.join(words[:2])


def pattern_filter(meta_new,organism,master_db):
 df =pd.DataFrame()

 for i in range(meta_new.shape[0]):
    d=d[d['Compound Name'].str.contains((meta_new["Name"][i]),case=False) ]
    df=pd.concat([d,df])
 return df