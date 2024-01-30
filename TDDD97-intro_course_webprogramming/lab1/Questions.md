# Questions Lab 1

## Question 1
Q: Why do we validate data before sending it to the server at client-side, as opposed to just letting the server data before using it? What we get and what we lose by it?

A: To minimize the load on the server and minimize uneccicary network traffic. What we loose somewhat is control, since the user can tamper with the validation function or forge requests to the server.

## Question 2
Q: How secure is the system using an access token to authenticate? Is there any way to circumvent it and get access to private data?

A: This is very insecure, because you can access others tokens by input in console, you can retrive most if not all data from the user you want to find. Even password.

## Question 3
Q: What would happen if a user were to post a message contatining Javascript-code? Would the code be executed? How can it oppose a threat to the system? Would the counter measure?

A: Yes the user could input code in a message. Either a XSS or CRTF attack and it could be devastating. You need to sanitize the input.

## Question 4
Q:What happens when we use the back/forward buttons while working with Twidder? Is this the expected behaviour? Why are we getting this behaviour? What would be the solution?

A: Because the application is a single page application it would go back to the previous website you were visiting. This is a expected behaviour. Before backing you would display that you are about to exit the page.

## Question 5
Q: What happends when the user refreshes the page while woring with Twidder? Is this the excpected behaviour? Why are we getting this behaviour?

A: The page is reset to the users home page. This is, again, because Twidder is a single page application and the deafult tab is Home.

## Question 6
Q: Is it a good idea to read views from the server instead of embedding them inside of the "client.html"? What are the advantages and disadvantages of it comparing to the current approach?

A: The problem with having the views on the server is the network traffic of sending each view, every time a user decides to change view. An advantage could be that the user don't have access the structure of a view without propper authetication, if every view is stored localy, the user has access to the html structure of every view.

## Question 7
Q: Is it a good idea to return true or false to state if an operation has gone wrong at the server-side or not? How can it be improved?

A:It is a good idea to retain true of false state from server side so the client knows how to proceed with data from the server. It's a good idea to bunlde the true or false value in the repsonse object, see res.success.

## Question 8
Q: Is it reliable to perform data valdiation at client-side? If so please explain how and if not what would be the solution to improve it?

A: No, data validation should be done at server-side. This is because it can be a security threat to handle data at client side because it easier to access than in the server-side.

## Question 9
Q: Why isnt it a good idea to use tables for layout purposes? What would be the replacement?

A: They are bad. >:( Use CSS flex-dic-in-a-box instead :)

## Question 10
Q: How do you think SPA can contribute to the future of the web? What is their advatanges and disadvantages from usage and development point of view?

A: SPA does only load css html and js once in a lifespan so it will be faster in the long run to use SPA, easier to debug, use same backend for many purposes. Disadvantage is it can be very slow to first load if it is a big application and it requires js that can be a security threat sometimes, async with ajax can be a problem sometimes.
