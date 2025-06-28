# Day 4: Jinja2 Control Structures & Template Inheritance  
  
## Logic in Templates:  
▫️Use {% for %} for loop.  
▫️Use {% if %} for conditionals.  
▫️For Variables Use {{ variable }}  
  
## Template Inheritance:  
▫️Create base.html with common layout (header/footer)  
▫️Other templates extend it using:  
    {% extends "base.html" %}  
    {% block content %} {% endblock %}  