#Reccomendation Engine Test
## Logan Thomas

Purpose:
* To build a basic reccomendation engine using python and c++
* database will be stored using sql

##Intended Databases
###Purchase
* Each entry is an purchase, this db will hold all purchases made. This information can be used for both personalized and unpersonalized engines.
* Each entry will have the form UserID, ItemID, PurchaseID
  * **UserID**: Each User's unique Identifier.
  * **ItemID**: Each Item's Unique Identifier, note that for a purchase in which a user buys 3 items, 3 entries get added to the Purchase Database.
  * **PurachseID**: Each time a user checksout that is given a unique purchase Identifier, as explained before, if a user buys 3 items at once, 3 entries are added however they all get the same PurchaseID.

###Ratings
---
* Each Entry in this database is a rating. Ratings can be used to assist personalized Recommendation engines.
* Each entry will have the form UserID, ItemID, Rating
  * **Rating**: A number between 1-10 telling how much the user liked the item

###Items
---
* Each entry is an item, this keeps track of some characteristics of the item
* Each entry is formatted: ItemID, Name, Price, CategoryID
  * **Name**: Name of the item
  * **Price**: Self explanatory, price of the item
  * **CategoryID**: Unique identifier of the category the item belongs in

###Users
---
* Each entry is a User. Information contained in this assists in personal engines.
* Each entry is formatted: UserID, ZipCode, PersonalPrefs
  * **ZipCode** : If user puts in location then this will be their zip code, distance measures can be made from this information
  * **PersonalPrefs** : this can be more than one field. If user is prompted to give information about themself this is where that is stored. This can be used for personal engines.


##Intended Classes

###DataBaseManager
---
* DataBaseManager provides a python interface for dealing with the sql(probably csv as the start, sql later) database
* will handle adding, removing, and querying entries from all the databases.

###Recommender
---
* Recommender is a base class meant to be inherited and overwritten.
* Will provide basic functions and attributes common to all Recommenders.
* Options to recommend by item, user, or both.
* Will work with DataBaseManager to provide meaningful recommendations.
