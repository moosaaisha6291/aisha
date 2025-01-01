import os
import pyfiglet
from termcolor import colored

# Function to display the menu
def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
    
    # Display the "Created by CPS" message at the top
    print(colored("Created by CPS", 'magenta'))
    
    # Create a colorful header with figlet text
    ascii_art = pyfiglet.figlet_format("Web Pentesting Tools")
    print(colored(ascii_art, 'cyan'))
    
    # Print the main menu in colorful text
    print(colored("Select a Tool to Use:", 'yellow'))
    print(colored("1. Automated Cross-Site Scripting (XSS) Scanner", 'green'))
    print(colored("2. SQL Injection Vulnerability Detector", 'green'))
    print(colored("3. Brute Force Login Attempt Tool", 'green'))
    print(colored("4. Web Application Firewall (WAF) Testing Tool", 'green'))
    print(colored("5. Cross-Site Request Forgery (CSRF) Testing Tool", 'green'))
    print(colored("6. Directory Traversal Vulnerability Scanner", 'green'))
    print(colored("7. Content Security Policy (CSP) Checker", 'green'))
    print(colored("8. HTTP Security Headers Scanner", 'green'))
    print(colored("9. SSL/TLS Security Scanner", 'green'))
    print(colored("10. Subdomain Discovery Tool", 'green'))
    print(colored("11. Web Application Security Report Generator", 'green'))
    print(colored("12. Session Management and Cookie Security Checker", 'green'))
    print(colored("0. Exit", 'red'))

# Function to handle the user's menu selection
def select_tool():
    while True:
        display_menu()
        
        # Get user's selection
        try:
            choice = int(input(colored("Enter the number of the tool you want to use: ", 'yellow')))
        except ValueError:
            print(colored("Invalid input, please enter a number from 0 to 12.", 'red'))
            continue
        
        # Handling the user's choice
        if choice == 1:
            print(colored("Launching Automated Cross-Site Scripting (XSS) Scanner...", 'blue'))
            # Call your XSS Scanner function here
        elif choice == 2:
            print(colored("Launching SQL Injection Vulnerability Detector...", 'blue'))
            # Call your SQL Injection Detector function here
        elif choice == 3:
            print(colored("Launching Brute Force Login Attempt Tool...", 'blue'))
            # Call your Brute Force Tool function here
        elif choice == 4:
            print(colored("Launching Web Application Firewall (WAF) Testing Tool...", 'blue'))
            # Call your WAF Testing Tool function here
        elif choice == 5:
            print(colored("Launching Cross-Site Request Forgery (CSRF) Testing Tool...", 'blue'))
            # Call your CSRF Testing Tool function here
        elif choice == 6:
            print(colored("Launching Directory Traversal Vulnerability Scanner...", 'blue'))
            # Call your Directory Traversal Tool function here
        elif choice == 7:
            print(colored("Launching Content Security Policy (CSP) Checker...", 'blue'))
            # Call your CSP Checker function here
        elif choice == 8:
            print(colored("Launching HTTP Security Headers Scanner...", 'blue'))
            # Call your HTTP Headers Scanner function here
        elif choice == 9:
            print(colored("Launching SSL/TLS Security Scanner...", 'blue'))
            # Call your SSL/TLS Scanner function here
        elif choice == 10:
            print(colored("Launching Subdomain Discovery Tool...", 'blue'))
            # Call your Subdomain Discovery Tool function here
        elif choice == 11:
            print(colored("Launching Web Application Security Report Generator...", 'blue'))
            # Call your Report Generator function here
        elif choice == 12:
            print(colored("Launching Session Management and Cookie Security Checker...", 'blue'))
            # Call your Session Management Checker function here
        elif choice == 0:
            print(colored("Exiting the program...", 'red'))
            break
        else:
            print(colored("Invalid choice. Please choose a number from 0 to 12.", 'red'))

if __name__ == "__main__":
    select_tool()
