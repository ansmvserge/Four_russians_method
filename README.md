
## Four Russians algotithm

Python implementation of Four Russains method for boolean matrices multiplication

## Algorithm description
- Get matrices A and B
- Calculate blocks size and number
- Split A matrix on column blocks and B matrix on row blocks
- Create and fill the table to store all combinations of rows of matrix Bk
- Fill the resulting matrix regarding rows Ak and corresponding entries in table

The time comlexity is O(n^3/lg n).There are improvements for O(n^3/ lg^2 n) complexity. 
Algotithm details with full description and examples can be found [here][df1].

## Usage
Download project and open in python supporting ide e.g. pycharm. Project consists of .main file with implementation and test files. Tests were provided by 'unittest', matrices implementations were used with numpy. 
To run the algorithm run .main file and fill the matrixA.txt and matrixB.txt files with imput data.
The format of input is:

```sh
1,0
0,1
```

To run in terminal go to project directory and run with:


```sh
python3 main.py
```

   [df1]: <https://louridas.github.io/rwa/assignments/four-russians/>
