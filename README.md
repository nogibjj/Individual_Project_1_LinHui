[![Install](https://github.com/nogibjj/Individual_Project_1_LinHui/actions/workflows/Install.yml/badge.svg)](https://github.com/nogibjj/Individual_Project_1_LinHui/actions/workflows/Install.yml)
[![Format](https://github.com/nogibjj/Individual_Project_1_LinHui/actions/workflows/Format.yml/badge.svg)](https://github.com/nogibjj/Individual_Project_1_LinHui/actions/workflows/Format.yml)
[![Lint](https://github.com/nogibjj/Individual_Project_1_LinHui/actions/workflows/Lint.yml/badge.svg)](https://github.com/nogibjj/Individual_Project_1_LinHui/actions/workflows/Lint.yml)
[![Test](https://github.com/nogibjj/Individual_Project_1_LinHui/actions/workflows/Test.yml/badge.svg)](https://github.com/nogibjj/Individual_Project_1_LinHui/actions/workflows/Test.yml)


# Individual Project 1 IDS 760

This individual project includes 
- Python script performing descriptive statistics using Pandas
- Jupyter notebook that performs the same descriptive statistics
- lib.py file that shares the common code between the script and notebook
- Makefile with tests, format, lint, installation of dependencies
- test_script.py to test script
- test_lib.py to test library
- nbval plugin for pytest in the Jupyter notebook
- Pinned requirements.txt
- CI via github actions with yml file

## Dataset: Apple’s stock price in the past year. It contains:

- Date
- Open price
- High price
- Low price
- Adjusted close price
- Trading volumn

## Summary Stats:

- Open: Mean = 160.47, Median = 154.93, Std = 19.01
- High: Mean = 162.26, Median = 157.44, Std = 18.77
- Low: Mean = 158.89, Median = 153.42, Std = 19.28
- Close: Mean = 160.65, Median = 155.32, Std = 19.01
- Adj Close: Mean = 160.19, Median = 154.7, Std = 19.19
- Volumn: Mean = 69482141.2, Median = 64624600, Std = 24118947.76

## AAPL stock price change over the year
![Open price figure](https://github.com/nogibjj/Individual_Project_1_LinHui/assets/83142133/bae8b869-bd66-4a44-8c54-d6958688f31b)

## Demo video

https://www.youtube.com/watch?v=yY53HjRepr4

P.S. I updated the Github action workflow, and it's now displaying four different badges. Please ignore the one shown in the demo video.








