<a name="readme-top"></a>



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Lio-S/Projet_Satisfaction">
  </a>

<h3 align="center">The fly satisfaction project by ELF</h3>

  <p align="center">
    A programm to get more happy passenger, because life is a journey we want to make beautiful
    <br />
    <br />

  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#Relationnal Data Base creation and testing">Usage</a></li>
    <li><a href="#Trello link and Agile method">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This application is delayed to understand how a flight company can make happy passengers. It uses machine learning to predict passenger happyness according to features such as arrival delays, on board services, ease of check-in.<br>
<br>
It's a Simplon school project on 2+ days work. We made it carrefully, between three proud student of this great school !
Hope our product owners/teachers will be proud of us.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python-shield]][Python-url]
* [![Streamlit][Streamlit-shield]][Streamlit-url]



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these steps.
You'll need python to run this properly.

### Prerequisites

No prerequisites necessary here. Just follow instruction please.

### Installation


1. Clone the repo
   ```sh
   git clone https://github.com/Lio-S/Projet_Satisfaction
   ```
3. Install required packages
   ```sh
   pip install -r requirements.txt
   ```

4. CD into your /Projet_Satisfaction/ directory, and run the app inside your browser
   ```py
   streamlit run app.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Our application is divided in three tabs.

-Tab one : 'Tableau de bord, Prévision'

This is the functionnal part for the app's user. Here the user can adjust variable such as departure delay, travel classes and others to simulate a passenger experience.

After adjusting these parameters, the user should click the 'Prédire la satisfaction client' buton to let the prediction model evaluate the satisfaction of the simulated customer. Once the button is clicked, the user will get the answer about the prediction on passenger satisfaction.

-Tab two : 'Apprentissage'

The second tab is a summary of the machine learning model training. We use 'Random Forest' as a model to predict passenger satisfaction. The full dataset was splitted into train and test sample on a 80%, 20% subpart respectively. Details on features processing are as follow : 

Passenger ID = Removed, it is just random numbers with no impact on passenger satisfaction

delay = Sum of arrival and departure delay

Passenger travel classes = divided in three features for model training
gender = 0 for male; 1 for female

customer_type : 0 for disloyal customer; 1 for loyal customer

Tot = tipe of travel. Personnal travel : 0; Business travel : 1

flight distance = flight distance in km

iwservice = Inflight wifi service, scored by passenger from 0 to 5

da_time_convenient = Departure/Arrival time convenient, scored by passenger from 0 to 5

ease_online_booking = Ease of Online booking, scored by passenger from 0 to 5

gate_location = Gate location, scored by passenger from 0 to 5

food_and_drink = Food and drink, scored by passenger from 0 to 5

online_boarding = Online boarding, scored by passenger from 0 to 5

seat_comfort = Seat comfort, scored by passenger from 0 to 5

inflight_entertainmt = Inflight entertainment, scored by passenger from 0 to 5

on_board_service = On-board service, scored by passenger from 0 to 5

leg_room_service = Leg room service, scored by passenger from 0 to 5

baggage_handling = Baggage handling, scored by passenger from 0 to 5

chk_service = Checkin service, scored by passenger from 0 to 5

inflight_service = Inflight service, scored by passenger from 0 to 5

cleanliness = Cleanliness,scored by passenger from 0 to 5

-Tab two : 'Test et ajout de données'

The last tab will be used by user to upload more data and use them to train the machine learning model. The new data will be processed as the original data set to fit in our prediction assay.

Three data format are available here comma separated files (.csv), excel type files (.xl), and JSON files (.json)

Might still be buggy, you can [open an issue](https://github.com/Insiares/Projet-NLT/issues).


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- RELATIONNAL DATA BASE CREATION AND TESTING -->
### Relationnal Data Base creation and testing

As a part of the project we created a relational database. We decided to use a 'SQLite' Data Base due to the type of the project and the relative simplicity of the data we get. This database is made of a central table surrounded by five dimensionnal tables. 

Such as follow :

Genders = 1 : male, 2 : female

Customer_types = 1 : Loyal Customer, 2 : disloyal Customer

Type_of_travel = 1 : Personal Travel, 2 : Business travel

Classes =  1 : Eco plus, 2 : Business, 3 : Eco

Satisfaction = 1 : neutral or dissatisfied, 2 : satisfied

To create the Data Base, you must launch the program create_db.py, that will first use the data file 'data/Airline_Dataset.csv' to create a 'data/Airline_Dataset_to_BDD.csv' and create a fully operationnal SQLite Data Base.

If you want to test the Data Base, please, use the 'test/read_tbl_test.py' program that should make some reading og the data base and insure that jointures are properly working by reading the Data Base and assigning the proper values.

<!-- TRELLO LINK AND AGILE METHOD -->
## Trello link and Agile method

We did this job as Agile method experience. We first designed 'user stories' that you can overview at 'https://trello.com/invite/b/lW7lwk1i/ATTI28b223c31d2ae2532259531eea44cffc694C9DEA/the-plane-project-trello'. Then, we discuss two times a day our progress on the project, requesting advices and help from the whole team on specific topic. We did a planing poker to adjust amount of work needed for each of the user stories. We did our best to keep people in the team fully invested and to maintain a good organization.

<!-- ROADMAP -->
## Roadmap

- [x] Prototype
- [x] Exploring and processing data for Machine learning
- [x] Realational Data Base conception and creation
- [x] Machine-Learning effective prediction
- [X] Uploading New files functionality
- [X] User experience, prediction of passenger happyness
- [~] app log-in

See the [open issues](https://github.com/Insiares/Projet-NLT/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

We are up tu ear any suggestion, feel free to contribute !

Should the extrem necessity emerges, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".


1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
6. Leave Star on your way out !

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the Simplon students, we live in a free country ! 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Find us if you can.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Antony for the tortuous brief, and the helpful assistance !](https://github.com/DeVerMyst)
* [The whole group of Simplon Dev/IA group for discussion and exchange on the project]
* [The Simplon team, smiles and gentlyness !]

<p align="right">(<a href="#readme-top">back to top</a>)</p>
