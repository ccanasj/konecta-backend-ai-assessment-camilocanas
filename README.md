# API Konecta

# Installation

1. Clone the project repository

   - Open a terminal or command prompt.
   - Navigate to the directory where you want to clone the project.
   - Use the `git clone` command followed by the repository URL to clone the project. For example:
     ```
     git clone https://github.com/ccanasj/konecta-backend-ai-assessment-camilocanas
     ```

2. Create a virtual environment (optional but recommended)

   - While optional, it is recommended to create a virtual environment for the project. This helps keep the project's dependencies isolated from the global Python system.
   - Navigate to the cloned project directory.
   - Create a virtual environment with the following command:
     ```
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
         ```
         venv\Scripts\activate
         ```
     - On macOS and Linux:
         ```
         source venv/bin/activate
         ```

3. Install project dependencies

   - Ensure you are in the app directory of the cloned project with the virtual environment activated.
   - Use the command `pip install -r requirements.txt` to install the project dependencies.

4. Create environment variables

   - In the app directory, create a file named `.env` (if it doesn't already exist).
   - Open the `.env` file in a text editor.
   - Add the following lines to the file, specifying the values for each environment variable:
     ```
     MYSQL_USER=user
     MYSQL_PASSWORD=123456789
     MYSQL_HOST=localhost
     MYSQL_PORT=3306
     MYSQL_DATABASE=task_manager
     JWT_SECRET_KEY=secretkey
     ```

5. Init the database

   - Start docker
   - Use the following command to start the database on local

   ```
   docker run -d --name my-mariadb -e MYSQL_USER=user -e MYSQL_PASSWORD=123456789 -e MYSQL_DATABASE=task_manager -e MARIADB_ROOT_PASSWORD=root -p 3306:3306 mariadb
   ```

6. Run the project

   - Use the following command to start the FastAPI server:

   ```
   uvicorn main:app --reload
   ```

7. Test the project

   - Open a web browser and go to `http://localhost:8000/`. You should see the OpenAPI documentation.

   That's it! Now you have the FastAPI project installed and running in your local environment. You can explore the defined routes and functionalities in the project and perform testing as needed.

# Usage

## Tests

**Note:** Remember to activate the virtual environment with the project requirements and Docker should be installed on your machine.

1. Open a terminal or command prompt.

2. Run the following command to start a MariaDB Docker container:

```bash
docker run -d --name my-mariadb \
  -e MYSQL_ROOT_PASSWORD=Prueba123 \
  -e MYSQL_USER=Tester \
  -e MYSQL_PASSWORD=Prueba123 \
  -e MYSQL_DATABASE=tests \
  -p 3307:3306 \
  mariadb
```

3. Go to source folder

```bash
cd app/
```

4. Set environment variable

   - **Linux**

      ```bash
      export TESTING="True"
      ```

   - **Windows**

      ```powershell
      $env:TESTING="True"
      ```

5. Run the tests

   ```bash
   python -m pytest tests/
   ```

## Migrations

**Note:** Do not delete the migrations folder.

### Generating migrations

```bash
alembic revision --autogenerate -m "Comment here"
```

### Checking the current migration

```bash
alembic current
```

### Running the latest migration

```bash
alembic upgrade head
```

**Note:** Before running the migration, check the latest created version inside the version folder.

### Creating migration functions

Inside the version file, there are two functions:

- upgrade
- downgrade

These functions can be modified if any errors occur.

## Docker Compose

### Start containers

```bash
docker-compose up --build -d
```

This command starts the containers defined in the `docker-compose.yml` file.

- The `-d` option runs the containers in the background (detached mode).
- The `--build` This command builds or rebuilds the containers defined in the `docker-compose.yml` file.

### Stop containers

```bash
docker-compose down
```

This command stops and removes the containers defined in the `docker-compose.yml` file.

### View container status

```bash
docker ps
```

This command displays the status of the containers defined in the `docker-compose.yml` file. It provides information such as the container name, status, exposed ports, and project name.

### Restart containers

```bash
docker-compose restart
```

This command restarts the containers defined in the `docker-compose.yml` file.

Remember to execute these commands from the directory where the `docker-compose.yml` file is located.
