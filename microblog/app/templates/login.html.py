#Aaina Vannan
#12/10/18

{%extends "base.html.py" %}
#extends base page templates

{% block content %}
    <h1>Sign In </h1>
    <form action = "" method = "post"> #attribute and method = 2 attributes
    #by passing in an empty string for action, it tells the att. to just use current string
        {{ form.hidden_tag() }} #needed for flask-wtf, as it protects from attack
        <p>
            {{ form.username.label }} <br> #br = line break
            {{ form.username(size = 32) }} #html for that field 
        </p>
        <p>
            {{form.password.label }} <br>
            {{form.password(size = 32) }}
        </p>
        <p> {{ form.remember_me() }}, {{form.remember_me.label }} </p>
        <p> {{ form.submit() }} </p>
    </form>
{% endblock %}
