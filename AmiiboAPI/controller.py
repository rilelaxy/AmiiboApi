import requests
from PyQt6.QtWidgets import QMessageBox

def search_amiibo(amiibo_name, app_instance):
    """
    Searches for Amiibo data based on the provided name
    """
    if not amiibo_name:
        QMessageBox.warning(app_instance, "Warning", "Please enter an Amiibo name.")
        return

    url = f"https://www.amiiboapi.com/api/amiibo/?name={amiibo_name}"
    try:
        response = requests.get(url)
        data = response.json()
        if 'amiibo' in data and data['amiibo']:
            amiibo_data = data['amiibo'][0]
            display_amiibo_info(amiibo_data, app_instance)
        else:
            app_instance.series_value.setText("")
            app_instance.release_value.setText("")
            app_instance.name_value.setText("Amiibo not found.")
    except Exception as e:
        QMessageBox.critical(app_instance, "Error", f"Error fetching Amiibo data: {str(e)}")

def display_amiibo_info(amiibo_data, app_instance):
    """
    Updates the app with the  Amiibo information.
    """
    name = amiibo_data.get('name', 'N/A')
    series = amiibo_data.get('amiiboSeries', 'N/A')
    release = amiibo_data.get('release', {}).get('na', 'N/A')

    app_instance.name_value.setText(name)
    app_instance.series_value.setText(series)
    app_instance.release_value.setText(release)
