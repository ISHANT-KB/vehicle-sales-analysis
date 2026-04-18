import pandas as pd
df = pd.read_csv("../data/car_prices.csv")
print("Basic info about the dataset: ",df.info())
print("Shape of the dataset: ", df.shape)
null_info = df.isnull().sum()
print(null_info)
print("removing duplicate rows....")
df=df.drop_duplicates()
print("removed duplicate rows....")

print("shape of the dataset is: ", df.shape)

print("filling important columns....")

df["make"] = df["make"].fillna("Unknown")
df["model"] = df["model"].fillna("Unknown")
df["trim"] = df["trim"].fillna("Unknown")
df["body"] = df["body"].fillna(df["body"].mode()[0])
df["transmission"] = df["transmission"].fillna(df["transmission"].mode()[0])
df['mmr'] = df['mmr'].fillna(df['mmr'].median())
df['color'] = df['color'].fillna('Unknown')
df['interior'] = df['interior'].fillna('Unknown')
df['condition'] = df['condition'].fillna(df['condition'].median())

print("filled important columns")

print("Removing unwanted columns....")
df = df.drop(columns=['vin','trim','seller'])

print("removed unwanted columns....")

#Remove Outliers
def cap_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    print(f"{column} -> Lower: {lower}, Upper: {upper}")

    df[column] = df[column].clip(lower, upper)
    return df

df = cap_outliers(df, 'sellingprice')
df = cap_outliers(df, 'odometer')
df = cap_outliers(df, 'mmr')


def clean_data():
    return df
