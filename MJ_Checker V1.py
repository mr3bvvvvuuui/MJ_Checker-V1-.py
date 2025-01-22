import requests
from discord_webhook import DiscordWebhook
import random
import string
import time
from colorama import Fore, init

init(autoreset=True)

def choose_platform():
    print(Fore.CYAN + "Choose the platform you want to check:")
    print("1. Discord")
    print("2. TikTok")
    print("3. Instagram")
    platform_choice = input("Enter the platform number (1/2/3): ")
    return platform_choice

def generate_username(length):
    letters_and_digits = string.ascii_letters + string.digits
    username = ''.join(random.choice(letters_and_digits) for i in range(length))
    return username

def check_discord_username(username, webhook_url, proxies=None):
    url = f"https://discord.com/api/v9/users/{username}"
    try:
        response = requests.get(url, proxies=proxies)
        if response.status_code == 404:
            print(Fore.GREEN + f"[{username}] is available on Discord")
            send_to_webhook(username, webhook_url)
        elif response.status_code == 403:
            print(Fore.RED + f"[{username}] is banned on Discord")
        else:
            print(Fore.YELLOW + f"[{username}] is not available on Discord")
    except requests.RequestException as e:
        print(Fore.RED + f"Error checking Discord username: {e}")

def check_tiktok_username(username, webhook_url, proxies=None):
    url = f"https://www.tiktok.com/@{username}"
    try:
        response = requests.get(url, proxies=proxies)
        if response.status_code == 404:
            print(Fore.GREEN + f"[{username}] is available on TikTok")
            send_to_webhook(username, webhook_url)
        elif response.status_code == 403:
            print(Fore.RED + f"[{username}] is banned on TikTok")
        else:
            print(Fore.YELLOW + f"[{username}] is not available on TikTok")
    except requests.RequestException as e:
        print(Fore.RED + f"Error checking TikTok username: {e}")

def check_instagram_username(username, webhook_url, proxies=None):
    url = f"https://www.instagram.com/{username}/"
    try:
        response = requests.get(url, proxies=proxies)
        if response.status_code == 404:
            print(Fore.GREEN + f"[{username}] is available on Instagram")
            send_to_webhook(username, webhook_url)
        elif response.status_code == 403:
            print(Fore.RED + f"[{username}] is banned on Instagram")
        else:
            print(Fore.YELLOW + f"[{username}] is not available on Instagram")
    except requests.RequestException as e:
        print(Fore.RED + f"Error checking Instagram username: {e}")

def send_to_webhook(username, webhook_url):
    try:
        webhook = DiscordWebhook(url=webhook_url, content=f"Available username: {username}")
        webhook.execute()
    except requests.RequestException as e:
        print(Fore.RED + f"Error sending webhook: {e}")

def set_proxy():
    proxies = {
        'http': 'http://your_proxy_here',
        'https': 'http://your_proxy_here',
    }
    return proxies

def setup():
    print(Fore.MAGENTA + "MJ CHECKER V1 - Developed by Majestic")
    print(Fore.YELLOW + "This tool is provided for educational purposes only.")
    print(Fore.CYAN + "Please use it responsibly and follow all platform policies.")
    
    platform_choice = choose_platform()
    username_length = int(input("Enter the number of characters for the username: "))
    webhook_url = input("Enter your Discord Webhook URL: ")
    
    print(Fore.CYAN + "Installing requirements and checking internet connection...")
    
    proxies = set_proxy()
    
    print(Fore.GREEN + "Tool is ready to use!")
    
    return platform_choice, username_length, webhook_url, proxies

def main():
    platform_choice, username_length, webhook_url, proxies = setup()

    while True:
        username = generate_username(username_length)
        print(Fore.YELLOW + f"Checking: {username}")

        if platform_choice == '1':
            check_discord_username(username, webhook_url, proxies)
        elif platform_choice == '2':
            check_tiktok_username(username, webhook_url, proxies)
        elif platform_choice == '3':
            check_instagram_username(username, webhook_url, proxies)
        else:
            print(Fore.RED + "Invalid choice! Please select a valid platform.")
            break
        
        time.sleep(2)

if __name__ == "__main__":
    main()