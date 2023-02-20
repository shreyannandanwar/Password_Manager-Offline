# Password Manager

It's a desktop application to manage websites, username/email stores and generate passwords with a description input field for any details or note which needs to be stored.

## Installation

Open terminal and in [terminal](https://opensource.com/article/21/8/linux-change-directories)  open this project file.

Step1:[pipenv](https://pypi.org/project/pipenv/) is to create virtual specific environment
```bash
pip install pipenv
```
once done:
```bash
pipenv shell
```

Step2:libraries needs to be:
```bash
pip install pyperclip
```
```bash
pip install py2app
```
once done open main.py file and change DEFAULT_EMAIL variable to your choice.

Step3: For Mac users : [py2app](https://www.metachris.com/2015/11/create-standalone-mac-os-x-applications-with-python-and-py2app/)
```bash
python setup.py py2app -A
```

after following the steps in the main folder a 'dict' folder is created open it and click on app to start the application.
![Screenshot 2023-02-21 at 3 15 44 AM](https://user-images.githubusercontent.com/98053839/220202950-853cd52b-1172-4bfc-8bc4-c61336c4954e.png)
it should appear like this. 

Further drag the app to Applications 
Step3:For windows is coming soon....


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
