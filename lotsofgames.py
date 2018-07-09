# [Start Imports]
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CateItem, User

engine = create_engine('postgresql://catalog:password@localhost/catalog')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Add a user
user1 = User(
   name="Rpg Fan",
   email="rpgfan@gmail.com")
session.add(user1)
session.commit()

# Create the Role-Playing game category
category1 = Category(user=user1, name="Role-Playing")
session.add(category1)
session.commit()


# Create the Action game category
category2 = Category(user=user1, name="Action")
session.add(category2)
session.commit()

# Create the Puzzle game category
category3 = Category(user=user1, name="Puzzle")
session.add(category3)
session.commit()

# Create the Shooter game category
category4 = Category(user=user1, name="Shooter")
session.add(category4)
session.commit()

# Create the Fighting game category
category5 = Category(user=user1, name="Fighting")
session.add(category5)
session.commit()

# Create the Sports game category
category6 = Category(user=user1, name="Sports")
session.add(category6)
session.commit()

# Create the Racing game category
category7 = Category(user=user1, name="Racing")
session.add(category7)
session.commit()

# Create the Adventure game category
category8 = Category(user=user1, name="Adventure")
session.add(category8)
session.commit()

# Create the Strategy game category
category9 = Category(user=user1, name="Strategy")
session.add(category9)
session.commit()


# Add Video Games into category
game1 = CateItem(name="Tales of Zestiria",
                            description="Tales of Zestiria takes place on a fictional continent named Glenwood.",
                            category=category1, user=user1)
session.add(game1)
session.commit()

game2 = CateItem(name="Dragon Quest XI",
                            description="DRAGON QUEST XI tells a captivating tale of a\
                            hunted hero and is the long-awaited role-playing.",
                            category=category1, user=user1)
session.add(game2)
session.commit()

game3 = CateItem(name="Overwatch",
                            description="Overwatch is gone but the world still needs heroes.",
                            category=category2, user=user1)
session.add(game3)
session.commit()

game4 = CateItem(name="Blackhole",
                            description="The crew of the spaceship Endera is sucked into a black hole.",
                            category=category3, user=user1)
session.add(game4)
session.commit()


game5 = CateItem(name="Far Cry 5",
                            description="'Welcome to Hope County, Montana, land of the free, the brave,\
                            but also home to a fanatical doomsday cult known as Eden's Gate.",
                            category=category4, user=user1)
session.add(game5)
session.commit()


game6 = CateItem(name="Soulcalibur VI",
                            description="Soulcalibur VI represents the latest entry in the premier fighting game.",
                            category=category5, user=user1)
session.add(game6)
session.commit()


game7 = CateItem(name="FIFA 17",
                            description=" Experience Life in the Premier League",
                            category=category6, user=user1)
session.add(game7)
session.commit()


game8 = CateItem(name="The Crew 2",
                            description="In The Crew 2, take on the American motorsports scene.",
                            category=category7, user=user1)
session.add(game8)
session.commit()


game9 = CateItem(name="Moss",
                            description="Moss is a single-player action-adventure puzzle game.",
                            category=category8, user=user1)
session.add(game9)
session.commit()

game10 = CateItem(name="Horizon Zero Dawn",
                            description="In an era where machines roam the land, mankind is no\
                            longer the dominant species.",
                            category=category8, user=user1)
session.add(game10)
session.commit()

game11 = CateItem(name="Valkyria Chronicles Remastered",
                            description="In the world of Valkyria Chronicles, the year is 1935 E.C.",
                            category=category9, user=user1)
session.add(game11)
session.commit()

game12 = CateItem(name="Styx: Shards of Darknes",
                            description="Following the fall of Akenash tower, an extraordinary matter has forced\
                            Styx out of hiding.",
                            category=category9, user=user1)
session.add(game12)
session.commit()

print "Video game data have been populated!"
