import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample data
data = {
    "Subject": ["Math", "Science", "English", "History", "Art"],
    "Marks": [88, 92, 80, 76, 85]
}
df = pd.DataFrame(data)

# Simple bar chart
sns.barplot(x="Subject", y="Marks", data=df)
plt.title("Student Marks")
plt.show()
