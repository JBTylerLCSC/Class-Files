#This is a test file for GitHub Repsository
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file containing Melbourne housing data
mydata = pd.read_csv("C:/Users/josh/Dropbox/Josh/CWI/datasets/SP25/melb_data.csv")

# Set the number of top sellers to display
top_n = 5 

# Group data by seller, calculate median price, sort in descending order and get top sellers
groupd = mydata.groupby(['Seller']).agg(Median_Value=('Price', 'median')).sort_values(by='Median_Value',ascending=False).head(top_n)

# Create labels combining seller name and median value
groupd['Labels'] = groupd.apply(lambda x: f"{x.name}\n{x['Median_Value']}", axis=1)

# Display the grouped data
print(groupd)

# Create a pie chart showing median values by seller
groupd.plot(kind='pie', title='Sales output', y="Median_Value", labels=groupd['Labels'])

# Add legend to the plot
plt.legend(loc='upper left', bbox_to_anchor=(0, 0), fontsize='small')

# Add axis labels
plt.xlabel("Sellers")
plt.ylabel("Total Sales")

# Display the plot
plt.show()