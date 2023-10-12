# YouTube Recipes LLM

Welcome to the **YouTube Recipes LLM** project repository! This project is designed to help you download captions from YouTube videos of a particular channel and convert those captions into ingredient lists and recipe instructions. This repository contains the necessary code and data to achieve this goal.

## Web Application
A streamlit web app was created to search and lookup recipes created with LLM. The app can be accessed here [here](https://youtube-recipes-llm.streamlit.app/)


## Project Overview

- **youtube_recipes_llm** is a Python project that enables you to extract data from YouTube captions and transform it into a more structured format, specifically, ingredient lists and recipe instructions.

- The project consists of two main components, each residing in its own Jupyter Notebook:
  1. **yt_data.ipynb**: In this notebook, you will find the code to download captions from YouTube videos and save the results to a CSV file located in the `data/recipes.csv` directory.
  2. **palm_model.ipynb**: The second notebook reads the data from `data/recipes.csv` and utilizes the PALM Google model to convert the text into recipe cards.

## Setup

To get started with this project, please follow these steps:

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/youtube_recipes_llm.git
   cd youtube_recipes_llm
   ```

2. Create a virtual environment (venv) to isolate the project's dependencies:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

5. Obtain a Google API Key:
   - To use the PALM Google model for text conversion, you will need to obtain an API key from Google. You can request the api key from [here](https://makersuite.google.com/waitlist)

6. Store the API key in a `config.py` file located inside the `notebooks` folder. The file should look like this:
   ```python
   palm_api_key = "YOUR_API_KEY"
   ```

## Usage

1. **yt_data.ipynb**: Open the "yt_data.ipynb" Jupyter Notebook in the `notebooks` folder. Follow the instructions in the notebook to download captions from YouTube videos of the specific channel. The results will be saved to the `data/recipes.csv` file.

2. **palm_model.ipynb**: Once you have the captions data in `data/recipes.csv`, open the "Convert to Recipe Cards" Jupyter Notebook in the `notebooks` folder. Run the code to convert the captions into recipe cards using the PALM Google model.

## Contributions

Contributions to this project are welcome. If you have any improvements, bug fixes, or new features to add, please feel free to create a pull request.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this code as long as you comply with the terms of the license.

Enjoy using the **YouTube Recipes LLM** project, and may your cooking endeavors be filled with delightful and easy-to-follow recipes! If you have any questions or run into issues, please don't hesitate to reach out.
