# Export Twitter Block List to CSV file

This Python script allows you to export your Twitter block list to a CSV file for easy backup or analysis.

## Prerequisites

1. You need to have Python 3 installed on your computer.
2. You need to have a Twitter account and have created a block list.
3. You need to have Twitter Developer account and have created an App.
4. The App's Consumer Key and Secret Key should be added to the config.py file.

## Installation
1. Clone this repository or download the export_block_list.py file.
2. Install the required Python packages by running ``` pip install -r requirements.txt ``` in your terminal.

## Usage
1. In the config.py file, replace the values of CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN and ACCESS_TOKEN_SECRET with your own Twitter API credentials.
2. Run python bot.py in your terminal.
3. The script will prompt you to input the name of the CSV file you want to create.
4. The script will then export your Twitter block list to the CSV file specified in step 3.
5. You can open the CSV file using Microsoft Excel or any other spreadsheet software to view or analyze the block list.

Note: The CSV file will contain the following columns: Screen Name, User ID, Name, and Blocked On.

## License
This project is licensed under the MIT License. Feel free to use, modify and distribute the code.
