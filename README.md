# Supreme Shopper
Automate the buying process of supreme clothing.

## How To Run
Download the requirements that are outlined in the requirements.txt file.
Please note that this is a pyhton3.7 program.

Captcha Solver: you will need to get an api key (key should be free) to google's
  speech-to-text api. This will allow us to break the captcha automatically and
  give us our best chance of getting all the way through checkout.

Proxies: go to stormproxies.com and get residentail rotating ip addresses;
  you need to copy and paste your proxies into a csv file

Payment: you are going to need to populate a json with payment information
  for every item that you intend to buy. You will need one card per item because
  all items that are purchased by the same card will get canceled.

## After you have all of the payment information and have appropriate proxies to give to the webdriver, you just have to run the program ~5 minutes before drop (Thursdays at 10:55). The bot should be able to handle the rest.

# TODO
Make requirements.txt
Captcha Breaker: need to write a function that will record the audio from the captcha
  and then feed that to Google's speech-to-text api.
