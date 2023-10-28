# How to run below assignment

- Clone repository to local machine
- Add employees.csv and expenses.csv to /data folder (instead of employees_placeholder.txt and expenses_placeholder.txt)
- rename .exampleenv to .env or create your own .env file
- Run steps outlined under "Steps We Will Take to Review Your Solution"


# Plooto Data Engineer Take Home Task

## Instructions

**Context** : The test is intended to evaluate on three basis aspects of data engineering: database concepts, data pipelines and SQL.

Included in this repo are the following:
- A `data` directory with some sample data.
- A `docker-compose.yml` file for running the application with a containerized Postgres database.
- A `src` directory with a few files for you to complete.
- A shell of a `Dockerfile` to get you started. 

## Assessment Tasks
There are three distinct parts to this assessment:

1. **Database Setup** : Create a bootstrap script to create a Postgres database with the following tables (feel free to use the `public` schema): 
`employees` and `expenses`. You should take a look at the mock data files in the `data` directory to see what the data looks like.


2. **Data Pipeline** : Create a seed script to insert the included mock data into the database from step 1.

3. **Data Analysis** : Create an analysis script to query the containerized database, and print out the results of the following questions:
  - What is the name of the employee with the greatest TOTAL expenses? What was their total expense?
  - What is the name of the employee with the greatest TOTAL expenses in the first quarter of 2022? What was their total expense in this time frame?
  - What is the name of the employee with the greatest AVERAGE expense? What was their average expense?
  - Expected Output format for Data Analysis:
    ```
    Summary of transactions:
    1. Overall highest expense : $ xx,xxx.x by XXXXXX
    2. Overall highest expense for Q1 2022 : $ xx,xxx.xx by XXXXXX
    3. Overall highest average expense : $ xx,xxx.xx by XXXXXX
    ```
 

## Suggestions and Notes

- Feel free to use any data tools you'd like, as long as they can be containerized and included in your docker image.
- You will need to create a Dockerfile to build your image. 
- Note: the mock data CSV files are pipe `|` seperated to avoid issues with commas in the JSON column. 
- In the analysis script, we would like you to query the containerized database using SQL queries. Please do not find the answers by parsing the CSV files with python directly. 
- You can print the result directly or write into a file in csv format or text format 

## Steps We Will Take to Review Your Solution
1. `docker-compose build`
2. `docker-compose up`
3. **Database Setup** : `docker-compose run app python bootstrap.py`
4. **Data Pipeline** : `docker-compose run app python seed.py`
5. **Data Analysis** : `docker-compose run app python analysis.py`
