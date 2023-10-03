# GitHub Gists API

The GitHub Gists API is a simple HTTP API built with Python and Flask that interacts with the GitHub API to retrieve a user's publicly available Gists.

## Getting Started

To get started, follow these instructions to set up and run the API on your local machine.

## Prerequisites
### API
- docker

### Testing framework
- Python 3.x
- requests

## Installation

This API is provided as a Docker container

1. Run from the same directory as this README.

2. Build docker image:

   ```bash
   docker build -t github-gists-api .
   ```

3. Start the ontainer, it will automatically start the API:

   ```bash
   docker run --name alex-github-gists-api -p 8080:8080 github-gists-api
   ```

4. When finished, press Ctrl+C to exit

5. (Recommended) Clean up the docker container and image.
    ```bash
    docker rm alex-github-gists-api
    docker image rm github-gists-api
    ```
## Using the API

   The API will be accessible at `http://localhost:8080`.

1. To retrieve a user's Gists, make a GET request to the following endpoint:

   ```
   http://localhost:8080/<USERNAME>
   ```

   Replace `<USERNAME>` with the GitHub username of the user whose Gists you want to retrieve.

## API Endpoints

### Get User's Gists

- **Endpoint**: `/username`
- **HTTP Method**: GET
- **Parameters**:
  - `username` (string): The GitHub username of the user whose Gists you want to retrieve.
- **Response**:
  - Status Code: 200 OK
  - Body: JSON array containing the user's public Gists.

    Example Response:
    ```json
    [
      {
        "id": "gist_id",
        "description": "Gist Description",
        "files": {
          "file1.txt": {
            "filename": "file1.txt",
            "content": "Gist Content"
          }
        }
      },
      // More Gists...
    ]
    ```

  - Status Code: 404 Not Found
  - Body: JSON object with an error message when the user is not found.

    Example Response:
    ```json
    {
      "error": "User not found"
    }
    ```

  - This API will return Status Code 500 for all other cases.

## Testing Framework

The included file(s) in the `test` directory use the unittest framework in Python.
Make sure the API is running (as shown above) when running the tests. These tests will verify that the API works as expected and handles both valid and invalid cases.

Cases tested:
- User: `octocat` (As requested)
- User: `nonexistentuser` which should return a 404 error, which is handled gracefully by the API 

To run the tests, execute the following command:
```
python -m unittest tests/github_gists_api_test.py
```


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Cheers to [Equal Experts](https://www.equalexperts.com/) for requesting this fun project.
