import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/pritp/Desktop/internship_file/zomato_sample_dataset.csv")

top_votes = df.groupby('Restaurant Name')['Votes'].max().sort_values(
    ascending=False).head(10)

print("Top 10 Restaurants by Votes:")
print(top_votes)

top_votes.plot(kind='bar', figsize=(10,5))
plt.title('Top 10 Restaurants by Votes')
plt.xlabel('Restaurant Name')
plt.ylabel('Votes')
plt.xticks(rotation=45)
plt.show()