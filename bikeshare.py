import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january', 'february', 'mars', 'april', 'may', 'june']
WEEK = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saterday', 'sunday']
FILTER_TYPES = ['month', 'day', 'both', 'none']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter name of a city to analyze: ")
    while city not in CITY_DATA:
         city = input("Enter a valid name of a city to analyze: ")


   # TO DO: get user input for month (all, january, february, ... , june)
    print()
    global filter_type
    filter_type = input("would you like to filter the data by month, day, both or not at all? Type 'none' for no time filter.")
    while filter_type not in FILTER_TYPES:
        filter_type = input("Enter a valid keyword: ")

    if filter_type == 'month':
        day = None
        month = input("Enter a name of the month to filter by(ex:'may'): ")
        while month not in MONTHS:
            month = input('Enter a valid name of the month to filter by: ')

    elif filter_type == 'day':
        month = None
        day = input("Enter a name of the day of week to filter by(ex:'saterday'): ")
        while day not in WEEK:
            day = input('Enter a valid name of the day of week to filter by: ')


    elif filter_type == 'both':
        month = input('Enter a name of the month to filter by: ')
        while month not in MONTHS:
            month = input('Enter a valid name of the month to filter by: ')

        day = input('Enter a name of the day of week to filter by: ')
        while day not in WEEK:
            day = input('Enter a valid name of the day of week to filter by: ')

    else:
        day = None
        month = None
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    print(df.head())
    if month != None:

        df = df[df['month'] == MONTHS.index(month)  +  1]

    if day != None:

        df = df[df['day'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if filter_type == 'none' or filter_type == 'day':
        print('The most common month:'+ str(df['month'].mode()[0]) + ", " + "Count: " + str(df['month'].value_counts().max()) + ", " + "Filter: " + filter_type)

    # TO DO: display the most common day of week
    if filter_type == 'none' or filter_type == 'month':
        print('Most common day:', df['day'].mode()[0] + ", " + "Count: " + str(df['day'].value_counts().max()) + ", " + "Filter: " + filter_type)

    # TO DO: display the most common start hour
    items_counts = df['hour'].value_counts()
    max_item = items_counts.max()
    print(max_item)
    print('Most common start hour: ' + str(df['hour'].mode()[0]) + ", " + "Count: " + str(df['hour'].value_counts().max()) + ", " + "Filter: " + filter_type)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most commnly used start station: " + str(df['Start Station'].mode()[0]) + ", " + "Count: " + str(df['Start Station'].value_counts().max()) + ", " + "Filter: " + filter_type)

    # TO DO: display most commonly used end station
    print("Most commnly used End station: " + str(df['End Station'].mode()[0]) + ", " + "Count: " + str(df['End Station'].value_counts().max()) + ", " + "Filter: " + filter_type)


    # TO DO: display most frequent combination of start station and end station trip

    print("Most frequent combination of start and end station: " + str(df.groupby(['Start Station','End Station']).size().idxmax()) + ", " + "Count: " + str(df.groupby(['Start Station'])['End Station'].value_counts().max()) + ", " + "Filter: " + filter_type)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Trip Duration: " + str(df['Trip Duration'].sum()) + ", Count: " + str(df['Trip Duration'].count()) + ", Filter: " +filter_type)

    # TO DO: display mean travel time
    print("Average Durarion:", df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("User types:")
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print()
    print("Gender:")
    print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print()
    print("Earliest year:", df['Birth Year'].min())
    print("Recent year:", df['Birth Year'].max())
    print("Most common year", df['Birth Year'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city != 'washington':
            user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
