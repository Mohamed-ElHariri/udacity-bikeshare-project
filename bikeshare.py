import time
import pandas as pd


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    cities = ['chicago', 'new york city', 'washington']
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    days = ['sunday', 'saturday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']

    city = None
    month = None
    day = None

    
    print('Hello! Let\'s explore some US bikeshare data!')
    
    while city not in cities:
        city = input("Please enter a city name (Chicago, New York City, Washington): ").lower()
        if city not in cities:
            print("Invalid city name. Please try again.")

    
    while month not in months:
        month = input("Please enter a month of your choice (all, january, february, ... , june): ").lower()
        if month == 'all':
            month = None
            break
        elif month not in months:
            print("Invalid month. Please try again.")

    
    while day not in days:
        day = input("Please enter a day of your choice (all, monday, tuesday, ... sunday): ").lower()
        if day == 'all':
            day = None
            break
        elif day not in days:
            print("Invalid day. Please try again.")


    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    # To convert the month names into numbers for use in filtering later in the code
    MONTH_NUM = {'january': 1,
               'february': 2,
               'march': 3,
               'april': 4,
               'may': 5,
               'june': 6}
    
    df = pd.read_csv('./'+CITY_DATA[city])

    # Filtering the dataframe by month
    if month is not None:
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df = df[df['Start Time'].dt.month == MONTH_NUM[month]]

        # Filtering the dataframe by day
        if day is not None:
            df['Start Time'] = pd.to_datetime(df['Start Time'])
            df['Day of the Week'] = df['Start Time'].dt.day_name()
            df = df[df['Day of the Week'] == str(day).title()]
        
    elif day is not None:
            df['Start Time'] = pd.to_datetime(df['Start Time'])
            df['Day of the Week'] = df['Start Time'].dt.day_name()
            df = df[df['Day of the Week'] == str(day).title()]
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    return df


def time_stats(df: pd.DataFrame):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # This dictionary is made to translate the month numbers into names to display it to the user.
    MONTH_NAME = {1 : 'January',
                  2 : 'February',
                  3 : 'March',
                  4 : 'April',
                  5 : 'May',
                  6 : 'June'}

    

    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    month_counts = df['Month'].value_counts()
    most_common_month = month_counts.index[0]

    print("The most common month is:", MONTH_NAME[most_common_month])
    print("With a total of {} Rides".format(month_counts.iloc[0]))

    

    df['Day of Week'] = df['Start Time'].dt.day_name()
    day_counts = df['Day of Week'].value_counts()
    most_common_day = day_counts.index[0]

    print("\nThe most common day of the week is:", most_common_day)
    print("With a total of {} Rides".format(day_counts.iloc[0]))

    

    df['Start Hour'] = df['Start Time'].dt.hour
    hour_counts = df['Start Hour'].value_counts()
    most_common_hour = hour_counts.idxmax()

    print("\nThe most common hour is:", most_common_hour)
    print("With a total of {} Rides".format(hour_counts.iloc[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df: pd.DataFrame):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    

    start_station_counts = df['Start Station'].value_counts()
    most_common_start_station = start_station_counts.idxmax()

    print("The most commonly used start station is:", most_common_start_station)
    print("It has been used {} times".format(start_station_counts.iloc[0]))

    

    end_station_counts = df['End Station'].value_counts()
    most_common_end_station = end_station_counts.idxmax()

    print("The most commonly used end station is:", most_common_end_station)
    print("It has been used {} times".format(end_station_counts.iloc[0]))

    
    station_combination_counts = df.groupby(['Start Station', 'End Station']).size()
    most_common_station_combination = station_combination_counts.idxmax()
    common_combined_start_station, common_combined_end_station = most_common_station_combination

    print("The most common combination is from [{}] =to=> [{}]".format(common_combined_start_station, common_combined_end_station))
    print("they have been used {} times".format(station_combination_counts.iloc[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df: pd.DataFrame):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    
    # Calculate the sum of the 'Total Travel Time' column
    total_travel_time = df['Trip Duration'].sum() 

    # Convert the sum to hours, minutes, and seconds
    total_hours, total_remainder = divmod(total_travel_time, 3600)
    total_minutes, total_seconds = divmod(total_remainder, 60)

    print("Total Trip Duration is: {} Hours {} Minutes {} Seconds".format(total_hours, total_minutes, total_seconds))

    

    # Calculate the mean of the 'Total Travel Time' column
    mean_travel_time = df['Trip Duration'].mean() 

    # Convert the sum to hours, minutes, and seconds
    mean_hours, mean_remainder = divmod(mean_travel_time, 3600)
    mean_minutes, mean_seconds = divmod(mean_remainder, 60)

    print("Mean Trip Duration is: {} Hours {} Minutes {} Seconds".format(int(mean_hours), int(mean_minutes), int(mean_seconds)))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df: pd.DataFrame):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    

    # Get the value count for user types
    user_type_count = df['User Type'].value_counts()

    # Print the count for each specific user
    sub_count = user_type_count['Subscriber']
    customer_count = user_type_count['Customer']

    print("Subscriber count:", sub_count)
    print("Customer count:", customer_count)

   

    # Since the city of washington doesn't have data on the genders of its users, I am going to use a try statement to resolve the error.
    try:
        # Get the value count for user gender type
        user_gender_count = df['Gender'].value_counts()

        # Print the count for each specific user
        male_count = user_gender_count['Male']
        female_count = user_gender_count['Female']
        unspecified_count = df['Gender'].isnull().sum()

        print("\nMale user count:", male_count)
        print("Female user count:", female_count)
        print("Unspecified user count:", unspecified_count)

        

        # Earliest user birth year
        earlist_birth_year = df['Birth Year'].min()

        # Most recent user birth year
        most_recent_birth_year = df['Birth Year'].max()

        # Most common birth year
        birth_year_counts = df['Birth Year'].value_counts()
        most_common_birth_year = birth_year_counts.index[0]

        print("\nEarliest Birth Year:", int(earlist_birth_year))
        print("Most Recent Birth Year:", int(most_recent_birth_year))
        print("Most common Birth Year:", int(most_common_birth_year))

    except KeyError:
        print("\nSelected City doesn't have birth date and gender type data on its users.")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df: pd.DataFrame):
    # Initialize a variable to keep track of the starting index
    start_index = 0

    show_data = None
    # Prompt the user if they want to see 5 lines of raw data
    while True:
        user_input = input("Do you want to view the raw data? (yes/no): ").lower()
        if user_input == 'yes':
            show_data = True
            break
        elif user_input == 'no':
            show_data = False
            break
        else:
            print("Please reply with 'yes' or 'no'.")

    # Loop until the user enters 'no' or there is no more raw data to display
    while show_data == True and start_index < len(df):
        # Get the next 5 lines of raw data
        next_5_rows = df.iloc[start_index:start_index+5]
        
        # Display the next 5 lines of raw data
        print(next_5_rows)
        
        # Update the starting index for the next iteration
        start_index += 5
        
        # Prompt the user again
        while True:
            user_input = input("Do you want to see the next 5 lines of raw data? (yes/no): ").lower()
            if user_input == 'yes':
                show_data = True
                break
            elif user_input == 'no':
                show_data = False
                break
            else:
                print("Please reply with 'yes' or 'no'.")
                
        print("End of data display.")

    
    print('-'*40)

def main():
    restart = True

    while  restart:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        
        while True:
            user_input = input('\nWould you like to restart? (yes/no): ').lower()
            if user_input == 'yes':
                break
            elif user_input == 'no':
                restart = False
                break
            else:
                print("Please reply with 'yes' or 'no'.")


if __name__ == "__main__":
	main()
