# Cybersecurity-Safe-Password-Generator
API created using FastAPI to generate safe passwords based on users' choice.

Stop using silly and obvious passwords, for your safety use something out of the box!
Just make a request to the end point and get the generated password for your needs.

The body request should have:

![example image](./example-spg.png)

The image shows a test in Postman, but in the body you should provide: 

{ \
&nbsp;&nbsp;&nbsp;&nbsp;"caracterlen": 8, \
&nbsp;&nbsp;&nbsp;&nbsp;"havenumbers": true, \
&nbsp;&nbsp;&nbsp;&nbsp;"haveletters": true, \
&nbsp;&nbsp;&nbsp;&nbsp;"havesymbols": true, \
&nbsp;&nbsp;&nbsp;&nbsp;"havesigns": true, \
&nbsp;&nbsp;&nbsp;&nbsp;"havecapitalletters": true\
} 

The minimum length for a password is 8 (as a good practice) and the other parameters are optional.

In this repository you will find two different versions:
1. Deployed on AWS in a EC2 (no longer available to use): \
Endpoint: http://54.243.5.214/safepassword \
Documentation: http://54.243.5.214/docs \

3. Deployed on AWS in Lambda: \
Endpoint: https://eer6p533griarwyetgzb5edmmu0bvdzr.lambda-url.eu-north-1.on.aws/safepassword \
Documentation: https://eer6p533griarwyetgzb5edmmu0bvdzr.lambda-url.eu-north-1.on.aws/docs \
