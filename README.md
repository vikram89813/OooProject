# Read mail Service
Python service to read from live, hotmail, outlook or any microsoft email service, this service uses Imaplib python to read email with IMAP protocol.
## Prerequisite Libraries
Please make sure you have these libraries installed on your system first before running this code:
 * email
 * imaplib
 * smtplib
 * datetime
 * flask

## Running the service
1. rename config.py.sample to config.py and update `config.py` to your credentials.
2. run `python app.py`
3. test the endpoint using `curl http://127.0.0.1:5000/fetch`

## Endpoints

### `/fetch`
This endpoint makes a call to your email inbox then reads the latest unread message.

If subject doesn't contain `ooo`

```
{
  "from": "not required!!",
  "subject": "not ooo case!!"
}
```

if the subject does contain `ooo` returns email of the sender and the subject of the email message. 

```
{
  "from": "test@test.com",
  "subject": "ooo message"
}
```

## Future work
1. Add other identifiers such as `on leave`, `on sick leave` etc.
2. Add authentication and other security measures.
3. Add logging.
4. Add more endpoints for features like send mail, read mail body etc.
5. Add test cases
6. Handle corner cases.
 
 

