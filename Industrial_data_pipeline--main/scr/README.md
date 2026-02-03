# Data_Pipeline 
This repo demonstartes my apporach for **reproducible, scalable, and production-oriented data pipelines**. This project mainly focuses on transforming raw, noisy data into analytical ready output.

# Key objectives
- To build a modular and maintainable data pipeline
- To handel real- world imperfections
- To ensure reproducibility and transparency
- To reliable analytics and decision support

# Tasks
- Perform pre-processing and normalization steps
- Validating and restructuring
- Filtering records based on target attributes or any condition
- Categorising records into predefined groups based on numerical thresholds
- Computing total metric as a combination of multiple input fields

## Overview About The Given Data Sets
The give datasets,
- Consists structured information about various recipies with their name, ingredients, preparation method which also contains images and URLS.
- Contains mix of categorical, numerical,textual, time based, Semi-structure, structured data
- Description of Columns,
     - name : tells the name of recipe
     - ingredients : gives the list of ingredients needed to prepare the particular dish
     - URL : URL that links to the recipe source of the dish
     - image : URL that links to the image of dish
     - cookTime : The actual time needed to cook the dish which is given in ISO 8601 duration format where P stands for 'Period', T stands for 'Time',H stands for 'Hour' and M stands for 'Minutes'
     - recipeYield : describes the number of servings
     - datePublished : tells when the recipe was published
     - prepTime : The time needed to prepare the dish which is given in ISO 8601 duration format where P stands for 'Period', T stands for 'Time',H stands for 'Hour' and M stands for 'Minutes'
     - description : Describes about the recipe

## Project Structure
- input folder : containing all the .json files as given
- output folder : contains .csv files that is obtained during the process along with data visualizations and final output of the code
- input_csv folder : contains the converted .csv files along with merged.csv file(for easy processing)
- scripts : contains the actual scripts to satisfy the given task. the scripts folder consists of following .py files,
   - data_preprocessing.py
   - data_cleaning.py
   - data_analysis.py
   - data_visualization.py
   - utils.py
- main.py : main python file where all the functions of other .py files are called and executed
- ETL_README.md : Documentation 

## Approach for the given task
1) Created input folder where all the 3 .json files are loaded
2) Created scripts folder where we will have 5 python files
3) In the data_preprocessing.py file, we convert .json files to .csv file and create input_csv folder and store all the converted .csv files and merge them for further processing
4) ISO 8601 time formate is converted into minutes using isodate module
5) Null and NaN values are filled with median values as mean values are not suitable in this situation
6) Outliers are capped using  IQR method/Winsorization method, as out of 1047 rows there are 231 outliers for cookTime and prepTime columns which is 22.06% of given data and is not suggestible to drop off the columns with outliers 
7) In data_analysis.py file, initial function is to filter out the ingredients that contains "beef" and then find the average value based on total_cooking_time
8) Ingredients are stored in list formate in the given dataset, hence parsing is required
9) The dataset is then classified into easy, medium and hard based on the given condition in the Task 2
10) Histogram and Box plots are plotted to check if the outliers still exists in the dataset
11) util.py is used as helping function for organization and reusability and handles errors with try-except blocks
12) Normalization method was not that suitable for the particular dataset as the time frame was getting converted between 0-1 range which is not suitable to run Task2
13) manin.py files calls all the functions that are defined in other .py files
14) .md file is used for documentation 

## Output 
- The final output is stored in output folder in virtual environment folder
- It helps us to classify the difficulty level and categorise it as easy, medium and hard by calculating average total cooking time
- Graphs used for data visualization helps us to understand about the dataset and outliers

## Conclusion
- The application contains ETL pipeline along with structured, efficiency, maintainability and scalability
- Data ingestion, transformation and storage is done successfully and graphs for data visualization are obtained
- Modular design of code with logging, error handling and supporting helper files 
- ETL pipelining provides good pathway for scalability and automation

