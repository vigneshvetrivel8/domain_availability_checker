import concurrent.futures
import requests
import time

api_key = "YOUR_API_KEY" # Modify this with your API key here.
api_secret = "YOUR_API_SECRET" # Modify this with your secret key here.

def txt_to_list(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
    return lines

file_path = 'words.txt' # Replace with the path to your text file
domains = txt_to_list(file_path)

def check_domain_availability(domain, domain_prices, session):
    url = f"https://api.ote-godaddy.com/v1/domains/available?domain={domain}&checkType=FULL"

    retry_attempts = 500
    retry_delay = 0.1

    for attempt in range(retry_attempts):
        response = session.get(url)

        if response.status_code == 200:
            result = response.json()
            if "available" in result:
                if result["available"]:
                    price = result.get("price", "Price information not available")
                    domain_prices[domain] = price  # Store the price in the dictionary
                    if (price / 12000) < 10000:
                        print(f"The domain {domain} is available for registration")
                        output = f"{domain}\n"
                        write_output(output)
                    else:
                        print(f"{domain} is not available for a cheap price")
                        # output = f"{domain}\n"
                        # write_output(output)
                        # comment out the above 2 lines if you wish to include available premium domains in the result
                else:
                    print(f"{domain} is taken")
                return  # Exit the function if request is successful
            else:
                print(f"Failed to retrieve availability status for {domain}.")
                return  # Exit the function if availability status is missing
        else:
            print(f"Failed to retrieve availability status for {domain}. Status Code: {response.status_code}")

        if attempt < retry_attempts - 1:
            # Retry after a delay
            time.sleep(retry_delay)

    print(f"Request for {domain} failed after {retry_attempts} attempts.")
    output2 = f"Request for {domain} failed.\n"
    write_output2(output2)

def write_output(output):
    with open("result.txt", "a") as file:
        file.write(output)

def write_output2(output):
    with open("failure.txt", "a") as file:
        file.write(output)

def main():
    max_workers = 2  # Limit the maximum number of concurrent threads
    domain_prices = {}  # Dictionary to store domain prices

    with requests.Session() as session:
        session.headers.update({"Authorization": f"sso-key {api_key}:{api_secret}", "Content-Type": "application/json"})
        session.mount('https://', requests.adapters.HTTPAdapter(pool_connections=2, pool_maxsize=2))

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit tasks to the executor
            futures = [executor.submit(check_domain_availability, domain, domain_prices, session) for domain in domains]

            # Wait for all tasks to complete
            concurrent.futures.wait(futures)

    # Process the results
    for domain, price in domain_prices.items():
        if (price / 12000) < 10000:
            print(f"The domain {domain} is available for registration")
            output = f"The domain {domain} is available for registration\n"
            write_output(output)
        else:
            print(f"{domain} is not available for a cheap price")

if __name__ == "__main__":
    main()
