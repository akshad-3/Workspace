import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("/Users/akshad/GitHub/Workspace/Python/Practice/Case-Study/Dataset/spam.csv", encoding="latin-1")

# Select required columns
data = data[['v1', 'v2']]
data.columns = ['label', 'message']

# Convert labels
data['label'] = data['label'].map({
    'ham': 0,
    'spam': 1
})

# Input and output
X = data['message']
y = data['label']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Convert text into numerical features
vectorizer = CountVectorizer()

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Naive Bayes classifier
model = MultinomialNB()

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

# Test a new message
message = ["Congratulations! You won a free prize"]

message = vectorizer.transform(message)

prediction = model.predict(message)

if prediction[0] == 1:
    print("Spam Mail")
else:
    print("Not Spam Mail")