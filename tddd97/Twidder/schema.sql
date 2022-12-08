create table users(
  email text primary key,
  password text,
  firstname text,
  familyname text,
  gender text,
  city text,
  country text);


create table messages(
  id integer primary key autoincrement,
  email_sender text,
  message text,
  recipient text);