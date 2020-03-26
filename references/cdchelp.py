<<<<<<< HEAD
#generate a plot grouping by birth_year and a column given
#Logscale on Y
def plot_gpYR(df,col,xlab,ylab,title,kind='line'):
    groupDF = df.groupby('birth_year')[col].value_counts().unstack()
    plt.figure(figsize=(20,20))
    groupDF.plot(kind=kind,logy=True, legend=True)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(title)
    return

#visual display of top n values in columns and their counts
def skewness (df,cols,n=10):
    for c in df.columns[cols]:
        print('\nCOLUMN: "{}"\n=============================='.format(c))
        info_string = df[c].value_counts(dropna=False).nlargest(n).to_string()
        print(info_string)
        continue
    return
#sample a dataframe given different fraction sizes and display
def sampler (df,samples):    
	for i in samples:
	print('\nFrac samples: {}=============================='.format(i))
	%time print(df.sample(frac=i).agg(['mean','std']))
	return
	
#return a sampled dataframe based on a given number of samples
def sampled_df (df,samples):    
    return df.sample(samples)
=======
#Put helperfxns here, avoid double naming things

#To check values of column, enter data_frame as normal, col as 
def val_check(data_frame, column_name = str):
    df = pd.DataFrame(data_frame)
    col = column_name
    print( "Value counts of %s \n" %(col), df[col].value_counts())
    print("Value counts of %s by year \n" %(col), df.groupby(['birth_year'])[col].value_counts())



<<<<<<< HEAD
 
>>>>>>> upstream/master
=======
 def pct_bplot(dataframe, group = str, target = 'admit_NICU', column_title = ['Y','N'] ):
    df1 = dataframe.groupby([group])[[target]].count()
    df2 =  dataframe.groupby([group])[target].value_counts().unstack()
    df2 = df2.reindex(columns=column_title)
    df3 = pd.merge(df1,df2, left_index = True, right_index = True)
    pct_df = pd.DataFrame(list(map(lambda x: df3[x]/df3[target] * 100, df3.columns[1:])))
    pct_df = pct_df.T
    pct_df.plot(kind = 'bar', stacked = True)
>>>>>>> upstream/master
