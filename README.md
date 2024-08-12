# The Globetrotter's Gazette
## Introduction

Welcome to the Globetrotter's Gazette, a place to share your travel experiences from all around the world. Read posts from all different countries, share these posts, even join in the conversation by leaving a comment! This is a community for globetrotter's alike to come together and share their love of travelling.

This website is made using the Django framework, alongside HTML, CSS, Javascript and Python. This is the 4th project in the Full Stack Software Development Diploma from Code Institute.

## User Experience (UX)

Development of this blog site was done using the five planes of UX as guidance. Below are the details listed for each plane.

### The Strategy Plane

The goal of 'The Globetrotter's Gazette' is to create an online community for people who love to travel, allowing them to share their experiences with each other. Users can create blog posts to share with others and can also search for other blog posts of their interest.

#### Business Needs

- Create a website for people to share their travel stories
- Allow travellers - novice and experienced - to get inspiration for their next trip

#### User Needs

- Blog about my travels to be able to store my memories online
- Read about others' experiences to get ideas for my next holiday/ expand my knowledge
- Engage with others and their travels by commenting on posts
- Be able to create an account to leave comments
- Be able to create an account to create my own posts

### The Scope Plane

#### Epics

7 epics were generated for this project, which were further broken down into user stories before starting development. Each epic and their related user stories can be seen on my [project board](https://github.com/users/mariam138/projects/6/views/1).

**Epic [1](https://github.com/mariam138/globetrotters-gazette/issues/2)**: Initial Django Setup  
**Epic [2](https://github.com/mariam138/globetrotters-gazette/issues/3)**: User Authentication  
**Epic [3](https://github.com/mariam138/globetrotters-gazette/issues/4)**: User Profile  
**Epic [4](https://github.com/mariam138/globetrotters-gazette/issues/5)**: User Travel Posts  
**Epic [5](https://github.com/mariam138/globetrotters-gazette/issues/6)**: Searching Travel Posts  
**Epic [6](https://github.com/mariam138/globetrotters-gazette/issues/7)**: Admin Profile  
**Epic [7](https://github.com/mariam138/globetrotters-gazette/issues/8)**: User Interaction  

#### User Stories

The seven epics listed above were split down further into user stories to help with the development of the project. User stories were labelled using **MoSCoW Prioritisation**. User stories were also labelled with story points, based on relative effort. For each iteration, a **milestone** was created to keep track of user stories. **Must have** stories were worked on first during each iteration, followed by **Should have** and finally **Could have**. User stories labelled with **Won't have** remained in the [Back log](https://github.com/mariam138/globetrotters-gazette/milestone/1) milestone. Any user stories that were start but not completed at the end of the iteration would be prioritised first in the next iteration. Below is a list of completed user stories, categorised by their respective epics:

##### **Epic [1](https://github.com/mariam138/globetrotters-gazette/issues/2)**: Initial Django Setup
- [#9](https://github.com/mariam138/globetrotters-gazette/issues/9#issue-2388350667) Initial Django Setup
- [#10](https://github.com/mariam138/globetrotters-gazette/issues/10#issue-2388393796) Connect Database to Django Project
- [#11](https://github.com/mariam138/globetrotters-gazette/issues/11#issue-2388393796) Create Environment Variables
- [#56](https://github.com/mariam138/globetrotters-gazette/issues/56#issue-2388393796) Deployment of Blog

##### **Epic [2](https://github.com/mariam138/globetrotters-gazette/issues/3)**: User Authentication
- [#13](https://github.com/mariam138/globetrotters-gazette/issues/13#issue-2388393796) Log into Site
- [#61](https://github.com/mariam138/globetrotters-gazette/issues/61#issue-2388393796) Register for Site
- [#14](https://github.com/mariam138/globetrotters-gazette/issues/14#issue-2388393796) Log Out of Site

##### **Epic [3](https://github.com/mariam138/globetrotters-gazette/issues/4)**: User Profile
- [#16](https://github.com/mariam138/globetrotters-gazette/issues/16#issue-2388393796) Create User Profile
- [#17](https://github.com/mariam138/globetrotters-gazette/issues/17#issue-2388393796) View User Profile
- [#18](https://github.com/mariam138/globetrotters-gazette/issues/18#issue-2388393796) Edit User Profile
- [#63](https://github.com/mariam138/globetrotters-gazette/issues/63#issue-2388393796) Upload Profile Picture
- [#59](https://github.com/mariam138/globetrotters-gazette/issues/59#issue-2388393796) View Own Posts
- [#19](https://github.com/mariam138/globetrotters-gazette/issues/19#issue-2388393796) Delete User Account

##### **Epic [4](https://github.com/mariam138/globetrotters-gazette/issues/5)**: User Travel Posts
- [#23](https://github.com/mariam138/globetrotters-gazette/issues/23#issue-2388393796) Read Blog Posts
- [#22](https://github.com/mariam138/globetrotters-gazette/issues/22#issue-2388393796) Create Travel Posts
- [#57](https://github.com/mariam138/globetrotters-gazette/issues/57#issue-2388393796) Upload Pictures to Blog Posts
- [#24](https://github.com/mariam138/globetrotters-gazette/issues/24#issue-2388393796) Edit User Posts
- [#25](https://github.com/mariam138/globetrotters-gazette/issues/25#issue-2388393796) Delete User Posts

##### **Epic [5](https://github.com/mariam138/globetrotters-gazette/issues/6)**: Searching Travel Posts
- [#29](https://github.com/mariam138/globetrotters-gazette/issues/29#issue-2388393796) View Paginated List of Posts
- [#28](https://github.com/mariam138/globetrotters-gazette/issues/28#issue-2388393796) Group Posts by Country/Region
- [#64](https://github.com/mariam138/globetrotters-gazette/issues/64#issue-2388393796) Search for Posts
- [#55](https://github.com/mariam138/globetrotters-gazette/issues/55#issue-2388393796) Display Travel Pictures on Home Page
- [#67](https://github.com/mariam138/globetrotters-gazette/issues/67#issue-2388393796) Create 404 Page

##### **Epic [6](https://github.com/mariam138/globetrotters-gazette/issues/7)**: Admin Profile
- [#33](https://github.com/mariam138/globetrotters-gazette/issues/33#issue-2388393796) Create Admin Profile
- [#34](https://github.com/mariam138/globetrotters-gazette/issues/34#issue-2388393796) View Admin Profile
- [#35](https://github.com/mariam138/globetrotters-gazette/issues/35#issue-2388393796) Edit Admin Profile
- [#42](https://github.com/mariam138/globetrotters-gazette/issues/42#issue-2388393796) Moderate Comments
- [#39](https://github.com/mariam138/globetrotters-gazette/issues/39#issue-2388393796) View About Page
- [#38](https://github.com/mariam138/globetrotters-gazette/issues/38#issue-2388393796) Create About Page
- [#40](https://github.com/mariam138/globetrotters-gazette/issues/40#issue-2388393796) Update About Page

##### **Epic [7](https://github.com/mariam138/globetrotters-gazette/issues/8)**: User Interaction
- [#43](https://github.com/mariam138/globetrotters-gazette/issues/43#issue-2388393796) Create Comments
- [#44](https://github.com/mariam138/globetrotters-gazette/issues/44#issue-2388393796) View Comments
- [#45](https://github.com/mariam138/globetrotters-gazette/issues/45#issue-2388393796) Edit Comments
- [#46](https://github.com/mariam138/globetrotters-gazette/issues/46#issue-2388393796) Delete Comments

### The Structure Plane

For the structure, I briefly created a simple site map. This allowed me to make sure there was flow throughout the design of the website, and that the correct pages linked together. This was created before the creating each page and was used as a template. The site map was created using **Lucidchart**.

![Sitemap of Globetrotter's Gazette](static/images/globetrotter-gazette-site-map.jpeg)

ERD diagrams were created to plan out the models to be used in the project. I settled on 3 models: a **Post** model, a **Comment** model and a **Profile** model. Below shows the database schema and the relationships between the models.

![ERD's for database](static/images/gg-erd.jpeg)

The ERD diagram was created using [Lucid Charts](https://lucid.co/).

### The Skeleton Plane

To create the skeleton of the website, I created wireframes using **Balsamiq**. Alternate versions were created in the application, as for some pages I wasn't entirely certain on the final layout. Listed below are the **final** versions of the wireframes used to create the layout of the website on desktop, tablet and mobile.

### The Surface Plane

#### Colour Scheme

The colour I wanted to choose to be the main standout colour was a bluey-gree, akin to the rivers or seas. After picking the colour `#35797e`, I then decided to generate a colour palette appropriate for a website using [Colormind](colormind.io/bootstrap). Setting `#35797e` as the main colour, the below palette was generated.

![Colour palette screenshot](static/images/colour-palette-screenshot.png)

I then went to check the accessibility of these colours to ensure they were visible to all readers. I liked the light `#F3EDF2` colour, so checked to see if the main colour `#35797e` would get a **AAA** rating according to the WGAC contrast. Using this [accessible colour generator](https://www.learnui.design/tools/accessible-color-generator.html), a darker main colour `#06585d` was given instead. So I decided to regenerate the palette.

![Second colour palette screenshot](static/images/colour-palette-2-screenshot.png)

I checked the accessibility of the white and black colours against the blue shades using the [EightShapes Contrast Grid](https://contrast-grid.eightshapes.com/?version=1.1.0&background-colors=&foreground-colors=%23FFFFFF%2C%20White%0D%0A%23F2F2F2%0D%0A%23DDDDDD%0D%0A%23CCCCCC%0D%0A%23888888%0D%0A%23404040%2C%20Charcoal%0D%0A%23000000%2C%20Black%0D%0A%232F78C5%2C%20Effective%20on%20Extremes%0D%0A%230F60B6%2C%20Effective%20on%20Lights%0D%0A%23398EEA%2C%20Ineffective%0D%0A&es-color-form__tile-size=compact&es-color-form__show-contrast=aaa&es-color-form__show-contrast=aa&es-color-form__show-contrast=aa18&es-color-form__show-contrast=dnp). The following graph shows all of the passing **AAA** colours.

![Accesibility contrast grid](static/images/accessibility-contrast-grid.png)

As all of the shades passed with **AAA**, I settled on these colours as my final colour palette.

#### Typography

For fonts, I started out choosing a font for headings. I used [Fontjoy](https://fontjoy.com/) to generate random fonts at first. I came across the font **Raleway** and liked that it was simple and clean, so decided on that for my headings. Then I searched up the **Raleway** font on [typ.io](https://typ.io/) to get suggestions for a font I could use for my paragraphs that pair well with **Raleway**. After looking at a few options, I decided on using **Cabin**. I chose it for it's similarity to **Raleway** in that it was also clean and easy to read, as I was also taking accessibility into consideration with my fonts. Below is a picture of the two fonts side by side, with the image taken from **Fontjoy**.

![Font pairing image](static/images/font-parings-image.png)

## Features

### Home Page

![Home page](static/images/home-page-signed-out.png)

On the Home page is a picture of Helsinki Cathedral as the Hero image. Underneath is some welcome text, followed by an image carousel with pictures of different cities from around the world. The pictures cycle automatically after the first click from a user.

### Navigation Bar

The navigation bar contains the website's name, followed by links to 'Home', 'About' and a dropdown list for 'Regions'. There is also a search bar which gets posts related to the query entered by the user. To the right hand side are 'Sign In' and 'Register' buttons if the visiting user is logged out/ not signed up. On smaller screens, the logo text compresses to its initials 'GG' to avoid taking up too much vertical space on the screen. The navigation links are condensed into a drop down menu which appears when clicking on the menu icon.

![Navbar when logged in](static/images/nav-bar-logged-in.png)

When a user logs into the site, the links in the navbar extend to add 'Create Post' and 'My Profile' links. 'Create Post' allows the user to create a post at any point when visiting the site as it is easily accessible in the navigation bar. The 'My Profile' link takes the user to a page which displays their information to them, and how other people will view their information when they visit their profile. The buttons to the right change to show just the 'Sign Out' button instead. On the home page only, some text appears in the bottom right corner displaying to the user that they are logged in, with their corresponding username.

### Footer

![Footer](static/images/footer.png)

The footer is kept basic, with just some icons for social media including Facebook, Instagram and X. Each icon is a link which will open the respective social media site in a new tab. The footer is a sticky footer, so it is stuck at the bottom of the page but only appears when the user scrolls down to it (if the content on the site is scrollable).

### Sign In Page

![Sign In Page](static/images/sign-in-page.png)

The Sign In page styling is extended from the base styling of the project, and overwrites the template given by Django AllAuth. If a user hasn't signed up to the website, a link is visible above the form which redirects them to the Register page. The sign in form is kept simple with just a username and password, and a checkbox allowing the user's log in details to be remembered. Once signed in, the user is redirected back to the index page and a message is displayed at the top indicating that the sign in was successful. If incorrect/non-existent credentials are entered, the sign in page reloads and displays an error message at the top, telling the user what the specific error is.

### Sign Out Page

![Sign Out Page](static/images/sign-out-page.png)

When a user clicks the 'Sign Out' button in the top right corner, they are redirected to a page which asks them to confirm their action. They will then click the 'Sign Out' button again which redirects them back to the index page with a message appearing at the top telling them that sign out was successful.

### Register Page

![Register Page](static/images/register-page.png)

If a user clicks or is redirected to the Register page, then a registration form is loaded. If a user already has an account, they have the option to sign in using the link above the form. The form asks for a username, an e-mail and a password. Some information text about the user's password is displayed below the form. Any errors in the form are displayed at the top of the page, such as a username already being taken or that the passwords do not match. Once registered, the user is redirected to the index page where they get two messages: one telling them they have signed in successfully, and another telling them that a verification e-mail has been sent to them. Although in this project I have made verification optional, in a real world setting this would be mandatory. Upon registering, a simple profile is made for the user from the username and e-mail given.

### Profile Page

![Profile Page](static/images/profile-page.png)

When a user clicks on the 'My Profile' link in the nav bar, they are taken to a page which fully displays their profile information. The profile page includes: a profile picture, name, birthday, e-mail (only visible to the logged in user), a bio, instagram and X link. Upon initial registration, the email field is automatically populated. The user can then click to edit their profile, view all their own posts or delete their account. If a user is viewing a profile other than their own, the only button available to them is the 'View Posts' button. The 'Edit Profile' button takes them to a page which has a profile form allowing them to upload a profile picture and edit some of the fields. Pressing 'Delete Account' will trigger a modal to appear asking them to confirm their action. If the user confirms their action, their profile is deleted and they will no longer be able to sign in. 

### Future Features

1. User Story [#65](https://github.com/mariam138/globetrotters-gazette/issues/65): On top of searching for posts on the blog site, I would like to include being able to search for people's profiles too. This would include making a view for a profile list and creating cards for each person's profile that would include their basic information such as their profile picture, username and name. 

2. User Story [#66](https://github.com/mariam138/globetrotters-gazette/issues/66): Although a user is able to view all their posts from their profile page, including drafts and unapproved posts, I would like to add a feature for when a user is creating a post, they can quickly access a list of their drafts from that page as well. I would like to introduce it as a drop down list which is prepopulated from the database, and then if a user chooses a draft to continue editing, then the draft information is pre-populated into the 'Create Post' form.

3. User Story [#58](https://github.com/mariam138/globetrotters-gazette/issues/58): An additional feature to be added to the 'About' page would be an interactive map which has pins for all the places I have travelled to. Each pin could maybe then also have links to posts I have written for that area. This could also be extended to the blog site in general where an interactive map could be pinned with each pin linking to all blog posts by all users about that particular place. Using Google Maps API would be how I could implement this feature.

4. User Story [#48](https://github.com/mariam138/globetrotters-gazette/issues/48): Being able to like a blog post is another feature I would like to incorporate. Then allowing the user to access all their liked posts in one place, much like Instagram's 'like' or 'bookmark' features. This would maybe be implemented using Javascript, so that if a 'like' button was clicked, the blog post could then be added to a list of other liked posts. Then I would create a link on the user's profile or in the Nav bar to access all these liked posts in one place.

5. A feature I would have liked to implement was making a user's name mandatory in the sign up process, allowing the name field in their profile to be automatically filled in alongside the username and e-mail. To do so I would have to add an extra field for the name in Django AllAuth's registration field, and then using signals, make sure this field is pre-populated in the profile. However, I ran out of time to implement this feature.

## Bugs

1. While writing the code to edit a user's profile, I came across an *Integrity Error* when trying to save the model in the **edit_profile** view. Below is the detailed message of the Integrity error:

    > DETAIL: Key (user_id)=(13) already exists.

    I found a solution on the following [Google Groups](https://groups.google.com/g/django-users/c/Pq-3UatNP60?pli=1) post. As I had set up my **user** field in my **Profile** model as a **one to one** relationship, adding `primary_key=True` helped to fix the duplicate key value issue.

2. I wanted to implement client-side uploading of profile images for users to upload and change their profile image as part of CRUD functionality. I used the **Django Crispy Forms** package to quickly create a form based on the **Profile** model I had created. This created a simple *'Upload'* form field for a user to upload their profile picture. When the button was clicked, it lead to opening the user's own local files to choose a picture from. I wanted to include **Cloudinary**'s file upload widget for a better UI, so followed the steps to implement this. This all worked, except that when clicking the *'Choose files'* button, it would trigger **both** the local files on the user's computer to open, followed by the Cloudinary widget. Initially to overcome this, I tried to change the default widget that Crispy Forms rendered by creating a **CloudinaryFileInput** class which inherited from Django's **ClearableFileInput** class, which then would render a `<button>` element instead. I did this so that the local computer storage wasn't triggered to open when clicked. However, this didn't seem to work. In the end I found it difficult to implement the Cloudinary Upload widget with the pre-rendered Crispy Forms Profile Form, so changed route and tried to do a direct upload to the Cloudinary server without using the Upload widget. At first, any picture uploaded would not save to Cloudinary. I imported the *'CloudinaryFileField'* class into my **forms.py** file to then specify that the upload would be a Cloudinary file. Although this helped, whenever I tried to then upload a picture, the error message set up using Django's messaging framework would appear. After searching for why this was occurring, it turned out to be that I had not added the **enctype** attribute to my ,<form>, element. Once adding that, I could finally upload pictures to Cloudinary and have them appear on a profile page.

3. While creating the *Profile* model and it's functionality, I managed to get all of it working in the local server with no status errors. However, after a manual deployment, I came across a **Server 500** status code when trying to click on the *'My Profile'* link in the navbar when logged in. This error had not shown at all during local development. To be able to get a full trace of the error which was more detailed than the *Heroku logs*, I added my email into an **ADMINS** variable in **settings.py**. This allowed detailed errors to be e-mailed to me everytime the error occured. After setting all the desired email configurations, I tried to send test emails and access the deployed site to see if the e-mails would send. However, I could not get the emails to send. I initially set up my **Gmail** to be the receiver, but even when testing a sent email using python, I got the following error message:

        `smtplib.SMTPSenderRefused: (530, b'5.7.0 Authentication Required. For more information, go to\n5.7.0  https://support.google.com/mail/?p=WantAuthError 5b1f17b1804b1-427f941377csm117778905e9.48 - gsmtp', 'webmaster@localhost')`

    I read on several websites that I should allow access to less secure apps for my Gmail, but found that this option was only accessible to administrator accounts. As it was a personal account, and I did not have an administrator account, this method did not work in the end. I tried to overcome this by using my **Yahoo** mail account instead. However, even after following the same steps to set it all up, when sending a test email, I would get the following error:

        `smtplib.SMTPSenderRefused: (554, b'Email rejected', 'XXXX@yahoo.co.uk')`

    After checking all my configurations were correct using different websites as resources, I found that I came to a dead-end with using my own email to receive the traces as they would block emails sent from Django.

    Another alternative I found was to use [**Sentry**](sentry.io) and set it up with my Django application. Following the docs to install it with regards to Django, I was able to receive email alerts and also view specific errors and their tracebacks on the Sentry dashboard. However, I found that I couldn't get this to work for the deployed site. While testing Sentry in the deployed site, I found that I had accidentally pushed my project with **Debug** set to `True` rather than False. So when accessing the profile page, I managed to get a detailed error and traceback. I received a **ValueError**:

        `ValueError at /profile/mariam138/ Must supply cloud_name in tag or in configuration`

    This caused me to go back and check my configuration for Cloudinary. I reread through the installation documentation to check how I had configured my Cloudinary URL. It appeared that when I had set up a new cloud in my Cloudinary console, I didn't update my Cloudinary URL to contain the new API secret key. Updating the URL to the correct value fixed the issue, allowing me to properly access the profile page on the deployed site.

4. For a user editing their profile or creating a post, I decided to integrate the **Summernote** WYSIWYG editor into my project, as suggested in the Code Institute **I Think Therefore I Blog** runthrough. However, I continuosly ran into issues with it, despite following the documentation. It was unclear from the Django Summernote docs that summernote relies on jQuery, which I had not initially installed in this project in favour of using plain Javascript. Also, as I was using Bootstrap 5 over the older versions which states in the documentation that BS5 no longer relies on jQuery to work. So upon initialisation of the Summernote editor, I found that some of the drop down menus in the toolbar would not open when clicked on. Opening the DevTools showed that the jQuery syntax was not being recognised. So I installed jQuery into my project to hopefully solve the problem I was facing with the editor. However, even after including the CDN link, and fiddling around with the order of all the CDN links for dependencies, I struggled to get the editor to respond properly. Furthermore, as I was using **Crispy Forms** in my project to render any forms created from my models, the Summernote documentation recommends setting `iframe: False` in the configuration. However, this just caused the widget to not appear at all in both the admin and client side pages. I also struggled to find proper information on which versions of Summernote, jQuery and Bootstrap were all compatible in the end. For this reason, I decided to choose a different WYSIWYG editor called **Quill**.

5. For registration, I used the **Django AllAuth** package. I configured the settings so that e-mail is required for registration. I set verification as `'optional'` so that a user can continue to use the site upon registering. E-mail verifications are still sent out with this setting. In the local development server, this worked with no issues. However, when testing on the deployed site, once a user registered, a **500** server error was thrown. But the user, if they navigated back to the site, was still able to sign in. As I had set up a separate email account for testing, I checked the inbox to see that no e-mail had been sent. To debug this, I set up **Sentry** to my deployed app via Heroku and registered again. This gave the following error:

    ![Sentry E-mail Error](static/images/sentry-email-error.png)

    It turns out that the issue was because in my local settings, I had set up `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` using environment variables set in my **env.py**, but I hadn't set these same variables in Herko's *Config Vars.* After adding them to the Config Vars and attempting registration again on the deployed site, I was redirected back to the home page as expected with messages appearing to say registration was successful and an e-mail had been sent. I also checked the inbox of my test account and had received the email.

6. Another bug I came across during development was when I was attempting to run my automated tests. My tests wouldn't run as I would continuously come across this error:

    ![Testing Error](static/images/testing-error.png)

    Researching what the error meant was difficult but I understood that it could have been an issue with my database models. I had already tried to fix these errors by ensuring any model field which had a `CharField` had a `max_length` set. But this still didn't solve the issue and I kept coming across the same error. After talking to tutor support, we found that it was because my initial migrations of my models did not have the `max_length` attribute set which causes errors in SQLite3, but not PostgreSQL. It was decided that we would reset the migrations to have the initial 0001 migration as the current models I had created, but there still seemed to be a mismatch between the two databases. In the end, I had to resort to moving my data to a new database by creating a `.json` file to dump the data into and then reload it into the new database. This worked, allowing both the PostgreSQL database to work as expected, and the SQLite3 testing database to also work without throwing the error above.

7. I had a common bug with both my *About* and *Profile* pages where no information from the database was displaying. For example, the profile page as seen below:

    ![Profile page not displaying any info](static/images/about-page-error.png)

    Although it had been displaying information previously, near the end of my project however, these pages both started displaying blank. For the profile page, with the help of tutor support I ended up changing the URL from `profile/<str:username>` to just `profile/`. With debugging print statements in my `profile_page` view, I had correctly retrieved the profile instance from the database, but this was not being correctly passed through to the template, making the change to the URL, instead getting the profile instance based on `request.user`. However, the same issue was occurring on the *About* page, despite the URL being configured to simply `/about/`. In the view, I had named my instance `about`, which again - with print statements - showed the instance was correctly being retrieved from the database. But in the template, `{{ about }}` was showing up as `/about/` and `{{ about.title }}` was showing as `/About/`. This showed to be similar to the URL path I had found. Looking into it, I found that there was a conflict between the URL and the instance name. When I changed the instance name to `about_detail` and updated this accordingly in the template, all the information showed properly. I concluded that this must have also been the reason that no information was displaying on my profile page, as the URL in the project URLs file was named `/profile/` and I had also named the instance in the view `profile`. 


## Testing

### Code Validation

#### Javascript

All Javascript files were validated using [JSHint](https://jshint.com/), adjusting the configuration for ES6 Javascript.

- Validation for `comments.js`:
![Screenshot of comments.js validation](static/images/comments-js-validation.png)
    I chose to ignore the comment about `bootstrap` being an undefined variable due to using Bootstrap's Javascript in my `base.html` template. No other errors were found.

## Technologies

Several technologies were used in creating this blog site.

### Planning

- Balsamiq Wireframes - used to create wireframes for the skeleton plane
- Lucidchart - used to create the site map for the scope plane
- (Mockaroo)[mockaroo.com] - used to create my own mock data to use as django fixtures for blog posts

### Frameworks

- Bootstrap - to help ease the creation of the visual design of the website
- Django

### Django Libraries

- AllAuth
- Gunicorn
- Psycopg2

### Other Python Libraries

- Cloudinary - for media storage for the website
- Dj-database-url - to parse database url's in the project settings

## Deployment

The final project was deployed using Heroku via these steps:

1. Sign in to Heroku
2. Click *'Create New App'* located at the top of the dashboard
3. Create a unique app name
4. Choose 'Europe' as the server
5. Click *'Create App'*
6. On the app's dashboard, click on *'Deploy'*
7. Click **Github** for the deployment method
8. Search for repository and connect to it on Heroku
9. Click on *Settings* on the app dashboard
10. Scroll down and click on *'Reveal Config Vars'*
11. For initial deployment, insert the following key:value pairs:
    - DATABASE_URL : *<database_url>*
    - SECRET_KEY : *<secret_key>*
    - DISABLE_COLLECTSTATIC : *1*
12. Click on *'Deploy'* to go back to the deploy tab
13. Scroll down to *Manual deployment*
14. Ensure the *'main'* branch is selected
15. Click *'Deploy Branch'*

### Forking the repository

A fork of this repository can be made to add your own changes **without** affecting the original repository. This can be done via the following steps:  
1. Click on the repository name
2. Click the *Fork* dropdown menu
3. Select *Create a new fork*
4. Rename the repository name if you wish
5. Click on *Create fork*

### Cloning the repository

You can clone this repository to create a remote copy on your local machine. This can be done via the following steps:  
1. Navigate to the repository on Github
2. Click the *'<> Code'* button at the top of the repository page
3. Copy the URL for repository
    - For HTTPS, copy the URL under the *HTTPS* section
    - For SSH, copy the SSH Key under the *SSH* section
    - For Github CLI, click the button next to the URL under the *Github CLI* section
4. Open a new terminal in your coding space
5. Type `git clone` followed by the URL that has been copied
6. Press *'Enter'* to create your local clone

## Code Adaptations

### Documentation

- Throughout the creation of this project, I referred to the [Django documentation](https://docs.djangoproject.com/en/4.2/) with regards to **models**, **views**, **forms** and **signals**. These have been referenced throughout the code.
- I referred to the [Cloudinary documentation](https://cloudinary.com/documentation/django_integration) throughout the project also, especially in creating the **photo upload widget** and it's parameters. This code has been referenced throughout.
- In my forms, I used the **Django Summernote** WYSIWYG editor for text fields to allow for custom editing. Installation and use was adapted from the [Django Summernote documentation](https://github.com/summernote/django-summernote)
- For styling, I used **Bootstrap 5** as my framework, using the [documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/) for any adaptations of code.
- I used **Django AllAuth** to help with user authorisation and creation. Basic installation and settings were done with help from the [AllAuth documentation](https://docs.allauth.org/en/latest/#)
    - I used [this post](https://dev.to/gajesh/the-complete-django-allauth-guide-la3) for further help understanding settings when setting up AllAuth


### Other adaptations

- Code to create a date picker widget when editing a user's profile is adapted from the [Django Forums](https://forum.djangoproject.com/t/cant-change-type-attribute-in-django-crispy-forms/10054)
- Code to fix duplicate key value when saving instances of the **Profile** model is adapted from [Google Groups](https://groups.google.com/g/django-users/c/Pq-3UatNP60?pli=1)
- Code to use signals to create a **Profile** model when a **User** model has also been created is adapted from [this post](https://dev.to/earthcomfy/django-user-profile-3hik) on **dev.to**.
- Code to prepopulate a slug field from the client side was adapted from [this post](https://stackoverflow.com/questions/55314246/pre-populate-slug-field-into-a-form-field-of-a-django-site) on Stack Overflow
- Code to add Cloudinary's image URL to the Post model from the upload widget was adapted from [this post](https://stackoverflow.com/questions/61153317/how-to-get-the-cloudinary-widget-image-info-on-upload) on Stack Overflow
- Code to define the `get_queryset()` method for my **UserPostList** view was adapted from [this post](https://stackoverflow.com/questions/66511758/can-you-pass-an-argument-to-listview-in-django) on Stack Overflow, with help from the Django documentation for dynamic filtering
- Code to edit and delete comments using Javascript was adapted from [Code Institute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101_WTS+4/courseware/713441aba05441dfb3a7cf04f3268b3f/21a16093c0084895a6073422447c3f7d/)
- Code to dynamically create a sibling element in Javascript was adapted from the [MDN Webdocs](https://developer.mozilla.org/en-US/docs/Web/API/Element/after)
- Code to call Django URLs using Javascript was adapted from [this post](https://stackoverflow.com/questions/37311042/call-django-urls-inside-javascript-on-click-event) on Stack Overflow
- Code to allow user to search for posts using Django's Q filter was adapted from [LearnDjango](https://learndjango.com/tutorials/django-search-tutorial) and [this post](https://stackpython.medium.com/django-search-with-q-objects-tutorial-9c701db74e0e) on Medium
- Code to get the profile picture from the Profile model and use it in the About model was adapted from [this post](https://stackoverflow.com/questions/60987626/django-how-to-use-one-field-from-one-model-to-another-model
) on Stack Overflow
- Code to allow emails to be sent for verification upon registering was adapted from [Dorian Szafranski](https://medium.com/@dorianszafranski17/email-register-confirmation-django-django-allauth-299c4427726f) on Medium
- Code to find the corresponding label of a form input in Javascript is adapted from [this post](https://javascript.plainenglish.io/how-to-find-the-html-label-element-associated-with-a-given-input-with-javascript-486d15710591) on Medium
- Code to get a specific item in a Node list in Javascript is adapted from the [MDN WebDocs](https://developer.mozilla.org/en-US/docs/Web/API/NodeList/item)

## Media Credits

- Main index image of Helsinki Cathedral is from [Vish Pix](https://www.pexels.com/photo/cathedral-over-buildings-in-helsinki-23227693/) on Pexels
- Carousel images on index page are all from **Pexels**:
    - **Dubai**: Photo by Nextvoyage: https://www.pexels.com/photo/city-buildings-during-sunset-1470502/
    - **Cairo**: Photo by Dimitra M.K: https://www.pexels.com/photo/cityscape-of-cairo-with-the-nile-in-the-center-20840204/
    - **Osaka**: Photo by Amy Chandra: https://www.pexels.com/photo/low-angle-photography-japan-buildings-1020769/
- FAVICON
- Blog post pictures are taken from Pexels
    - **Paris** photo - Photo by Elina Sazonova: https://www.pexels.com/photo/eiffel-tower-behind-buildings-1850619/
    - **Stockholm** photo - Photo by Eleanore Stohner: https://www.pexels.com/photo/baroque-buildings-in-stockholm-old-town-square-17555989/
    - **Manila** photo - Photo by jon manosca: https://www.pexels.com/photo/skyline-of-makati-city-in-manila-philip-11076203/
    - **Indonesia** photo - Photo by Nuh Rizqi: https://www.pexels.com/photo/man-standing-beside-black-motorcycle-1237087/
    - **Shanghai** photo - Photo by Manuel Joseph: https://www.pexels.com/photo/city-with-skyscrapers-19885/
    - **Amethysts in Lapland** photo taken from: https://youngadventuress.com/2017/03/amethyst-finland.html
    - **Toronto** photo - Photo by Vincent Albos: https://www.pexels.com/photo/people-gathered-in-front-of-toronto-freestanding-signage-1750754/
    - **Buenos Aires** photo - Photo by Vinicius Garcia: https://www.pexels.com/photo/crowd-in-a-theater-bookstore-7858378/
    - **South Africa** photo - Photo by Kiekie & Kie: https://www.pexels.com/photo/brown-bird-perched-on-green-plant-8207371/
    - All other photos are either mine or the author of the post

## Acknowledgments