# Day 3 : HTML Templates in Flask  
  
## Flask Template Engine:  
Flask uses **Jinja2** templating engine to render dynamic HTML pages.  
  
## Basics:  
▫️HTML files go inside the templates/folder.  
▫️Use render_template('filename.html') to return a page.  
▫️Pass Python variables to HTML like:  
    render_template('profile.html',username="Hardik")  
  
## Jinja2 Syntax (in HTML):  
▫️{{variable}} - for printing variables.  
▫️{%...%} - for logic like if/for statements.  