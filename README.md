# Week 7

This week is meant to give you a basic introduction to analyzing graph data as well as *geo*graphical data. Also, we will spend time on debugging, exceptions, and unit testing. In particular, we will focus on the following:

- Networks and graphs
- Mapping geocoded data
- Debugging, Exceptions, and Unit Testing

## Setup

1. [Fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository) this repository.
2. [Create a Codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository#creating-a-codespace-for-a-repository) for your repository. Use this to view the lab notebook and work on your weekly coding exercise.
3. Once you're ready, [commit and push](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace#committing-your-changes) your final changes to your repository. *Note: You can also make quick edits using the [GitHub Dev Editor](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor#opening-the-githubdev-editor).*

## Packages Available:

The environment for this week is built with the following environment.yml:

```yml
name: week-7
dependencies:
  - python=3.11
  - pip
  - pip:
    - ipykernel  # for Jupyter Notebook
    - streamlit
    - seaborn
    - pandas
    - numpy
    - lxml
    - networkx
    - geopy
    - haversine
    - plotly
    - nbformat
```

*Note: you are welcome to install more packages in your codespace, but they will not be used by the autograder.*

 ---

My Summary
This project focused on debugging, exception handling, and unit testing.
I fixed issues in loader.py by adding proper indentation and try–except blocks to handle geocoding errors.

The script now successfully creates a geo_data.csv file containing location, latitude, longitude, and type data.

In test_loader.py, I implemented:
  test_valid_locations() to confirm valid places return coordinates.
  test_invalid_location() to confirm invalid names return empty values.

All tests passed successfully, confirming the functions work as intended.

Files Updated:
  loader.py – Debugged and fixed.
  test_loader.py – Added unit tests.
  geo_data.csv – Output generated from the script.


  ---

## 🧩 My Summary

This week’s project focused on **debugging, exception handling, and unit testing**.

### 🔧 Fixes and Improvements
- Debugged and cleaned the `loader.py` file.  
- Added `try–except` handling for geocoding timeouts and other errors.  
- Ensured the script correctly generates a `geo_data.csv` file containing  
  **location**, **latitude**, **longitude**, and **type** data.  

### 🧪 Unit Testing
Implemented tests in `test_loader.py` using Python’s `unittest` module:
- **`test_valid_locations()`** → Verifies that valid locations (e.g., *New York*) return valid coordinates.  
- **`test_invalid_location()`** → Verifies that invalid entries (e.g., *asdfqwer1234*) return empty or `None` values.  

All tests ran successfully, confirming both functions work as intended.

### 📂 Files Updated
- `loader.py` – Debugged, cleaned, and fully functional.  
- `test_loader.py` – Added and passed all tests.  
- `geo_data.csv` – Successfully generated output file.  

### ✅ Result
All tasks were completed successfully.  
Both valid and invalid locations were handled properly, and all tests passed without errors.
