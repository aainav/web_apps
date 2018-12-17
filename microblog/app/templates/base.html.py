#Aaina Vannan
#12/4/18

#holds html code
<html>
    <head>
    {% if title %} #when variable is avaliable
    <title>{{ title }} - Microblog</title>
    {% else %} #when variable is not avaliable
    <title>Welcome to Microblog!</title>
    {% endif %} 
    </head>
    <body>
        <div>Microblog:
            <a href = "/index">Home</a></div>
            <a href = "/login"> login </a>
        {% block content %}{% endblock %}
    </body>
</html>


#stuff in double brackets is an HTML template place holder that passes in user values


