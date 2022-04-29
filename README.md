# wagtail-bulma-starter-kit
A template project for Wagtail along with the Bulma CSS framework, a small amount of default styling and some custom components such as accordions.

This project is intended to be used as a basic front end setup for a smaller sites which don't require compiling JavaScript. Support for compiling JavaScript may be added in the future, but will likely only include basic features such as polyfills and importing files.

Note that this also doesn't include the Bulma flexbox grid by default, however this can easily be added by uncommenting the import in main.scss.

# Current Framework Versions
- Django 3.2 (LTS)
- Wagtail 2.15 (LTS)
- Bulma 0.9.3

# Installation
## Back-end Setup
- Firstly fork/copy this code into its own directory.
- cd into templatesite (feel free to change this name, and the names of the home and templatesite directories within it).
- Just like a regular Wagtail install, install the requirements with pip, run migrations, create a super user, and run the server (feel free to replace pip with something else if you prefer):
```
$ pip install -r requirements.txt
$ ./manage.py migrate
$ ./manage.py createsuperuserv
```

## Front-end Setup
- Make sure you have Dart SASS installed. If you are using a Mac with Homebrew you can run: `brew install sass/sass/sass`
- Run `npm install`
- Decide if you want to use Bulma grid (this is commented out by default in main.scss).
- Have a look through the code in templatesite/static/sass and update the variables in _variables.scss to match the design colors etc.

# Running the Project
- Make sure you are inside the templatesite directory.
- Run the backend server: `./manage.py runserver`
- Compile SASS: `npm run watch` (or build it once with `npm run build`).

# Front-end Styling
- Parts of the site which will usually need to be updated early on (such as fonts and SASS variables) can be found by searching for `Update after setup:`

# Branches / Versions (including road map for planned features)
- develop: Unstable version with features still in progress and likely to have bugs.
- 0.1 (planned for late May 2022):
    - Basic functionality
    - All style guide components working as includes/blocks
    - Home page, standard page, article page and article index page
    - Update default colors and styles
    - Add help text and admin improvements
- 0.2 (planned for June 2022):
    - Update to Django 4.0
    - Add carousel
    - Improve HTML semantics and accessibility
- 0.3 (planned for August/September 2022):
    - Update to Wagtail 3.0 (this includes the new admin design which is expected to be released in August 2022)
    - Update to Django 4.1
- Possible future versions:
    - Integrate forms
    - Flat nav package for menus
    - Finish set up of django-debug-toolbar and consider including jupyter notebooks
    - Add CSS Grid
    - Add polyfills and the option to compile JavaScript if needed

# Misc
* ipdb: Adding this to your code should act as a breakpoint when it runs: `import ipdb; ipdb.set_trace()`.
* django-debug-toolbar: See the amount of database requests made and some long they take (not fully set up yet).
* jupyter: Not yet set up, may be included in a future version.