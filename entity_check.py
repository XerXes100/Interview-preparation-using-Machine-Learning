import matplotlib.pyplot as plt

# Sample values
labels = ['Apples', 'Oranges', 'Bananas', 'Pears']
sizes = [35, 20, 25, 20]
colors = ['#ff5733', '#ffa600', '#ffd700', '#9acd32']  # Custom colors

# Create figure and axes objects
fig, ax = plt.subplots(figsize=(8, 6))

# Add a title
ax.set_title('Fruit Distribution', fontsize=20)

# Create the pie chart
pie = ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
             startangle=90, counterclock=False, wedgeprops=dict(width=0.4),
             textprops=dict(color="white", fontsize=14))

# Add a legend
ax.legend(pie[0], labels, loc="best", fontsize=12)

# Show the chart
plt.show()
