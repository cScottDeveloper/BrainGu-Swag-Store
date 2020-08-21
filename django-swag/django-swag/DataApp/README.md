# Sample App for Data Visualization

This app uses Chart.js to visualize some dummy data.  The data was used from this [tutorial](https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html).

### To run the app:
```bash
python manage.py migrate
python manage.py loaddata countries.json cities.json
python manage.py runserver
```

The app can be found at [http://localhost:8000/](http://localhost:8000/).
