# Python Hybrid Framework
<h3> What is Framwork?

Framework is an organising way of maintaing the files.In the Framework all the files will communicate with each other to perform certain tasks.

<h4>Objectives:

- Reusability
- Maintainability

<h4>Types:

1) Built in Frameworks: Pytest, robotFramework, Unittest
2) Customiozed or User Defined Framworks:
Data driven Framework, Heyword Driven Framework, Hybrid driven Framework

<h4>Steps:

- Analyse the Application, technology and skill set of the team, choose test cases.
- Design and Implementation of the framework
- Execution of the test cases in jenkins or local or particular test cases.
- Maintainance (version control system)

E-Commerce Applications:
- Frontend : demo-nop-commerce.com
- Backend: demo-nop-commerce.com /customers module.

<h4>Note:We can execute the test cases based on the markers amoung all the test cases
- cmd : pytest -s -v -m "sanity" --html-./reports/report.html testcases/ --browser chrome 
output : collecting x items x eselected x item selected 

<h3>Git Tutorials:

1) Create a Local git Repository - git inti //create a local repository
2) git remote add origin url // connect local repository with global repository
3) setup git global configs : git config --global user.email "xyz@gmail.com" and git config --global user.name "xyz"
4) git add 
5) git status 
6) git commit -m "text msg"
7) git push -u origin brance_name


<h3>Jenkins Guidelines</h3>

1) Install the jenkins from the official website //download jenkins.war files
2) Install the java from the oracle java 
3) install the suggested plugins
4) go to cmd and select the run as admistrator option of the cmd 
5) run cmd : java -jar jenkins.war
6) set up the admistrator or admin details.
7) open the jenkins go to new items and enter an item name and select the freestyle project 
8) select git and go to the source code option






 
