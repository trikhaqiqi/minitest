import requests
import calendar

api_key = 'd1f7f1d42ce9fe62fafc2798e6747635'
api_call = 'https://api.openweathermap.org/data/2.5/forecast?appid=' + api_key

running = True

print('Welcome to 5 day weather forecast application using OpenWeatherMap\'s API!')

while running:
    while True:
        try:
            print('\nThis application supports search by city(0) or search by zip code(1).')
            search = int(input('Please input 0 or 1: '))
        except ValueError:
            print("Sorry, I didn't understand that.")
        else:

            if search == 0:
                city = input('Please input the city name: ')
                if city.lower() == 'id':
                    city = 'jakarta, ID'

                api_call += '&q=' + city
                break
                
            elif search == 1:
                print("sorry this feature in maintainer")
                
            else:
                print('{} is not a valid option.'.format(search))

    json_data = requests.get(api_call).json()

    location_data = {
        'city': json_data['city']['name'],
        'country': json_data['city']['country']
    }

    print('\n{city}, {country}'.format(**location_data))

    current_date = ''
    for item in json_data['list']:
        time = item['dt_txt']
        next_date, hour = time.split(' ')
        if current_date != next_date:
            current_date = next_date
            year, month, day = current_date.split('-')
            date = {'y': year, 'm': month, 'd': day}
            print("\n Weather Forecast: " + ' {d} {m} {y}'.format(**date))


        import pandas as pd

        temp = pd.Timestamp('{y}-{m}-{d}'.format(**date))
        # print(temp.day_name())


        hour = int(hour[:2])
        if hour < 12:
            if hour == 0:
                hour = 12
            meridiem = 'AM'
        else:
            if hour > 12:
                hour -= 12
            meridiem = 'PM'

        temperature = item['main']['temp']
        
        bulan = month
        if bulan == '01':
            print(temp.day_name() + ', {d} '.format(**date) + "Jan" + ' {y}'.format(**date) + ':' + ' {:.2f}'.format(temperature - 273.15) + " °C" + " Pada jam" + ' %i:00 %s' % (hour, meridiem))
        if bulan == '02':
            print(temp.day_name() + ', {d} '.format(**date) + "Feb" + ' {y}'.format(**date) + ':' + ' {:.2f}'.format(temperature - 273.15) + " °C" + " Pada jam" + ' %i:00 %s' % (hour, meridiem))
        if bulan == '03':
            print(temp.day_name() + ', {d} '.format(**date) + "Mar" + ' {y}'.format(**date) + ':' + ' {:.2f}'.format(temperature - 273.15) + " °C" + " Pada jam" + ' %i:00 %s' % (hour, meridiem))
        if bulan == '04':
            print(temp.day_name() + ', {d} '.format(**date) + "Apr" + ' {y}'.format(**date) + ':' + ' {:.2f}'.format(temperature - 273.15) + " °C" + " Pada jam" + ' %i:00 %s' % (hour, meridiem))
        if bulan == '05':
            print(temp.day_name() + ', {d} '.format(**date) + "Mei" + ' {y}'.format(**date) + ':' + ' {:.2f}'.format(temperature - 273.15) + " °C" + " Pada jam" + ' %i:00 %s' % (hour, meridiem))
        if bulan == '06':
            print(temp.day_name() + ', {d} '.format(**date) + "Jun" + ' {y}'.format(**date) + ':' + ' {:.2f}'.format(temperature - 273.15) + " °C" + " Pada jam" + ' %i:00 %s' % (hour, meridiem))
        if bulan == '07':
            print(temp.day_name() + ', {d} '.format(**date) + "Jul" + ' {y}'.format(**date) + ':' + ' {:.2f}'.format(temperature - 273.15) + " °C" + " Pada jam" + ' %i:00 %s' % (hour, meridiem))
        if bulan == '08':
            print(temp.day_name() + ', {d} '.format(**date) + "Aug" + ' {y}'.format(**date) + ':' + ' {:.2f}'.format(temperature - 273.15) + " °C" + " Pada jam" + ' %i:00 %s' % (hour, meridiem))
        if bulan == '09':
            print(temp.day_name() + ', {d} '.format(**date) + "Sep" + ' {y}'.format(**date) + ':' + ' {:.2f}'.format(temperature - 273.15) + " °C" + " Pada jam" + ' %i:00 %s' % (hour, meridiem))
        if bulan == '10':
            print(temp.day_name() + ', {d} '.format(**date) + "Oct" + ' {y}'.format(**date) + ':' + ' {:.2f}'.format(temperature - 273.15) + " °C" + " Pada jam" + ' %i:00 %s' % (hour, meridiem))
        if bulan == '11':
            print(temp.day_name() + ', {d} '.format(**date) + "Nov" + ' {y}'.format(**date) + ':' + ' {:.2f}'.format(temperature - 273.15) + " °C" + " Pada jam" + ' %i:00 %s' % (hour, meridiem))
        if bulan == '12':
            print(temp.day_name() + ', {d} '.format(**date) + "Des" + ' {y}'.format(**date) + ':' + ' {:.2f}'.format(temperature - 273.15) + " °C" + " Pada jam" + ' %i:00 %s' % (hour, meridiem))
    break

