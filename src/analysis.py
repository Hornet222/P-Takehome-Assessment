# This is the file where you will run the analysis code.

import os
import logging
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Setup logging
logging.basicConfig(filename='/logs/logfile.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
logger = logging.getLogger()

load_dotenv()

# Reading environment variables
DATABASE_URL = os.getenv('DATABASE_URL')

# Connect to the target database
engine = create_engine(DATABASE_URL)

def execute_query(query):
    try:
        with engine.connect() as connection:
            result = connection.execute(text(query))
            return result.fetchall()
    except Exception as e:
        logger.error(f"Error executing query: {str(e)}")
        return None

def main():
    queries = {
        "overall_highest_expense": """
            SELECT e.name, SUM(exp.cost) as total_expense
            FROM employees e
            JOIN (
                SELECT metadata::json ->>'employeeId' as employeeId, cost
                FROM expenses
            ) exp ON e."employeeId" = exp.employeeId
            GROUP BY e.name
            ORDER BY total_expense DESC
            LIMIT 1
        """,
        "highest_expense_q1_2022": """
            SELECT e.name, SUM(exp.cost) as total_expense
            FROM employees e
            JOIN (
                SELECT metadata::json ->>'employeeId' as employeeId, cost, metadata::json ->>'date' as expense_date
                FROM expenses
            ) exp ON e."employeeId" = exp.employeeId
            WHERE expense_date >= '2022-01-01' AND expense_date <= '2022-03-31'
            GROUP BY e.name
            ORDER BY total_expense DESC
            LIMIT 1
        """,
        "highest_average_expense": """
            SELECT e.name, AVG(exp.cost) as average_expense
            FROM employees e
            JOIN (
                SELECT metadata::json ->>'employeeId' as employeeId, cost
                FROM expenses
            ) exp ON e."employeeId" = exp.employeeId
            GROUP BY e.name
            ORDER BY average_expense DESC
            LIMIT 1
        """
    }

    results = {
        "overall_highest_expense": None,
        "highest_expense_q1_2022": None,
        "highest_average_expense": None
    }

    for key, query in queries.items():
        result = execute_query(query)
        if result:
            results[key] = result[0]

    summary = (
        f"Summary of transactions:\n"
        f"1. Overall highest expense : $ {results['overall_highest_expense'][1]:,.2f} by {results['overall_highest_expense'][0]}\n"
        f"2. Overall highest expense for Q1 2022 : $ {results['highest_expense_q1_2022'][1]:,.2f} by {results['highest_expense_q1_2022'][0]}\n"
        f"3. Overall highest average expense : $ {results['highest_average_expense'][1]:,.2f} by {results['highest_average_expense'][0]}\n"
    )

    with open('/output/results.txt', 'w') as f:
        f.write(summary)

    print(summary)
    logger.info(f"Successfully ran analysis!.")

if __name__ == '__main__':
    main()

