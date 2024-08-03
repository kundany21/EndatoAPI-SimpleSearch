import requests
import json
import os
from colorama import Fore, Style, init

init()  

def main():
    
    try:
        with open("config.txt", "r") as config_file:
            ap_name = config_file.readline().strip()
            ap_password = config_file.readline().strip()
            search_type = config_file.readline().strip()
    except FileNotFoundError:
        print(Fore.RED + "Error: config.txt not found. Please create it with your API credentials." + Style.RESET_ALL)
        return

    print(Fore.MAGENTA + Style.BRIGHT +
          "    //   ) )                                              \n" +
          "   ((         ___      ___      __      ___     / __      \n" +
          "     \\     //___) ) //   ) ) //  ) ) //   ) ) //   ) )   \n" +
          "       ) ) //       //   / / //      //       //   / /    \n" +
          "((___ / / ((____   ((___( ( //      ((____   //   / /     \n" +
          Style.RESET_ALL)

    print(Fore.GREEN + "Available Options:" + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Person Search" + Style.RESET_ALL)

    choice = input(Fore.CYAN + "Enter your choice (1): " + Style.RESET_ALL)

    if choice == '1':
        payload = build_payload()
        send_request(payload, ap_name, ap_password, search_type)

def build_payload():
    payload = {}
    optional_fields = {
        "FirstName": "First Name",
        "MiddleName": "Middle name or middle initial",
        "LastName": "Last name",
        "Akas": "Alternative Names (Name{})",
        "Dob": "Date of birth (mm/dd/yyyy)",
        "Age": "Age",
        "AgeRangeMinAge": "Age range minimum",
        "AgeRangeMaxAge": "Age Range Maximum",
        "AgeRange": "Age Range (Format: ##-##)",
        "Ssn": "Social security number (###-##-####)",
        "Addresses": "Addresses (List of Address{})",
        "Email": "E-mail Address",
        "ClientIp": "Search by IP Address (###.###.###.###)",
        "Phone": "Phone number (###-###-####, (###)###-####)",
        "Relatives": "List of names of relatives (Name{})",
        "TahoeIds": "Tahoe ID (string{})",
        "FirstNameCharOffset": "Levenshtein distance offset for first name",
        "LastNameCharOffset": "Levenshtein distance offset for last name",
        "DobFormat": "Override default DOB date format (mm-dd-yyyy etc.)",
        "MaxAddressYears": "Filter out addresses beyond this many years",
        "MaxPhoneYears": "Filter out phone numbers beyond this many years"
    }

    for field, description in optional_fields.items():
        include = input(f"Include {description}? (y/n): ")
        if include.lower() == 'y':
            if field == "Addresses" or field == "Relatives":
                
                num_entries = int(input(f"How many {field} to enter? "))
                entries = []
                for i in range(num_entries):
                    entry = {}
                    if field == "Addresses":
                        entry["AddressLine1"] = input(f"  Address {i+1} - Address Line 1: ")
                        entry["AddressLine2"] = input(f"  Address {i+1} - Address Line 2: ")
                        entry["County"] = input(f"  Address {i+1} - County: ")
                    elif field == "Relatives":
                        entry["FirstName"] = input(f"  Relative {i+1} - First Name: ")
                        entry["MiddleName"] = input(f"  Relative {i+1} - Middle Name: ")
                        entry["LastName"] = input(f"  Relative {i+1} - Last Name: ")
                    entries.append(entry)
                payload[field] = entries
            else:
                payload[field] = input(f"Enter {description}: ")

    return payload

def send_request(payload, ap_name, ap_password, search_type):
    url = "https://devapi.endato.com/PersonSearch"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "galaxy-ap-name": ap_name,
        "galaxy-ap-password": ap_password,
        "galaxy-search-type": search_type
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        
        if not os.path.exists("results"):
            os.makedirs("results")

        
        filename = f"results/person_search_results_{os.urandom(4).hex()}.json"
 
        with open(filename, "w") as result_file:
            json.dump(response.json(), result_file, indent=4)

        print(f"Results saved to {filename}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    main()