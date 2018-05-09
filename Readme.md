# Machine Learning

_Elective for [CS graduate students](https://www.fh-rosenheim.de/technik/informatik-mathematik/informatik-master/) at the [University of Applied Sciences Rosenheim](https://www.fh-rosenheim.de). --- Wahlmodul inm [Masterstudiengang Informatik](https://www.fh-rosenheim.de/technik/informatik-mathematik/informatik-master/) an der [Hochschule Rosenheim](https://www.fh-rosenheim.de)._



## Class Schedule and Credits

**Time and Location:** Thursdays at 1.45p, B0.09

**Communication** on [Mattermost](https://inf-mattermost.fh-rosenheim.de/ml-2018/channels/town-square) ([register](https://inf-mattermost.fh-rosenheim.de/signup_user_complete/?id=xuci9kd4fjrcpkzc64yxxrxw4a)) and via the [Community](https://www.fh-rosenheim.de/community/inf-community/).

**Format:** We'll discuss the foundations of machine learning and how to conduct scientific experiments to analyze system performance.

_Note: This class is taught by Profs. Breunig, Riedhammer and Schmidt; not all materials are available here._


**Credits:** Oral exam at the end of the semester, tentative date: July 10.


_Note: Materials will be in English, the lectures/tutorials will be taught in German; the oral exam in the language of your choice._


## Recommended Textbooks

- Niemann, H: _Klassifikation von Mustern._ 2. Überarbeitete Auflage, 2003 ([available online](https://www5.cs.fau.de/fileadmin/Persons/NiemannHeinrich/klassifikation-von-mustern/m00-www.pdf))
- Russel, SJ and Norvig, P: Artificial Intelligence: A Modern Approach (2010)
by Stuart J. Russell  (Autor),‎ Peter Norvihttps://www.amazon.de/dp/0136042597
- Goodfellow, I and Bengio,Y and Courville, A: _Deep Learning._ 2016 ([available online](http://www.deeplearningbook.org/))


## Syllabus

- **March 15 (1): Introduction (BrM, RiKo, SJ)**
	
	We'll start with series of motivational examples why it's a great idea to study machine learning.
	We share experiences we've made in our fields: data science, speech and image processing.

- **March 15 (2): [Non-parametric](/1-knn/) and [Parametric Classifiers](/2-logr/) (RiKo)**
	
	We distinguish between _non-parametric_ classifiers, which use part of the training data to make decisions, and _parametric_ classifiers, which use a model _learned from data_ to make decisions.
	We'll start with the non-parametric _k-nearest-neighbor_ and contrast that with the _parametric_ logistic regression (which is actually a classification).

- **March 22: Regression (BrM)**
	
	Learn how to estimate and apply linear and polynomial regression to obtain a numeric value based on some input.
	
	_Materials available in the [Community](https://www.fh-rosenheim.de/community/inf-community/lehrveranstaltungen/)._

- _March 29: no class (Easter)_

- **April 5: Clustering, pt. 1 (RiKo)**
	
	Identify clusters of data in an unsupervised manner.
	We'll discuss _k-means_ and the related _k-medoid_, and the LBG vector quantization algorithm.

- **April 12: Custering, pt. 2 (BrM)**

	Learn how Gaussian mixture models can be used to identify clusters, and how to estimate the parameters using _expectation maximization (EM)_.

	_Materials available in the [Community](https://www.fh-rosenheim.de/community/inf-community/lehrveranstaltungen/)._

- **April 19: Statistical Classification (SJ)**
	
	Combining Bayes' statistics with cost functions allows us to define the _optimal classifier_.
	We then look at two statistical classifiers: the _naive Bayes_ and _Gaussian_ classifier.

	_Materials available in the [Community](https://www.fh-rosenheim.de/community/inf-community/lehrveranstaltungen/)._

- **April 26: Artificial Neural Networks (RiKo)**
	
	We start at a single neuron (which is related to logistic regression), and work our way up to single and multi-layer perceptrons ("deep neural nets").
	Learn how _error backpropagation_ can be used to learn these fascinating classifiers.

- **May 3: Non-parametric Classifiers (BrM)**

	Decision trees are a simple yet powerful non-parametric classifier: they don't rely on statistical distributions but on instances of the training data.
	We'll discuss how _classification and regression trees (CART)_ can be learned with C4.5.
	The related random forests combine decision trees and are thus parametric classifiers.

	_Materials available in the [Community](https://www.fh-rosenheim.de/community/inf-community/lehrveranstaltungen/)._

- _May 10: no class (Ascension Day)_

- **May 17: [Support Vector Machines](/svm/svm.pdf) (RiKo)**

	Support vector machines are a powerful non-parametric classifier.
	They are based on large margin optimization, and particularly robust against outliers.
	Their simple evaluation scheme makes them an excellent choice for embedded systems.

- **May 24: Scientific Experiments (BrM)**

	Learn how to run scientific experiments: distinguish between training and test, understand boostrapping and cross-validation, and how to read _receiver operator curves (ROC)_.

	_Materials available in the [Community](https://www.fh-rosenheim.de/community/inf-community/lehrveranstaltungen/)._

- _May 31: no class (Corpus Christi)_

- **June 7: Feature Normalization (SJ)**
	
	So far, most of this class focused on _how to train_ the systems, but less so the data.
	Feature normalization is an important step for many algorithms, since they rely on different assumptions on the data.

	_Materials available in the [Community](https://www.fh-rosenheim.de/community/inf-community/lehrveranstaltungen/)._

- **June 14: Principal Component Analysis (SJ)**

	The _principal component analysis (PCA)_ can be used to reduce the dimensions of your input features, and thus make the computation more efficient.
	Also, system performance tends to improve, since unneccessary information is removed.
	
	_Materials available in the [Community](https://www.fh-rosenheim.de/community/inf-community/lehrveranstaltungen/)._

- **June 21: Feature Rating and Feature Selection (SJ)**

	No clue what features to use?
	Just extract a lot and have the system learn which features are important for the task.

	_Materials available in the [Community](https://www.fh-rosenheim.de/community/inf-community/lehrveranstaltungen/)._

- **June 28: Review (BrM, RiKo, SJ)**

	We'll recap and discuss the syllabus and wrap up the semester.

- **July 5: Oral Exams (tentative)**


_Subscribe to [https://github.com/hsro-inf-ml/hsro-inf-ml.github.io](https://github.com/hsro-inf-ml/hsro-inf-ml.github.io/) repository to follow updates._
