#! /bin/sh

echo "--------------------------------------------------------------------------"
echo "This will setup the local environment."
echo "--------------------------------------------------------------------------"
read -p "Would you like to continue? (y/n): " choice

if [[ "$choice" == "y" || "$choice" == "Y" ]]; then
    echo "Checking for the environment folder..."
    if [[ -d ".virtual_env" ]]; then
        echo ".virtual_env folder already exists, proceeding further..."
    else
        echo "creating .virtual_env folder and installing the dependencies..."
        python3 -m venv .virtual_env
    fi
    . .virtual_env/bin/activate

    pip3 install --upgrade pip
    pip3 install -r requirements.txt

    deactivate

elif [[ "$choice" == "n" || "$choice" == "N" ]]; then
    echo "Chose no. No Problem. So exiting..."
else
    echo "Invalid choice. So exiting..."
fi