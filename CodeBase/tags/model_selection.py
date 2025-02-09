
from sklearn import tree, svm, cross_validation
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
from scipy import interp
from sklearn.cross_validation import StratifiedKFold
import random
import numpy as np
import sqlite3


def main(database="blah.db"):

    # Generating handler for database
    print "Connecting to database"
    cursor = select_agility_content(database)

    # Extracting features and labels from database
    print "Extracting Features"
    features = []
    labels = []

    for feature in cursor:
        labels.append(int(feature[0]))
        features.append(feature[2:len(feature)+1])

    plot_roc(features, labels)


    #print "Generating Report"
    # Generating metrics for database under 6 known classification models
    #analyse_tree(features, labels)
    #analyse_gtb(features, labels)
    #analyse_sgd(features, labels)
    #analyse_forrest(features, labels)
    #analyse_logistic_regression(features, labels)
    #analyse_svm(features, labels)

def model(values=None, database="tags/lex.db"):

    # Generating handler for database
    print "Connecting to database"
    cursor = select_lexical_content(database)

    # Extracting features and labels from database
    print "Extracting Features"
    features = []
    labels = []

    for feature in cursor:
        labels.append(int(feature[0]))
        features.append(feature[2:len(feature)+1])

    classifier = RandomForestClassifier(n_estimators=10)
    classifier = classifier.fit(features, labels)
    lab = classifier.predict(values)
    print lab



def select_lexical_content(database):
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cursor = cur.execute("Select * from lexical")
        return cursor
    except sqlite3.Error as e:
        print "An error occurred: ", e.args[0]


def select_agility_content(database):
    try:
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cursor = cur.execute("Select * from Features")
        return cursor
    except sqlite3.Error as e:
        print "An error occurred: ", e.args[0]


# Generating an analysis for the given database under default SVM model
def analyse_svm(features, labels):

    # Generating the classifier
    classifier = svm.SVC()

    # Calculating various metrics under 10-fold cross validation
    accuracy = cross_validation.cross_val_score(classifier, features, labels, cv=10)
    roc = cross_validation.cross_val_score(classifier, features, labels, cv=10, scoring="roc_auc")
    precision = cross_validation.cross_val_score(classifier, features, labels, cv=10, scoring="precision")
    recall = cross_validation.cross_val_score(classifier, features, labels, cv=10, scoring="recall")

    # Generating Report for SVM as a model on the given database
    print "\n"
    print "Report: SVM model"
    print "Accuracy for SVM is: %0.2f (+/- %0.2f)" % (accuracy.mean(), accuracy.std())
    print "ROC for SVM is: %0.2f (+/- %0.2f)" % (roc.mean(), roc.std())
    print "Precision for SVM is: %0.2f (+/- %0.2f)" % (precision.mean(), precision.std())
    print "Recall for SVM is: %0.2f (+/- %0.2f)" % (recall.mean(), recall.std())


# Generating an analysis for the given database under default Decision Tree model
def analyse_tree(features, labels):

    # Generating the classifier
    classifier = tree.DecisionTreeClassifier()

    # Calculating various metrics under 5-fold cross validation
    accuracy = cross_validation.cross_val_score(classifier, features, labels, cv=10)
    roc = cross_validation.cross_val_score(classifier, features, labels, cv=10, scoring="roc_auc")
    precision = cross_validation.cross_val_score(classifier, features, labels, cv=10, scoring="precision")
    recall = cross_validation.cross_val_score(classifier, features, labels, cv=10, scoring="recall")

    # Generating Report for SVM as a model on the given database
    print "\n"
    print "Report: Decision Tree model"
    print "Accuracy for Decision Tree is: %0.2f (+/- %0.2f)" % (accuracy.mean(), accuracy.std())
    print "ROC for Decision Tree is: %0.2f (+/- %0.2f)" % (roc.mean(), roc.std())
    print "Precision for Decision Tree is: %0.2f (+/- %0.2f)" % (precision.mean(), precision.std())
    print "Recall for Decision Tree is: %0.2f (+/- %0.2f)" % (recall.mean(), recall.std())


# Generating an analysis for the given database under default Stochastic Gradient Descent model
def analyse_sgd(features, labels):

    # Generating the classifier
    classifier = SGDClassifier(loss="hinge", penalty="l2", shuffle=True)

    # Calculating various metrics under 5-fold cross validation
    accuracy = cross_validation.cross_val_score(classifier, features, labels, cv=10)
    roc = cross_validation.cross_val_score(classifier, features, labels, cv=10, scoring="roc_auc")
    precision = cross_validation.cross_val_score(classifier, features, labels, cv=10, scoring="precision")
    recall = cross_validation.cross_val_score(classifier, features, labels, cv=10, scoring="recall")

    # Generating Report for SVM as a model on the given database
    print "\n"
    print "Report: Gradient Descent model"
    print "Accuracy for Gradient Descent is: %0.2f (+/- %0.2f)" % (accuracy.mean(), accuracy.std())
    print "ROC for Gradient Descent is: %0.2f (+/- %0.2f)" % (roc.mean(), roc.std())
    print "Precision for Gradient Descent is: %0.2f (+/- %0.2f)" % (precision.mean(), precision.std())
    print "Recall for Gradient Descent is: %0.2f (+/- %0.2f)" % (recall.mean(), recall.std())


# Generating an analysis for the given database under default Gradient Tree Boosting model
def analyse_gtb(features, labels):

    # Generating the classifier
    classifier = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)

    # Calculating various metrics under 5-fold cross validation
    accuracy = cross_validation.cross_val_score(classifier, features, labels, cv=10)
    roc = cross_validation.cross_val_score(classifier, features, labels, cv=10, scoring="roc_auc")
    precision = cross_validation.cross_val_score(classifier, features, labels, cv=10, scoring="precision")
    recall = cross_validation.cross_val_score(classifier, features, labels, cv=10, scoring="recall")

    # Generating Report for SVM as a model on the given database
    print "\n"
    print "Report: Gradient Tree Boosting model"
    print "Accuracy for Gradient Boosting is: %0.2f (+/- %0.2f)" % (accuracy.mean(), accuracy.std())
    print "ROC for Gradient Boosting is: %0.2f (+/- %0.2f)" % (roc.mean(), roc.std())
    print "Precision for Gradient Boosting is: %0.2f (+/- %0.2f)" % (precision.mean(), precision.std())
    print "Recall for Gradient Boosting is: %0.2f (+/- %0.2f)" % (recall.mean(), recall.std())


# Generating an analysis for the given database under default Random Forest model
def analyse_forrest(features, labels):

    # Generating the classifier
    classifier = RandomForestClassifier(n_estimators=10)

    # Calculating various metrics under 5-fold cross validation
    accuracy = cross_validation.cross_val_score(classifier, features, labels, cv=10)
    roc = cross_validation.cross_val_score(classifier, features, labels, cv=10, scoring="roc_auc")
    precision = cross_validation.cross_val_score(classifier, features, labels, cv=10, scoring="precision")
    recall = cross_validation.cross_val_score(classifier, features, labels, cv=10, scoring="recall")

    # Generating Report for SVM as a model on the given database
    print "\n"
    print "Report: Random Forest model"
    print "Accuracy for Random Forest is: %0.2f (+/- %0.2f)" % (accuracy.mean(), accuracy.std())
    print "ROC for Random Forest is: %0.2f (+/- %0.2f)" % (roc.mean(), roc.std())
    print "Precision for Random Forest is: %0.2f (+/- %0.2f)" % (precision.mean(), precision.std())
    print "Recall for Random Forest is: %0.2f (+/- %0.2f)" % (recall.mean(), recall.std())


# Generating an analysis for the given database under default Logistic Regression model
def analyse_logistic_regression(features, labels):

    # Generating the classifier
    classifier = LogisticRegression()

    # Calculating various metrics under 5-fold cross validation
    accuracy = cross_validation.cross_val_score(classifier, features, labels, cv=10)
    roc = cross_validation.cross_val_score(classifier, features, labels, cv=10, scoring="roc_auc")
    precision = cross_validation.cross_val_score(classifier, features, labels, cv=10, scoring="precision")
    recall = cross_validation.cross_val_score(classifier, features, labels, cv=10, scoring="recall")

    # Generating Report for SVM as a model on the given database
    print "\n"
    print "Report: Logistic Regression model"
    print "Accuracy for Logistic Regression is: %0.2f (+/- %0.2f)" % (accuracy.mean(), accuracy.std())
    print "ROC for Logistic Regression is: %0.2f (+/- %0.2f)" % (roc.mean(), roc.std())
    print "Precision for Logistic Regression is: %0.2f (+/- %0.2f)" % (precision.mean(), precision.std())
    print "Recall for Logistic Regression is: %0.2f (+/- %0.2f)" % (recall.mean(), recall.std())


def plot_roc(features, labels):

    classifier = []
    name = []
    classifier.append(tree.DecisionTreeClassifier())
    name.append("Decision Tree")
    classifier.append(LogisticRegression())
    name.append("Logistic Regression")
    classifier.append(RandomForestClassifier(n_estimators=10))
    name.append("Random Forest")
    classifier.append(GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0))
    name.append("Gradient Boosting")
    classifier.append(SGDClassifier(loss="log", penalty="l2", shuffle=True))
    name.append("Gradient Descent")


    plt.figure()
    for i, temp in enumerate(classifier):
        print name[i]
        calculate_roc(features, labels, temp, name[i])

    plt.plot([0, 1], [0, 1], '--', color=(0.6, 0.6, 0.6), label='Luck')

    plt.xlim([-0.05, 1.05])
    plt.ylim([-0.05, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC for Lexical Analysis')
    plt.legend(loc="lower right")
    plt.show()


def calculate_roc(features, labels, classifier, name ):
    # Classification and ROC analysis
    features = np.asarray(features)
    labels = np.asarray(labels)

    # Run classifier with cross-validation and plot ROC curves
    cv = StratifiedKFold(labels, n_folds=10)

    mean_tpr = 0.0
    mean_fpr = np.linspace(0, 1, 100)

    for i, (train, test) in enumerate(cv):
        probas_ = classifier.fit(features[train], labels[train]).predict_proba(features[test])
        # Compute ROC curve and area the curve
        fpr, tpr, thresholds = roc_curve(labels[test], probas_[:, 1])
        mean_tpr += interp(mean_fpr, fpr, tpr)
        mean_tpr[0] = 0.0

    mean_tpr /= len(cv)
    mean_tpr[-1] = 1.0
    mean_auc = auc(mean_fpr, mean_tpr)
    plt.plot(mean_fpr, mean_tpr, 'k', label=name+' (area = %0.2f)' % mean_auc, lw=1, color=(random.random(), random.random(), random.random()))

if __name__ == "__main__": main()
