# Cybersecurity-Safe-Password-Generator
API created using FastAPI to generate safe passwords based on users' choice

the body request should have:

{\
  &nbsp;&nbsp;&nbsp;&nbsp;"caracterlen": minimum 8,\
  &nbsp;&nbsp;&nbsp;&nbsp;"havenumbers": optional,\
  &nbsp;&nbsp;&nbsp;&nbsp;"haveletters": optional,\
  &nbsp;&nbsp;&nbsp;&nbsp;"havesymbols": optional,\
  &nbsp;&nbsp;&nbsp;&nbsp;"havesigns": optional,\
  &nbsp;&nbsp;&nbsp;&nbsp;"havecapitalletters": optional\
}

It is deployed on AWS: http://54.243.5.214/ \
Endpoint: http://54.243.5.214/safepassword \
Its documentation: http://54.243.5.214/docs 
