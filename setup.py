import pandas as pd

# head() funtion just shows the top 5 rows of a data frame
# a data frame is a table like data strcuture to show data in better format
# import the training dataset
train_df = pd.read_csv('data/train.csv', header=None)
print(train_df.head())

# importing the test data
test_df = pd.read_csv('data/test.csv', header=None)
print(test_df.head())


# Here, a label of 1 means the review is bad, and a label of 2 means the review is good.
# we are going to change this to 1--> 0 and 2--> 1
train_df[0] = (train_df[0] == 2).astype(int)
test_df[0] = (test_df[0] == 2).astype(int)

print(train_df.head())
print(test_df.head())


# to make things BERT friendly we need to change the daat format
train_df_bert = pd.DataFrame({
    'id':range(len(train_df)),
    'label':train_df[0],
    'alpha':['a']*train_df.shape[0],
    'text': train_df[1].replace(r'\n', ' ', regex=True)
})


print("\nBert Style Training data\n")
print(train_df_bert.head())


# For convinience now test data is named dev_df_bert
dev_df_bert = pd.DataFrame({
    'id':range(len(test_df)),
    'label':test_df[0],
    'alpha':['a']*test_df.shape[0],
    'text': test_df[1].replace(r'\n', ' ', regex=True)
})

print("\nBert Style Test data\n")
print(dev_df_bert.head())


# now we save these formats into .tsv that BERT likes
train_df_bert.to_csv('data/train.tsv', sep='\t', index=False, header=False)
dev_df_bert.to_csv('data/test.tsv',sep='\t',index=False,header=False)