from ipywidgets import widgets
import pandas as pd

LOCATION_PATH = './State_County_Data'

# Stores UI data not needed for use of api or plots
class AppData: # So the user doesn't have to re-enter the same data every time
    def __init__(self):
        # User states
        self.start_date = '01/01/2022' #TODO: remove this
        self.end_date = '03/01/2022'
        self.state = None
        self.county = None
        self.location = ''
        self.selected_sensors = ()

        # Data gathered from APIs
        self.sensor_data = None
        self.bounding_box = None

app_data = AppData() # Initialize data object

def process_location(location):
    keys = [key.strip() for key in location.split('/')]
    return keys[0], keys[1]

def process_date(data):
    keys = [key.strip() for key in data.split('/')]
    year, month, day = keys[2], keys[1], keys[0]
    date = f'{year}-{month}-{day}'

    return date

def load_states():
    STATE_PATH = f'{LOCATION_PATH}/us_states.csv'

    sorted_states = pd.read_csv(STATE_PATH).sort_values('NAME')

    return sorted_states[['NAME', 'STATEFP']].values.tolist()

def load_counties(statefp):
    COUNTY_PATH = f'{LOCATION_PATH}/us_counties.csv'

    counties = pd.read_csv(COUNTY_PATH)
    state_counties = counties[counties['STATEFP'] == statefp].sort_values('NAME')

    return state_counties['NAME'].values.tolist()

# Code for the gather data scene elements.
def gather_data_elements():
    start_date_box = widgets.Text(
        placeholder='dd/mm/yy',
        description='Date/Start Date:',
        disabled=False  
    )

    end_date_box = widgets.Text(
        placeholder='dd/mm/yy',
        description='End date:',
        disabled=False
    )

    state_dropdown = widgets.Dropdown(
        options=[(state[0], state[1]) for state in load_states()],
        value=41,
        description='State:',
        disabled=False,
    )

    county_dropdown = widgets.Dropdown(
        description='County:',
        options = load_counties(state_dropdown.value),
        value='Jackson',
        disabled=False,
    )

    gather_data_button = widgets.Button(
        description='Gather data',
        disabled=False,
        layout=widgets.Layout(width='auto'),
        tooltip='Gather data nescessary to plot statistics.',
    )

    def state_dropdown_change(e):
        county_dropdown.options = load_counties(state_dropdown.value)
        county_dropdown.value = county_dropdown.options[0]

    state_dropdown.observe(state_dropdown_change, names='value')

    return start_date_box, end_date_box, state_dropdown, county_dropdown, gather_data_button

# Code for the make plot scene elements.
def make_plot_elements():
    sensor_select = widgets.SelectMultiple(
        layout=widgets.Layout(width='auto'),
        disabled=False
    )

    back_to_gather_data_button = widgets.Button(
        description='Back',
        disabled=False,
        layout=widgets.Layout(width='auto'),
        tooltip='Go back to the data gathering screen.',
    )

    make_plot_button = widgets.Button(
        description='Plot Selected Sensor(s)', # Multi Sensor data in future?
        disabled=False,
        layout=widgets.Layout(width='auto'),
        tooltip='Create a plot with data.',
    )

    return sensor_select, back_to_gather_data_button, make_plot_button

# Code for the view plot scene elements.
def view_plot_elements():
    view_plot_home_button = widgets.Button(
        description='Home',
        disabled=False,
        layout=widgets.Layout(width='auto'),
        tooltip='Go back to the home screen.',
    )

    back_to_make_plot_button = widgets.Button(
        description='Back',
        disabled=False,
        layout=widgets.Layout(width='auto'),
        tooltip='Go back to the plot selection screen.',
    )

    return view_plot_home_button, back_to_make_plot_button
