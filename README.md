# Slovenia Driving Licence Open Spot Finder

This application utilizes the Scrapy framework with Playwright to fetch the latest available open practical exam slots for obtaining a driving license in Slovenia. The app's purpose is to notify users when new slots become available.

## Table of Contents

-  [Project Description](#project-description)
-  [TODO](#todo)
-  [Installation](#installation)
-  [Usage](#usage)
-  [Contributing](#contributing)
-  [License](#license)

## Project Description

The Slovenia Driving Licence Open Spot Finder is an application designed to help individuals seeking a driving license in Slovenia. By utilizing the Scrapy framework with Playwright, the app automatically fetches the latest available open practical exam slots.

## TODO

### Save Fetched Data

The Scrapy spider should be modified to save the fetched data for future reference. This will allow tracking and comparison of available slots over time.

### Display Latest Dates

Currently, all fetched data dates are displayed. The application needs to be updated to only display the latest date, providing users with quick information about the most recent available slots.

### Email Notifications

Implement an email notification service to inform subscribed users about newly opened appointment slots. This feature will enhance user convenience by sending timely updates directly to their email.

### Dockerfile

A Dockerfile should be created to containerize the application. This will enable easy deployment and distribution of the Slovenia Driving Licence Open Spot Finder.

### Deployment

The application should be deployed to a server, making it accessible to users. Deploying to a server ensures availability and allows users to access the spot finder from various devices.

## Installation

To install the Slovenia Driving Licence Open Spot Finder, follow these steps:

1. Clone the repository: `git clone https://github.com/your/repo.git`
2. Change to the project directory: `cd repo`
3. Install dependencies: `pip install -r requirements.txt`

## Usage

Follow these instructions to use the Slovenia Driving Licence Open Spot Finder:

1. Set up the required configuration, such as email settings and notification preferences.
2. Run the application: `python app.py` or `./app.py` (depending on your system).
3. The app will regularly check for new available slots and notify subscribed users via email.

## Contributing

Contributions are welcome! If you'd like to contribute to the Slovenia Driving Licence Open Spot Finder, please follow these guidelines:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test your changes thoroughly.
5. Submit a pull request detailing your changes.

We appreciate your contributions!

## License

[Add license information here]

Feel free to customize the above content as per your project requirements and provide license information.
