# CAPTCHA Architecture

CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart) is used to distinguish between human users and automated bots.

## Components

1. Challenge Generator
   - Generates distorted text, images, or audio.

2. User Interface
   - Displays the challenge to the user.

3. Response Collector
   - Collects the user's response.

4. Validation Module
   - Checks whether the response is correct.

5. Decision Module
   - Determines whether the user is human or bot.

## Working

1. The system generates a CAPTCHA challenge.
2. The challenge is presented to the user.
3. The user enters the response.
4. The system verifies the answer.
5. If correct, access is granted.

## Examples of CAPTCHA

- Distorted text CAPTCHA
- Image recognition CAPTCHA
- reCAPTCHA