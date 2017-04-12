# Import the model classes we just wrote.
>>> from polls.models import Question, Choice

# No questions are in the system yet.
>>> Question.objects.all()
<QuerySet []>
 
# Create a new Question.
from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())

#Create question 3

q3 = Question(question_text="What's new 3?", pub_date=timezone.now(),owner_id="NONE")
 
# Save the object into the database. You have to call save() explicitly.
q.save()
q3.save()

#id is auto-assigned
q.id

# Access model field values via Python attributes.
q.question_text
q.pub_date
 
# Change values by changing the attributes, then calling save().
q.question_text = "What's up?"
q.save()
q3.owner_id = "Question 3 User"
q3.save()
 
# objects.all() displays all the questions in the database.
Question.objects.all()


# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
Question.objects.filter(id=1)

Question.objects.filter(question_text__startswith='What')


# Request an ID that doesn't exist, this will raise an exception.
Question.objects.get(id=3)

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
Question.objects.get(pk=1)


# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
q.choice_set.all()


# Create three choices.
q.choice_set.create(choice_text='Not much', votes=0)

q.choice_set.create(choice_text='The sky', votes=0)

c = q.choice_set.create(choice_text='Just hacking again', votes=0)

# Choice objects have API access to their related Question objects.
c.question


# And vice versa: Question objects get access to Choice objects.
q.choice_set.all()
q.choice_set.count()


# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
Choice.objects.filter(question__pub_date__year=2017)


# Let's delete one of the choices. Use delete() for that.
c = q.choice_set.filter(choice_text__startswith='Just hacking')
c.delete()
