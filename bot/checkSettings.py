
import os
from colored import Fore, Back, Style
from clearConsole import clear_console
from accountManage import *
from menu import menu
from countdown import *


url_path = './config/urls.json'
ssf_path = './sessions'
CONFIG_DIR = "./config"
SETTINGS_FILE = "settings.json"
SETTINGS_PATH = os.path.join(CONFIG_DIR, SETTINGS_FILE)

def back_to_menu():
	input("Any key...")
	clear_console()
	menu()

def check_module():
	print(f"{Fore.green}[Checking...]{Style.reset}")
	create_accounts_file()
	create_sessions_folder()
	time.sleep(1)

	# Because the standard account is still development so use session instead....
	if is_folder_empty(ssf_path):
		print(f"{Fore.red}The folder '{ssf_path}' is empty.{Style.reset}")
		print(f"{Fore.red}[!] Please add session before do this.{Style.reset}")
		back_to_menu()
	else:
		time.sleep(1)
		print(f"{Fore.green}[+] The folder '{ssf_path}' is not empty.{Style.reset}")

	
	# Setting.json check
	settings = load_data_from_json(SETTINGS_PATH)
	if settings is None:
		settings = {}
	# Not set the url
	required_keys = ['session', 'url', 'quantity', 'attempt']
	for key in required_keys:
		value = settings.get(key)
		if value is None or value == "":
			print(f"{Fore.red}[-] You haven't set {key} in settings.json.{Style.reset}")
			print(f"{Fore.red}[!] Please add {key} to settings.json before continuing.{Style.reset}")
			back_to_menu()
		else:
			print(f"{Fore.green}[+] {key.capitalize()}: ✔️{Style.reset}")

	time.sleep(1)
	print(f"{Fore.green}[COMPLETED]{Style.reset}")
	time.sleep(1)
	clear_console()


	print(f"""
{Fore.rgb(90, 110, 139)}============================================================================{Style.reset}
{Fore.green}Folder{Style.reset}        : {Fore.cyan}sessions{Style.reset}                             ✔️
{Fore.green}JSON{Style.reset}          : {Fore.cyan}account.json{Style.reset}                         ✔️
{Fore.green}JSON{Style.reset}          : {Fore.cyan}settings.json{Style.reset}                        ✔️
{Fore.green}Session{Style.reset}       : {Fore.rgb(123, 86, 225)}{settings['session']}.json{Style.reset}
{Fore.green}URL{Style.reset}           : {Fore.rgb(123, 86, 225)}{settings['url']}{Style.reset}
{Fore.green}Quantity{Style.reset}      : {Fore.rgb(123, 86, 225)}{settings['quantity']}{Style.reset}
{Fore.green}Refresh times{Style.reset} : {Fore.rgb(123, 86, 225)}{settings['attempt']}{Style.reset}
{Fore.green}Auto Checkout{Style.reset} : {Fore.rgb(123, 86, 225)}{settings['order']}{Style.reset}
{Fore.green}Payment method{Style.reset}: {Fore.rgb(123, 86, 225)}{settings['payment']}{Style.reset}
""")

