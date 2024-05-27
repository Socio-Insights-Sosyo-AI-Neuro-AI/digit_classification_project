Digit Classification with CNN and PyQt5

This project is a digit classification application that uses a Convolutional Neural Network (CNN) for digit recognition and PyQt5 for the graphical user interface (GUI). The application allows users to draw digits on a canvas and classify them using a pre-trained CNN model.

Features

	•	Draw digits on a canvas and classify them.
	•	Add noise to the drawn digit before classification.
	•	Choose between two different CNN models for classification.
	•	View classification results with probabilities for each digit.
	•	Save classification results if desired.

Installation

Prerequisites

	•	Python 3.6+
	•	pip (Python package installer)

Required Libraries

You can install the required libraries using the following command:

pip install numpy matplotlib opencv-python PyQt5 keras


Clone the Repository

Clone this repository to your local machine using:

git clone https://github.com/your-username/digit-classification-cnn-pyqt5.git
cd digit-classification-cnn-pyqt5


Usage

	1.	Prepare the Models: Ensure that the pre-trained models (model1.h5 and model2.h5) are present in the same directory as your script. If not, you can train the models using the provided code in the script and save them.
	2.	Run the Application: Execute the script to start the application:

 python app.py

 	3.	Draw and Classify Digits: Use the “Draw Canvas” button to open the drawing canvas. Draw a digit and click “OK!”. Load the drawn image using the “Open Canvas” button, select the desired CNN model, add noise if needed, and click “Predict” to classify the digit.
	4.	View Results: The predicted digit and the probabilities for each class will be displayed. You can save the results if the “Save Result” checkbox is checked.

 Project Structure

	•	app.py: Main script containing the GUI and CNN implementation.
	•	model1.h5, model2.h5: Pre-trained CNN models.
	•	icon1.png: Icon used in the application.
	•	input_img.png: Placeholder for the drawn digit image.
	•	Output.txt: File to save the classification results (if the “Save Result” option is selected).

Dependencies

	•	PyQt5
	•	numpy
	•	matplotlib
	•	opencv-python
	•	keras

Contributing

If you wish to contribute to this project, please fork the repository and submit a pull request. We welcome all improvements and suggestions.

License

This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgements

This project uses the MNIST dataset for training and testing the CNN models.

Replace your-username with your actual GitHub username in the clone URL. This README provides a comprehensive overview and setup instructions for the project, making it easier for others to understand and use your digit classification application.
