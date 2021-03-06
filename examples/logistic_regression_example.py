# -*- coding: utf-8 -*-
"""
@Author: tushushu
@Date: 2018-08-21 17:16:29
@Last Modified by:   tushushu
@Last Modified time: 2018-08-21 17:16:29
"""
import os
os.chdir(os.path.split(os.path.realpath(__file__))[0])

import sys
sys.path.append(os.path.abspath(".."))

from imylu.utils import get_acc, load_breast_cancer, min_max_scale, run_time, \
    train_test_split
from imylu.linear_model.logistic_regression import LogisticRegression


def main():
    @run_time
    def batch():
        print("Tesing the accuracy of LogisticRegression(batch)...")
        # Train model
        clf = LogisticRegression()
        clf.fit(X=X_train, y=y_train, lr=0.05, epochs=200)
        # Model accuracy
        get_acc(clf, X_test, y_test)

    @run_time
    def stochastic():
        print("Tesing the accuracy of LogisticRegression(stochastic)...")
        # Train model
        clf = LogisticRegression()
        clf.fit(X=X_train, y=y_train, lr=0.01, epochs=200,
                method="stochastic", sample_rate=0.5)
        # Model accuracy
        get_acc(clf, X_test, y_test)

    # Load data
    X, y = load_breast_cancer()
    X = min_max_scale(X)
    # Split data randomly, train set rate 70%
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=10)
    batch()
    stochastic()


if __name__ == "__main__":
    main()
