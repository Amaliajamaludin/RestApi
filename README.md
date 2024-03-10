# RestApi
# Twitter Archive Explorer API

## Introduction
This set of REST APIs allows users to explore their Twitter archive by interacting with a JSON file deployed on a server. By making simple HTTP requests, users can retrieve information about tweets and user profiles.

## Getting Started
To use these APIs, follow the steps below:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Amaliajamaludin/RestApi.git
    ```
2. **Run the application:**
    ```bash
    python RestApi.py
    ```

3. **Open Postman and start making requests.**

## API Endpoints

### 1. Get All Tweets
- **Endpoint:** `/tweets`
- **Method:** `GET`
- **Description:** Retrieve a list of all tweets in the archive, including creation time, tweet ID, and tweet text.

### 2. Get All External Links
- **Endpoint:** `/links`
- **Method:** `GET`
- **Description:** Extract all external links from tweet text using regular expressions. Links are grouped based on tweet IDs.

### 3. Get Tweet Details
- **Endpoint:** `/tweets/<tweet_id>`
- **Method:** `GET`
- **Description:** Retrieve detailed information about a specific tweet using its ID, including creation time, tweet text, user screen name, and language.

### 4. Get User Details
- **Endpoint:** `/users/<screen_name>`
- **Method:** `GET`
- **Description:** Retrieve detailed profile information about a Twitter user using their screen name. Information includes name, description, followers count, friends count, and favorites count.

## Sample Requests

- **Get All Tweets:**
  
