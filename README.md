# Pokemon Team Creator
Application to log pokemon caught and their attributes for the SFIA project due Monday week 6 (9/12/2019) at QAC academy


## Index
[Brief](#brief)
   * [Solution](#solution)
   
[Architecture](#architecture)
   * [Entity Relationship Diagrams](#erd)
   * [Multi Tier Architechture Diagram](#mla)
	
[Testing](#testing)
   * [Report](#report)

     
[Deployment](#depl)
   * [Technologies Used](#tech)
     
[Front End Design](#FE)

[Improvements for the Future](#improve)

[Authors](#auth)

[Acknowledgements](#ack)

<a name="brief"></a>
## The Brief

To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training.

<a name="solution"></a>
### Solution

This application is designed to allow users to log recently caught pokemon and their attributes (ie movesets) with the intention of using these pokemon to form teams. 

Below are entailed a series of user stories for how the app may be used and their level of requirement according to a MoSCoW (Must, Shoud, Could, Would) scale.



|  | User Stories and their MoSCoW |
| ------ | ------ |
| MUST | As a trainer, I want to be able to add pokemon to my database so that I know what they are |
| MUST | As a trainer, I want to be able to add pokemon moves so that I know what moves are available and what their power is |
| MUST | As a trainer, I want to be able to view the pokemon and their movesets that I have entered |
| SHOULD | As a trainer, I want to be able to create a team out of the pokemon in the database so that I can use a preset team in gameplay |
| SHOULD | As a trainer, I want to be able to create multiple teams out of the pokemon in the database so that I can create teams for gameplay |
| SHOULD | As a trainer, I want to be able to delete teams when I no longer need them so that my team list does not become too cluttered |
| SHOULD | As a trainer, I want to see the pokemon in the my team so that I know what that team is good for |
| COULD | As a trainer, I want to see the movesets and damage of the pokemon in my team so that I can better see what my team is good for |
| COULD | As a trainer, I want to be able to see the theme (typing) of my teams so that I can easily select one for gameplay |
| COULD | As a user, I want to use an app that looks nice so that I can enjoy using it |


<a name="architecture"></a>
## Architecture
<a name="erd"></a>
### Entity Relationship Diagrams
#### Initial plan
![Initial ERD](/Documentation/ERD_Initial.jpeg)

The initial plan for the project, reflected in the ERD above, consisted of a lot more tables and entities than were produced in the final application. Given the time constraints and technical capability issues, I decided to narrow the range of the scope of the project and so started with a MVP (Minimum Viable Product), which has been created and so I only managed to deliver two tables plus a join, as shown below. 

#### Delivered solution
![Final ERD](/Documentation/ERD_Final.jpeg)

As shown in this ERD, the focus of the initial tables has been altered slightly to remove the team and move set additions. Simply due to time constraints and techinical limitations, I started to create the app more simply, with the intention of expanding it once the MVP was done. However, the MVP was only just completed in time (and with issues!) and so none of the stretch goals (the Could and Should of the MoSCow table) have been achieved.

<a name="testing"></a>
## Testing

Pytest unit testing has been used to test the web app, unfortunately, this is currently broken.


<a name="depl"></a>
## Deployment

A webhook linked to the GitHub feature branch (can also be linked to the master branch if desired) allows for the continouos building and deployment of the web app through a Jenkins server (hosted on a GCP instance), which is triggered whenever an update is pushed to GitHub.
An instance on the GCP cloud platform containing a mySQL instance hosted the database and was linked to another GCP instance hosting the Flask application. 

![Deployment Pipeline](/Documentation/CI_Pipeline.jpeg)
<a name="tech"></a>
### Technologies Used

* Google Cloud Platform VMs
* mySQL Instance on VCP - Database
* Python - Programming
* Flask - Web microframework
* Jenkins - CI Server
* Pytest - Unit Testing



### Final Appearance

<a name="improve"></a>
## Improvements for the Future

Currently, IDs are required to update poses and routines, and to add or remove poses from routines. In my next sprint, I would like to create buttons in the front end which allow this functionality without the need for IDs, which would allow the object IDs to be hidden from the user.

In later sprints, I would also like create a health-benefit entity which would have a many to many relationship with poses, so that users can create routines based on their focus for their practice. After this, I would add the capability to create different user accounts. At this point, I would remove the functionality for the user to add and remove poses themselves in the front end. These would instead be hard coded into the database, which the user could manipulate only for adding and removing them from their own routines.

<a name="auth"></a>
## Authors

Jelle Vinkenoog
