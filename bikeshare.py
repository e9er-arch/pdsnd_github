import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_name = ''
    while city_name.lower() not in CITY_DATA:
        city_name = input("\nFor what city would you like to analyze data? Enter either chicago, new york city, washington)\n")
        if city_name.lower() in CITY_DATA:
            #Valid entry, able to return data
            city = CITY_DATA[city_name.lower()]
        else:
            #Invalid entry, not able to return data
            print("We were not able to find the city you entered - Enter either chicago, new york city or washington.\n")

    # get user input for month (all, january, february, ... , june)
    month_name = ''
    while month_name.lower() not in MONTH_DATA:
        month_name = input("\nFor which month do you want to filter data? Enter either 'all' or january, february, march, april, may, june)\n")
        if month_name.lower() in MONTH_DATA:
            #Valid entry, able to return data
            month = month_name.lower()
        else:
            #Invalid entry, not able to return data
            print("We were not able to find the month you entered - Enter either 'all' or january, february, march, april, may, june.\n")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = ''
    while day_name.lower() not in DAY_DATA:
        day_name = input("\nFor which day do you want to filter data? Enter either 'all' or monday, tuesday, wednesday, thursday, friday, saturday, sunday)\n")
        if day_name.lower() in DAY_DATA:
            #Valid entry, able to return data
            day = day_name.lower()
        else:
            #Invalid entry, not able to return data
            print("We were not able to find the day name you entered- Enter either 'all' or monday, tuesday, wednesday, thursday, friday, saturday, sunday.\n")

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
    # load data file into a dataframe
    df = pd.read_csv(city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTH_DATA.index(month)

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month from the data is: " + MONTH_DATA[common_month].title())

    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of week from the data is: " + common_day_of_week)

    # display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("The most common start hour from the given fitered data is: " + str(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station from the data is: " + common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station from the data is: " + common_end_station)

    # display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip from the data is: " + str(frequent_combination.split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time from the data is: " + str(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time from the data is: " + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types from the data is: \n" + str(user_types))

    if city == 'chicago.csv' or city == 'new_york_city.csv':
    # Display counts of gender
        gender = df['Gender'].value_counts()
        print("The count of user gender from the data is: \n" + str(gender))

    # Display earliest, most recent, and most common year of birth
        earliest_birth_yr = df['Birth Year'].min()
        most_recent_birth_yr = df['Birth Year'].max()
        most_common_birth_yr = df['Birth Year'].mode()[0]
        print('Earliest birth from the data is: {}\n'.format(earliest_birth_yr))
        print('Most recent birth from the data is: {}\n'.format(most_recent_birth_yr))
        print('Most common birth from the data is: {}\n'.format(most_common_birth_yr))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """Displays raw data"""

    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you like to view the next five rows of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        while True:
            view_raw_data = input('\nWould you like to view first five row of raw data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
