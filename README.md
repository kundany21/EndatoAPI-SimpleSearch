# Person Search API Script 🕵️‍♀️

This Python script provides a user-friendly interface to interact with the Endato Person Search API. It allows you to build custom search queries and saves the results to a JSON file for easy analysis. 📊

## Features ✨

- **Reads API credentials from `config.txt`:** Securely stores your API credentials in a separate file. 
- **Colorful and modern menu:** Uses `colorama` for a visually appealing and informative menu. 
- **Saves results to a file:** Saves the JSON response to a file in the `results` folder for easy review. 
- **Unique filenames:** Generates unique filenames for result files to prevent overwriting. 
- **Error handling:** Handles missing `config.txt` and provides informative error messages. 

## Requirements 🧰

- Python 3 🐍
- `requests` package: `pip install requests` 📦
- `colorama` package: `pip install colorama` 🎨

## Setup 🛠️

1. **On `config.txt`:**
2. **Add API credentials:** Enter your `galaxy-ap-name`, `galaxy-ap-password`, and `galaxy-search-type` into `config.txt`, each on a separate line:. 
- `galaxy-ap-name` is your KeyName.
- `galaxy-ap-password` is your Key Password.
- `galaxy-search-type` is the type of search you want to perform.

There are 4 different search types for the Person Search, defined by the `"galaxy-search-type"`:

* **Person:** For detailed information, mainly used for "logged in or paying" users.
* **Teaser:** Provides limited data, mainly used for "logged out" users.
* **ReversePhonePersonTeaser:** Similar to Teaser but uses a phone number.
* **ReversePhonePerson:** Similar to Person but uses a phone number.

**JSON Request Properties:**

- `FirstName` (optional, string): First Name
- `MiddleName` (optional, string): Middle name or middle initial
- `LastName` (optional, string): Last name
- `Akas` (optional, Name{}): Alternative Names
- `Dob` (optional, string): Date of birth (format: mm/dd/yyyy)
- `Age` (optional, int): Age
- `AgeRangeMinAge` (optional, int): Age range minimum
- `AgeRangeMaxAge` (optional, int): Age Range Maximum
- `AgeRange` (optional, string): Age Range (Format: ##-##)
- `Ssn` (optional, string): Social security number (format: ###-##-####)
- `Addresses[].AddressLine1` (optional, string): House number and street name or PO Box
- `Addresses[].AddressLine2` (optional, string): State or City and State Or Zip
- `Addresses[].County` (optional, string): County
- `Email` (optional, string): E-mail Address
- `ClientIp` (optional, int): Search by IP Address (format: ###.###.###.###)
- `Phone` (optional, string): Phone number (formats: ###-###-####, (###)###-####)
- `Relatives` (optional, Name{}): List of names of relatives
- `TahoeIds` (optional, string{}): Tahoe ID
- `FirstNameCharOffset` (optional, int): Levenshtein distance offset for first name
- `LastNameCharOffset` (optional, int): Levenshtein distance offset for last name
- `DobFormat` (optional, string): Overrides the default DOB date format
- `MaxAddressYears` (optional, int): Filters out addresses beyond a certain number of years
- `MaxPhoneYears` (optional, int): Filters out phone numbers beyond a certain number of years

## Usage 🚀

1. **Run the script:** `python main.py`
2. **Choose an option:** The menu will display the available option (Person Search).
3. **Enter search criteria:** Follow the prompts to specify the search criteria for each optional field.
4. **View results:** The results will be saved to a JSON file in the `results` folder. The filename will be printed on the console.

## Example `config.txt` 📝

your_galaxy_ap_name
your_galaxy_ap_password
your_galaxy_search_type

## Contributing 🤝

Contributions are welcome! Please feel free to submit pull requests or open issues. We appreciate your help in making this script even better!

## License 📜

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.

## Thank You 🙏

Thank you for using this script! We hope it helps you streamline your Person Search API interactions.
