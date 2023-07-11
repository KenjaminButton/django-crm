# TodoList

- [x] Create virtual environment, install `django` and create project
- [x] Base pages/ templates

  - [x] Create app for pages
  - [x] Create base template
  - [x] Create front page
  - [x] Create ABOUT US page

- [x] Authentication

  - [x] Create DB model for userprofiles
  - [x] sign up functionality
  - [x] login functionality
  - [x] logout functionality
  - [x] Create DB model for userprofiles
  - [x] Create DB model for userprofiles
  - [x] Simple dashboard

- [x] Create new leads

  - [x] New Django App
  - [x] Set up Django models
  - [x] Create views and forms for leads
  - [x] Need page to list out all our leads
  - [x] View detail page of leads

- [x] Delete and edit leads
- [x] Convert leads to clients
- [x] Show all clients
- [x] Show details page of a client
- [x] Adding a client while skipping leads process
- [x] Edit and delete clients

- [] Implement solution for teams

  - [x] Create teams app
  - [x] Create model for teams
  - [x] When lead is created, guarantee that team is set
  - [x] When client is created, guarantee that team is set
  - [x] If user is logged in and not a member of a team, create one.
  - [x] If user is the owner, make it possible to edit team

- [x] Have dashboard list out "n" newest leads and "n" newest clients

  - [x] Implement feature where being a member of a team is necessary
  - [x] Limit # of leads (freemium of max n leads)
  - [x] Limit # of clients (freemium of max n clients)

**Refactoring**

- [x] Install Tailwind and stop using CDN
- [x] Add name spaces to all "apps"
- [x] Replace show leads with class based view
- [x] Replace leads detail with class based view
- [x] Replace leads delete with class based view
- [x] Replace leads edit with class based view
- [x] Replace leads add with class based view
- [x] Replace convert leads to client with class based views

- [x] add comments for leads and clients
- [x] export info for leads and clients
- [x] leads and clients connection
- [x] Upload files to leads and clients

- [x] Replace the dispatch with loginrequiredmixin
- [x] Show active team in menu
- [] Team detail page with member list
- [] Clean up base.html with includes
- [] Fix styling for login and signup

- [] Implement a payment solution / Monthly recurring payments
- [] Deploy

1. To activate virtual environment, `source django.env/bin/activate`
2. To start app on dev server, `python3 manage.py runserver`

**Need to install tailwind and disregard CDN upon deployment**
[Tailwind CSS CDN](https://tailwindcss.com/docs/installation/play-cdn)
