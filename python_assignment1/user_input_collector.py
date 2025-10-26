"""
Python Input Collector - Assignment
Collecting user input for different data types (string, integer, float)
"""

import json
import os
from datetime import datetime


# Terminal colors for better display
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'


def print_header(text):
    """Print a styled header"""
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*70}")
    print(f"{text.center(70)}")
    print(f"{'='*70}{Colors.END}\n")


def print_success(text):
    """Print success message in green"""
    print(f"{Colors.GREEN}✓ {text}{Colors.END}")


def print_error(text):
    """Print error message in red"""
    print(f"{Colors.RED}✗ {text}{Colors.END}")


def print_info(text):
    """Print info message in cyan"""
    print(f"{Colors.CYAN}ℹ {text}{Colors.END}")


def get_string_input(prompt, min_length=1, max_length=100):
    """Get and validate string input"""
    while True:
        user_input = input(f"{Colors.BOLD}{prompt}{Colors.END}").strip()
        
        if not user_input:
            print_error("Input cannot be empty. Please try again.")
            continue
            
        if len(user_input) < min_length:
            print_error(f"Input too short. Minimum {min_length} characters.")
            continue
            
        if len(user_input) > max_length:
            print_error(f"Input too long. Maximum {max_length} characters.")
            continue
            
        print_success(f"Accepted: {user_input}")
        return user_input


def get_integer_input(prompt, min_val=None, max_val=None):
    """Get and validate integer input"""
    while True:
        try:
            user_input = input(f"{Colors.BOLD}{prompt}{Colors.END}").strip()
            value = int(user_input)
            
            if min_val and value < min_val:
                print_error(f"Value too small. Minimum is {min_val}.")
                continue
                
            if max_val and value > max_val:
                print_error(f"Value too large. Maximum is {max_val}.")
                continue
                
            print_success(f"Accepted: {value}")
            return value
            
        except ValueError:
            print_error(f"'{user_input}' is not valid. Please enter a whole number.")


def get_float_input(prompt, min_val=None, max_val=None):
    """Get and validate float input"""
    while True:
        try:
            user_input = input(f"{Colors.BOLD}{prompt}{Colors.END}").strip()
            value = float(user_input)
            
            if min_val and value < min_val:
                print_error(f"Value too small. Minimum is {min_val}.")
                continue
                
            if max_val and value > max_val:
                print_error(f"Value too large. Maximum is {max_val}.")
                continue
                
            print_success(f"Accepted: {value}")
            return value
            
        except ValueError:
            print_error(f"'{user_input}' is not a valid number. Please enter a decimal number.")


def display_data_table(data):
    """Display collected data in a table"""
    print(f"\n{Colors.GREEN}{Colors.BOLD}{'='*70}")
    print(f"{'USER INFORMATION SUMMARY'.center(70)}")
    print(f"{'='*70}{Colors.END}\n")
    
    # Display data
    print(f"{Colors.BOLD}{'Field':<20} {'Value':<30} {'Type':<15}{Colors.END}")
    print("-" * 70)
    
    print(f"{'Name':<20} {data['name']:<30} {Colors.CYAN}{type(data['name']).__name__:<15}{Colors.END}")
    print(f"{'Email':<20} {data['email']:<30} {Colors.CYAN}{type(data['email']).__name__:<15}{Colors.END}")
    print(f"{'Age':<20} {data['age']} years{' '*21} {Colors.CYAN}{type(data['age']).__name__:<15}{Colors.END}")
    print(f"{'Height':<20} {data['height']:.2f} cm{' '*20} {Colors.CYAN}{type(data['height']).__name__:<15}{Colors.END}")
    print(f"{'City':<20} {data['city']:<30} {Colors.CYAN}{type(data['city']).__name__:<15}{Colors.END}")
    print(f"{'Salary':<20} ${data['salary']:,.2f}{' '*19} {Colors.CYAN}{type(data['salary']).__name__:<15}{Colors.END}")
    
    print("-" * 70)
    
    # Show some calculations
    print(f"\n{Colors.BOLD}Extra Information:{Colors.END}")
    print(f"  • Height in meters: {data['height']/100:.2f} m")
    print(f"  • Annual salary: ${data['salary']*12:,.2f}")
    print(f"  • Birth year (approx): {datetime.now().year - data['age']}")
    
    print(f"\n{Colors.GREEN}{'='*70}{Colors.END}")


def show_type_conversions(data):
    """Show type conversion examples"""
    print_header("TYPE CONVERSIONS")
    
    print(f"{Colors.BOLD}Original Data Types:{Colors.END}")
    for key, value in data.items():
        if key != 'timestamp':
            print(f"  {key}: {Colors.CYAN}{type(value).__name__}{Colors.END}")
    
    print(f"\n{Colors.BOLD}Conversion Examples:{Colors.END}")
    print(f"  Age (int) to String: '{str(data['age'])}' → {type(str(data['age'])).__name__}")
    print(f"  Age (int) to Float: {float(data['age'])} → {type(float(data['age'])).__name__}")
    print(f"  Height (float) to Integer: {int(data['height'])} → {type(int(data['height'])).__name__}")
    
    print(f"\n{Colors.YELLOW}⚠ Note: Converting float to int removes decimal places!{Colors.END}")


def save_to_file(data):
    """Save data to JSON file"""
    try:
        os.makedirs("data", exist_ok=True)
        filepath = os.path.join("data", "user_data.json")
        
        # Load existing data
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                all_data = json.load(f)
        else:
            all_data = []
        
        # Add new data
        all_data.append(data)
        
        # Save
        with open(filepath, 'w') as f:
            json.dump(all_data, f, indent=4)
        
        print_success(f"Data saved to {filepath}")
        
    except Exception as e:
        print_error(f"Could not save data: {str(e)}")


def main():
    """Main function"""
    # Welcome message
    print_header("USER INPUT COLLECTOR")
    print_info("This program collects different types of data")
    print_info("All inputs are validated\n")
    
    input(f"{Colors.BOLD}Press Enter to start...{Colors.END}")
    
    # Collect string inputs
    print(f"\n{Colors.BLUE}{Colors.BOLD}[1/6] Personal Information{Colors.END}")
    name = get_string_input("Enter your full name: ", min_length=2, max_length=50)
    
    print(f"\n{Colors.BLUE}{Colors.BOLD}[2/6] Contact Information{Colors.END}")
    email = get_string_input("Enter your email: ", min_length=5, max_length=100)
    
    # Collect integer input
    print(f"\n{Colors.BLUE}{Colors.BOLD}[3/6] Age{Colors.END}")
    print_info("Enter age between 1-150")
    age = get_integer_input("Enter your age: ", min_val=1, max_val=150)
    
    # Collect float inputs
    print(f"\n{Colors.BLUE}{Colors.BOLD}[4/6] Height{Colors.END}")
    print_info("Enter height in cm (50-250)")
    height = get_float_input("Enter your height (cm): ", min_val=50.0, max_val=250.0)
    
    print(f"\n{Colors.BLUE}{Colors.BOLD}[5/6] Location{Colors.END}")
    city = get_string_input("Enter your city: ", min_length=2, max_length=50)
    
    print(f"\n{Colors.BLUE}{Colors.BOLD}[6/6] Salary{Colors.END}")
    print_info("Enter monthly salary in USD")
    salary = get_float_input("Enter monthly salary: ", min_val=0.0)
    
    # Store data
    user_data = {
        "name": name,
        "email": email,
        "age": age,
        "height": height,
        "city": city,
        "salary": salary,
        "timestamp": datetime.now().isoformat()
    }
    
    # Show results
    print_success("\nAll data collected!")
    display_data_table(user_data)
    show_type_conversions(user_data)
    
    # Save option
    print_header("SAVE DATA")
    save_choice = input(f"{Colors.BOLD}Save data? (y/n): {Colors.END}").strip().lower()
    
    if save_choice in ['y', 'yes']:
        save_to_file(user_data)
    else:
        print_info("Data not saved")
    
    # End
    print_header("COMPLETE")
    print(f"{Colors.GREEN}{Colors.BOLD}Thank you for using the program!{Colors.END}")
    print_info("Assignment complete! 🎉\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Program stopped by user{Colors.END}\n")
    except Exception as e:
        print_error(f"\nError occurred: {str(e)}\n")

