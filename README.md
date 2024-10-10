# Movie Recommendation System

This is a supervised learning model for a movie recommendation system, which throughout the execution of the program the user is prompt to say what genres of movies he prefers, the app accepts full sentences without any special requirements, with the expectation of correct grammar, the application is case insensitive

Ex. I like to watch hORror movies and Drama, but sometimes I can watch Comedy movies

The app extract all the mentioned genres and recommend to the user the movies that satisfies the most it's request

## Getting started

### Installation
1. Clone the repository:
   ```sh
    git clone https://github.com/StiVit/movie-recommendation-system.git
    cd movie-recommendation-system
   ```
2. **Run the Makefile:**

    Use the `make` command to automate the setul process.
   ```sh
   make
   ```
   
   This command will perform the following steps:

   - Create a virtual encironment (`.venv`)
   - Activate the virtual environment
   - Install the dependencies from `requirements.txt`
   
    **Note:** The virtual environment activation step will print a message on how to manually activate the virtual environment. Follow the instructions for your operating system:

    - On Linux and macOS:
      ```sh
      source venv/bin/activate
      ```
    - On Windows:
      ```sh
      venv\Scripts\activate
      ```
      
### Manual Steps (if not using Makefile)
    
If you prefer to run each step manually, follow these commands:

1. **Create and activate a virtual environment:**
    
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```
       
Now you have your development environment set up and the application running. Enjoy coding!

### Usage

1. Launch the `main.py` file from console to load the data and process it
2. You'll be prompt to introduce you'r preferede genre, Write full sentences about what you love
3. Admire the result

### Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.