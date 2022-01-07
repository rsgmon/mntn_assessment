# mntn_assessment

prerequisites: python 3+ installed

To run at a console: 
    navigate to repo folder    
    python main.py

Approach:
I wasn't exactly sure about what was meant by "executable" which is usually platform specific. This is why I kept it in
python file. But I wanted it to be as close to being executable as possible. So nothing outside the python
standard library is included. No virtual environment or installation of any libraries is needed.

Approach was to make a simple python script that dynamically called the catfact api with some parameters. Then it
verifies the endpoint was successfully hit and tests the parameter is correctly working.
