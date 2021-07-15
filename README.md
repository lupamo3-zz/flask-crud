<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
-->





<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Flask Collect Details API</h3>
</p>



<!-- ABOUT THE PROJECT -->
## About The Project

An application that allows users to create accounts, create certificates, view certificates, edit certificates, edit their profile, view certificate statistics and send the certificates via Email.

.

Here are some of the features:
* Create Accounts
* Create Certificates
* Edit Certificates
* View Certificates
* Edit their profiles
* Send certificates via email
* View Certificate Statistics
* It has implemented DRY principles  :smile:



### Built With

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Python](https://www.python.org/)
* [PostgresQl](https://www.postgresql.org/)



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
  ```sh
  
  ```

### Installation

1. Access Github [https://github.com](https://github.com)
2. Clone the repo
   ```sh
   git clone https://github.com/lupamo3/flask-crud.git
   ```
3. Change directory into the iReporter-Flask directory :
   ```sh
   cd iReporter-Flask
   ```
4. Create and activate your virtual environment :

   ```sh
   Virtual venv python=[Python-Version]
   Pip install auto-env
   ```
5. Install Project Requirements
```sh
pip install -r requirements.txt
```
6. Run the application
```sh
flask run
```

### Test the application on Postman
## Test The API end-points
 - Run [iReporter](https://ireporterflask-api-heroku.herokuapp.com/) on your postman to test the URLs

or use:

| URL                                 | METHOD                 | MESSAGE                                |
| ------------------------------------|:----------------------:| --------------------------------------:|
|/api/v1/personal/                    | POST                   | Create a user/student.                 |
|/api/v1/personal/                    | GET                    | Get all students.                      |
|api/v1/personal/<int:user_id>        | GET<int:id>            | Get a Specific Student                 |
|api/v1/personal/me                   | PUT                    | Update Specific Student  records       |
|api/v1/personal/me                   | DELETE                 | Delete a Student record                |
|api/v1/personal/me                   | GET                    | Get a Students personal record         |
|api/v1/personal/login                | POST                   | Login a student.                       |
|/api/v1/certificate/                 | POST                   | Create a Certificate.                  |
|/api/v1/certificate/<int:certificate_id>| GET<int:certificate_id>| Get a specific Certificate          |  

---


<!-- USAGE EXAMPLES -->
## Additional Information

- **Feel free to reach me via email and to fork this project**
    - Any feedback would be appreciated.
    - The Pull requests have bit by bit application documentation


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


<!-- CONTACT -->
## Contact

Your Name - [@nlanjichi](https://twitter.com/nlanjichi)

Project Link: [https://github.com/lupamo3/flask-crud/tree/master](https://github.com/lupamo3/flask-crud/tree/master)


