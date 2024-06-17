# Welcome to QuestHub!

![QuestHub mockup](docs/readme/questhub-mockup.jpeg)

Welcome to QuestHub, a web application that enables you to share your knowledge, ask questions and find answers! QuestHub empowers you to ask questions, find answers, and connect with like-minded individuals worldwide.

Visit live site: [QuestHub](https://django-portfolio-468596d338f0.herokuapp.com/)

# Table of Contents


## Features

### Existing Features:

#### Home Page:
![Home page](docs/readme/home.jpeg)
The home page displays a list of posts with the latest post shown first and a pinned post from the website owner displaying some rules. Each post shows the avatar of the person who has created the post along with information about when the post was created, last update, and how many comments it has. Opening any of the posts opens the corresponding post detail page. 
The search bar lets users filter posts to easily find what they're looking for.

#### Post Detail Page:
![Post detail page](docs/readme/post_detail.jpeg)
When i user opens a post to come to the post detail oage they can see the full contents of the post along with any comments it has.

Under each post theres a button for writing comments which will open up a form only if a user is logged in and if not a message will be displayed for the user to tell them to login or register an account.

The comments are sorted from oldest to newest in order. Under each comment theres a delete and edit button only if a the comment belongs to the logged in user (gives the user full CRUD capabilities), which makes it easy for a user to edit or delete the comments they make in a quick way.

#### Register/Login Page:
![Login page](docs/readme/login.jpeg)
The pages for account registration and user login are kept simple and clean and the designs are mostly from django allauth. New users can sign up using a username, email and a password, with all obligatory fields.

#### Profile Page:
![User Profile page](docs/readme/profile.jpeg)
On the profile page, an logged in user can write a bio and upload a profile picture if they want. There's also a button for deleting the account that opens up a deletion modal to confirm deletion. Users can also see a list of the posts and comments they have made with each one linking to its origin if opened.


#### About Page:
![About page](docs/readme/about.jpeg)
The About page of QuestHub is a brief description of the goal of the site, inviting everyone to join in the quest for knowledge and growth.

### Future Implementations:
In a potential future iteration:
- I'd like to add private messaging system.

- I'd also add a sorting system to search and post pages.

- A new view to add likes functionalities.

- Update the profile page so users can display there socials in an effective manner to build friendships with others easily.

### Defensive Design Features

## User Experience
### User Stories
|                                       ||                                                                                   |
| :-------------------------------------|--|:------------------------------------------------------------------------------------------- |
|**USER REGISTRATION**             |  ||
|                                       |  | As a user, I want to be able to register on the website|             
|                                       |  | Then the user can log in.|
|                                       |  | When the user is logged in they can comment on any post they want.|
|**POST/OPEN THREADS**   |  || 
|                                       |  | When a blog post title is clicked on a detailed view of the post is seen.|
|                                       |  | Given a logged in user, they can create a post.|
|                                       |  | Given a logged in user, they can read a post.|
|**MANAGE COMMENTS**                            |  ||
|                                       |  | Given a logged in user, they can comment on a post.|
|                                       |  | Given a logged in user, they can read a comment|
|                                       |  | Given a logged in user, they can update a comment they have made.|
|                                       |  | Given a logged in user, they can delete a comment they have made.|
|**USER PROFILES**                               |  ||
|                                       || As a logged in user, I get an automatic profile page when new account is registered.|
|                                       || As a site user, I can view the profile page for my account and others.|                                  
|                                       || As a site user, I can see my posts, comments and profile picture on my profile page.|
|**EDIT / DELETE PROFILE**                       |  ||
|                                       || As a logged in user, I can upload a profile picture.|
|                                       || As a logged in user, I can write a profile bio and update it.|
|                                       || As a logged in user, I can delete my own profile.|
|**POST PAGINATION**              |  ||
|                                       || Given more than one post in the database, these multiple posts are listed.|
|                                       || When a user opens the main page a list of posts is seen.|
|                                       || Then the user sees all post titles with pagination to choose what to read.|
---

### Agile Methodology
I used GitHub projects to manage this project's development stages using Agile methodology. You can see my iterations and project board to learn more.

 I added all the user stories to the Issues page and connected them to the project board. I kept iterations short and somewhat flexible. Each user story has a list of acceptance criteria and associated tasks, each one with a checkbox for easy tracking of progress.

 During the making of the project i decided some of the user stories was not as important to focus on during the scope of time to finsih the project and decited not to do them. I also created an excel sheet to more easily update and rewrite user stories. A user story i added that is not seen on the project board is the full CRUD functionality for comments. I also added a user stories for profiles so that i could easily keep track of what i wanted the functionalities to be.
![User Stories](docs/readme/user-stories.jpeg)


## Design
### Color Pallete
I decided to keep the color pallete very clean and stick with black and white. The only 'color' to the page would be user avatar images.

### Typography
For this site, I kept it simple with a clean sans-serif font across the whole site.

### Imagery
The site uses no imagery of its own and instead leaves the whole image space for users profile pictures.


### Wireframes
Before building the site, I made wireframes for all the main sites. When building the site i made some changes on the pages such as the layout on tablet screens to fit the design better.

Home Wireframe:
<details>
<summary>Desktop</summary>

![Wireframe](docs/readme/home-lg-wf.jpeg)
</details>
<details>
<summary>Tablet</summary>

![Wireframe](docs/readme/home-md-wf.jpeg)
</details>
<details>
<summary>Phone</summary>

![Wireframe](docs/readme/home-sm-wf.jpeg)
</details>

---
Post Details Wireframe:
<details>
<summary>Desktop</summary>

![Wireframe](docs/readme/post-lg-wf.jpeg)
</details>
<details>
<summary>Tablet</summary>

![Wireframe](docs/readme/post-md-wf.jpeg)
</details>
<details>
<summary>Phone</summary>

![Wireframe](docs/readme/post-sm-wf.jpeg)
</details>

---
Profile Wireframe:
<details>
<summary>Desktop</summary>

![Wireframe](docs/readme/profile-lg-wf.jpeg)
</details>
<details>
<summary>Tablet</summary>

![Wireframe](docs/readme/profile-md-wf.jpeg)
</details>
<details>
<summary>Phone</summary>

![Wireframe](docs/readme/profile-sm-wf.jpeg)
</details>



### Accessibility
### Database Schema
The database schema shows the structure of the database, the type and their relationship. This schema was done using [Lucid Chart](https://www.lucidchart.com/).

![Database Schema](docs/readme/db-schema.jpeg)


## Technologies Used
### Languages Used
### Frameworks & Libraries Used
### Other Technologies Used

## Deployment
### Heroku
### GitHub

## Testing
### Solved Bugs
### Unfixed Bugs

## Credits
### Media
### Tutorials & Code Used

