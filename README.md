<p align="center"><img src="https://github.com/alexandre-75/Develop_a_web_application_CashGameEdge/blob/main/pictures/142323.gif" alt="logo" /></p>

## The Project

- Use the **Django** framework.
- Using server-side rendering in **Django**.
- Developing a web application using Django with **MVT structure** (Model-View-Template).
- The app is an **MVP** (Produit Viable Minimum).

## Context

- Site that lists gaming establishments offering Cash Game poker.
- Only in France.
- He site has geographical separations.

## Database

- This repository comes with a pre-populated SQLite database of some user accounts.
- we have used SQLite for this project.

##  Project download

_Tested on Windows 10, Python 3.10.6. and Django 4.2.2_

####  1. project recovery

    $ git clone https://github.com/alexandre-75/Develop_a_web_application_CashGameEdge.git

####  2. Creating a virtual environment

    python<version> -m venv nom_env_virtuel

    Activate the environment  `mon_env_virtuel\Scripts\activate` (Windows)

####  3. Installing packages

    pip<version> install -r requirements.txt
    
####  4. Start the program

- From the project root folder, go with the terminal to the ***source*** folder :
    ```sh
     cd source/
     ```
- ***Run the server*** by executing the command :
  ```sh
  python manage.py runserver
  ```

- Open your favorite browser and navigate to the ***local development server*** at :
  ```sh
  http://127.0.0.1:8000/
  ```

#### 5. Create an account directly with the application or use the account below 
  ```sh
  http://127.0.0.1:8000/admin
  ```
   ```sh
   Username: gazelle732
   Password: password
   ```
#### 6. Database recovery
- From the project root folder, go with the terminal to the ***source*** folder :
  ```sh
   python manage.py loaddata data.json
   ```