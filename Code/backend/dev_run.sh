#! /bin/sh

echo "------------------------------------------------------------------------"
echo "This will start the backend in development environment."
echo "------------------------------------------------------------------------"
read -p "Ready to go? (y/n): " choice

if [[ "$choice" == "y" || "$choice" == "Y" ]]; then
    if [[ -d ".virtual_env" ]]; then
        echo "Enabling the dev environment..."
        . .virtual_env/bin/activate
        export ENV=dev
        python3 app.py
        deactivate
        

    else
        echo "Dev environment isn't set up yet. Try running 'env_setup.sh' first !!"
        
    fi

elif [[ "$choice" == "n" || "$choice" == "N" ]]; then
    echo "No worries. Exiting..."

else
    echo "Invalid choice. So exiting..."

fi