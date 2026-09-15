```python
import re
import os
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


# File names
DATASET = "dataset.csv"
RESULT_FOLDER = "results"


# Common words found in phishing emails
phishing_words = [
    "urgent",
    "verify",
    "verification",
    "account suspended",
    "account locked",
    "click here",
    "login",
    "password",
    "confirm",
    "security alert",
    "winner",
    "prize",
    "free",
    "claim",
    "bank",
    "credit card",
    "immediately",
    "reset password"
]


# Find URLs in the email
def find_urls(text):
    urls = re.findall(
        r"https?://[^\s]+|www\.[^\s]+",
        text,
        re.IGNORECASE
    )

    return urls


# Count suspicious words
def count_phishing_words(text):
    text = text.lower()

    count = 0

    for word in phishing_words:
        if word in text:
            count += 1

    return count


# Display basic email features
def analyze_email(text):

    urls = find_urls(text)
    suspicious_words = count_phishing_words(text)

    print("\nEmail Analysis")
    print("----------------------")
    print("Email length:", len(text))
    print("Number of URLs:", len(urls))
    print("Suspicious keywords:", suspicious_words)

    if len(urls) > 0:
        print("URLs found:")

        for url in urls:
            print("-", url)


# Load dataset
if not os.path.exists(DATASET):

    print("dataset.csv file not found.")
    exit()

data = pd.read_csv(DATASET)


# Check required columns
if "text" not in data.columns or "label" not in data.columns:

    print("Dataset must contain 'text' and 'label' columns.")
    exit()


# Remove empty rows
data = data.dropna(subset=["text", "label"])


print("=" * 50)
print("PHISHING EMAIL DETECTION MODEL")
print("=" * 50)

print("\nTotal emails:", len(data))

print("\nDataset distribution:")
print(data["label"].value_counts())


# Input and output
emails = data["text"]
labels = data["label"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    emails,
    labels,
    test_size=0.20,
    random_state=42,
    stratify=labels
)


print("\nTraining emails:", len(X_train))
print("Testing emails:", len(X_test))


# Convert email text into numerical features
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=5000,
    ngram_range=(1, 2)
)

X_train_vector = vectorizer.fit_transform(X_train)
X_test_vector = vectorizer.transform(X_test)


# Create machine learning model
model = LogisticRegression(
    max_iter=1000
)


# Train the model
print("\nTraining model...")

model.fit(
    X_train_vector,
    y_train
)


# Make predictions
predictions = model.predict(X_test_vector)


# Calculate accuracy
accuracy = accuracy_score(
    y_test,
    predictions
)


print("\nModel Results")
print("----------------------")
print("Accuracy:", round(accuracy * 100, 2), "%")


# Classification report
print("\nClassification Report")
print("----------------------")

print(
    classification_report(
        y_test,
        predictions,
        zero_division=0
    )
)


# Create results folder
os.makedirs(RESULT_FOLDER, exist_ok=True)


# Create confusion matrix
matrix = confusion_matrix(
    y_test,
    predictions,
    labels=["safe", "phishing"]
)


display = ConfusionMatrixDisplay(
    confusion_matrix=matrix,
    display_labels=["Safe", "Phishing"]
)

display.plot()

plt.title("Phishing Email Detection")
plt.tight_layout()


# Save confusion matrix
matrix_file = os.path.join(
    RESULT_FOLDER,
    "confusion_matrix.png"
)

plt.savefig(matrix_file)

plt.show()

print("\nConfusion matrix saved to:", matrix_file)


# Test a new email
while True:

    choice = input(
        "\nDo you want to test an email? (y/n): "
    ).lower()

    if choice == "n":
        break

    if choice != "y":
        print("Please enter y or n.")
        continue

    print("\nEnter the email text.")
    print("Type END when finished.")

    email_lines = []

    while True:

        line = input()

        if line.strip().upper() == "END":
            break

        email_lines.append(line)

    new_email = " ".join(email_lines)

    if new_email.strip() == "":
        print("No email entered.")
        continue


    # Analyze email
    analyze_email(new_email)


    # Convert email into TF-IDF features
    new_email_vector = vectorizer.transform(
        [new_email]
    )


    # Predict
    result = model.predict(
        new_email_vector
    )[0]


    # Prediction probability
    probability = model.predict_proba(
        new_email_vector
    )

    confidence = max(probability[0]) * 100


    print("\nPrediction")
    print("----------------------")

    if result.lower() == "phishing":

        print("Result: PHISHING")

    else:

        print("Result: SAFE")

    print(
        "Confidence:",
        round(confidence, 2),
        "%"
    )


print("\nProgram completed.")
```

### Keep these files together

```text
phishing-email-detection-model/
|
├── phishing_detector.py
├── dataset.csv
├── requirements.txt
├── README.md
├── .gitignore
|
└── results/
```

### Run it

In Git Bash:

```bash
cd ~/Desktop/phishing-email-detection-model
```

Install the libraries:

```bash
pip install -r requirements.txt
```

Run:

```bash
python phishing_detector.py
```

After training, you'll get:

```text
Accuracy
Classification Report
Confusion Matrix
```

and this file will be created automatically:

```text
results/confusion_matrix.png
```

**One important point:** the 20-row sample dataset I gave earlier is only for checking that your code works. For your internship submission, use a substantially larger dataset; otherwise the accuracy can be misleadingly high.
