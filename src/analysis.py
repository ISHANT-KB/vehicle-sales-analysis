import matplotlib.pyplot as plt
import seaborn as sns
from clean import clean_data

# Get cleaned data
df = clean_data()

# Feature Engineering
df['price_diff'] = df['sellingprice'] - df['mmr']

#Price vs Mileage
plt.figure(figsize=(8,6))
plt.scatter(df['odometer'], df['sellingprice'], alpha=0.3)
plt.xlabel("Mileage")
plt.ylabel("Price")
plt.title("Price vs Mileage")

plt.savefig("../output/price_vs_mileage.png", dpi=300, bbox_inches='tight')
plt.close()

# Condition vs Price
sns.boxplot(x=df['condition'], y=df['sellingprice'])
plt.xticks(rotation=90)
plt.title("Condition vs Price")

plt.savefig("../output/condition_vs_price.png", dpi=300, bbox_inches='tight')
plt.close()

# Top 10 Car Brands by Sales
top_brands = df['make'].value_counts().head(10)

top_brands.plot(kind='bar')
plt.title("Top 10 Car Brands by Sales")
plt.xlabel("Brand")
plt.ylabel("Count")
plt.savefig("../output/top_brands.png", dpi=300, bbox_inches='tight')
plt.close()

# mmr vs selling price
plt.scatter(df['mmr'], df['sellingprice'], alpha=0.3)
plt.xlabel("MMR (Market Value)")
plt.ylabel("Selling Price")
plt.title("MMR vs Selling Price")
plt.savefig("../output/mmr_price.png", dpi=300, bbox_inches='tight')
plt.close()