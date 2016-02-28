# Spend_ya

This is home of _Spend_Ya_ - Telegram bot for [**_Ya.Hack_**](https://events.yandex.ru/events/meetings/03-2016/). 

P.S. Please, **do not tell him** that he is just a bot, he will never forgive you that :smirk:

## Running locally

Before running locally copy `config.example.py` from `spend_ya_project` into new file `config.py` and add your information:

```sh
cd spend_ya_project
cp config.example.py config.py
```

For running an application locally you could use of of these commands:

```sh
$ heroku local web
```
or
```sh
$ python manage.py runserver 0.0.0.0:5000
```

Your app should now be running on [localhost:5000](http://localhost:5000/).


## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)


