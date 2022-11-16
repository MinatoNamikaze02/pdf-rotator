# Pdf-rotator
A python REST api to rotate any page of a pdf. Internship test.

## How to use.
- Install dependencies by running
    ```
    pip install -r requirements.txt
    ```
- Start the Server by running
    ```
    python app.py
    ```
- Test the endpoint by giving the below mentioned flags in the POST body.
  - relative path to pdf
  - page number
  - degree of roation

- NOTE: entering incorrect or invalid values will raise HTTP exceptions.

## Demo
- The pdf and the rotated one are both available in this repository under pdf and res directories.

![demo](https://github.com/MinatoNamikaze02/pdf-rotator/blob/main/demo/Screenshot%202022-11-16%20at%201.03.41%20PM.png)
