#Aaina Vannan
#12/4/18

{% extends "base.html.py" %}

{% block content %}
    <h1>Hi, {{ user.username }}!</h1>
    {% for post in posts %} #similar to loop in routes.py
    <div><p>{{ post.author.username }} says: <b>{{ post.body }}</b></p></div> #p = paragraph in our loop
    {% endfor %}
{% endblock %}


#stuff in double brackets is an HTML template place holder that passes in user values


