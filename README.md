# AirBnb : The consoel #
This project is divided into 4 different parts:
The frontend: which what is in this repo, the console using the cmd model
The backend: Applying OOP concept here
The dataBase: we will use JSON as a file storage for the objects storage
Testing: Using the unittest model
It will be modefied after learning about frontend, FLASK, and SQL frameworks.
## Applying OOP concpet here and the main big picture: ##
We will have a big class that will be the base of everything created in our web app. This class is named `BaseModel` by implementing any attribute or methods in it, we will be able to control the flow for the other children classes. Now this class has:
Public instance attributes:
1. id: string - assign with an uuid when an instance is created
2. uuid.uuid4() to generate unique id but don’t forget to convert to a string the goal is to have unique id for each BaseModel
3. created_at: datetime - assign with the current datetime when an instance is created
4. updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
_str_ method : should print: [<class name>] (<self.id>) <self.__dict__>
---
Public instance methods:
1. save(self): updates the public instance attribute updated_at with the current datetime
2. 2. to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance by using self.__dict__, only instance attributes set will be returned a key __class__ must be added to this dictionary with the class name of the object
3. created_at and updated_at must be converted to string object in ISO format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259) you can use isoformat() of datetime object This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our BaseModel.
- put in place a parent class (called BaseModel) to take care of the initialization.
- serialization and deserialization of your future instances create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine.
![Capture](https://github.com/SolomonChidera/AirBnB_clone/assets/139129370/d2527ceb-4e3b-4a73-bd93-45b926962d9e)

## What’s a command interpreter? ##


It's the same as our Shell project, but it's limited to a specific use-case. In our case, we want to be able to manage the objects of our project:
*You can check the other repos to find more about writting your own shell*
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

After having our base model that all other objects are going to inherit from, we will start building other blockes based on it. Starting with a USER block, a review, state, city, amenity, and a place.

## The saving engine (JSON file) ##
But why are we using a json storage system here?:
Because JSON is an official representation of all oop concepts in a form that is humanly readable and language friendly for other developers. If another programmer used this in his JS file, he will be able to extract all dictionary values from the json file. Which means all objects instances will be humanly readable for the other parties.
