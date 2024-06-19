# parallel-befisc

This Python script performs the following tasks:

- Sends 5 parallel POST requests to any free API (chosen from Google).
- Waits for the first request to complete and skips the remaining requests.
- Prints the response data from the first completed request.
- Prints the total execution time of the entire script.

## Setup and Initialization

### Setup

- Ensure you have Docker installed on your system.
- Use Python 3.10+ version for this.
- No frontend is required for this application.
- Dockerize the entire application and its dependencies.

### Initialization

1. **Setup virtual environment**

    ```bash
    python3 -m venv venv
    ```

2. **Clone the repository:**

    ```bash
    git clone https://github.com/Omkie-111/parallel-befisc.git
    ```

3. **Build the Docker containers:**

    ```bash
    make build
    ```

4. **Run the Docker containers:**

    ```bash
    make run
    ```

   This command will set up the application and print the output.

## Libraries Used 

  1. **requests** : to post requests to the API.
  2. **concurrent.futures** : for dealing with parallel processing in python. 
        **Alternatively asyncio and aiohttp can also be used, I used concurrent.futures for simplicity**
  3. **Time** : for calculating time.
