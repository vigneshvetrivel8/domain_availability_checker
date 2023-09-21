# Introduction:
With this script you can check the availability of a domain name with godaddy api key and secret key.

There are 3 versions v1.py, v2.py, v3.py.

The above 3 python files use features such as multithreading, file i/0, retry mechanism, control flow, concurrency
and other required features.

# Files:
Replace these lines in the beginning: api_key = "YOUR_API_KEY" and api_secret = "YOUR_API_SECRET", with
your api key and secret key from godaddy in whichever python file you are looking to use.

In v1.py, we can look for all 1-letter words and numbers, 2-letter words and numbers, and so on.
(ex: aa.com, 6.com, xyz.net etc.).  
we may include or remove TLD's according to the requirement in list named "last".  
run command: "python v1.py" or "python3 v1.py".

In v2.py, we can include all the domain name like abcd.com, efgh.net, 1234.org and so on 
(each domain name in seperate line) which we are looking to check in a file named "words.txt" 
and check for the availability.   
The domain names can consist of numbers or letters in uppercase or lowercase.  
run command: "python v2.py" or "python3 v2.py".

In v3.py, we can include all the words we want to check in the 'words.txt' file(each word in seperate line).  
we may include or remove TLD's according to the requirement in list named "last". The words can be any number 
or any letter in capital or small.  
run command: "python v3.py" or "python3 v3.py".  


# Other Info:
The above files do not include available premium domain names in the results. If you wish to include available premium domain names 
then uncomment below 2 lines:  
output = f"{domain}\n".  
write_output(output). 

You can find the mentioned lines at:
* v1.py: 48, 49 or nearby.
* v2.py: 38, 39 or nearby.
* v3.py: 42, 43 or nearby.  

In the main function of all 3 files we have lines such as:
max_workers = 2 and
session.mount('https://', requests.adapters.HTTPAdapter(pool_connections=2, pool_maxsize=2))

You can increase the number to improve processing speed or performance. However, please note that there is a rate limit of approximately 60 requests per minute, so after few tests we found these configurations to be matching our requirements.

# Note:
It was also found that api tends to have some inaccuracy at times. Hence, some unavailable domain names were also 
included in results.

While the accuracy is not 100%, the results produced were correct almost all of the time.
