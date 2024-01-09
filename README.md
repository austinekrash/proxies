
Note
The script does not handle or log non-working proxies explicitly. 
You may modify the except block in the extract function to include logging or handling of failed proxy checks.

Dependencies
requests: The script relies on the requests library for making HTTP requests.
concurrent.futures: The ThreadPoolExecutor is part of the concurrent.futures module and is used for parallel execution.

Requirements

Python 3.x

Internet connectivity for making HTTP requests


How to Run
Save the proxy list in the http.csv file.
Execute the script.
python proxxies.py



