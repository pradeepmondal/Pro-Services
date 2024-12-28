# Pro Services - One Stop Solution for all your Household Needs

This was the project work under the MAD 2 coursework @ IIT Madras.
<br />

It is a platform connecting professionals providing household services to customers.

<br />

Core technologies used:
- Vue 3 for frontend
- Flask for backend/api
- SQLite for data storage
- Redis for caching
- Celery for asynchronous task processing
- Celery Beat for scheduled tasks
- etc.
<br />


To setup the project locally:
- navigate to the Code directory
- Backend setup: Navigate to the backend folder, open any terminal in this path, then,
  - type ```sh env_setup.sh``` to run the ```env_setup``` shell script and follow the instructions to setup the virtual environment and install the dependencies 
  - type ```sh dev_run.sh``` to run the ```dev_run``` shell script and follow the instructions to initiate a local run on your machine
- Frontend setup: Navigate to the frontend folder, open any terminal in this path, then,
  - type ```pnpm install``` to install the required dependencies
  - type ```pnpm run dev``` to run the project in the development mode
- start the redis service as per your os, for macos, type ```brew services start redis```
- start the mailhog service as per your os, for macos, type ```brew services start mailhog``` ( required only if you want to test the scheduled mailing service )

- Celery: navigate to backend folder, activate the virtual environment, and type in ```celery -A app:celery_app worker -l INFO``` to start the celery worker
- Celery Beat: navigate to backend folder, activate the virtual environment, and type in ```celery -A app:celery_app beat -l INFO ``` to start the celery beat for scheduled services
- head over to the port 5173 of your localhost to explore the project

  Built-in admin Credentials for testing:<br /><br />
    email: admin@proservices.xyz  [ Just for presentation, not belongs to me :) ] <br />
    password: test
  
<br />
Few glimpses of the app:
<br /><br />

Landing Page
![Landing Page](/resources/project_screenshot_1.png?raw=true "Landing Page")

Admin Dashboard
![Admin Dashboard](/resources/project_screenshot_2.png?raw=true "Admin Dashboard")

User Statistics Page
![User Statistics](/resources/project_screenshot_3.png?raw=true "User Statistics")

Pradeep Mondal<br/>
28th December, 2024
