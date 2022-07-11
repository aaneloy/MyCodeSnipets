# read csv without unnamed columns
health_df = pd.read_csv(r'dataset\processed.csv')
health_df = health_df.loc[:, ~health_df.columns.str.contains('^Unnamed')]
print(health_df.shape)
health_df.head(5)

#skip unnamed colums
df.to_csv(r"dataset\processed.csv", index=False)

# Delete rows containing either 70% or more than 90% NaN Values
perc = 70.0
min_count =  int(((100-perc)/100)*df.shape[1] + 1)
mod_df = df.dropna( axis=0,
                    thresh=min_count)
print("Modified Dataframe : ")
print(mod_df)


#Drop Dataframe columns containing 60% missing value
df_2 = df.dropna(thresh=df.shape[0]*0.6,how='all',axis=1)

#missing value imputer
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(mod_df)
imputed_df = imputer.transform(mod_df.values)

#drrop rows by range
health_df = health_df.drop(health_df.index[92064:100766])

#ALternative of label-encoder, python mapping
df = pd.DataFrame({col: df[col].astype('category').cat.codes for col in df}, index=df.index)
{col: {n: cat for n, cat in enumerate(df[col].astype('category').cat.categories)}
     for col in df}


#reshape
df = pd.DataFrame([[1,2,3],[4,5,6]])
print(pd.DataFrame(df.values.reshape(1,-1)))