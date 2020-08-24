Reguired version:
---
This code runs on Python 2.7 and not Python 3. So, we needd to create a virtual environment using Python 2.7 with required installations.

----> virtualenv --python=/usr/bin/python2.7 BDTR

Required installations:
---
--> Tensorflow 1.14
--> numpy (latest)
--> sklearn
--> opencv

Dataset related code changes:
---
--> Download weights of Alexnet from the link given in Readme.md file
--> n_classes should be set to number of classes in the dataset (presently set to 16)
--> the same change would be applied to classification net (softmax layer ) in model.py
--> batch size should be smaller than n_classes for this implementation. Will be changed later, if required.
