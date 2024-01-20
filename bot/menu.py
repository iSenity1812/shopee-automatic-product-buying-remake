from colored import Fore, Back, Style
from clearConsole import clear_console
from accountManage import *


CONFIG_DIR = "./config"
SETTINGS_FILE = "settings.json"
SETTINGS_PATH = os.path.join(CONFIG_DIR, SETTINGS_FILE)


# [MENU HEADER]
def print_menu_header(*header_lines):
	for line in header_lines:
		print(f"{Fore.red}Current:{Style.reset} {Fore.cyan}{line}{Style.reset}")
	print("====================================================")


def print_menu_header_option(*header_lines):
	for line in header_lines:
		formatted_line = line.replace("[", f"[{Fore.white}").replace("]", f"{Style.reset}{Fore.blue}]")
		print(f"| {Fore.blue}{formatted_line}{Style.reset}")

# [INVALID INPUT]
def handle_invalid_input():
	clear_console()
	print(f"[CONSOLE]{Fore.red}[!] Invalid input. Please try again!{Style.reset}")

# [FILE IS EMPTY]
def checkFile_isNotEmpty():
	# Checking if there is any account
	json_file_path = "./accounts.json"
	usernames_list = view_all_usernames_in_json_file(json_file_path)

	if len(usernames_list) == 0:
		print(f"{Fore.yellow}[!] You don't have any account to action.{Style.reset}")
		input("Any key to back to the menu...")
		menu()

# View account in sessions
def checkSessionFolder_isNotEmpty():
	ss_exist = view_all_sessions_in_folder()
	if not ss_exist:
		input("Any key to back...")
		clear_console()
		Func6_Order_Area()

#=======================================================================
# [ADD ACCOUNT]
def Func1_addAccount():

	print_menu_header("Menu > Insert")
	print_menu_header_option("[1] Insert accounts", "[b/B] Back to menu")
	Func_choice = input(f"{Fore.yellow}Choice:{Style.reset} ")
	if Func_choice == "1":
        # Execute Function
		username = input(f"{Fore.cyan}[?]{Style.reset} Enter the username: ")
		password = input(f"{Fore.cyan}[?]{Style.reset} Enter the password: ")
		add_account(username, password)
	elif Func_choice == "B".lower():
		clear_console()
		menu()	
	else:
		clear_console()
		print(f"{Fore.red}[!] Invalid input.{Style.reset}")
		Func1_addAccount()

	print(f"{Fore.green}[+] Account added successfully!{Style.reset}")
	input("Any key to back to the menu...")
	clear_console()
	menu()


#=======================================================================
# [ADD SESSIONS]
def Func1a_addSession():
	print_menu_header("[Menu > Insert]")
	print_menu_header_option("[1] Insert Sessions", "[b/B] Back to menu")
	Func_choice = input(f"{Fore.yellow}Choice:{Style.reset} ")
	if Func_choice == "1":
		clear_console()
		print_menu_header("[Menu > Order > Order-Area > Login-Method > Sessions > New-Session]")

		session_data = input(f"{Fore.yellow}[?] Your session data: {Style.reset}")
		session_name = input(f"{Fore.yellow}[?] Your session name: {Style.reset}")
		save_session(session_data, session_name)
		clear_console()
		
		print(f"{Fore.green}[+] Session file created {Fore.cyan}{session_name}.json{Style.reset}")
		clear_console()
		input("Any key to back...")
		menu()
	elif Func_choice.lower() == "b":
		clear_console()
		menu()
	else:
		handle_invalid_input()
		Func1a_addSession()


#=======================================================================
# [EDIT ACCOUNTS]
def Func2_editAccount():
	print_menu_header("[Menu > Edit]")
	# Checking if there is any account
	checkFile_isNotEmpty()
	print_menu_header_option("[1] Edit accounts", "[2] Back")
	Func_choice = input(f"{Fore.yellow}[?] Choice:{Style.reset} ")

	if Func_choice == "1":
        # Execute Function
		username = input(f"{Fore.green}[+] Enter the username of the account to edit: {Style.reset}")

        # Check if the username is not empty
		if username:
            # Call edit_account only if the account with the entered username exists
			if any(account.username == username for account in get_accounts()):
				new_username = input(f"{Fore.cyan}[?]{Style.reset} Enter the new username: ")
                # Check if the new username is not empty
				if new_username:
					new_password = input(f"{Fore.cyan}[?]{Style.reset} Enter the new password: ")
					edit_account(username, new_username, new_password)
				else:
					print(f"{Fore.rgb(192, 210, 25)}[!] New username cannot be empty.{Style.reset}")
			else:
				print(f"{Fore.rgb(192, 210, 25)}[!] The account with username {Fore.cyan}{username}{Style.reset} {Fore.yellow}does not exist.{Style.reset}")
		else:
			print(f"{Fore.rgb(192, 210, 25)}[!] Username cannot be empty.{Style.reset}")
		# REDO
		redo_choice = input(f"{Fore.yellow}[?] Redo {Style.reset}({Fore.green}Y{Style.reset}/{Fore.red}N{Style.reset}): ")
		if redo_choice == "Y".lower():
			clear_console()
			Func2_editAccount()
		if redo_choice == "N".lower():

			input("Any key to back to the menu...")
			clear_console()
			menu()
		else:
			clear_console()
			print(f"{Fore.red}[!] Invalid input.{Style.reset}")
			menu()
	elif Func_choice == "B".lower():
		clear_console()
		menu()
	else:
		clear_console()
		print(f"{Fore.red}[!] Invalid input.{Style.reset}")
		Func2_editAccount()


#=======================================================================
# [DELETE ACCOUNT]
def Func3_deleteAccount():
	print_menu_header("[Menu > Delete]")
	# Checking if there is any account
	checkFile_isNotEmpty()
	print_menu_header_option("[1] Delete accounts", "[2] Back")
	Func_choice = input(f"{Fore.yellow}Choice:{Style.reset} ")

	if Func_choice == "1":
		#Execute Function
		username = input(f"{Fore.yellow}Enter the username of the account to delete: {Style.reset}")
		if username:
            # Call edit_account only if the account with the entered username exists
			print(f"{Fore.yellow}[CHECKING ACCOUNT... ]{Style.reset}")
			if any(account.username == username for account in get_accounts()):
				print(f"{Fore.green}[!] Founded account with username '{username}'{Style.reset}")

				confirm = input(f"{Fore.blue}Your account will be deleted{Style.reset} [{Fore.cyan}{username}{Style.reset}] ({Fore.green}Y{Style.reset}/{Fore.red}N{Style.reset}): ")
				if confirm == "Y".lower():
					delete_account(username)

					redo_choice = input(f"{Fore.yellow}[?] Redo {Style.reset}({Fore.green}Y{Style.reset}/{Fore.red}N{Style.reset}): ")
					if redo_choice == "Y".lower():
						clear_console()
						Func3_deleteAccount()
					if redo_choice == "N".lower():
						input("Any key to back to the menu...")
						clear_console()
						menu()
					elif confirm == "N".lower():
						Func3_deleteAccount()
			else:
				clear_console()
				print(f"{Fore.rgb(192, 210, 25)}[!] The account with username {Fore.cyan}{username}{Style.reset} {Fore.yellow}does not exist.{Style.reset}")
				Func3_deleteAccount()
		else:
			print(f"{Fore.rgb(192, 210, 25)}[!] Username cannot be empty.{Style.reset}")
	elif Func_choice == "B".lower():
		clear_console()
		menu()
	else:
		clear_console()
		print(f"{Fore.red}[!] Invalid input.{Style.reset}")
		Func3_deleteAccount()


#=======================================================================
# [VIEW SPECIFIC ACCOUNT]
def Func4_exportAccount():
	print_menu_header("[Menu > Export]")
	# Checking if there is any account
	checkFile_isNotEmpty()

	print_menu_header_option("[1] Export account", "[b/B] Back")
	Func_choice = input(f"{Fore.yellow}[?] Choice:{Style.reset} ")

	if Func_choice == "1":
       # Enter account to export (view)
		username = input(f"{Fore.green}[+] Enter the username of the account to view: {Style.reset}")
       # Check if username is not empty
		if username:
			view_account(username)
		else:
			print(f"{Fore.rgb(192, 210, 25)}[!] Username cannot be empty.{Style.reset}")
       # REDO
		redo_choice = input(f"{Fore.yellow}[?] Redo {Style.reset}({Fore.green}Y{Style.reset}/{Fore.red}N{Style.reset}): ")

		if redo_choice.lower() == "y":
			clear_console()
			Func4_exportAccount()
		elif redo_choice.lower() == "n":
			input("Any key to back to the menu...")
			clear_console()
			menu()
		else:
			print(f"{Fore.red}[!] Invalid input.")
			clear_console()
			Func4_exportAccount()

	elif Func_choice.lower() == "b":
		clear_console()
		menu()
	else:
		clear_console()
		print(f"{Fore.red}[!] Invalid input.{Style.reset}")
		Func4_exportAccount()



#=======================================================================
# [VIEW ALL ACCOUNTS]
def Func5_viewAllAccounts():
	print_menu_header("[Menu > View-all-Accounts]")
	checkFile_isNotEmpty()
	print_menu_header_option("[1] View all accounts", "[b/B] Back")
	Func_choice = input(f"{Fore.yellow}[?] Choice:{Style.reset} ")

	if Func_choice == "1":
		# Execute viewing all account
		json_file_path = "./accounts.json"
		usernames_list = view_all_usernames_in_json_file(json_file_path)

		print(f"{Fore.green}[List of all available account]{Style.reset}")
		for username in usernames_list:
			print(username)

		input("Any key to back to the menu...")
		clear_console()
		menu()

	elif Func_choice.lower() == "b":
		clear_console()
		menu()
	else:
		clear_console()
		print(f"{Fore.red}[!] Invalid input.{Style.reset}")
		Func5_viewAllAccounts()


#========================================================================
# [ORDER] 
def handle_standard_method():
	clear_console()
	print(f"{Fore.red}[-] Sorry this feature is still in development. Please use sessions instead...{Style.reset}")
	Func6_Order_Area()

def update_exported_url(exported_url):
	settings = load_data_from_json(SETTINGS_PATH) or {}
	settings["url"] = exported_url
	save_data_to_json(settings, SETTINGS_PATH)

	print(f"{Fore.green}[+] Settings updated successfully.{Style.reset}")
	print(f"{Fore.green}[URL]{Style.reset} - {settings['url']}")

def insert_url():
	url_name = input(f"{Fore.blue}[?] Site's name:{Style.reset} ")
	url_value = input(f"{Fore.blue}[?] URL:{Style.reset} ")

	save_url(url_name, url_value)
	handle_url_saved_confirmation()

def handle_url_saved_confirmation():
	config_folder = './config'
	urls_file_path = os.path.join(config_folder, 'urls.json')

	yn = input(f"{Fore.blue}[?] Do you want to save it to settings.json {Style.reset}({Fore.green}Y{Style.reset}/{Fore.red}N{Style.reset}): ")
	
	if yn.lower() == "y":
		urlS = load_data_from_json(urls_file_path)
		if urlS:
			new_site = urlS[-1]
			print(f"{Fore.green}[+] Site's name: {Style.reset}{new_site['name']}")
			print(f"{Fore.green}[+] Your url:{Style.reset}{new_site['url']}")

			# Save to settings.json
			if not os.path.exists(CONFIG_DIR):
				os.makedirs(CONFIG_DIR)

			settings = load_data_from_json(SETTINGS_PATH)
			if settings is None:
				settings = {}
			settings["url"] = new_site['url']
				        
			# Save updated settings to settings.json in the ./config directory
			save_data_to_json(settings, SETTINGS_PATH)

			print(f"{Fore.green}[+] Settings updated successfully.{Style.reset}")
			print(f"URL: {settings['url']}")
			input("Any key to back...")
			clear_console()
			Func6_Order()
		else:
			print(f"{Fore.red}[-] No urls found {Style.reset}")
			input("Any key to back...")
			menu()
	else:
		clear_console()
		Func6_Order_Area()


def export_url_from_settings():
	config_folder = './config'
	urls_file_path = os.path.join(config_folder, 'urls.json')

	view_all_url_names()
	site_name = input(f"{Fore.yellow}[?] Enter the name to export the URL: {Style.reset}")
	exported_url = export_url(site_name)

	if export_url is not None:
		update_exported_url(exported_url)
	else:
		print(f"{Fore.red}[-] Unable to export URL for '{site_name}'.{Style.reset}")

	input("Any key to back...")
	clear_console()
	Func6_Order()


def set_quantity_rt_checkout():
	quantity = input(f"{Fore.yellow}[?] Quantity:{Style.reset} ")
	attempt = input(f"{Fore.yellow}[?] Refresh times:{Style.reset} ")
	order = input(f"{Fore.yellow}[?] Auto Checkout{Style.reset} ({Fore.green}on{Style.reset}/{Fore.red}off{Style.reset}):{Style.reset} ")

	if order.lower() in ["on", "off"]:
		print(f"{Fore.yellow}[Waiting..]{Style.reset}")
	else:
		handle_invalid_input()
		input("Any key...")
		Func6_Order_Area()	

	# Load settings
	update_settings_with_qrtc(quantity, attempt, order)
	settings = load_data_from_json(SETTINGS_PATH)

	if settings is not None:
		print(f"{Fore.green}[+] Settings updated successfully.{Style.reset}")
		print(f"{Fore.cyan}Quantity:{Style.reset} {settings['quantity']}")
		print(f"{Fore.cyan}Refresh times:{Style.reset} {settings['attempt']}")
		print(f"{Fore.cyan}Auto Checkout:{Style.reset} {settings['order']}")
			
		input("Any key to back...")
		clear_console()
		Func6_Order()


def update_settings_with_qrtc(quantity, attempt, order):
	settings = load_data_from_json(SETTINGS_PATH)
	if settings is None:
		settings = {}
	settings["quantity"] = quantity
	settings["attempt"] = attempt
	settings["order"] = order
	# Save updated settings to settings.json in the ./config directory
	save_data_to_json(settings, SETTINGS_PATH)


def Func6_Order():
	print_menu_header("[Menu > Order]")
	print_menu_header_option("[1] Order Area Settings", "[b/B] Back to menu")
	Func_choice = input(f"{Fore.yellow}[?] Choice:{Style.reset} ")

	if Func_choice == "1":
		clear_console()
		Func6_Order_Area()
	elif Func_choice.lower() == "b":
		clear_console()
		menu()
	else:
		clear_console()
		print(f"{Fore.red}[!] Invalid input.{Style.reset}")
		Func6_Order()


def Func6_Order_Area():
	print_menu_header("[Menu > Order > Order-Area]")
	print_menu_header_option("[1] Choose sign-in method", "[2] Insert and choose URL", "[3] Order settings", "[b/B] Back")
	Func_choice = input(f"{Fore.yellow}[?] Choice:{Style.reset} ")
	# [Sign-in]
	if Func_choice == "1":
		clear_console()
		print_menu_header("[Menu > Order > Order-Area > Sign-in-Method]")
		print_menu_header_option("[1] Standard", "[2] Sessions", "[b/B] Back")
		method = input(f"{Fore.yellow}[?] Choice:{Style.reset} ")
		if method == "1":
			handle_standard_method()
		elif method == "2":
			Func6_Order_Area_Sessions()
		elif method.lower() == "b":
			clear_console()
			Func6_Order()
		else:
			handle_invalid_input()
			Func6_Order_Area()
	# [URL]
	elif Func_choice == "2":
		clear_console()
		print_menu_header("[Menu > Order > Order-Area > URLs]")
		print_menu_header_option("[1] Insert URL", "[2] Export URLs", "[b/B] Back")
		choice = input(f"{Fore.yellow}[?] Choice: {Style.reset}")
		if choice == "1":
			insert_url()
			handle_url_saved_confirmation()
		# Export URL to settings
		elif choice == "2":
			export_url_from_settings()
		elif choice.lower() == "b":
			clear_console()
			Func6_Order()
		else: 
			clear_console()
			print(f"{Fore.red}[!] Invalid input.{Style.reset}")
			Func6_Order_Area()
	# [Quantity, refresh times, checkout] 
	elif Func_choice == "3":
		set_quantity_rt_checkout()
	elif Func_choice.lower() == "b":
		clear_console()
		Func6_Order()
	else: 
		handle_invalid_input()
		Func6_Order_Area()


def choose_sessions(chosen_session_name):
    sessions_folder = 'sessions'
    # Check if the chosen session exists
    session_path = os.path.join(sessions_folder, f'{chosen_session_name}.json')
    if os.path.exists(session_path):

        print(f"{Fore.green}[+] Founded{Style.reset}")
        return chosen_session_name
    else:
        print(f"\nSession '{chosen_session_name}' not found.")
        Func6_Order_Area_Sessions()


# Sessions method
def Func6_Order_Area_Sessions():
	# Key: Choose -> Save to settings.json
	# Check if session folder have session
	checkSessionFolder_isNotEmpty()
	view_session_names()
	# Choose sessions
	chosen_session_name = input("\nEnter the session name: ")

	name = choose_sessions(chosen_session_name)

	# Save to settings.json
	if not os.path.exists(CONFIG_DIR):
		os.makedirs(CONFIG_DIR)

	settings = load_data_from_json(SETTINGS_PATH)
	if settings is None:
		settings = {}
	settings['session'] = name
	
	# Save updated settings to settings.json in the ./config directory
	save_data_to_json(settings, SETTINGS_PATH)

	print(f"{Fore.green}[+] Settings updated successfully.{Style.reset}")
	print(f"Session: {settings['session']}")
	input("Any key to back...")
	clear_console()
	Func6_Order()



#=====================================================================#
# [OPTIONS PROCESSOR]
def optionProcessing(choice):
	clear_console()
	if choice == "1":
		Func1_addAccount()
	if choice == "1a":
		Func1a_addSession()
	elif choice == "2":
		Func2_editAccount()
	elif choice == "3":
		Func3_deleteAccount()
	elif choice == "4":
		Func4_exportAccount()
	elif choice ==  "5":
		Func5_viewAllAccounts()
	elif choice == "6":
		Func6_Order()
	elif choice in ["0", "q"]:
		exit()
	elif choice.lower() in ["start", "s"]:
		from checkSettings import check_module
		check_module()

	else:
		print(f"""
#==============================================#
#[CONSOLE]{Fore.yellow}[!] Invalid input. Please try again!{Style.reset} #
#==============================================#
			""")
		menu()



def menu():
	global choice
	print(f"{Fore.green}[Checking if account file exist...]{Style.reset}")
	create_accounts_file()
	create_sessions_folder()
	clear_console()

	print(f"{Fore.red}Folder: {Fore.cyan}session {Fore.green}[Done]{Style.reset}")
	print(f"{Fore.red}JSON: {Fore.cyan}account {Fore.green}[Done]{Style.reset}")

	print(f"""
================================================
# {Fore.red}ALERT: Because the multi-payment methods is{Style.reset}  #
#{Fore.red}still in development.{Style.reset}                         #
# {Fore.red}Make sure to change your payment to COD{Style.reset}      #
================================================
#      {Fore.rgb(147, 23, 161)}Thanh chien shoppe sieu cap vjp pro{Style.reset}     #
================================================
#               {Fore.rgb(123, 86, 225)}Bot's Name{Style.reset}:  {Fore.blue}SFS{Style.reset}	       #
#               {Fore.rgb(123, 86, 225)}Made by:{Style.reset} As...                 #
#               {Fore.rgb(86, 225, 169)}Contact:{Style.reset} isepipi3289           #
================================================
|      {Fore.rgb(216, 154, 47)}Functions{Style.reset}      |    {Fore.rgb(216, 154, 47)}Using{Style.reset}    |  {Fore.rgb(216, 154, 47)}Status{Style.reset}  |
|---------------------|-------------|----------|
|   {Fore.rgb(47, 216, 194)}Insert accounts{Style.reset}   |  [Key-1]    |    {Fore.green}✔️{Style.reset}    |
|   {Fore.rgb(47, 216, 194)}Insert Sessions{Style.reset}   |  [Key-1a]   |    {Fore.green}✔️{Style.reset}    |
|    {Fore.rgb(47, 216, 194)}Edit account{Style.reset}     |  [Key-2]    |    {Fore.green}✔️{Style.reset}    |
|    {Fore.rgb(47, 216, 194)}Delete account{Style.reset}   |  [Key-3]    |    {Fore.green}✔️{Style.reset}    |
|    {Fore.rgb(47, 216, 194)}Export account{Style.reset}   |  [Key-4]    |    {Fore.green}✔️{Style.reset}    |
|   {Fore.rgb(47, 216, 194)}View accounts{Style.reset}     |  [Key-5]    |    {Fore.green}✔️{Style.reset}    |
|       {Fore.rgb(47, 216, 194)}Order{Style.reset}         |  [Key-6]    |    {Fore.green}✔️{Style.reset}    |
| {Fore.rgb(47, 216, 194)}View Product's URL{Style.reset}  |  [Key-7]    |    {Fore.red}❌{Style.reset}    |
|   {Fore.rgb(47, 216, 194)}Export to excel{Style.reset}   |  [Key-8]    |    {Fore.red}❌{Style.reset}    |
|       {Fore.rgb(47, 216, 194)}Settings{Style.reset}      |  [Key-9]    |    {Fore.red}❌{Style.reset}    |
|	 {Fore.rgb(47, 216, 194)}Exit{Style.reset}	      |  [Key-0]    |    {Fore.green}✔️{Style.reset}    |
|{Fore.rgb(47, 216, 194)}Search product's name{Style.reset}|  [Key-11]   |    {Fore.red}❌{Style.reset}    |
================================================
#            {Fore.green}START{Style.reset}          #     {Fore.red} [start]{Style.reset}     # 
================================================
""")

	choice = input(f"{Fore.yellow}Choice:{Style.reset} ")
	# print(type(choice))
	optionProcessing(choice)



# if __name__ == "__main__":
# 	menu()
