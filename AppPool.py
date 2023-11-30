import subprocess

def start_app_pool(app_pool_name):
    try:
        # Use the `appcmd` command to start the specified application pool
        subprocess.run(['appcmd', 'start', 'apppool', f'/{app_pool_name}'], check=True)
        print(f"Application pool '{app_pool_name}' started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error starting application pool '{app_pool_name}': {e}")

def stop_app_pool(app_pool_name):
    try:
        # Use the `appcmd` command to stop the specified application pool
        subprocess.run(['appcmd', 'stop', 'apppool', f'/{app_pool_name}'], check=True)
        print(f"Application pool '{app_pool_name}' stopped successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error stopping application pool '{app_pool_name}': {e}")

# Example usage:
app_pool_name = 'YourAppPoolName'

# Stop the application pool
stop_app_pool(app_pool_name)

# Start the application pool
start_app_pool(app_pool_name)
