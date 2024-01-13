# AirBnb Console

![AirBnb Logo](path/to/your/logo.png)

## Project Overview

Welcome to the AirBnb Console project! This repository is organized into four main parts, each playing a crucial role in the functioning of our web application:

1. **Frontend:** This repository primarily focuses on the frontend, which encompasses the console built using the cmd model.

2. **Backend:** Applying Object-Oriented Programming (OOP) concepts, the backend is structured to handle the core functionalities of our application.

3. **Database:** We leverage JSON as a file storage solution for storing objects, ensuring seamless data management.

4. **Testing:** The unittest model is employed for comprehensive testing, guaranteeing the robustness of our classes and storage engine.

## Object-Oriented Programming (OOP) Concept

The backbone of our project revolves around a central class named `BaseModel`. This class serves as the foundation for all entities within our web app. It encompasses:

### Public Instance Attributes

- **id (string):** Assigned a unique uuid when an instance is created using `uuid.uuid4()`. The goal is to ensure a distinct id for each `BaseModel` instance.

- **created_at (datetime):** Assigned the current datetime when an instance is created.

- **updated_at (datetime):** Assigned the current datetime when an instance is created and updated every time an object is modified.

### Public Instance Methods

- **save(self):** Updates the public instance attribute `updated_at` with the current datetime.

- **to_dict(self):** Returns a dictionary containing all keys/values of the instance. Only set instance attributes will be included. Additionally, a key named "class" with the object's class name must be added to this dictionary. The `created_at` and `updated_at` attributes are converted to a string object in ISO format.

These methods form the initial steps of the serialization/deserialization process, creating a dictionary representation of our `BaseModel`.

## Serialization and Deserialization

To achieve serialization/deserialization, a parent class (`BaseModel`) is implemented to handle initialization, serialization, and deserialization for future instances. The flow involves:

Instance <-> Dictionary <-> JSON string <-> File

All classes used for AirBnB (User, State, City, Place, etc.) inherit from `BaseModel`. The first abstracted storage engine implemented in the project is the File storage.

## Command Interpreter

The command interpreter, akin to our Shell project, is tailored for the specific use case of managing objects in our project. Key functionalities include:

- Creating a new object (e.g., User or Place).
- Retrieving an object from a file, a database, etc.
- Performing operations on objects (count, compute stats, etc.).
- Updating attributes of an object.
- Destroying an object.

For more details on writing your own shell, you can refer to other repositories.

Feel free to explore the different components of our AirBnb Console project and contribute to making it even more awesome! If you have any questions or need assistance, don't hesitate to reach out to the community. Happy coding!
