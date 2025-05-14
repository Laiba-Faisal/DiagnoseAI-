# DiagnoseAI

**DiagnoseAI** is a web-based disease prediction tool that uses machine learning to predict potential health conditions based on the symptoms entered by users. The application provides a simple and intuitive interface, where users can select their symptoms, and the model predicts the possible disease based on the input data.

## Features

- Predicts diseases based on user-inputted symptoms.
- Utilizes a trained machine learning model for accurate predictions.
- Clean and simple interface built with Flask.
- Real-time disease prediction based on a list of symptoms.

## How it Works

1. Users enter their symptoms via a web form.
2. The symptoms are passed to a machine learning model trained on various disease data.
3. The model predicts the disease that matches the given symptoms.
4. Users receive the prediction on the results page.

## Setup and Installation

### Prerequisites

Before setting up this project, ensure you have the following installed:
- Python 3.6 or higher
- Flask
- joblib (for loading the trained model)
- Other dependencies listed in `requirements.txt`

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/DiagnoseAI.git
   cd DiagnoseAI
