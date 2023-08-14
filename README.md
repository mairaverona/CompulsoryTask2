# mySite - bookClub

## Description

bookClub is your go-to hub for sharing and tracking your reading journey. This Django-powered web application offers a user-friendly way to:

- Keep a record of books you've read.
- Discover what fellow readers are exploring this month.
- Stay excited about upcoming reads in your queue.
Experience the joy of reading in a whole new light with bookClub – where sharing stories meets digital convenience.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Credits](#credits)

## Installation

To run this project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/mairaverona/CompulsoryTask2.git`
2. Navigate to the project directory: `cd your-project`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Set up the database: `python manage.py migrate`
5. Create a superuser account (for admin access): `python manage.py createsuperuser`
6. Start the development server: `python manage.py runserver`
7. Access the project in your web browser at `http://localhost:8000/`

## Usage

After following the installation steps, you can use bookClub as follows:

1. Open a web browser and navigate to 'http://127.0.0.1:8000/'
2. To go to currently reading page navigate to 'http://127.0.0.1:8000/currently_reading/'
3. To go to past readings page navigate to 'http://127.0.0.1:8000/past_weeks/'
4. To go to next read page navigate to 'http://127.0.0.1:8000/next_read/'

### Screenshots

![Home page](https://firebasestorage.googleapis.com/v0/b/new-repository-4a050.appspot.com/o/Screenshot%202023-08-14%20at%2015.41.24.png?alt=media&token=ed0cba7a-e98f-413f-ade3-20a040040f4d)
Register or Login

![Currently reading](https://firebasestorage.googleapis.com/v0/b/new-repository-4a050.appspot.com/o/Screenshot%202023-08-14%20at%2015.41.34.png?alt=media&token=87cfe7be-305e-4643-a395-d30a05b33435)
Currently reading book

![Next read](https://firebasestorage.googleapis.com/v0/b/new-repository-4a050.appspot.com/o/Screenshot%202023-08-14%20at%2015.41.42.png?alt=media&token=fb20b375-217c-452d-b35b-f8c21d6351ca)
Next book on the list

![Past weeks](https://firebasestorage.googleapis.com/v0/b/new-repository-4a050.appspot.com/o/Screenshot%202023-08-14%20at%2015.41.51.png?alt=media&token=115b4a7e-6243-4c0b-bbd9-8177a6f66bbe)
Past books already read on previous weeks

## Credits

This project was created by Maira Verona

Special thanks to the following resources:

- [Django Documentation](https://docs.djangoproject.com/)
- [HyperionDev](http://hyperiondev.com)

---
