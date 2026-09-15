# Phishing Email Detection Model

## About the Project

This project is a machine learning based phishing email detection system developed as part of my cybersecurity internship.

The main purpose of this project is to identify whether an email is phishing or safe by analyzing its content and some common phishing indicators.

The model is developed using Python and Scikit-learn.

## What This Project Does

The project can:

* Train a model using phishing and safe emails
* Analyze the text content of emails
* Detect suspicious keywords
* Detect URLs in emails
* Check for suspicious URL patterns
* Classify an email as Phishing or Safe
* Calculate the model accuracy
* Display the classification report
* Generate a confusion matrix
* Test a new email entered by the user

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib

## Machine Learning Algorithm

I used Logistic Regression for classification.

The email text is converted into numerical features using TF-IDF before training the model.

## Features Used

The project checks different characteristics of an email, including:

* Email text
* Email length
* Number of URLs
* Suspicious URLs
* Phishing-related keywords
* Special characters
* Numbers in the email

## Project Structure

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
    └── confusion_matrix.png
```

## How to Run

First, install the required Python libraries:

```bash
pip install -r requirements.txt
```

Then run the program:

```bash
python phishing_detector.py
```

The program will load the dataset and train the machine learning model.

After training, it will display the accuracy and classification report.

It will also generate the confusion matrix inside the `results` folder.

## Example

A phishing email may contain messages like:

```text
Urgent! Your account has been suspended.
Click here to verify your password immediately.
```

The model will analyze the email and predict:

```text
Result: PHISHING
```

A normal email such as:

```text
Hello, the project meeting is scheduled for tomorrow at 10 AM.
```

may be classified as:

```text
Result: SAFE
```

## Model Evaluation

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

The confusion matrix is saved as:

```text
results/confusion_matrix.png
```

## Dataset

The dataset contains email text and its corresponding label.

The labels used in this project are:

```text
phishing
safe
```

For better results, a larger dataset containing different types of phishing and legitimate emails can be used.

## Limitations

This is a basic machine learning project created for learning and internship purposes.

The model may sometimes classify a legitimate email as phishing or a phishing email as safe.

Phishing methods also change over time, so the model should be trained with updated datasets.

## Future Improvements

Some improvements I can add in the future are:

* Use a larger dataset
* Add email header analysis
* Improve URL analysis
* Check sender information
* Add a web-based interface
* Add real-time email scanning
* Use more machine learning algorithms
* Integrate threat intelligence sources

## What I Learned

Through this project, I learned about:

* Phishing attacks
* Machine learning classification
* Natural Language Processing
* TF-IDF
* Logistic Regression
* Feature extraction
* Model evaluation
* Confusion matrix
* Basic email security

## Author

Pawan Badarli

B.Tech in Electronics and Communication Engineering

Visvesvaraya Technological University
