import pandas as pd

def read_seen_values(log_file):
    try:
        with open(log_file, 'r') as file:
            seen_values = set(line.strip() for line in file)
    except FileNotFoundError:
        seen_values = set()
    return seen_values

def write_seen_values(log_file, seen_values):
    with open(log_file, 'w') as file:
        for value in seen_values:
            file.write(f"{value}\n")

def log_found_info(df, log_file):
    seen_values = read_seen_values(log_file)
    new_values = set()
    
    for row in df.index:
        for col in df.columns:
            value = df.at[row, col]
            cell_identifier = f"{row},{col}"
            if value > 0 and cell_identifier not in seen_values:
                print(f"Value found at Row: {row}, Column: {col}, Value: {value}")
                new_values.add(cell_identifier)
    
    seen_values.update(new_values)
    write_seen_values(log_file, seen_values)

def remove_logged_values(df, log_file):
    seen_values = read_seen_values(log_file)
    for value in seen_values:
        row, col = value.split(',')
        row_time = pd.to_datetime(row).time()  # Convert row to time object
        col_date = pd.to_datetime(col)  # Convert col to datetime object
        if row_time in df.index.time and col_date in df.columns:
            df.at[row_time, col_date] = 0
    return df

def apply_filters(df, min_hour, top_hour, days_to_keep, number_of_spots, log_file='seen_values.log'):
    # Ensure the DataFrame index is a DatetimeIndex
    df.index = pd.to_datetime(df.index, format='%H:%M')
    
    # Convert min_hour and top_hour to time objects for comparison
    min_hour_dt = pd.to_datetime(min_hour, format='%H:%M').time()
    top_hour_dt = pd.to_datetime(top_hour, format='%H:%M').time()
    
    # Filter rows based on the time range
    mask = (df.index.time >= min_hour_dt) & (df.index.time <= top_hour_dt)
    df = df.loc[mask]
    
    # Convert columns to datetime objects
    df.columns = pd.to_datetime(df.columns)
    
    # Filter columns based on days_to_keep
    filtered_columns = [col for col in df.columns if col.day_name() in days_to_keep]
    df = df[filtered_columns]
    
    # Filter cells based on the number_of_spots
    df = df.applymap(lambda x: x if x >= number_of_spots else 0)
    
    # Remove logged values
    df = remove_logged_values(df, log_file)
    
    # Log the found info
    log_found_info(df, log_file)
    
    return df