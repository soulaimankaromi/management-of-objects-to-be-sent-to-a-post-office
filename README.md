# management-of-objects-to-be-sent-to-a-post-office
Workshop 3: management of objects to be sent to a post office
We want to design classes and a program that could be useful to a postal employee to process objects to be shipped.
1. Define a PostalObject class whose characteristics are as follows:
⚫ the name of the recipient (character string),
·
the recipient's address (character string),
⚫ the postal code (entire),
• the name of the destination city (character string),
•
and a boolean which indicates whether the item should be sent by registered mail or not.
We will need to provide this class with the following methods:
⚫ a builder,
⚫ a price method returning an actual corresponding to the postage price,
Firstly, you must create a simple PostalObject class with the data mentioned above,
In fact, the PostalObject class does not actually correspond to any existing object (abstract class), it only brings together the characteristics common to all postal objects actually manipulated by the application, which will be instances of the Letter and Parcel classes that we Let's define it below.
A consequence of this is that the price method of the PostObject class has no definition, it will actually be defined in the subclasses.
This will be the subject of an application exercise when we have developed the notion of an abstract class.
2. Define a Letter class, a subclass of Postal Object, which has, apart from the inherited data, a Boolean type data which indicates whether the letter must be sent urgently or not.
This class will have a constructor, and will calculate the postage price as follows:
⚫ the normal postage price is 0.53 euros,
·
if the letter must be sent by registered mail, there is an additional cost of 1.5 euros,
·
if the letter must be sent urgently, there is also an additional cost of 0.6 euros.
3. Define a Parcel class, a subclass of PostalObject, which has, apart from the inherited data, real type data which gives the weight of the parcel, expressed in grams.
This class will have a constructor, and will calculate the postage price as follows:
· the normal postage price is calculated on the basis of 0.8 euros per weight unit of 100 grams,
·
if the package must be sent by registered mail, there is an additional cost of 3 euros.
4. Create a menu that allows you to calculate the price to pay to send a postal item
