# Scrabble

It's Scrabble game that give you value of word directly from prompt or give you words from files with .txt extension

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You need to have

```
Python 3.7
```

### How to run it

After downloading repository you need to run main.py script. To do this you need to open prompt, go to the file location and write:  

```
python3 main.py [source] [name]
```
Where in **source** you can choose between prompt and txt.
If you write prompt the value of name must be word like e.g. 'Python'

example
```
python3 main.py prompt Python
```
Program will give you value 14 which is value of this word in scrabble.

If you write **txt** in [source] you can choose to write in [name] word like **dictionary** which gives the biggest value of a dictionary.txt file.
```
python3 main.py txt dictionary
```

 if you write **score** as integer e.g. 33, program will give you back every word in dictionary.txt that has this score.

 ```
 python3 main.py txt 33
 ```



## Tests
  Plan in the future


## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Python 3](https://www.python.org/) - high-level programming language

## Authors

* **Krystian Klik** - *Initial work*



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
