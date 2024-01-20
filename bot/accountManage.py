import json
from colored import Fore, Back, Style
import os
import time



class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password
        }

# [SAVE ACCOUNT] #
def save_accounts(accounts):
    with open("accounts.json", "w") as f:
        json.dump([account.to_dict() for account in accounts], f, indent=4)


def save_data_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)


#[Load]
def load_data_from_json(filename):
    if not filename:
        return None
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return None


# [CREATE ACCOUNT JSON FILE] #
def create_accounts_file():
    accounts_file_path = "accounts.json"

    # Check if the file already exists
    if not os.path.exists(accounts_file_path):
        # Create the file with an empty list
        with open(accounts_file_path, "w") as f:
            json.dump([], f, indent=4)
        print(f"{Fore.red}File is not created...{Style.reset}")
        print(f"{Fore.yellow}[/] Creating...{Style.reset}")
        time.sleep(1)
        print(f"{Fore.green}[+] Completed{Style.reset}")
        print(f"{Fore.green}[!] The {Fore.cyan}{accounts_file_path}{Fore.green} file has been created with an empty list.{Style.reset}")
        time.sleep(1)
    else:
        print(f"The {accounts_file_path} file already exists.")
        time.sleep(1)


def create_sessions_folder():
    sessions_folder_path = "./sessions"

    # Check if the path already exists
    if not os.path.exists(sessions_folder_path):
        # Create the empty 'sessions'  folder
        print(f"{Fore.red}Folder 'sessions' is not created...{Style.reset}")
        print(f"{Fore.yellow}[/] Creating...{Style.reset}")
        time.sleep(2)
        os.makedirs(sessions_folder_path)
        print(f"{Fore.green}[+] Completed{Style.reset}")
        print(f"{Fore.green}The empty {Fore.cyan}{sessions_folder_path}{Fore.green} folder has been created.{Style.reset}")
    else:
        print(f"The {sessions_folder_path} folder already exists.")
        time.sleep(1)


def is_jsonFile_empty(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return len(data) == 0
    except (FileNotFoundError, json.JSONDecodeError):
        return True


def is_folder_empty(folder_path):
    try:
        folder_contents = os.listdir(folder_path)
        return len(folder_contents) == 0
    except FileNotFoundError:
        return True


# [CHECK IF JSON FILE WRITABLE] #
def is_accounts_file_writable(filename):
    try:
        with open(filename, "r") as f:
            json.load(f)
    except FileNotFoundError:
        return True
    except json.decoder.JSONDecodeError:
        return True
    except PermissionError:
        return False
    return True


# [GET ACCOUNT FROM USER INPUT] #
def get_accounts():
    try:
        with open("accounts.json", "r") as f:
            account_data_list = json.load(f)
    except FileNotFoundError:
        account_data_list = []
    except json.decoder.JSONDecodeError:
        print("Error: JSON file is empty or contains invalid data.")
        account_data_list = []

    accounts = []
    for account_data in account_data_list:
        accounts.append(Account(account_data["username"], account_data["password"]))
    return accounts


# [VIEW SPECIFIC ACCOUNT]
def view_account(username):
    accounts = get_accounts()

    # Check if the account with the entered username exists
    if any(account.username == username for account in accounts):
        print(f"{Fore.green}[+] Account Details for Username '{username}':{Style.reset}")
        for account in accounts:
            if account.username == username:
                print(f"  - Username: {account.username}")
                print(f"  - Password: {account.password}")
                break
    else:
        print(f"{Fore.rgb(192, 210, 25)}[!] The account with username {Fore.cyan}{username}{Style.reset} {Fore.yellow}does not exist.{Style.reset}")


# [CHECK IF USERNAME IS EXISTED]
def check_username_exists(username, account_json_file):

    try:
        with open(account_json_file, "r") as f:
            account_data = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        account_data = []

    for account in account_data:
        if account.get("username") == username:
            return True
    return False


# [INSERT NEW ACCOUNT] #
def add_account(username, password):
    account_json_file = "accounts.json"

    if not is_accounts_file_writable(account_json_file):
        print("File is not writable")
        return
    
    accounts = get_accounts()

    if check_username_exists(username, account_json_file):
        print(f"{Fore.red}Username already exists.{Style.reset}")
        redo = input(f"{Fore.yellow}[?] Redo {Style.reset}({Fore.green}Y{Style.reset}/{Fore.red}N{Style.reset}): ")
        if redo.lower() == 'y':
            add_account(input(f"{Fore.cyan}[?]{Style.reset} Enter the username: "),
                        input(f"{Fore.cyan}[?]{Style.reset} Enter the password: "))
        return

    accounts.append(Account(username, password))
    save_accounts(accounts)


# [IMPORT ACCOUNT FROM JSON]
def import_account(username):
    """Imports an account from the JSON file.

    Args:
        username: The username of the account to import.

    Returns:
        An Account object, or None if the account is not found.
    """

    accounts = get_accounts()
    for account in accounts:
        if account.username == username:
            return account
    return None



# [DELETE ACCOUNT]
def delete_account(username):
    """Deletes an account from the JSON file.

    Args:
        username: The username of the account to delete.
    """
    accounts = get_accounts()
    initial_length = len(accounts)
    accounts = [account for account in accounts if account.username != username]
    
    if len(accounts) == initial_length:
        print(f"{Fore.rgb(192, 210, 25)}The account with username {Fore.cyan}{username}{Style.reset} {Fore.rgb(192, 210, 25)}does not exist.{Style.reset}")
    else:
        print(f"{Fore.green}The account with username {Fore.cyan}{username}{Style.reset} {Fore.green}has been deleted.{Style.reset}")
        save_accounts(accounts)


# [EDIT ACCOUNT]
def edit_account(username, new_username, new_password):
    """Edits an account in the JSON file.

    Args:
        username: The username of the account to edit.
        new_username: The new username for the account.
        new_password: The new password for the account.
    """
    accounts = get_accounts()

    # Check if the account exists
    account_exists = any(account.username == username for account in accounts)

    print(f"{Fore.yellow}[CHECKING ACCOUNT... ]{Style.reset}")

    if account_exists:
        # Account exists, proceed with editing
        for account in accounts:
            if account.username == username:
                print(f"{Fore.green}[!] Founded account with username '{username}'{Style.reset}")

                # Check if the new_username and new_password are empty
                if new_username and new_password:
                    # Check if the new username is a duplicate
                    if is_username_duplicate(accounts, new_username):
                        print(f"{Fore.rgb(192, 210, 25)}[!] The new username '{new_username}' is already in use. Please choose a different one.{Style.reset}")
                    else:
                        account.username = new_username
                        account.password = new_password
                        print(f"{Fore.green}[!] The account with username {Fore.cyan}{username}{Style.reset} {Fore.green}has been updated.{Style.reset} [{Fore.rgb(156, 109, 192)}{new_username}{Style.reset}/{Fore.rgb(156, 109, 192)}{new_password}{Style.reset}]")
                        save_accounts(accounts)
                else:
                    print(f"{Fore.rgb(192, 210, 25)}[!] Both new username and password are required for editing.{Style.reset}")
                break
    else:
        # Account does not exist, print notification
        print(f"{Fore.rgb(192, 210, 25)}The account with username {Fore.cyan}{username}{Style.reset} {Fore.yellow}does not exist.{Style.reset}")


# [GET USERNAME FROM JSON]
def get_username_from_json_acount(account_json_file, account_index):
    with open (account_json_file, "r") as f:
        account_data = json.load(f)
    
    if int(account_index) >= len(account_data) or int(account_index) < 0:
        raise IndexError("Account index out of range")
    username = account_data[int(account_index)]["username"]

    return  username


# [VIEW ALL USERNAMES]
def view_all_usernames_in_json_file(account_json_file):
    usernames = []

    try:
        with open(account_json_file, "r") as f:
            # Check if the file is not empty
            if f.readable():
                f.seek(0)  # Move the file pointer to the beginning
                account_data = json.load(f)

                for index, account in enumerate(account_data, start=1):
                    usernames.append(f"- Account{index}: {account['username']}")
    except FileNotFoundError:
        print(f"File not found: {account_json_file}")
    except json.decoder.JSONDecodeError as e:
        print(f"Error decoding JSON in file {account_json_file}: {e}")

    return usernames


# [SESSIONS PART]
def view_all_sessions_in_folder():
    # Check if 'sessions' folder exists
    sessions_folder = 'sessions'
    if not os.path.exists(sessions_folder):
        print("No sessions found.")
        return False

    # List all files in 'sessions' folder
    session_files = os.listdir(sessions_folder)
    
    if not session_files:
        print("No sessions found.")
        return False

    return True


# [SAVE SESSIONS]
def save_session(session_string, session_name):
    # Create 'sessions' folder if it doesn't exist [Recheck]
    sessions_folder = 'sessions'
    if not os.path.exists(sessions_folder):
        os.makedirs(sessions_folder)

    session_data = json.loads(session_string)
    # Save the session data to a file
    session_path = os.path.join(sessions_folder, f'{session_name}.json')
    with open(session_path, 'w') as f:
        json.dump(session_data, f, indent=4)

    print(f"Session '{session_name}' has been saved.")


# [VIEW SESSION'S NAME]
def view_session_names():
    # Check if 'sessions' folder exists
    sessions_folder = 'sessions'
    if not os.path.exists(sessions_folder):
        print("No sessions found.")
        return False

    # List all files in 'sessions' folder
    session_files = os.listdir(sessions_folder)
    
    if not session_files:
        print("No sessions found.")
        return False

    # Print available session names
    print(f"{Fore.green}Available Session Names:{Style.reset}")
    for session_file in session_files:
        if session_file.endswith('.json'):
            session_name = os.path.splitext(session_file)[0]
            print(f"- {session_name}")


# [VIEW SESSION DATA - IN DEVS]
def view_session_data():
    view_session_names()
    sessions_folder = 'sessions'
    # Input session name
    chosen_session_name = input("\nEnter the session name to view its data: ")
    # Check if the chosen session exists
    session_path = os.path.join(sessions_folder, f'{chosen_session_name}.json')
    if os.path.exists(session_path):
        # Load and print the data
        with open(session_path, 'r') as f:
            session_data = json.load(f)
            print(f"\nData for session '{chosen_session_name}':")
            print(json.dumps(session_data, indent=4))
            return session_data
    else:
        print(f"\nSession '{chosen_session_name}' not found.")
        return None


# [INSERT URLs]
def save_url(name, url):
    config_folder = './config'
    urls_file_path = os.path.join(config_folder, 'urls.json')

    # Create the directory if it doesn't exist
    if not os.path.exists(config_folder):
        os.makedirs(config_folder)

    # Load existing data or initialize an empty list
    try:
        with open(urls_file_path, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    # Add the new URL to the list
    data.append({'name': name, 'url': url})

    # Save the updated data back to the file
    with open(urls_file_path, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"URL '{name}' saved to: {urls_file_path}")


# [VIEW AND EXPORT URLs]
def view_and_export_urls():
    urls_file_path = "urls.json"

    try:
        with open(urls_file_path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    # Print names of all URLs
    print("URL Names:")
    for i, url_data in enumerate(data, 1):
        print(f"{i}. {url_data['name']}")

    # Get user choice
    choice = input("\nEnter the number to export the corresponding URL (or 'b' to back): ")

    if choice.lower() == 'b':
        print("Back to previous...")
        return

    try:
        choice = int(choice)
        if 1 <= choice <= len(data):
            chosen_url = data[choice - 1]['url']
            print(f"\nThe URL for '{data[choice - 1]['name']}' is: {chosen_url}")
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


# [EXPORT URL WITH NAME INPUT]
def export_url(name):
    urls_file_path = './config/urls.json'

    # Check if the file exists
    if not os.path.exists(urls_file_path):
        print(f"Error: File '{urls_file_path}' not found.")
        return

    try:
        with open(urls_file_path, 'r') as f:
            data = json.load(f)

        # Search for the URL with the given name
        for entry in data:
            if entry.get("name") == name:
                url_to_export = entry.get("url")
                print(f"[+] Exported URL for '{name}': {url_to_export}")
                return url_to_export

        # If the name is not found
        print(f"Error: URL not found for '{name}'.")

    except Exception as e:
        print(f"Error: {e}")


URLS_PATH = './config/urls.json'
SETTINGS_PATH = './config/settings.json'

def view_all_url_names():
    try:
        with open(URLS_PATH, 'r') as f:
            data = json.load(f)

        if data:
            print(f"{Fore.yellow}URL Names:{Style.reset}")
            for entry in data:
                print(f"- {entry['name']}")
        else:
            print(f"{Fore.red}[-] No URLs found.{Style.reset}")

    except Exception as e:
        print(f"Error: {e}")
