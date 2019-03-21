# First to test the database we need to import the database 
# This should cause no other errors other than the 
# FSADeprecationWarning Error
from application import db

# Next we can run a command to create the database rows and columns
db.create_all()

# Then the user models need to be imported
from application import Post, User

# Now we can create some dummy data to populate the database
user_1 = User(username='Holden', email='hd@demo.com', password='password')
user_2 = User(username='JohnDoe', email='jd@demo.com', password='password')

# Then we can use the .add() method to add the user info
db.session.add(user_1)
db.session.add(user_2)

# The data isn't officially in our database until we commit it.
db.session.commit()

# Next we can use the query method on our User model to query some of the info
User.query.all()

# User.query.first() will return the first user in the database
User.query.first()

# The .filter_by() method can be use to filter out the users by their info
User.query.filter_by(username="Holden").all()
User.query.filter_by(email="jd@demo.com").all()
 
# The query can also be assigned to a variable and use the .first() method
# to only get the first user in the database with that specific filter
user = User.query.filter_by(username='JohnDoe').first()

# Now we can get the user's info by using the variable
user
user.posts
user.id

# Now to test the posts lets add some dummy post data
post_1 = Post(title='Blog 1', content='First Post Content!', user_id=user.id)
post_2 = Post(title='Blog 2', content='Second Post Content', user_id=user.id)

# Just like the user the posts need added and committed to the database
db.session.add(post_1)
db.session.add(post_2)
db.session.commit()

# Now we can check the post by the user variable
user.posts

# We can even loop through the posts
for post in posts:
	# And print the title of the posts
	print(post.title)

# Just like with the user we can assign querys of the posts to a variable
post = post.query.first()
 # and use it to get post info
 post
 post.author
 post.user_id

 # Now we can clean up the database to start fresh when we begin dev again
 db.drop_all()

 # and recreate the database
 db.create_all()

 # now just check that there are no remain Users or Posts info
 User.query.all()
 Post.query.all()