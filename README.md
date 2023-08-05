Welcome Light illumination calculator

About the project:

    There are street lights placed evenly every 20 meters on a straight road.
    Most of the street lights are working and have the same illumination intencity.
    Non-working street lights are provided as a list of their indexes.
    If a street light is not working - its position can still be illuminated by neighboring lights.
    Illumination is decreasing exponentially when the distance decreases from a street light.   

    Notes:
    - The road lenght can be from 0 to 2000000m.
    - The street lights are indexed from 0 and the first one stands at the begining of the road.
    - The intensity of illumination can be calculated using f(x) = 3^(-(x/100)^2) formula, 
  where x is a distance from the street ligth in meters.
    - If the street light is very far away and its illumination intencity is less than 0.01 - its illumination has to be ignored.
    - In case there are several street lights with the same lowest illumination - provide the one with the lowest index.

Settings

To have same settings please do steps below:

    Install Python(for this project, I used Python 3.10.4).
    Create vitual environment:

    python -m venv venv

Install all packages from requirements.txt:

pip install -r requirements.txt

    Activate vitual environment

Usage

Run the calculator:

   python3 app.py

Testing

    Main functions for App functionality can be found in test_app.py
    Testing was made using Unittest module.
    To run the test:

   python3 test_app.py


Author

Aurimas Gaidamavičius
Github: @Aurimaso
Email: aurimas.gaidamavicius@gmail.com