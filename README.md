# **Anna's Cookbook Blog**

## **Introduction**

Anna's Cookbook Blog is a blog-type website where I will be posting my own recipes for others to look at and make themselves. It is an updated version of my original [Cookbook](https://annacakes281.github.io/my-cookbook/index.html) Website that I had created before using basic HTML and CSS. Users will also have the option to like and comment on recipe posts.

The blog is aimed at anyone who enjoys cooking and is interested in trying a variety of recipes. The recipes are easy to follow along with and for different levels of cooking experience.

## **Table of Contents**

<details>
<summary><a href="#creators-comments">Creators Comments</a></summary>
<ul>
<li>Reasons Behind The Blog</li>
<li>Inspirations</li>
<li>My Thoughts</li>
</ul>
</details>
<details>
<summary><a href="#page-design">Page Design</a></summary>
<ul>
<li>Wireframes</li>
</ul>
</details>
<details>
<summary><a href="#agile-development">Agile Development</a></summary>
<ul>
<li>User Stories</li>
<li>MoSCoW Prioritisation</li>
<li>Milestones</li>
</ul>
</details>
<details>
<summary><a href="#features">Features</a></summary>
<ul>
<li>Django & Bootstrap</li>
<li>Homepage</li>
<li>Nav Bar</li>
<li>Search</li>
<li>Accounts</li>
<li>Admin Page</li>
<li>Post New Recipe</li>
<li>Recipe View</li>
<li>Liking</li>
<li>Comments, Tips & Recommendations</li>
<li>Contact Page</li>
<li>Optimisation</li>
</ul>
</details>
<details>
<summary><a href="#django">Django</a></summary>
<ul>
<li>External Libraries</li>
<li>Models</li>
<li>Views</li>
<li>Forms</li>
<li>URLs</li>
<li>Admin</li>
</ul>
</details>
<details>
<summary><a href="#testing">Testing</a></summary>
<ul>
<li>HTML & CSS Testing</li>
<li>Python Testing</li>
<li>Django Testing</li>
<li>Manual Testing</li>
<li>Built-in Linter</li>
<li>Unfixed Bugs</li>
</ul>
</details>
<details>
<summary><a href="#deployment">Deployment</a></summary>
<ul>
<li>Beta Testing</li>
<li>Heroku</li>
<li>Django</li>
</ul>
</details>
<details>
<summary><a href="#credits">Credits</a></summary>
<ul>
<li>Content</li>
<li>Images</li>
</ul>
</details>

<br>

## **Creators Comments**

In this section I will talk about my reasons behind creating the blog, any inspirations that I had used for creating it, as well as my thoughts on using Django as well as the other external libraries.

The reason I have included this section was to add some of my personal thoughts and insight behind my creation.

### **_Reasons Behind The Blog_**

I decided to make a Cookbook Blog as I am always cooking at home and thought getting my recipes out there and just food ideas that I make would be an interesting concept. It seemed like the most appropriate idea at the time and I enjoyed creating it.

Although throughout the process I did change my design idea a few times from a standard website and then decided to create a blog instead as I wanted to be able to only post my own recipes rather than having different users posting theirs.

### **_Inspirations_**

There were a few different websites and blogs that I used for inspirations and for creating my inital ideas for the blog. I mainly used them for some design and layout ideas.

- [Natasha's Kitchen](https://natashaskitchen.com/) was one of the blog websites I used as inspiration for a blog as my idea, as this is a website that I have used several times myself when making food and I really like how it is set out, as well as easy to use.
- [Cookpad](https://cookpad.com/uk/home) was a website I looked at during my design phase for ideas on layout and ideas of how I could design my website. This website was going to be used as an inital design before I decided to create a blog instead, however I did still decide to implement a section from here.
- [Let the Baking Begin](https://letthebakingbegin.com/) was another blog that I looked at when creating my blog idea for how to create my layout and features to include. This is another blog that I have personally used before.
- [CodeStar Blog](https://github.com/Code-Institute-Solutions/Django3blog/tree/master) was the project I did follow from to help create the inital base for my blog, although I did make several changes to the code, design, views, models to suite my blog. 

### **_My Thoughts_**

I really enjoyed using Django to create my blog, despite having some issues that I needed to think outside the box to fix. I used several different external libraries with Django to help create several features, such as [Cloundinary](https://cloudinary.com/) to store my images and media files externally, [Bootstrap](https://getbootstrap.com/) as a framework for further CSS design and [ElephantSQL](https://www.elephantsql.com/) as an external SQL database. I will further discuss the external libraries that were used in the <a href="#external-libraries">External Libraries</a> section.

I would definetly use Django again for future projects and I would like to learn more about the different features involved to be able to create more complex projects in the future. 

I am very happy with the blog that I have designed and the features that I have included, and I look forward to implementing more in the future.

## **Page Design**

- a few sentances intro into what app you used to create the design for website
- say had a few ideas but the more you built the more the idea became clear and it changed a lot during making the website

### **_Wireframes_**

- inital wireframe and explain how it differs from the finished content and why

## **Agile Development**

- explain the use agile development and why you found it helpful
- using user stories ond moscow throughout hhe project

### **_User Stories_**

- link to project board (ensure it is set to public)
- explain the user stories

### **_MoSCoW Prioritisation_**

- link to project board (ensure set to public)
- explain sections
- predicted start date and actual start date for each feature
- what features werent implemented and why

### **_Milestones_**

- found in issues tab
- each feature and user story in a milestone

## **Features**

- intro into what this section will be about

### **_Django & Bootstrap_**

- used django and bootstrap to create the project
- used some external libraries for more help

### **_Homepage_**

- photo of homepage
- what is included on the home page

### **_Nav Bar_**

- photo of nav bar
- what is on the nav bar
- purpose of it and what it does

### **_Search_**

- photo of search bar
- purpose of it and what it does

### **_Accounts_**

- photo of the different account side
- purpose of it and what it does

### **_Admin_**

- photo of admin view (only accesible/visble if admin)
- purpose and what it does

### **_Post New Recipe_**

- photo of post recipe button (only accessible/visible if admin)
- purpose of it and what it does

### **_Recipe View_**

- photo of homepage and when clicked on recipe
- purpose and what it does

### **_Liking_**

- photo of liking feature
- users must be logged in to like
- purpose of it

### **_Comments, Tips & Recommendations_**

- photo of commenting, etc feature
- users must be logged in to comment, etc
- purpose of it

### **_Contact Page_**

- photo of contact page
- email get sent to me using the js
- photo of popup box (need to implement)

### **_Optimisations_**

- bootstrap classes have allowed for optimsing on different screen sizes
- added some media queries on the css for some features
- what features and how they get optimised
- add photos for reference

## **Django**

- intro into using django to create the application in more detail

### **_External Libraries_**

- further detail into the external libraries used in project and reason behind using them (poss add links?)

### **_Models_**

- talk about each of the models implemented and reasons behind it
- add photos of how it looks on the admin view?

### **_Views_**

- talk about each of the views implemented and reasons behind it
- add photos of how it looks?

### **_Forms_**

- talk about each of the forms implemented and reasons behind it
- add photos of how it looks?

### **_URLs_**

- talk about each of the url pattern files implemented and reasons behind it
- add photos of how it looks?

### **_Admin_**

- talk about the admin view files and reasons behind it
- add photos of how it looks?

## **Testing**

- into into the testing section and eachof the tests carried out for the project

### **_HTML & CSS Testing_**

- the html and css testing tool to check code is correct (add photos)

### **_Python Testing_**

- PEP8 python tester (add photos)

### **_Django Testing_**

- using the testing unicode to test the models, views, forms, javascript (still need to finish and do)

### **_Manual Testing_**

- manual testing of clicking and checking everything works myself without errors (only issue so far is contact form on mobile not sending emails)

### **_Built-in Linter_**

- errors from the built-in linter that show up that are related to code, and whether they are necessary

### **_Unfixed Bugs_**

- any unfixed bugs and why they werent addressed

## **Deployment**

- intro into deployment for the project

### **_Beta Testing_**

- done some beta testing throughout milestones to check content working the way it is needed

### **_Heroku_**

- steps taken to deploy to heroku
- add photos

### **_Django_**

- what steps in django needed to deploy (settings, env, requirements)

## **Credits**

- intro into section

### **_Content_**

- external content sources used to help with project
- codestar (include videos/source code)
- <https://forum.djangoproject.com/t/creating-a-button-for-the-admin-page/15147>
  <https://stackoverflow.com/questions/11916297/django-detect-admin-login-in-view-or-template>
  <https://stackoverflow.com/questions/35557129/css-not-loading-wrong-mime-type-django>
  <https://devmaesters.com/blog/34>
  <https://learndjango.com/tutorials/django-search-tutorial>
  https://stackoverflow.com/questions/59811002/display-search-bar-and-search-button-inline-with-css
  <https://www.youtube.com/watch?v=H4QPHLmsZMU>
  (format these properly)
- mentor suggestions for whitenoise and summernote pages

### **_Images_**

- adobe stock photos for placeholder image (update the placeholder image)
