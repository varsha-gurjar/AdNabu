
Steps To Run This Script On Local Machine

1. Clone this repository using ssh "git clone git@github.com/varsha-gurjar/AdNabu.git"
2. Go to the terminal and open the project base folder.
3. Create the virtual environment for the project "python3 -m venv venv"
4. Activate the virtual environment of the project "source venv/bin/activate"
5. Install the required packages "pip3 install -r requirements.txt"
6. Download and add the chrome driver based on your machine's Chrome version to this location "/utils/driver/chromedriver_mac64"
7. To run all the test form the base directory of the project, execute "pytest"
8. To run the test from specific directory, execute "pytest /path"
9. To run specific test file, execute "pytest /path/filename.py"
10. To run with all other variable and reports. "URL=https://adnabu-arjun.myshopify.com/ pytest -v -s --html=AdNabu_test_report.html --self-contained-html"