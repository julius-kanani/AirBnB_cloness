# 0x00. AirBnB clone - The console

![hbnb Logo](https://i.imgur.com/sxvbWgO.png "hbnb Logo")

## Description
The **AirBnB clone - The console** project is a team project realised halfway during our Software Engineering programme at ALX. It's the first project of the series of project whose purpose is to create our own version of the AirBnB website on both front and back end.

## Download
Make on **Ubuntu 20.04 LTS** with **Python 3.8.10**
```
$ git clone https://github.com/julius-kanani/AirBnB_clone.git
$ cd AirBnB_clone
$ ./console.py
(hbnb)
```

## Output
This console works in "interactive mode":
```
$ ./console.py
(hbnb) create BaseModel
338edc32-ce7a-4631-a76d-f6a837a5c713
```
As well as in "non-interactive mode":
```
$ echo "create BaseModel" | ./console.py
(hbnb) a5106cf2-5da2-4542-9938-2e5ad23747de
(hbnb)
```

## Functions
| Functions | Usage | Description |
| --- | --- | --- |
| `create` | `create <class_name>` | Create a new instance of a specified class and show its ID|
| `all` | `all <class_name>` | Display the info of all instance (or all of the same class) |
| `show` | `show <class_name> <id>` | Display the info of an instance with its ID|
| `count` | `<class_name>.count()` | Count the number of instance of a class |
| `update` | ` update <class_name> <id> <attribute_name> <attribute_value>` | Update (or create) one attribute of an instance with its ID|
| `update` | ` <class_name>.update("<id>", {"<attribute_name>": <attribute_value>})` | Update (or create) multiple attributes (with a dict) of an instance with its ID|
| `destroy` | `destroy <class_name> <id>` | Destroy an instance with its ID |
| `help` | `help <function_name>` | Display info of one or all functions |

You can use these functions in 2 different forms:
* create User
* User.create()

## Different classes
* BaseModel
* User
* State
* City
* Place
* Amenity
* Review

## Usage
```
$ ./console.py
(hbnb) help show
Show string representation of an instance

(hbnb) show BaseModel a5106cf2-5da2-4542-9938-2e5ad23747de
[BaseModel] (a5106cf2-5da2-4542-9938-2e5ad23747de) {'id': 'a5106cf2-5da2-4542-9938-2e5ad23747de', 'created_at': datetime.datetime(2022, 7, 1, 13, 14, 2, 760448), 'updated_at': datetime.datetime(2022, 7, 1, 13, 14, 2, 760454)}
(hbnb) BaseModel.destroy("338edc32-ce7a-4631-a76d-f6a837a5c713")
(hbnb) BaseModel.count()
0
(hbnb) quit
$
```

## Authors
* [JULIUS MOMANYI KANANI](https://github.com/julius-kanani) - juliusm.kanani@gmail.com
* [Psalm Chiemenam Orah](https://github.com/orahpsalm) - psalmorahcle@gmail.com
