# Overview
The Single-Node Container Scheduling project is designed to handle user requests through a command line interface (CLI) and Docker containers. It efficiently processes input files, executes specific commands, and generates output files based on the user's operations.

## Prerequisites
To run this project, you need to have the following:
- A machine with sufficient resources (recommended: 4 Ubuntu Server 20.04 virtual machines).
- Docker installed on your system.

## Installation
Set up your environment:

You may use a primary machine with sufficient resources. If you encounter issues with the number of CPU cores, consider using Docker.
Install Docker:

Follow the official Docker installation guide to install Docker on your machine.
Clone this repository:

'''
git clone https://github.com/DianCrafts/VM-manager

'''
Build Docker images:

Navigate to the project directory and run:
```
docker build -t <image-name> .
```
## Running the Project
To run the project, execute the following command in your terminal:

```
python3 main.py
```
## Request Format
Requests to the system should be formatted as follows:

{<operation name, input file path>, <operation name, input file path>, …, <output directory>}
### Example Request:

javascript
Copy code
{<min,/tmp/grade.txt>, <max, /tmp/grade.txt>, </tmp/gradeStat>}
Command Execution
The application will handle requests in the following manner:

It will queue incoming requests.
Process the requests using available Docker containers.
Generate output files based on the executed commands.
Implementation Details
Threading: The implementation uses threading to manage concurrent request handling and job execution.
File Handling: Input files are processed according to the requested operations (e.g., min, max, sort).
Docker Integration: The project utilizes Docker to create isolated environments for command execution.
